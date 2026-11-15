"""Generate text with a language model (LLM), behind one small interface.

The model and its settings are chosen in .env (LLM_BACKEND, LLM_MODEL, LLM_NUM_CTX, LLM_NUM_GPU...).
Two backends share the attributes and the generate() method of ChatModel:
- OllamaChatModel, the local model: the default, and the only one meant for real questions;
- OpenAICompatibleChatModel, an OpenAI-compatible API such as Groq, used only for the session 7
  experiment (does a bigger model write better?) on the test questions, never on personal data.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from compliance_copilot.config import LLM_BACKENDS, Settings

OUT_OF_MEMORY = re.compile(r"out of memory|unable to allocate|cudamalloc|more system memory", re.IGNORECASE)
RETRYABLE_STATUS = {429, 500, 502, 503, 504}  # rate limit or a passing server error: wait, then try again
USER_AGENT = "compliance-copilot/0.1"  # the default Python user agent is refused by the API's front (Cloudflare error 1010, HTTP 403)


@dataclass
class Generation:
    text: str
    prompt_tokens: int
    completion_tokens: int
    seconds: float  # whole call, model loading included
    tokens_per_second: float  # writing speed of the answer
    truncated: bool  # stopped by the max_tokens limit, so the end of the answer is missing
    reasoning: str = ""  # reasoning written by an API model before its answer: hidden from the user, but counted in completion_tokens


class ChatModel(Protocol):
    model: str
    num_ctx: int  # context size in tokens: prompt + answer must fit in it
    max_tokens: int

    def generate(self, messages: list[dict], on_text: Callable[[str], None] | None = None) -> Generation:
        """Answer the conversation; on_text receives each piece of text as soon as it is written."""
        ...


class LLMError(RuntimeError):
    """A generation request failed; the message can be shown to the user as is."""


class OllamaChatModel:
    """Chat with a model served by the local Ollama server (POST /api/chat, streamed)."""

    def __init__(
        self,
        base_url: str,
        model: str,
        num_ctx: int = 8192,
        num_gpu: int | None = None,
        temperature: float = 0.1,
        max_tokens: int = 700,
        timeout: float = 900,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.num_ctx = num_ctx
        self.num_gpu = num_gpu
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout

    def _request_body(self, messages: list[dict]) -> dict:
        options = {"temperature": self.temperature, "num_ctx": self.num_ctx, "num_predict": self.max_tokens}
        if self.num_gpu is not None:
            options["num_gpu"] = self.num_gpu
        return {"model": self.model, "messages": messages, "stream": True, "options": options}

    def _explain(self, detail: str) -> str:
        """Turn an Ollama error into a message that says what to do."""
        if "not found" in detail:
            return f"Le modèle {self.model} n'est pas installé dans Ollama ({detail}). Lancez « ollama pull {self.model} »."
        if OUT_OF_MEMORY.search(detail):
            if self.num_gpu is None:
                gpu = "choix d'Ollama"
            else:
                gpu = "toutes" if self.num_gpu >= 99 else str(self.num_gpu)
            return (
                f"Mémoire insuffisante pour le modèle {self.model} (contexte de {self.num_ctx} tokens, couches sur la "
                f"carte graphique : {gpu}). Dans le fichier .env, baissez LLM_NUM_CTX (par exemple 6144 ou 4096) ou "
                "LLM_NUM_GPU (par exemple 20), ou laissez LLM_NUM_GPU vide pour laisser Ollama choisir (plus lent), "
                f"puis relancez. Détail d'Ollama : {detail}"
            )
        return f"Ollama a renvoyé une erreur : {detail}"

    def generate(self, messages: list[dict], on_text: Callable[[str], None] | None = None) -> Generation:
        request = urllib.request.Request(
            f"{self.base_url}/api/chat",
            data=json.dumps(self._request_body(messages)).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        pieces: list[str] = []
        final: dict = {}
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                for line in response:  # one JSON object per line while the answer is written
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if "error" in data:
                        raise LLMError(self._explain(data["error"]))
                    piece = data.get("message", {}).get("content", "")
                    if piece:
                        pieces.append(piece)
                        if on_text:
                            on_text(piece)
                    if data.get("done"):
                        final = data
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            try:
                detail = json.loads(body).get("error", body)
            except ValueError:
                detail = body
            raise LLMError(self._explain(f"HTTP {error.code} : {detail}")) from error
        except (urllib.error.URLError, TimeoutError) as error:
            raise LLMError(f"Ollama ne répond pas sur {self.base_url} ({error}). Lancez l'application Ollama.") from error

        completion_tokens = final.get("eval_count", 0)
        writing_seconds = final.get("eval_duration", 0) / 1e9
        return Generation(
            text="".join(pieces),
            prompt_tokens=final.get("prompt_eval_count", 0),
            completion_tokens=completion_tokens,
            seconds=final.get("total_duration", 0) / 1e9,
            tokens_per_second=completion_tokens / writing_seconds if writing_seconds else 0.0,
            truncated=final.get("done_reason") == "length",
        )


class OpenAICompatibleChatModel:
    """Chat with a model behind an OpenAI-compatible API (POST /chat/completions, not streamed), e.g. Groq.

    The API key is read from the environment variable whose NAME is given (GROQ_API_KEY, from .env).
    It is kept private: never in repr(), in an error message or in a file. Rate limits (HTTP 429) and
    passing server errors are waited for (retry-after header, else 2, 4, 8… s) and tried again; the
    time spent waiting is counted apart, in waited_seconds, so that it does not count as generation time.
    With reasoning_effort set (none, low…), the value is sent as is; a reasoning text returned by the model goes
    to Generation.reasoning, and its tokens count in completion_tokens and in the max_tokens limit.
    """

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key_env: str,
        num_ctx: int = 8192,
        temperature: float = 0.1,
        max_tokens: int = 700,
        reasoning_effort: str = "",
        timeout: float = 300,
        max_attempts: int = 8,
        max_wait: float = 300,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key_env = api_key_env
        self.num_ctx = num_ctx  # kept for fit_passages, so that the passages stay those of the local model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.reasoning_effort = reasoning_effort
        self.timeout = timeout
        self.max_attempts = max_attempts
        self.max_wait = max_wait  # a longer wait means the quota of the day is used up: stop instead
        self._sleep = sleep
        self._api_key = os.environ.get(api_key_env, "").strip()
        self.waited_seconds = 0.0  # waits for the rate limits and time lost in failed attempts, counted apart
        self.rate_limits: dict[str, str] = {}  # x-ratelimit-* headers of the last answer (they hold no secret)
        self.last_usage: dict = {}  # usage of the last answer: tokens and the server's own timings (no secret)

    def __repr__(self) -> str:
        return f"OpenAICompatibleChatModel(base_url={self.base_url!r}, model={self.model!r}, api_key_env={self.api_key_env!r})"

    def _hide_key(self, text: str) -> str:
        return text.replace(self._api_key, "***") if self._api_key else text

    def _explain(self, status: int, detail: str) -> str:
        if status in (401, 403):
            return f"Clé refusée par l'API (HTTP {status}) : vérifiez {self.api_key_env} dans le fichier .env."
        if status == 404:
            return f"Modèle {self.model} inconnu de l'API {self.base_url} (HTTP 404) : vérifiez LLM_MODEL."
        return self._hide_key(f"L'API {self.base_url} a renvoyé une erreur (HTTP {status}) : {detail}")

    def _wait_seconds(self, retry_after: str | None, attempt: int) -> float:
        try:
            return max(float(retry_after), 1.0) if retry_after else min(2.0**attempt, 60.0)
        except ValueError:
            return min(2.0**attempt, 60.0)

    def _require_key(self) -> None:
        if not self._api_key:
            raise LLMError(f"Clé absente : ajoutez {self.api_key_env}=… dans le fichier .env (jamais dans le code ni dans Git).")

    def _headers(self) -> dict[str, str]:
        return {"Content-Type": "application/json", "Authorization": f"Bearer {self._api_key}", "User-Agent": USER_AGENT}

    def list_models(self) -> list[str]:
        """The ids of the models the key may use (GET /models): nothing is sent but the key."""
        self._require_key()
        request = urllib.request.Request(f"{self.base_url}/models", headers=self._headers())
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = json.load(response)
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")[:300]
            if error.code == 404:
                raise LLMError(f"L'adresse {self.base_url}/models n'existe pas (HTTP 404) : vérifiez LLM_API_BASE_URL.") from None
            raise LLMError(self._explain(error.code, detail)) from None
        except (urllib.error.URLError, TimeoutError) as error:
            raise LLMError(self._hide_key(f"L'API {self.base_url} ne répond pas ({error}). Vérifiez la connexion.")) from None
        return sorted(model["id"] for model in data.get("data", []) if isinstance(model, dict) and "id" in model)

    def generate(self, messages: list[dict], on_text: Callable[[str], None] | None = None) -> Generation:
        self._require_key()
        payload = {"model": self.model, "messages": messages, "temperature": self.temperature,
                   "max_completion_tokens": self.max_tokens, "stream": False}  # max_tokens is deprecated by the API
        if self.reasoning_effort:
            payload["reasoning_effort"] = self.reasoning_effort
        body = json.dumps(payload).encode("utf-8")
        for attempt in range(1, self.max_attempts + 1):
            request = urllib.request.Request(
                f"{self.base_url}/chat/completions",
                data=body,
                headers=self._headers(),
            )
            start = time.perf_counter()
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    data = json.load(response)
                    self.rate_limits = {k.lower(): v for k, v in response.headers.items() if k.lower().startswith("x-ratelimit")}
                seconds = time.perf_counter() - start
                break
            except urllib.error.HTTPError as error:
                self.waited_seconds += time.perf_counter() - start  # a failed attempt may take long before the error comes back
                detail = error.read().decode("utf-8", errors="replace")[:300]
                if error.code not in RETRYABLE_STATUS or attempt == self.max_attempts:
                    raise LLMError(self._explain(error.code, detail)) from None
                wait = self._wait_seconds(error.headers.get("retry-after"), attempt)
                if wait > self.max_wait:
                    raise LLMError(
                        f"Quota de l'API atteint : il faudrait attendre {wait / 60:.0f} min (limite par jour probable). "
                        "Relancez plus tard."
                    ) from None
                reason = "limite de débit atteinte" if error.code == 429 else f"erreur passagère du serveur (HTTP {error.code})"
                print(f"[API] {reason}, attente de {wait:.0f} s (essai {attempt}/{self.max_attempts})", file=sys.stderr, flush=True)
                self._sleep(wait)
                self.waited_seconds += wait
            except (urllib.error.URLError, TimeoutError) as error:
                raise LLMError(self._hide_key(f"L'API {self.base_url} ne répond pas ({error}). Vérifiez la connexion.")) from None

        choice = data["choices"][0]
        message = choice.get("message", {})
        text = message.get("content") or ""
        if on_text and text:
            on_text(text)
        usage = data.get("usage", {})
        self.last_usage = usage
        completion_tokens = usage.get("completion_tokens", 0)
        writing_seconds = usage.get("completion_time") or seconds  # Groq gives the writing time itself
        return Generation(
            text=text,
            prompt_tokens=usage.get("prompt_tokens", 0),
            completion_tokens=completion_tokens,
            seconds=seconds,
            tokens_per_second=completion_tokens / writing_seconds if writing_seconds else 0.0,
            truncated=choice.get("finish_reason") == "length",
            reasoning=message.get("reasoning") or message.get("reasoning_content") or "",
        )


def make_chat_model(settings: Settings) -> OllamaChatModel | OpenAICompatibleChatModel:
    """The language model configured in .env: local Ollama by default."""
    if settings.llm_backend not in LLM_BACKENDS:
        raise LLMError(f"LLM_BACKEND doit valoir {' ou '.join(LLM_BACKENDS)} (reçu : {settings.llm_backend}).")
    if settings.llm_backend == "openai":
        return OpenAICompatibleChatModel(
            settings.llm_api_base_url,
            settings.llm_model,
            settings.llm_api_key_env,
            num_ctx=settings.llm_num_ctx,
            temperature=settings.llm_temperature,
            max_tokens=settings.llm_max_tokens,
            reasoning_effort=settings.llm_api_reasoning_effort,
        )
    return OllamaChatModel(
        settings.ollama_base_url,
        settings.llm_model,
        num_ctx=settings.llm_num_ctx,
        num_gpu=settings.llm_num_gpu,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
    )

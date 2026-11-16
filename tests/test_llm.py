"""Offline tests for the chat models (local Ollama and OpenAI-compatible API): the HTTP calls never leave the test."""

import dataclasses
import io
import json
import urllib.error

import pytest

from compliance_copilot import llm
from compliance_copilot.config import Settings, optional_int
from compliance_copilot.llm import LLMError, OllamaChatModel, OpenAICompatibleChatModel, make_chat_model, provider_name

BASE_URL = "http://localhost:11434"
MESSAGES = [{"role": "user", "content": "Dois-je désigner un DPO ?"}]


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()


def streamed(*objects: dict) -> FakeResponse:
    """What Ollama sends while it writes: one JSON object per line."""
    return FakeResponse("".join(json.dumps(item) + "\n" for item in objects).encode("utf-8"))


END = {"done": True, "done_reason": "stop", "prompt_eval_count": 100, "eval_count": 10, "eval_duration": 500_000_000, "total_duration": 2_000_000_000}


@pytest.fixture
def sent_bodies(monkeypatch) -> list[dict]:
    bodies = []

    def fake_urlopen(request, timeout):
        bodies.append(json.loads(request.data))
        return streamed({"message": {"content": "Bon"}, "done": False}, {"message": {"content": "jour [1]"}, "done": False}, END)

    monkeypatch.setattr(llm.urllib.request, "urlopen", fake_urlopen)
    return bodies


def fail_with(monkeypatch, error: Exception) -> None:
    def fake_urlopen(request, timeout):
        raise error

    monkeypatch.setattr(llm.urllib.request, "urlopen", fake_urlopen)


def http_error(code: int, message: str) -> urllib.error.HTTPError:
    return urllib.error.HTTPError(f"{BASE_URL}/api/chat", code, "error", {}, io.BytesIO(json.dumps({"error": message}).encode()))


def test_streamed_answer_is_assembled_with_its_statistics(sent_bodies):
    pieces = []
    model = OllamaChatModel(BASE_URL, "ministral-3:3b", num_ctx=8192, num_gpu=99, temperature=0.1, max_tokens=700)

    generation = model.generate(MESSAGES, on_text=pieces.append)

    assert pieces == ["Bon", "jour [1]"]
    assert generation.text == "Bonjour [1]"
    assert (generation.prompt_tokens, generation.completion_tokens) == (100, 10)
    assert generation.tokens_per_second == 20.0
    assert generation.truncated is False
    body = sent_bodies[0]
    assert body["stream"] is True
    assert body["options"] == {"temperature": 0.1, "num_ctx": 8192, "num_predict": 700, "num_gpu": 99}


def test_empty_num_gpu_lets_ollama_decide(sent_bodies):
    OllamaChatModel(BASE_URL, "ministral-3:3b", num_gpu=None).generate(MESSAGES)

    assert "num_gpu" not in sent_bodies[0]["options"]
    assert optional_int("") is None and optional_int("20") == 20


def test_answer_stopped_by_the_length_limit_is_marked_as_truncated(monkeypatch):
    monkeypatch.setattr(llm.urllib.request, "urlopen", lambda request, timeout: streamed({**END, "done_reason": "length"}))

    assert OllamaChatModel(BASE_URL, "ministral-3:3b").generate(MESSAGES).truncated is True


def test_unreachable_ollama_gives_a_clear_error(monkeypatch):
    fail_with(monkeypatch, urllib.error.URLError("connection refused"))

    with pytest.raises(LLMError, match="Ollama ne répond pas"):
        OllamaChatModel(BASE_URL, "ministral-3:3b").generate(MESSAGES)


def test_missing_model_suggests_pulling_it(monkeypatch):
    fail_with(monkeypatch, http_error(404, 'model "ministral-3:3b" not found, try pulling it first'))

    with pytest.raises(LLMError, match="ollama pull ministral-3:3b"):
        OllamaChatModel(BASE_URL, "ministral-3:3b").generate(MESSAGES)


def test_out_of_memory_explains_which_settings_to_lower(monkeypatch):
    fail_with(monkeypatch, http_error(500, "llama runner process has terminated: CUDA error: out of memory"))

    with pytest.raises(LLMError) as error:
        OllamaChatModel(BASE_URL, "ministral-3:3b", num_ctx=8192, num_gpu=99).generate(MESSAGES)

    assert "Mémoire insuffisante" in str(error.value)
    assert "LLM_NUM_CTX" in str(error.value) and "LLM_NUM_GPU" in str(error.value)


# ---------------------------------------------------------------- OpenAI-compatible API (session 7 experiment)

API_URL = "https://api.example.test/openai/v1"
KEY_ENV = "TEST_LLM_API_KEY"
FAKE_KEY = "gsk_" + "x" * 32  # built at run time, so that this file does not look like a secret to the scanner


class FakeAPIResponse(FakeResponse):
    def __init__(self, data: dict, headers: dict | None = None):
        super().__init__(json.dumps(data).encode("utf-8"))
        self.headers = headers or {}


def api_answer(text="Bonjour [1]", finish_reason="stop") -> dict:
    return {
        "choices": [{"message": {"role": "assistant", "content": text}, "finish_reason": finish_reason}],
        "usage": {"prompt_tokens": 100, "completion_tokens": 10, "completion_time": 0.5},
    }


def api_error(code: int, retry_after: str | None = None) -> urllib.error.HTTPError:
    headers = {"retry-after": retry_after} if retry_after else {}
    return urllib.error.HTTPError(f"{API_URL}/chat/completions", code, "error", headers, io.BytesIO(b'{"error": {"message": "rate limit"}}'))


@pytest.fixture
def api_model(monkeypatch) -> tuple[OpenAICompatibleChatModel, list[float]]:
    monkeypatch.setenv(KEY_ENV, FAKE_KEY)
    sleeps: list[float] = []
    return OpenAICompatibleChatModel(API_URL, "big-model", KEY_ENV, temperature=0.1, max_tokens=2000, sleep=sleeps.append), sleeps


def answer_in_turn(monkeypatch, *outcomes) -> list:
    """urlopen returns (or raises) each outcome in turn; the requests sent are recorded."""
    requests, queue = [], list(outcomes)

    def fake_urlopen(request, timeout):
        requests.append(request)
        outcome = queue.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(llm.urllib.request, "urlopen", fake_urlopen)
    return requests


def test_api_answer_is_read_with_its_statistics_and_rate_limits(monkeypatch, api_model):
    model, _ = api_model
    requests = answer_in_turn(monkeypatch, FakeAPIResponse(api_answer(), {"x-ratelimit-limit-tokens": "12000", "Content-Type": "json"}))
    pieces = []

    generation = model.generate(MESSAGES, on_text=pieces.append)

    assert generation.text == "Bonjour [1]" and pieces == ["Bonjour [1]"]
    assert (generation.prompt_tokens, generation.completion_tokens, generation.tokens_per_second) == (100, 10, 20.0)
    assert generation.truncated is False
    assert model.rate_limits == {"x-ratelimit-limit-tokens": "12000"}
    body = json.loads(requests[0].data)
    assert body == {"model": "big-model", "messages": MESSAGES, "temperature": 0.1, "max_completion_tokens": 2000, "stream": False}
    assert requests[0].full_url == f"{API_URL}/chat/completions"
    assert requests[0].get_header("Authorization") == f"Bearer {FAKE_KEY}"
    assert requests[0].get_header("User-agent") == llm.USER_AGENT  # Python's default user agent gets a 403 from the API's front


def test_api_answer_stopped_by_the_length_limit_is_marked_as_truncated(monkeypatch, api_model):
    model, _ = api_model
    answer_in_turn(monkeypatch, FakeAPIResponse(api_answer(finish_reason="length")))

    assert model.generate(MESSAGES).truncated is True


def test_rate_limit_is_waited_for_then_tried_again(monkeypatch, api_model):
    model, sleeps = api_model
    requests = answer_in_turn(monkeypatch, api_error(429, retry_after="7"), api_error(503), FakeAPIResponse(api_answer()))
    clock = iter(range(0, 1000, 10))  # every reading of the clock is 10 s after the previous one
    monkeypatch.setattr(llm.time, "perf_counter", lambda: float(next(clock)))

    generation = model.generate(MESSAGES)

    assert generation.text == "Bonjour [1]" and len(requests) == 3
    assert sleeps == [7.0, 4.0]  # retry-after, then 2 ** attempt
    assert model.waited_seconds == 31.0  # the sleeps, plus the 10 s of each failed attempt
    assert generation.seconds == 10.0  # the successful attempt only


def test_quota_of_the_day_stops_instead_of_waiting_hours(monkeypatch, api_model):
    model, sleeps = api_model
    answer_in_turn(monkeypatch, api_error(429, retry_after="3600"))

    with pytest.raises(LLMError, match="Quota de l'API atteint"):
        model.generate(MESSAGES)
    assert sleeps == []


def test_refused_key_is_explained_without_showing_it(monkeypatch, api_model):
    model, _ = api_model
    answer_in_turn(monkeypatch, api_error(401))

    with pytest.raises(LLMError) as error:
        model.generate(MESSAGES)

    assert KEY_ENV in str(error.value) and FAKE_KEY not in str(error.value)
    assert FAKE_KEY not in repr(model) and FAKE_KEY not in str(vars(model).get("rate_limits"))


def test_missing_key_is_reported_before_any_call(monkeypatch):
    monkeypatch.delenv(KEY_ENV, raising=False)
    requests = answer_in_turn(monkeypatch)

    with pytest.raises(LLMError, match="Clé absente"):
        OpenAICompatibleChatModel(API_URL, "big-model", KEY_ENV).generate(MESSAGES)
    assert requests == []


def test_backend_is_chosen_in_the_settings(monkeypatch):
    monkeypatch.setenv(KEY_ENV, FAKE_KEY)
    local = Settings(ollama_base_url=BASE_URL, llm_model="qwen3:4b-instruct", embedding_model="bge-m3")
    api = dataclasses.replace(local, llm_backend="openai", llm_api_model="big-model", llm_api_base_url=API_URL, llm_api_key_env=KEY_ENV)

    assert isinstance(make_chat_model(local), OllamaChatModel)  # local by default
    assert make_chat_model(local).model == "qwen3:4b-instruct" and make_chat_model(local).remote is False
    remote = make_chat_model(api)
    assert isinstance(remote, OpenAICompatibleChatModel) and remote.num_ctx == local.llm_num_ctx
    assert remote.model == "big-model" and remote.remote is True  # LLM_API_MODEL, while LLM_MODEL stays the local model
    assert make_chat_model(dataclasses.replace(api, llm_api_model="qwen/qwen3.8-27b")).model == "qwen/qwen3.8-27b"
    assert api.generation_model == "big-model" and local.generation_model == "qwen3:4b-instruct"
    assert remote.reasoning_effort == ""
    assert make_chat_model(dataclasses.replace(api, llm_api_reasoning_effort="none")).reasoning_effort == "none"
    with pytest.raises(LLMError, match="LLM_BACKEND"):
        make_chat_model(dataclasses.replace(local, llm_backend="cloud"))


def test_reasoning_effort_is_sent_only_when_set(monkeypatch):
    monkeypatch.setenv(KEY_ENV, FAKE_KEY)
    requests = answer_in_turn(monkeypatch, FakeAPIResponse(api_answer()), FakeAPIResponse(api_answer()))

    OpenAICompatibleChatModel(API_URL, "big-model", KEY_ENV).generate(MESSAGES)
    OpenAICompatibleChatModel(API_URL, "big-model", KEY_ENV, reasoning_effort="low").generate(MESSAGES)

    assert "reasoning_effort" not in json.loads(requests[0].data)
    assert json.loads(requests[1].data)["reasoning_effort"] == "low"


def test_reasoning_of_the_model_is_kept_apart_from_its_answer(monkeypatch, api_model):
    model, _ = api_model
    answer = api_answer()
    answer["choices"][0]["message"]["reasoning"] = "Je réfléchis d'abord."
    answer["usage"]["queue_time"] = 0.01
    answer_in_turn(monkeypatch, FakeAPIResponse(answer))

    generation = model.generate(MESSAGES)

    assert generation.text == "Bonjour [1]" and generation.reasoning == "Je réfléchis d'abord."
    assert model.last_usage["queue_time"] == 0.01


def test_models_open_to_the_key_are_listed(monkeypatch, api_model):
    model, _ = api_model
    requests = answer_in_turn(
        monkeypatch, FakeAPIResponse({"object": "list", "data": [{"id": "qwen/qwen3.8-27b"}, {"id": "openai/gpt-oss-120b"}]})
    )

    assert model.list_models() == ["openai/gpt-oss-120b", "qwen/qwen3.8-27b"]
    assert requests[0].full_url == f"{API_URL}/models" and requests[0].data is None
    assert requests[0].get_header("Authorization") == f"Bearer {FAKE_KEY}"


def test_models_list_errors_are_explained_without_the_key(monkeypatch, api_model):
    model, _ = api_model
    answer_in_turn(monkeypatch, api_error(401))

    with pytest.raises(LLMError) as error:
        model.list_models()
    assert KEY_ENV in str(error.value) and FAKE_KEY not in str(error.value)


def test_retired_model_says_so_and_how_to_go_back_to_local_mode(monkeypatch, api_model):
    model, _ = api_model
    body = io.BytesIO(b'{"error": {"message": "The model `big-model` has been decommissioned", "code": "model_decommissioned"}}')
    answer_in_turn(monkeypatch, urllib.error.HTTPError(f"{API_URL}/chat/completions", 400, "error", {}, body), api_error(404))

    for _ in range(2):
        with pytest.raises(LLMError) as error:
            model.generate(MESSAGES)
        assert "retiré ou inconnu" in str(error.value) and "preview" in str(error.value)
        assert "--backend ollama" in str(error.value) and FAKE_KEY not in str(error.value)


def test_quota_and_missing_key_errors_say_how_to_go_back_to_local_mode(monkeypatch, api_model):
    model, _ = api_model
    answer_in_turn(monkeypatch, api_error(429, retry_after="3600"))
    with pytest.raises(LLMError, match="Quota de l'API atteint pour aujourd'hui") as error:
        model.generate(MESSAGES)
    assert "--backend ollama" in str(error.value)

    monkeypatch.delenv(KEY_ENV, raising=False)
    with pytest.raises(LLMError, match="Clé absente") as error:
        OpenAICompatibleChatModel(API_URL, "big-model", KEY_ENV).generate(MESSAGES)
    assert "--backend ollama" in str(error.value) and FAKE_KEY not in str(error.value)


def test_default_reasoning_effort_is_none_for_qwen3_only(monkeypatch):
    monkeypatch.setenv(KEY_ENV, FAKE_KEY)
    base = Settings(ollama_base_url=BASE_URL, llm_model="qwen3:4b-instruct", embedding_model="bge-m3", llm_backend="openai",
                    llm_api_base_url=API_URL, llm_api_key_env=KEY_ENV)  # LLM_API_MODEL left to its default, qwen/qwen3.8-27b

    assert make_chat_model(base).model == "qwen/qwen3.8-27b" and make_chat_model(base).reasoning_effort == "none"
    assert make_chat_model(dataclasses.replace(base, llm_api_reasoning_effort="low")).reasoning_effort == "low"
    assert make_chat_model(dataclasses.replace(base, llm_api_model="openai/gpt-oss-120b")).reasoning_effort == ""


def test_error_sent_in_the_middle_of_the_stream(monkeypatch):
    monkeypatch.setattr(
        llm.urllib.request,
        "urlopen",
        lambda request, timeout: streamed({"message": {"content": "Oui"}, "done": False}, {"error": "unable to allocate CUDA0 buffer"}),
    )

    with pytest.raises(LLMError, match="LLM_NUM_CTX"):
        OllamaChatModel(BASE_URL, "ministral-3:3b").generate(MESSAGES)


def test_provider_is_named_from_the_api_address():
    assert provider_name("https://api.groq.com/openai/v1") == "Groq"
    assert provider_name("https://api.example.test/v1/") == "api.example.test"
    assert OllamaChatModel(BASE_URL, "qwen3:4b-instruct").provider == "Ollama"

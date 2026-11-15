"""Offline tests for scripts/check_api.py: both HTTP calls are faked, and the key never appears in the output."""

import importlib.util
import io
import json
from pathlib import Path

from compliance_copilot import llm
from compliance_copilot.config import Settings

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_api.py"
spec = importlib.util.spec_from_file_location("check_api", SCRIPT)
check_api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_api)

API_URL = "https://api.example.test/openai/v1"
KEY_ENV = "TEST_LLM_API_KEY"
FAKE_KEY = "gsk_" + "y" * 32  # built at run time, so that this file does not look like a secret to the scanner
LIMIT_HEADERS = {
    "x-ratelimit-limit-requests": "1000",
    "x-ratelimit-remaining-requests": "999",
    "x-ratelimit-reset-requests": "23h59m",
    "x-ratelimit-limit-tokens": "8000",
    "x-ratelimit-remaining-tokens": "7900",
    "x-ratelimit-reset-tokens": "750ms",
    "content-type": "application/json",
}
MODELS = {"object": "list", "data": [{"id": "openai/gpt-oss-120b"}, {"id": "qwen/qwen3.8-27b"}]}
ANSWER = {
    "choices": [{"message": {"content": "C'est le RGPD.", "reasoning": "Le 2016/679 est le RGPD."}, "finish_reason": "stop"}],
    "usage": {"prompt_tokens": 40, "completion_tokens": 8, "completion_time": 0.02, "total_time": 0.1},
}


class FakeResponse(io.BytesIO):
    def __init__(self, data: dict, headers: dict | None = None):
        super().__init__(json.dumps(data).encode("utf-8"))
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def run(monkeypatch, outcomes: list, argv: list[str]) -> list:
    """Run the script with faked HTTP answers (in turn) and fixed settings; the requests sent are returned."""
    monkeypatch.setenv(KEY_ENV, FAKE_KEY)
    settings = Settings(ollama_base_url="http://localhost:11434", llm_model="qwen3:4b-instruct", embedding_model="bge-m3",
                        llm_api_base_url=API_URL, llm_api_key_env=KEY_ENV)
    monkeypatch.setattr(check_api, "load_settings", lambda: settings)
    requests, queue = [], list(outcomes)

    def fake_urlopen(request, timeout):
        requests.append(request)
        outcome = queue.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(llm.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr("sys.argv", ["check_api.py", *argv])
    return requests


def test_trial_call_lists_the_models_and_shows_the_limits_without_the_key(monkeypatch, capsys):
    requests = run(monkeypatch, [FakeResponse(MODELS), FakeResponse(ANSWER, LIMIT_HEADERS)],
                   ["--model", "qwen/qwen3.8-27b", "--reasoning-effort", "none"])

    assert check_api.main() == 0
    out = capsys.readouterr().out

    assert requests[0].full_url == f"{API_URL}/models" and requests[0].data is None
    body = json.loads(requests[1].data)
    assert body["model"] == "qwen/qwen3.8-27b" and body["reasoning_effort"] == "none"
    assert body["messages"] == check_api.TRIAL_MESSAGES and body["max_completion_tokens"] == settings_max_tokens()
    assert "2 modèle(s) ouvert(s)" in out and "[OK] qwen/qwen3.8-27b est dans la liste" in out
    assert "llama-3.3-70b-versatile : absent" in out
    assert "Réponse : C'est le RGPD." in out and "raisonnement d'environ 5 mots" in out and "réponse complète" in out
    assert "requêtes par jour (RPD), limite : 1000" in out and "tokens par minute (TPM), limite : 8000" in out
    assert "tokens par minute, remise à zéro dans : 750ms" in out and "total_time 0.10 s" in out
    assert "tokens par jour, TPD, ne figurent pas" in out
    assert FAKE_KEY not in out and KEY_ENV in out


def settings_max_tokens() -> int:
    return Settings(ollama_base_url="", llm_model="", embedding_model="").llm_max_tokens


def test_a_model_missing_from_the_list_is_pointed_out(monkeypatch, capsys):
    run(monkeypatch, [FakeResponse(MODELS), FakeResponse(ANSWER, LIMIT_HEADERS)], ["--model", "llama-3.3-70b-versatile"])

    assert check_api.main() == 0
    out = capsys.readouterr().out
    assert "[ATTENTION] llama-3.3-70b-versatile" in out and "reasoning_effort = non envoyé" in out


def test_api_errors_stop_the_script_with_a_clear_message(monkeypatch, capsys):
    error = llm.urllib.error.HTTPError(f"{API_URL}/models", 401, "error", {}, io.BytesIO(b"{}"))
    run(monkeypatch, [error], ["--model", "qwen/qwen3.8-27b"])

    assert check_api.main() == 1
    out = capsys.readouterr().out
    assert "[ERREUR] Clé refusée" in out and FAKE_KEY not in out


def test_limits_are_described_even_without_headers():
    lines = check_api.describe_limits({})
    assert lines[0].strip().startswith("aucun en-tête") and "TPD" in lines[-1]

    lines = check_api.describe_limits({"x-ratelimit-limit-tokens": "8000", "x-ratelimit-other": "1"})
    assert lines[0] == "  tokens par minute (TPM), limite : 8000" and lines[1] == "  x-ratelimit-other : 1"

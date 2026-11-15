"""Offline tests for scripts/ask.py in remote mode: the notice, the signature, the personal-data guard before any
call, and the clear errors. No index, no Ollama, no API: everything the script calls is faked."""

import importlib.util
from pathlib import Path

import pytest

from compliance_copilot.config import Settings
from compliance_copilot.llm import Generation, LLMError
from compliance_copilot.rag import CitationCheck, RagAnswer

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ask.py"
spec = importlib.util.spec_from_file_location("ask", SCRIPT)
ask = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ask)

LOCAL = Settings(ollama_base_url="http://localhost:11434", llm_model="qwen3:4b-instruct", embedding_model="bge-m3", answer_judge=False)
REMOTE = Settings(ollama_base_url="http://localhost:11434", llm_model="qwen/qwen3.8-27b", embedding_model="bge-m3",
                  llm_backend="openai", llm_api_base_url="https://api.groq.com/openai/v1", llm_api_key_env="TEST_LLM_API_KEY",
                  answer_judge=False)
QUESTION = "Dois-je désigner un DPO ?"


def rag_answer(text="Oui [1].") -> RagAnswer:
    generation = Generation(text, prompt_tokens=100, completion_tokens=10, seconds=0.5, tokens_per_second=20.0, truncated=False)
    return RagAnswer(question=QUESTION, text=text, raw_text=text, extracts=[], refused=False, passages=[], sources=[],
                     citations=CitationCheck(cited=[1], unknown=[]), warnings=[], generation=generation,
                     search_seconds=2.0, generation_seconds=1.0, wait_seconds=12.0)


class Calls:
    """What the faked pipeline was asked to do."""

    def __init__(self):
        self.embedder = self.chat_model = 0
        self.questions: list[str] = []


def run(monkeypatch, settings: Settings, argv: list[str], chat_model_error: LLMError | None = None) -> Calls:
    calls = Calls()

    def fake_embedder(settings, device):
        calls.embedder += 1
        return object()

    def fake_chat_model(settings):
        calls.chat_model += 1
        if chat_model_error:
            raise chat_model_error
        return object()

    def fake_answer(question, index_dir, embedder, chat_model, **kwargs):
        calls.questions.append(question)
        answer = rag_answer()
        if kwargs.get("on_text"):  # without the judge, the answer is streamed as it is written
            kwargs["on_text"](answer.text)
        return answer

    monkeypatch.setattr(ask, "load_settings", lambda: settings)
    monkeypatch.setattr(ask, "make_embedder", fake_embedder)
    monkeypatch.setattr(ask, "make_chat_model", fake_chat_model)
    monkeypatch.setattr(ask, "answer_question", fake_answer)
    monkeypatch.setattr("sys.argv", ["ask.py", *argv])
    return calls


def test_remote_mode_warns_before_the_answer_and_names_the_model_after_it(monkeypatch, capsys):
    calls = run(monkeypatch, LOCAL, ["--backend", "openai", "--model", "qwen/qwen3.8-27b", QUESTION])

    assert ask.main() == 0
    out = capsys.readouterr().out
    notice = out.index("Mode distant : votre question et les extraits de loi sont envoyés à Groq (qwen/qwen3.8-27b). "
                       "N'y mettez aucune donnée personnelle.")
    assert notice < out.index("Question :") < out.index("Oui [1].")
    assert out.index("Oui [1].") < out.index("Réponse rédigée par qwen/qwen3.8-27b, modèle distant servi par Groq.")
    assert "attente des limites de l'API 12 s (non comptée)" in out
    assert calls.questions == [QUESTION]


def test_local_mode_has_no_notice_and_signs_as_local(monkeypatch, capsys):
    run(monkeypatch, LOCAL, [QUESTION])

    assert ask.main() == 0
    out = capsys.readouterr().out
    assert "Mode distant" not in out
    assert "Réponse rédigée par qwen3:4b-instruct, modèle local (Ollama)" in out


@pytest.mark.parametrize(
    ("question", "kind"),
    [
        ("Puis-je garder l'adresse jean.dupont@example.org d'un ancien client ?", "une adresse e-mail"),
        ("Un adhérent, 06 12 34 56 78, demande l'effacement.", "un numéro de téléphone"),
        ("Dois-je chiffrer l'IBAN FR76 3000 6000 0112 3456 7890 189 ?", "un IBAN"),
        ("Le NIR 1 85 05 78 006 084 36 est-il une donnée sensible ?", "un numéro de sécurité sociale"),
    ],
)
def test_remote_mode_refuses_personal_data_before_building_or_calling_anything(monkeypatch, capsys, question, kind):
    calls = run(monkeypatch, REMOTE, [question])

    assert ask.main() == 2
    out = capsys.readouterr().out
    assert f"[REFUS] La question contient {kind} : en mode distant, rien n'a été envoyé à Groq." in out
    assert "--backend ollama" in out and "Mode distant :" not in out
    assert calls.embedder == 0 and calls.chat_model == 0 and calls.questions == []
    for value in ("jean.dupont@example.org", "06 12 34 56 78", "3456 7890", "006 084 36"):
        assert value not in out  # the data is never repeated


def test_local_mode_never_blocks(monkeypatch, capsys):
    calls = run(monkeypatch, LOCAL, ["Puis-je garder l'adresse jean.dupont@example.org d'un ancien client ?"])

    assert ask.main() == 0
    assert calls.questions and "[REFUS]" not in capsys.readouterr().out


def test_a_missing_key_is_a_clear_error_before_any_question_is_sent(monkeypatch, capsys):
    error = LLMError("Clé absente : ajoutez TEST_LLM_API_KEY=… dans le fichier .env, ou revenez au mode local avec --backend ollama.")
    calls = run(monkeypatch, REMOTE, [QUESTION], chat_model_error=error)

    assert ask.main() == 1
    out = capsys.readouterr().out
    assert "[ERREUR] Clé absente" in out and "--backend ollama" in out and calls.questions == []


def test_helpers():
    assert ask.provider(REMOTE) == "Groq"
    assert ask.provider(Settings(ollama_base_url="", llm_model="m", embedding_model="e", llm_api_base_url="https://api.example.test/v1")) == "api.example.test"
    assert ask.blocked_message(QUESTION, REMOTE) is None
    assert ask.apply_overrides(LOCAL, None, None) is LOCAL
    assert ask.apply_overrides(LOCAL, "openai", None).llm_backend == "openai" and ask.apply_overrides(LOCAL, "openai", None).llm_model == LOCAL.llm_model

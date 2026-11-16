"""Offline tests for scripts/ask.py in remote mode: the notice, the signature, the model of the chosen mode, the
refusal of personal data (raised by the core, only shown by the script) and the clear errors. No index, no Ollama,
no API: everything the script calls is faked, except the guard itself, which the fake answer_question runs first
exactly as rag.answer_question does."""

import dataclasses
import importlib.util
from pathlib import Path

import pytest
from conftest import FakeChatModel

from compliance_copilot.config import Settings
from compliance_copilot.llm import Generation, LLMError
from compliance_copilot.privacy import refuse_personal_data
from compliance_copilot.rag import CitationCheck, RagAnswer

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ask.py"
spec = importlib.util.spec_from_file_location("ask", SCRIPT)
ask = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ask)

LOCAL = Settings(ollama_base_url="http://localhost:11434", llm_model="qwen3:4b-instruct", embedding_model="bge-m3", answer_judge=False)
REMOTE = dataclasses.replace(LOCAL, llm_backend="openai", llm_api_base_url="https://api.groq.com/openai/v1", llm_api_key_env="TEST_LLM_API_KEY")
QUESTION = "Dois-je désigner un DPO ?"


def rag_answer(text="Oui [1].") -> RagAnswer:
    generation = Generation(text, prompt_tokens=100, completion_tokens=10, seconds=0.5, tokens_per_second=20.0, truncated=False)
    return RagAnswer(question=QUESTION, text=text, raw_text=text, extracts=[], refused=False, passages=[], sources=[],
                     citations=CitationCheck(cited=[1], unknown=[]), warnings=[], generation=generation,
                     search_seconds=2.0, generation_seconds=1.0, wait_seconds=12.0)


class Calls:
    """What the faked pipeline was asked to do."""

    def __init__(self):
        self.embedder = 0
        self.chat_models: list[FakeChatModel] = []  # the fake clients built, with what they received in .messages
        self.questions: list[str] = []  # the questions that reached the search and the model


def run(monkeypatch, settings: Settings, argv: list[str], chat_model_error: LLMError | None = None) -> Calls:
    calls = Calls()

    def fake_embedder(settings, device):
        calls.embedder += 1
        return object()

    def fake_chat_model(settings):
        if chat_model_error:
            raise chat_model_error
        model = FakeChatModel()
        model.model, model.remote = settings.generation_model, settings.remote
        model.provider = "Groq" if settings.remote else "Ollama"
        calls.chat_models.append(model)
        return model

    def fake_answer(question, index_dir, embedder, chat_model, **kwargs):
        refuse_personal_data(question, chat_model)  # the first thing rag.answer_question does
        calls.questions.append(question)
        answer = rag_answer()
        chat_model.generate([{"role": "user", "content": question}], on_text=kwargs.get("on_text"))
        return answer

    monkeypatch.setattr(ask, "load_settings", lambda: settings)
    monkeypatch.setattr(ask, "make_embedder", fake_embedder)
    monkeypatch.setattr(ask, "make_chat_model", fake_chat_model)
    monkeypatch.setattr(ask, "answer_question", fake_answer)
    monkeypatch.setattr("sys.argv", ["ask.py", *argv])
    return calls


def test_remote_mode_warns_before_the_answer_and_names_the_model_after_it(monkeypatch, capsys):
    calls = run(monkeypatch, LOCAL, ["--backend", "openai", QUESTION])  # no --model: LLM_API_MODEL, qwen/qwen3.8-27b

    assert ask.main() == 0
    out = capsys.readouterr().out
    notice = out.index("Mode distant : votre question et les extraits de loi sont envoyés à Groq (qwen/qwen3.8-27b). "
                       "N'y mettez aucune donnée personnelle.")
    assert notice < out.index("Question :") < out.index("Oui [1].")
    assert out.index("Oui [1].") < out.index("Réponse rédigée par qwen/qwen3.8-27b, modèle distant servi par Groq.")
    assert "attente des limites de l'API 12 s (non comptée)" in out
    assert calls.questions == [QUESTION]
    assert [model.model for model in calls.chat_models] == ["qwen/qwen3.8-27b"]  # the fake client was built for the remote model


def test_model_option_replaces_the_model_of_the_chosen_mode(monkeypatch, capsys):
    calls = run(monkeypatch, LOCAL, ["--backend", "openai", "--model", "other/remote-model", QUESTION])
    assert ask.main() == 0 and [model.model for model in calls.chat_models] == ["other/remote-model"]
    assert "Réponse rédigée par other/remote-model, modèle distant servi par Groq." in capsys.readouterr().out

    calls = run(monkeypatch, LOCAL, ["--model", "ministral-3:3b", QUESTION])
    assert ask.main() == 0 and [model.model for model in calls.chat_models] == ["ministral-3:3b"]
    assert "Réponse rédigée par ministral-3:3b, modèle local (Ollama)" in capsys.readouterr().out


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
def test_remote_mode_shows_the_refusal_of_the_core_and_nothing_reaches_the_client(monkeypatch, capsys, question, kind):
    calls = run(monkeypatch, REMOTE, [question])

    assert ask.main() == 2
    out = capsys.readouterr().out
    assert f"[REFUS] La question contient {kind} : en mode distant, rien n'a été envoyé à Groq." in out
    assert "--backend ollama" in out
    assert calls.questions == []  # the guard stopped the question before the search
    assert [model.messages for model in calls.chat_models] == [[]]  # the fake client received nothing
    refusal = out[out.index("[REFUS]"):]  # the question itself is echoed above, on the user's own screen
    for value in ("jean.dupont@example.org", "06 12 34 56 78", "3456 7890", "006 084 36"):
        assert value not in refusal  # the refusal never repeats the data


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


def test_overrides_touch_only_the_model_of_the_chosen_mode():
    assert ask.apply_overrides(LOCAL, None, None) is LOCAL
    remote = ask.apply_overrides(LOCAL, "openai", None)
    assert remote.llm_backend == "openai" and remote.generation_model == "qwen/qwen3.8-27b" and remote.llm_model == LOCAL.llm_model
    remote = ask.apply_overrides(LOCAL, "openai", "other/remote-model")
    assert remote.llm_api_model == "other/remote-model" and remote.llm_model == LOCAL.llm_model
    local = ask.apply_overrides(REMOTE, "ollama", "ministral-3:3b")
    assert local.llm_model == "ministral-3:3b" and local.llm_api_model == REMOTE.llm_api_model
    assert ask.apply_overrides(LOCAL, None, "ministral-3:3b").llm_model == "ministral-3:3b"

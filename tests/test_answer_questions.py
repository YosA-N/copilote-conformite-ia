"""Offline tests for scripts/answer_questions.py: the times line, and the answers kept when a stopped run resumes."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace

from compliance_copilot.llm import Generation
from compliance_copilot.rag import CitationCheck, RagAnswer

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "answer_questions.py"
spec = importlib.util.spec_from_file_location("answer_questions", SCRIPT)
answer_questions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(answer_questions)

TIMES = "Temps : recherche 2.4 s · génération 47.1 s (2880 tokens lus, 521 écrits, 35.6 tokens/s) · contrôle de pertinence 5.3 s"
ANSWERS_FILE = f"""# Réponses du copilote — v9

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
| q01 | Dois-je désigner un DPO ? | 2/2 | non | — | 55 s |
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 14 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui [1].

{TIMES}

## h01 — Quel est le taux de TVA en France ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

Temps : recherche 1.0 s · génération 10.0 s (2000 tokens lus, 20 écrits, 30.0 tokens/s)
"""


def rag_answer(reasoning: str = "", wait_seconds: float = 0.0, judge_seconds: float = 4.5) -> RagAnswer:
    generation = Generation("Oui [1].", prompt_tokens=2880, completion_tokens=521, seconds=47.1, tokens_per_second=35.6,
                            truncated=False, reasoning=reasoning)
    return RagAnswer(
        question="Dois-je désigner un DPO ?", text="Oui [1].", raw_text="EXTRAITS :\n\nRÉPONSE :\nOui [1].", extracts=[],
        refused=False, passages=[], sources=[], citations=CitationCheck(cited=[1], unknown=[]), warnings=[],
        generation=generation, search_seconds=2.4, generation_seconds=47.1, judge_seconds=judge_seconds, wait_seconds=wait_seconds,
    )


def test_times_line_names_the_reasoning_and_the_api_waits_only_when_there_are_some():
    assert answer_questions.times_line(rag_answer()) == (
        "Temps : recherche 2.4 s · génération 47.1 s (2880 tokens lus, 521 écrits, 35.6 tokens/s) · contrôle de pertinence 4.5 s"
    )
    assert answer_questions.times_line(rag_answer(reasoning="un deux trois", wait_seconds=12.0, judge_seconds=0)) == (
        "Temps : recherche 2.4 s · génération 47.1 s (2880 tokens lus, 521 écrits, raisonnement ≈ 3 mots, 35.6 tokens/s)"
        " · attente des limites de l'API 12 s (non comptée)"
    )


def test_previous_answers_keep_each_section_with_its_summary_row():
    previous = answer_questions.previous_answers(ANSWERS_FILE)

    assert list(previous) == ["q01", "h01"]
    row, lines = previous["q01"]
    assert row == "| q01 | Dois-je désigner un DPO ? | 2/2 | non | — | 55 s |"
    assert lines[0] == "## q01 — Dois-je désigner un DPO ?" and lines[-2] == TIMES and lines[-1] == ""
    assert "## h01" not in "\n".join(lines)
    assert previous["h01"][1][-2] == "Temps : recherche 1.0 s · génération 10.0 s (2000 tokens lus, 20 écrits, 30.0 tokens/s)"


def test_a_section_without_a_summary_row_is_not_kept():
    text = ANSWERS_FILE.replace("| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 14 s |\n", "")

    assert list(answer_questions.previous_answers(text)) == ["q01"]


def test_sections_written_are_read_back_whole_when_resuming():
    question = SimpleNamespace(id="q01", question="Dois-je désigner un DPO ?", expected=["gdpr:art_37"])
    answer = rag_answer(reasoning="je réfléchis un peu")
    lines, row = answer_questions.section(question, answer), answer_questions.summary_row(question, answer)
    text = "\n".join(["# Réponses", "", "| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |",
                      "|---|---|---|---|---|---|", row, ""] + lines)

    previous = answer_questions.previous_answers(text)

    assert list(previous) == ["q01"] and previous["q01"][0] == row
    assert "\n".join(previous["q01"][1]) == "\n".join(lines)
    assert "Raisonnement renvoyé par l'API (4 mots" in text and "raisonnement ≈ 4 mots" in text
    assert row == "| q01 | Dois-je désigner un DPO ? | 0/0 | non | — | 54 s |"

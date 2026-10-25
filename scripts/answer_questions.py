"""Ask the copilot every test question and write the raw answers to eval/answers_<version>.md.

The answers are written as they come, without any change, so that a person can review them.
The same pipeline as scripts/ask.py is used. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\answer_questions.py [--version v1]
    .venv\\Scripts\\python scripts\\answer_questions.py --questions eval\\questions_v1.jsonl --version heldout_v3
"""

import argparse
import json
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import describe_reference, first_hit_rank, load_questions
from compliance_copilot.index import IndexNotReadyError
from compliance_copilot.llm import LLMError, make_chat_model
from compliance_copilot.rag import RagAnswer, answer_question, render_footer
from compliance_copilot.sources import SOURCES

QUESTION_FILES = [EVAL_DIR / "questions_v0.jsonl", EVAL_DIR / "questions_offtopic_v0.jsonl"]
WARNING = (
    "> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version "
    "expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme "
    "information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel "
    "ou à la CNIL."
)


def ollama_version(base_url: str) -> str:
    try:
        with urllib.request.urlopen(f"{base_url}/api/version", timeout=5) as response:
            return json.load(response)["version"]
    except (OSError, ValueError, KeyError):
        return "inconnue"


def quoted(text: str) -> str:
    """The answer as a Markdown quote, line by line, without any other change."""
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def section(question, answer: RagAnswer) -> list[str]:
    generation = answer.generation
    passage_ids = [passage.id for passage in answer.passages]
    if question.expected:
        rank = first_hit_rank(passage_ids, question.expected)
        expected = " ou ".join(describe_reference(ref) for ref in question.expected)
        found = f"passage [{rank}]" if rank else "absent des passages donnés au modèle"
        expectation = f"Article attendu : {expected} — {found}."
    else:
        expectation = "Question hors sujet : aucun article attendu, le copilote devrait refuser."
    return [
        f"## {question.id} — {question.question}",
        "",
        expectation,
        "",
        "### Réponse du copilote",
        "",
        quoted(answer.text),
        "",
        "### Extraits, sources, contrôles et avertissement (ajoutés par le code)",
        "",
        "```text",
        render_footer(answer),
        "```",
        "",
        "<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>",
        "",
        "```text",
        answer.raw_text.strip(),
        "```",
        "",
        "</details>",
        "",
        f"Temps : recherche {answer.search_seconds:.1f} s · génération {answer.generation_seconds:.1f} s "
        f"({generation.prompt_tokens} tokens lus, {generation.completion_tokens} écrits, {generation.tokens_per_second:.1f} tokens/s)",
        "",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Écrit les réponses du copilote aux questions de test.")
    parser.add_argument("--version", default="v1", help="suffixe du fichier écrit : eval/answers_<version>.md")
    parser.add_argument("--questions", type=Path, nargs="+", default=QUESTION_FILES,
                        help="fichiers de questions à poser (par défaut : questions v0 et hors sujet v0)")
    args = parser.parse_args()
    output = EVAL_DIR / f"answers_{args.version}.md"

    settings = load_settings()
    embedder = make_embedder(settings, settings.query_embedding_device)
    chat_model = make_chat_model(settings)
    question_sets = [(path, load_questions(path)) for path in args.questions]
    questions = [question for _, loaded in question_sets for question in loaded]

    sections, summary = [], []
    for question in questions:
        print(f"{question.id} : {question.question}", flush=True)
        try:
            answer = answer_question(
                question.question, INDEX_DIR, embedder, chat_model, mode=settings.search_mode, lexicon=settings.search_lexicon,
                max_per_article=settings.search_max_per_article,
            )
        except (IndexNotReadyError, EmbeddingError, LLMError) as error:
            print(f"[ERREUR] {error}")
            return 1
        sections += section(question, answer)
        alerts = "; ".join(answer.warnings) if answer.warnings else "—"
        verified = f"{len(answer.verified_extracts)}/{len(answer.extracts)}"
        total = answer.search_seconds + answer.generation_seconds
        summary.append(f"| {question.id} | {question.question} | {verified} | {'oui' if answer.refused else 'non'} | {alerts} | {total:.0f} s |")
        print(f"     {total:.0f} s, extraits vérifiés {verified}, refus : {'oui' if answer.refused else 'non'}", flush=True)

    versions = ", ".join(f"{source.name} du {source.version_date}" for source in SOURCES)
    if settings.llm_num_gpu is None:
        gpu = "choix d'Ollama"
    else:
        gpu = "toutes" if settings.llm_num_gpu >= 99 else str(settings.llm_num_gpu)
    header = [
        f"# Réponses du copilote — {args.version}",
        "",
        WARNING,
        "",
        f"Générées le {datetime.now():%d/%m/%Y à %H:%M} par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.",
        "",
        f"- Génération : `{settings.llm_model}` via Ollama {ollama_version(settings.ollama_base_url)} — température "
        f"{settings.llm_temperature}, contexte {settings.llm_num_ctx} tokens, couches sur la carte graphique : {gpu}, "
        f"{settings.llm_max_tokens} tokens au plus par réponse",
        "- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles "
        "seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié",
        "- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), "
        "affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » "
        "absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, "
        "règlement non nommé quand la réponse mêle RGPD et AI Act",
        f"- Recherche : `{settings.embedding_model}` (sur {settings.query_embedding_device.upper()}), mode « {settings.search_mode} », "
        f"lexique « {settings.search_lexicon} », 5 passages par question, "
        + (f"{settings.search_max_per_article} au plus par article" if settings.search_max_per_article else "sans limite par article"),
        f"- Corpus : versions consolidées {versions}",
        "- Questions : " + ", ".join(
            f"`eval/{path.name}` ({sum(1 for q in loaded if q.expected)}"
            + (f" + {sum(1 for q in loaded if not q.expected)} hors sujet" if any(not q.expected for q in loaded) else "") + ")"
            for path, loaded in question_sets
        ),
        "",
        "| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |",
        "|---|---|---|---|---|---|",
        *summary,
        "",
    ]
    output.write_text("\n".join(header + sections), encoding="utf-8")
    print(f"\n[OK] {len(questions)} réponses écrites dans eval\\{output.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

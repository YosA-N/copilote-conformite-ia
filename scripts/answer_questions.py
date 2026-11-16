"""Ask the copilot every test question and write the raw answers to eval/answers_<version>.md.

The answers are written as they come, without any change, so that a person can review them.
The same pipeline as scripts/ask.py is used. Run scripts/build_index.py first.
The file is rewritten after every answer, so that nothing is lost if the run stops (for example when the
quota of an API is used up); --resume then keeps the answers already in the file and asks the other questions.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\answer_questions.py [--version v1]
    .venv\\Scripts\\python scripts\\answer_questions.py --questions eval\\questions_v1.jsonl --version heldout_v3
    .venv\\Scripts\\python scripts\\answer_questions.py --backend openai --reasoning-effort none --version v4_big_qwen27b
"""

import argparse
import dataclasses
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, LLM_BACKENDS, Settings, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import describe_reference, first_hit_rank, load_questions
from compliance_copilot.index import IndexNotReadyError
from compliance_copilot.llm import LLMError, make_chat_model
from compliance_copilot.rag import ABSTENTION, RagAnswer, answer_question, render_footer
from compliance_copilot.sources import SOURCES

QUESTION_FILES = [EVAL_DIR / "questions_v0.jsonl", EVAL_DIR / "questions_offtopic_v0.jsonl"]
WARNING = (
    "> ⚠️ **Attention : certaines réponses de ce fichier sont fausses.** Ce sont les réponses brutes d'une version "
    "expérimentale du copilote, conservées telles quelles pour mesurer ses erreurs. Ne les utilisez pas comme "
    "information juridique : reportez-vous aux textes officiels sur EUR-Lex et, en cas de doute, à un professionnel "
    "ou à la CNIL."
)
SECTION_TITLE = re.compile(r"^## (\w+) — ", re.MULTILINE)
SUMMARY_ROW = re.compile(r"^\| (\w+) \| .* \| \d+ s \|$")


def ollama_version(base_url: str) -> str:
    try:
        with urllib.request.urlopen(f"{base_url}/api/version", timeout=5) as response:
            return json.load(response)["version"]
    except (OSError, ValueError, KeyError):
        return "inconnue"


def quoted(text: str) -> str:
    """The answer as a Markdown quote, line by line, without any other change."""
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def times_line(answer: RagAnswer) -> str:
    """The times of one answer, in the format read back by scripts/compare_answers.py."""
    generation = answer.generation
    return (
        f"Temps : recherche {answer.search_seconds:.1f} s · génération {answer.generation_seconds:.1f} s "
        f"({generation.prompt_tokens} tokens lus, {generation.completion_tokens} écrits"
        + (f", raisonnement ≈ {len(generation.reasoning.split())} mots" if generation.reasoning else "")
        + f", {generation.tokens_per_second:.1f} tokens/s)"
        + (f" · contrôle de pertinence {answer.judge_seconds:.1f} s" if answer.judge_seconds else "")
        + (f" · attente des limites de l'API {answer.wait_seconds:.0f} s (non comptée)" if answer.wait_seconds else "")
    )


def section(question, answer: RagAnswer) -> list[str]:
    passage_ids = [passage.id for passage in answer.passages]
    if question.expected:
        rank = first_hit_rank(passage_ids, question.expected)
        expected = " ou ".join(describe_reference(ref) for ref in question.expected)
        found = f"passage [{rank}]" if rank else "absent des passages donnés au modèle"
        expectation = f"Article attendu : {expected} — {found}."
    else:
        expectation = "Question hors sujet : aucun article attendu, le copilote devrait refuser."
    lines = [
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
    ]
    reasoning = answer.generation.reasoning.strip()
    if reasoning:
        lines += [
            f"<details><summary>Raisonnement renvoyé par l'API ({len(reasoning.split())} mots, non affiché à l'utilisateur, "
            "compté dans les tokens écrits)</summary>",
            "",
            "```text",
            reasoning,
            "```",
            "",
            "</details>",
            "",
        ]
    return lines + [times_line(answer), ""]


def refusal_label(answer: RagAnswer) -> str:
    return "oui" if answer.refused else "abstention" if answer.abstained else "non"


def summary_row(question, answer: RagAnswer) -> str:
    alerts = "; ".join(answer.warnings) if answer.warnings else "—"
    verified = f"{len(answer.verified_extracts)}/{len(answer.extracts)}"
    total = answer.search_seconds + answer.generation_seconds + answer.judge_seconds
    return f"| {question.id} | {question.question} | {verified} | {refusal_label(answer)} | {alerts} | {total:.0f} s |"


def previous_answers(text: str) -> dict[str, tuple[str, list[str]]]:
    """The answers already in an answers file: id → (summary row, section lines), to resume a stopped run."""
    rows = {match.group(1): line for line in text.splitlines() if (match := SUMMARY_ROW.match(line))}
    titles = list(SECTION_TITLE.finditer(text))
    answers = {}
    for index, title in enumerate(titles):
        end = titles[index + 1].start() if index + 1 < len(titles) else len(text)
        if title.group(1) in rows:
            answers[title.group(1)] = (rows[title.group(1)], text[title.start():end].rstrip("\n").splitlines() + [""])
    return answers


def generation_line(settings: Settings) -> str:
    if settings.llm_backend == "ollama":
        if settings.llm_num_gpu is None:
            gpu = "choix d'Ollama"
        else:
            gpu = "toutes" if settings.llm_num_gpu >= 99 else str(settings.llm_num_gpu)
        return (
            f"- Génération : `{settings.generation_model}` via Ollama {ollama_version(settings.ollama_base_url)} — température "
            f"{settings.llm_temperature}, contexte {settings.llm_num_ctx} tokens, couches sur la carte graphique : {gpu}, "
            f"{settings.llm_max_tokens} tokens au plus par réponse"
        )
    effort = settings.llm_api_reasoning_effort
    return (
        f"- Génération : `{settings.generation_model}` via l'API compatible OpenAI {settings.llm_api_base_url} (expérience de la "
        "séance 7, questions de test seulement ; modèle tel que servi par l'API à la date ci-dessus) — température "
        f"{settings.llm_temperature}, raisonnement : {'« ' + effort + ' » (reasoning_effort)' if effort else 'réglage par défaut du modèle'}, "
        f"passages calculés pour un contexte de {settings.llm_num_ctx} tokens comme en local, {settings.llm_max_tokens} tokens au plus "
        "par réponse (raisonnement compris) ; le juge est le même modèle"
    )


def header(settings: Settings, version: str, question_sets: list, summary: list[str], kept: int) -> list[str]:
    versions = ", ".join(f"{source.name} du {source.version_date}" for source in SOURCES)
    lines = [
        f"# Réponses du copilote — {version}",
        "",
        WARNING,
        "",
        f"Générées le {datetime.now():%d/%m/%Y à %H:%M} par `scripts/answer_questions.py`, **sans aucune retouche**, pour relecture.",
        "",
        generation_line(settings),
        "- Prompt : le modèle recopie d'abord les phrases exactes des passages (EXTRAITS), puis répond à partir d'elles "
        "seulement (RÉPONSE) ; le code vérifie chaque extrait mot pour mot et remplace par un refus une réponse sans extrait vérifié",
        "- Contrôles du code sur la réponse : citations [n], phrases trop éloignées des extraits vérifiés (si aucune citation), "
        "affirmations d'absence sans extrait négatif, tutoiement, négation ajoutée ou retirée dans une exception, texte entre « » "
        "absent des extraits, exception reformulée, liste de cas incomplète, obligation d'un fournisseur sans le nommer, "
        "règlement non nommé quand la réponse mêle RGPD et AI Act",
        f"- Recherche : `{settings.embedding_model}` (sur {settings.query_embedding_device.upper()}), mode « {settings.search_mode} », "
        f"lexique « {settings.search_lexicon} », {settings.search_k} passages par question, "
        + (f"{settings.search_max_per_article} au plus par article" if settings.search_max_per_article else "sans limite par article")
        + (", 1er paragraphe ajouté quand un paragraphe suivant d'un article découpé est retenu" if settings.search_first_paragraph else ""),
        "- Contrôle de pertinence (juge) : "
        + ("activé ; si le modèle juge que les extraits ne répondent pas directement à la question, la réponse est remplacée par "
           f"« {ABSTENTION} »" if settings.answer_judge else "désactivé"),
        f"- Corpus : versions consolidées {versions}",
        "- Questions : " + ", ".join(
            f"`eval/{path.name}` ({sum(1 for q in loaded if q.expected)}"
            + (f" + {sum(1 for q in loaded if not q.expected)} hors sujet" if any(not q.expected for q in loaded) else "") + ")"
            for path, loaded in question_sets
        ),
    ]
    if kept:
        lines.append(
            f"- Reprise : {kept} réponse(s) conservée(s) d'une série précédente arrêtée en cours de route (par exemple par le quota "
            f"de l'API), {len(summary) - kept} générée(s) à la date ci-dessus"
        )
    return lines + ["", "| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |", "|---|---|---|---|---|---|", *summary, ""]


def main() -> int:
    parser = argparse.ArgumentParser(description="Écrit les réponses du copilote aux questions de test.")
    parser.add_argument("--version", default="v1", help="suffixe du fichier écrit : eval/answers_<version>.md")
    parser.add_argument("--questions", type=Path, nargs="+", default=QUESTION_FILES,
                        help="fichiers de questions à poser (par défaut : questions v0 et hors sujet v0)")
    parser.add_argument("--backend", choices=LLM_BACKENDS, help="moteur de génération, à la place de LLM_BACKEND du .env")
    parser.add_argument("--model", help="modèle, à la place de LLM_API_MODEL (mode distant) ou de LLM_MODEL (mode local) du .env")
    parser.add_argument("--reasoning-effort", help="reasoning_effort envoyé à l'API (none, low…), à la place de LLM_API_REASONING_EFFORT")
    parser.add_argument("--resume", action="store_true",
                        help="garder les réponses déjà dans le fichier et ne poser que les questions qui manquent")
    args = parser.parse_args()
    output = EVAL_DIR / f"answers_{args.version}.md"

    settings = load_settings()
    if args.backend:
        settings = dataclasses.replace(settings, llm_backend=args.backend)
    if args.model:  # the model of the chosen mode
        settings = dataclasses.replace(settings, **{"llm_api_model" if settings.remote else "llm_model": args.model})
    if args.reasoning_effort is not None:
        settings = dataclasses.replace(settings, llm_api_reasoning_effort=args.reasoning_effort.strip().lower())
    if settings.remote:
        print(f"[API] Modèle distant {settings.generation_model} ({settings.llm_api_base_url}) : questions de test seulement, "
              "aucune donnée personnelle.", flush=True)
    embedder = make_embedder(settings, settings.query_embedding_device)
    chat_model = make_chat_model(settings)
    question_sets = [(path, load_questions(path)) for path in args.questions]
    questions = [question for _, loaded in question_sets for question in loaded]

    previous = previous_answers(output.read_text(encoding="utf-8")) if args.resume and output.exists() else {}
    kept = {question.id: previous[question.id] for question in questions if question.id in previous}
    if args.resume:
        print(f"[REPRISE] {len(kept)} réponse(s) conservée(s) de eval\\{output.name}, {len(questions) - len(kept)} à générer", flush=True)
    rows = {id_: row for id_, (row, _) in kept.items()}
    sections = {id_: lines for id_, (_, lines) in kept.items()}

    def write() -> None:
        summary = [rows[question.id] for question in questions if question.id in rows]
        body = [line for question in questions if question.id in sections for line in sections[question.id]]
        output.write_text("\n".join(header(settings, args.version, question_sets, summary, len(kept)) + body), encoding="utf-8")

    for question in questions:
        if question.id in kept:
            continue
        print(f"{question.id} : {question.question}", flush=True)
        try:
            answer = answer_question(
                question.question, INDEX_DIR, embedder, chat_model, k=settings.search_k, mode=settings.search_mode,
                lexicon=settings.search_lexicon, max_per_article=settings.search_max_per_article, judge=settings.answer_judge,
                first_paragraph=settings.search_first_paragraph,
            )
        except (IndexNotReadyError, EmbeddingError, LLMError) as error:
            print(f"[ERREUR] {error}")
            if rows:
                print(f"[INFO] {len(rows)} réponse(s) déjà écrite(s) dans eval\\{output.name} : relancez avec --resume pour continuer.")
            return 1
        sections[question.id], rows[question.id] = section(question, answer), summary_row(question, answer)
        write()  # after every answer, so that a stopped run keeps what was done
        verified = f"{len(answer.verified_extracts)}/{len(answer.extracts)}"
        total = answer.search_seconds + answer.generation_seconds + answer.judge_seconds
        print(f"     {total:.0f} s, extraits vérifiés {verified}, refus : {refusal_label(answer)}"
              + (f", attente de l'API {answer.wait_seconds:.0f} s" if answer.wait_seconds else ""), flush=True)

    write()
    print(f"\n[OK] {len(rows)} réponses écrites dans eval\\{output.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

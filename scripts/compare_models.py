"""Compare language models (or prompts) on the same passages: verified extracts, refusals, citations, alerts,
length, time.

Every question is searched once; each model then answers from exactly the same passages.
With --prompt-file, the models use that system prompt instead of the current one (for example the
prompt of an earlier session, taken from Git), so that two prompts can be compared on the same day,
on the same passages. The details are saved to data/processed/model_comparison.json (not versioned)
and Markdown tables are printed. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_models.py ministral-3:3b qwen3:4b-instruct
    .venv\\Scripts\\python scripts\\compare_models.py qwen3:4b-instruct --prompt-file prompt_v1.txt --output data\\processed\\prompt_v1.json
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from statistics import median

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, PROCESSED_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import article_level, load_questions, matches
from compliance_copilot.index import IndexNotReadyError, search
from compliance_copilot.llm import LLMError, OllamaChatModel
from compliance_copilot.rag import SYSTEM_PROMPT, answer_from_passages, fit_passages, uses_tu

QUESTION_FILES = ["questions_v0.jsonl", "questions_offtopic_v0.jsonl", "questions_v1.jsonl"]
OUTPUT = PROCESSED_DIR / "model_comparison.json"


def alert_kind(warning: str) -> str:
    """'La réponse ne reprend que 0 des 3 cas…' → 'La réponse ne reprend que N des N cas…': the alert without its details."""
    return " ".join(re.sub(r"\d+", "N", warning).split()[:9]) + " …"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare des modèles (ou des prompts) sur les mêmes passages.")
    parser.add_argument("models", nargs="*", default=["ministral-3:3b", "qwen3:4b-instruct"])
    parser.add_argument("--prompt-file", type=Path, help="prompt système à utiliser à la place du prompt actuel")
    parser.add_argument("--output", type=Path, default=OUTPUT, help="fichier JSON du détail par question")
    args = parser.parse_args()
    system_prompt = args.prompt_file.read_text(encoding="utf-8").strip() if args.prompt_file else SYSTEM_PROMPT

    settings = load_settings()
    chat_models = [
        OllamaChatModel(settings.ollama_base_url, name, num_ctx=settings.llm_num_ctx, num_gpu=settings.llm_num_gpu,
                        temperature=settings.llm_temperature, max_tokens=settings.llm_max_tokens)
        for name in args.models
    ]
    questions = [question for name in QUESTION_FILES for question in load_questions(EVAL_DIR / name)]
    embedder = make_embedder(settings, settings.query_embedding_device)
    try:
        passages = {
            q.id: fit_passages(q.question, search(q.question, INDEX_DIR, embedder, k=settings.search_k, mode=settings.search_mode,
                                                  lexicon=settings.search_lexicon, max_per_article=settings.search_max_per_article,
                                                  first_paragraph=settings.search_first_paragraph),
                               chat_models[0])
            for q in questions
        }
    except (IndexNotReadyError, EmbeddingError) as error:
        print(f"[ERREUR] {error}")
        return 1

    records = []
    for chat_model in chat_models:  # one model after the other, so that Ollama loads each only once
        for question in questions:
            print(f"{chat_model.model} · {question.id}", file=sys.stderr, flush=True)
            try:
                answer = answer_from_passages(question.question, passages[question.id], chat_model, system_prompt=system_prompt,
                                              judge=settings.answer_judge)
            except LLMError as error:
                print(f"[ERREUR] {error}")
                return 1
            verified_ids = [answer.passages[e.passage - 1].id for e in answer.verified_extracts]
            records.append({
                "model": chat_model.model,
                "prompt": str(args.prompt_file) if args.prompt_file else "actuel",
                "question_id": question.id,
                "question": question.question,
                "off_topic": not question.expected,
                "expected": question.expected,
                "passage_ids": [p.id for p in answer.passages],
                "raw_text": answer.raw_text,
                "answer": answer.text,
                "answer_words": len(answer.text.split()),
                "refused": answer.refused,
                "abstained": answer.abstained,
                "judgment": answer.judgment,
                "found_passages": len(passages[question.id]),
                "extracts": len(answer.extracts),
                "verified_extracts": len(answer.verified_extracts),
                "expected_extract": any(matches(i, ref) for i in verified_ids for ref in article_level(question.expected)),
                "expected_paragraph_extract": any(matches(i, ref) for i in verified_ids for ref in question.expected),
                "cited": answer.citations.cited,  # [n] written in the answer itself
                "tutoiement": uses_tu(answer.text),
                "warnings": answer.warnings,
                "truncated": answer.generation.truncated,
                "prompt_tokens": answer.generation.prompt_tokens,
                "seconds": round(answer.generation_seconds, 1),
                "judge_seconds": round(answer.judge_seconds, 1),
                "tokens_per_second": round(answer.generation.tokens_per_second, 1),
            })
    args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    in_corpus = [q for q in questions if q.expected]
    off_topic = [q for q in questions if not q.expected]
    print(f"Prompt : {args.prompt_file or 'actuel (src/compliance_copilot/rag.py)'}\n")
    print("| Modèle | Réponses données (sur " + str(len(in_corpus)) + ") | Avec un extrait vérifié d'un article attendu | Hors sujet refusés (sur "
          + str(len(off_topic)) + ") | Extraits vérifiés / recopiés | Réponses coupées | Génération moyenne | tokens/s |")
    print("|---|---|---|---|---|---|---|---|")
    for chat_model in chat_models:
        mine = [r for r in records if r["model"] == chat_model.model]
        answered = [r for r in mine if not r["off_topic"] and not r["refused"] and not r["abstained"]]
        print(
            f"| `{chat_model.model}` | {len(answered)} | {sum(r['expected_extract'] for r in mine if not r['off_topic'])} | "
            f"{sum(r['refused'] or r['abstained'] for r in mine if r['off_topic'])} | "
            f"{sum(r['verified_extracts'] for r in mine)} / {sum(r['extracts'] for r in mine)} | "
            f"{sum(r['truncated'] for r in mine)} | {sum(r['seconds'] for r in mine) / len(mine):.1f} s | "
            f"{sum(r['tokens_per_second'] for r in mine) / len(mine):.1f} |"
        )

    print("\n| Modèle | Réponses avec [n] (sur les réponses données) | Tutoiements | Réponses avec au moins une alerte | Alertes "
          "| Réponse moyenne (mots, réponses données) | Prompt lu (tokens, moyenne) |")
    print("|---|---|---|---|---|---|---|")
    for chat_model in chat_models:
        mine = [r for r in records if r["model"] == chat_model.model]
        answered = [r for r in mine if not r["refused"]]
        print(
            f"| `{chat_model.model}` | {sum(bool(r['cited']) for r in answered)} / {len(answered)} | {sum(r['tutoiement'] for r in mine)} | "
            f"{sum(bool(r['warnings']) for r in mine)} / {len(mine)} | {sum(len(r['warnings']) for r in mine)} | "
            f"{sum(r['answer_words'] for r in answered) / max(1, len(answered)):.0f} | {sum(r['prompt_tokens'] for r in mine) / len(mine):.0f} |"
        )

    print("\n| Modèle | Abstentions du juge (dans le corpus · hors sujet) | Paragraphe attendu dans un extrait vérifié "
          "| Temps génération + juge : médian · maximal |")
    print("|---|---|---|---|")
    for chat_model in chat_models:
        mine = [r for r in records if r["model"] == chat_model.model]
        times = sorted(r["seconds"] + r["judge_seconds"] for r in mine)
        print(
            f"| `{chat_model.model}` | {sum(r['abstained'] for r in mine if not r['off_topic'])} · {sum(r['abstained'] for r in mine if r['off_topic'])} | "
            f"{sum(r['expected_paragraph_extract'] for r in mine if not r['off_topic'])} | {median(times):.0f} s · {times[-1]:.0f} s |"
        )

    for chat_model in chat_models:
        kinds = Counter(alert_kind(w) for r in records if r["model"] == chat_model.model for w in r["warnings"])
        print(f"\nAlertes de `{chat_model.model}` par type (nombre de réponses) :\n")
        for kind, count in kinds.most_common():
            questions_with = [r["question_id"] for r in records if r["model"] == chat_model.model and any(alert_kind(w) == kind for w in r["warnings"])]
            print(f"- {count} × {kind} ({', '.join(questions_with)})")
    print(f"\nDétail par question : {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

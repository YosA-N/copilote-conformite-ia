"""Compare language models on the same passages: verified extracts, refusals, time.

Every question is searched once; each model then answers from exactly the same passages.
The details are saved to data/processed/model_comparison.json (not versioned) and a Markdown
table is printed. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_models.py ministral-3:3b qwen3:4b-instruct
"""

import json
import sys

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, PROCESSED_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import load_questions, matches
from compliance_copilot.index import IndexNotReadyError, search
from compliance_copilot.llm import LLMError, OllamaChatModel
from compliance_copilot.rag import answer_from_passages, fit_passages

QUESTION_FILES = ["questions_v0.jsonl", "questions_offtopic_v0.jsonl", "questions_v1.jsonl"]
OUTPUT = PROCESSED_DIR / "model_comparison.json"


def main() -> int:
    models = sys.argv[1:] or ["ministral-3:3b", "qwen3:4b-instruct"]
    settings = load_settings()
    chat_models = [
        OllamaChatModel(settings.ollama_base_url, name, num_ctx=settings.llm_num_ctx, num_gpu=settings.llm_num_gpu,
                        temperature=settings.llm_temperature, max_tokens=settings.llm_max_tokens)
        for name in models
    ]
    questions = [question for name in QUESTION_FILES for question in load_questions(EVAL_DIR / name)]
    embedder = make_embedder(settings, settings.query_embedding_device)
    try:
        passages = {
            q.id: fit_passages(q.question, search(q.question, INDEX_DIR, embedder, k=5, mode=settings.search_mode, lexicon=settings.search_lexicon), chat_models[0])
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
                answer = answer_from_passages(question.question, passages[question.id], chat_model)
            except LLMError as error:
                print(f"[ERREUR] {error}")
                return 1
            verified_ids = [answer.passages[e.passage - 1].id for e in answer.verified_extracts]
            records.append({
                "model": chat_model.model,
                "question_id": question.id,
                "question": question.question,
                "off_topic": not question.expected,
                "expected": question.expected,
                "passage_ids": [p.id for p in answer.passages],
                "raw_text": answer.raw_text,
                "answer": answer.text,
                "refused": answer.refused,
                "extracts": len(answer.extracts),
                "verified_extracts": len(answer.verified_extracts),
                "expected_extract": any(matches(i, ref) for i in verified_ids for ref in question.expected),
                "warnings": answer.warnings,
                "truncated": answer.generation.truncated,
                "seconds": round(answer.generation_seconds, 1),
                "tokens_per_second": round(answer.generation.tokens_per_second, 1),
            })
    OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    in_corpus = [q for q in questions if q.expected]
    off_topic = [q for q in questions if not q.expected]
    print("| Modèle | Réponses données (sur " + str(len(in_corpus)) + ") | Avec un extrait vérifié d'un article attendu | Hors sujet refusés (sur "
          + str(len(off_topic)) + ") | Extraits vérifiés / recopiés | Réponses coupées | Génération moyenne | tokens/s |")
    print("|---|---|---|---|---|---|---|---|")
    for chat_model in chat_models:
        mine = [r for r in records if r["model"] == chat_model.model]
        answered = [r for r in mine if not r["off_topic"] and not r["refused"]]
        print(
            f"| `{chat_model.model}` | {len(answered)} | {sum(r['expected_extract'] for r in mine if not r['off_topic'])} | "
            f"{sum(r['refused'] for r in mine if r['off_topic'])} | {sum(r['verified_extracts'] for r in mine)} / {sum(r['extracts'] for r in mine)} | "
            f"{sum(r['truncated'] for r in mine)} | {sum(r['seconds'] for r in mine) / len(mine):.1f} s | "
            f"{sum(r['tokens_per_second'] for r in mine) / len(mine):.1f} |"
        )
    print(f"\nDétail par question : {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

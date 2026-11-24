"""Compare several search configurations on the question sets (hit@1, hit@5, ranks), by set and in total.

Two levels: the article, and the paragraph when a question names the one that matters (session 6).
Prints Markdown tables. The question vectors computed by Ollama on the CPU vary very slightly
from one run to the next, which can swap two passages with almost the same score: with
--repeat N, everything is measured N times and a varying result is shown as a range ("11–12").
The query rewriting is asked again at each run (the model's reply may vary too); with --rewrite-log,
the terms it gave are written to a JSON file. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_retrieval.py [--repeat 3]
    .venv\\Scripts\\python scripts\\compare_retrieval.py --repeat 3 --configs current,nolex,rerank,rw_local,rw_remote
"""

import argparse
import dataclasses
import json
import sys
from pathlib import Path

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import article_level, first_hit_rank, hit_at_k, load_questions
from compliance_copilot.index import IndexNotReadyError, search
from compliance_copilot.llm import LLMError, make_chat_model
from compliance_copilot.rerank import CrossEncoderReranker, RerankerError
from compliance_copilot.rewrite import rewrite_terms

DEPTH = 20
CURRENT = ("vector", "all", 2, True)  # mode, lexicon, at most 2 chunks per article, first paragraph of a split article
CONFIGS = {  # key: (label, mode, lexicon, limit per article, first paragraph, reranker, query rewriting backend or None)
    "start": ("vecteurs seuls (départ)", "vector", "off", None, False, False, None),
    "lexicon": ("vecteurs + lexique", "vector", "all", None, False, False, None),
    "limit": ("vecteurs + lexique + 2 par article", "vector", "all", 2, False, False, None),
    "current": ("actuelle (lexique + 2 par article + 1er paragraphe)", *CURRENT, False, None),
    "nolex": ("sans lexique (2 par article + 1er paragraphe)", "vector", "off", 2, True, False, None),
    "rerank": ("actuelle + reranker (20 → 5)", *CURRENT, True, None),
    "rw_local": ("actuelle + reformulation locale", *CURRENT, False, "ollama"),
    "rw_remote": ("actuelle + reformulation distante", *CURRENT, False, "openai"),
    "rw_local_rerank": ("actuelle + reformulation locale + reranker", *CURRENT, True, "ollama"),
    "rw_remote_rerank": ("actuelle + reformulation distante + reranker", *CURRENT, True, "openai"),
}
DEFAULT_CONFIGS = ["start", "lexicon", "limit", "current"]
LEVELS = [("article", True), ("paragraphe", False)]
SETS = {"v0": "questions_v0.jsonl", "v1": "questions_v1.jsonl", "v2": "questions_v2.jsonl", "author": "questions_author.jsonl",
        "exam2": "questions_exam2.jsonl"}
# tuning sets, measured by default; exam2 is measured only when asked for (--sets exam2), never while tuning
TUNING_SETS = ["v0", "v1", "v2", "author"]


class CachedReranker:
    """Score each (question, chunk) pair once: the cross-encoder is deterministic, only the embeddings vary."""

    def __init__(self, reranker):
        self.reranker = reranker
        self.model = reranker.model
        self.cache: dict[tuple[str, str], float] = {}

    def score(self, question: str, texts: list[str]) -> list[float]:
        missing = [text for text in texts if (question, text) not in self.cache]
        for text, score in zip(missing, self.reranker.score(question, missing) if missing else []):
            self.cache[question, text] = score
        return [self.cache[question, text] for text in texts]


class CachedEmbedder:
    """Embed each text once, whatever the number of configurations."""

    def __init__(self, embedder):
        self.embedder = embedder
        self.model = embedder.model
        self.cache: dict[str, list[float]] = {}

    def embed(self, texts: list[str]) -> list[list[float]]:
        missing = [text for text in texts if text not in self.cache]
        for text, vector in zip(missing, self.embedder.embed(missing) if missing else []):
            self.cache[text] = vector
        return [self.cache[text] for text in texts]


def spread(values: list) -> str:
    """'11' if every run gave 11, '11–12' if the runs differ."""
    shown = sorted({str(value) for value in values}, key=lambda value: (len(value), value))
    return shown[0] if len(shown) == 1 else f"{shown[0]}–{shown[-1]}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare les configurations de recherche sur les jeux de questions.")
    parser.add_argument("--repeat", type=int, default=1, help="nombre de mesures complètes (3 recommandé)")
    parser.add_argument("--configs", help=f"configurations, séparées par des virgules, parmi : {', '.join(CONFIGS)} "
                                          f"(par défaut : {','.join(DEFAULT_CONFIGS)})")
    parser.add_argument("--sets", default=",".join(TUNING_SETS),
                        help=f"jeux de questions parmi : {', '.join(SETS)} (par défaut : les jeux de réglage {', '.join(TUNING_SETS)} ; "
                             "exam2 seulement pour l'examen, jamais pour régler)")
    parser.add_argument("--rerank", action="store_true", help="ajouter la configuration « rerank » (RERANKER_MODEL, torch requis)")
    parser.add_argument("--rewrite-log", type=Path, help="fichier JSON où écrire les termes donnés par la reformulation")
    args = parser.parse_args()
    keys = args.configs.split(",") if args.configs else list(DEFAULT_CONFIGS)
    if args.rerank and "rerank" not in keys:
        keys.append("rerank")
    unknown = [key for key in keys if key not in CONFIGS] + [name for name in args.sets.split(",") if name not in SETS]
    if unknown:
        print(f"[ERREUR] Inconnu : {', '.join(unknown)}")
        return 2
    configs = [(key, *CONFIGS[key]) for key in keys]
    sets = args.sets.split(",")
    settings = load_settings()
    reranker = CachedReranker(CrossEncoderReranker(settings.reranker_model)) if any(c[6] for c in configs) else None
    rewriters = {backend: make_chat_model(dataclasses.replace(settings, llm_backend=backend))
                 for backend in {c[7] for c in configs if c[7]}}
    question_sets = {name: [q for q in load_questions(EVAL_DIR / SETS[name]) if q.expected] for name in sets}
    runs: list[dict[tuple[str, str, str], list[int | None]]] = []
    rewrite_log: list[dict] = []
    for run in range(args.repeat):
        embedder = CachedEmbedder(make_embedder(settings, settings.query_embedding_device))  # fresh vectors each run
        rewritten: dict[tuple[str, str], list[str]] = {}  # asked again at each run, shared by the configurations of a run
        ranks: dict[tuple[str, str, str], list[int | None]] = {}
        for key, label, mode, lexicon, limit, first_paragraph, rerank, backend in configs:
            print(f"… mesure {run + 1}/{args.repeat} : {label}", file=sys.stderr, flush=True)
            for name, questions in question_sets.items():
                found = []
                for q in questions:
                    try:
                        terms = None
                        if backend:
                            if (backend, q.id) not in rewritten:
                                rewritten[backend, q.id] = rewrite_terms(q.question, rewriters[backend])
                                rewrite_log.append({"run": run + 1, "backend": backend, "id": q.id, "terms": rewritten[backend, q.id]})
                            terms = rewritten[backend, q.id]
                        found.append([r.id for r in search(q.question, INDEX_DIR, embedder, k=DEPTH, mode=mode, lexicon=lexicon,
                                                           max_per_article=limit, first_paragraph=first_paragraph,
                                                           reranker=reranker if rerank else None,
                                                           rerank_candidates=settings.search_rerank_candidates, extra_terms=terms)])
                    except (IndexNotReadyError, EmbeddingError, RerankerError, LLMError) as error:
                        print(f"[ERREUR] {error}")
                        return 1
                for level, by_article in LEVELS:
                    ranks[key, name, level] = [
                        first_hit_rank(ids, article_level(q.expected) if by_article else q.expected) for ids, q in zip(found, questions)
                    ]
        runs.append(ranks)
    if args.rewrite_log:
        args.rewrite_log.write_text(json.dumps(rewrite_log, ensure_ascii=False, indent=1), encoding="utf-8")

    total = sum(len(questions) for questions in question_sets.values())
    print(f"Mesures répétées {args.repeat} fois ; « a–b » = résultat variable d'une mesure à l'autre. "
          f"Questions avec article attendu : {', '.join(f'{name} {len(qs)}' for name, qs in question_sets.items())} (total {total}).\n")
    for level, _ in LEVELS:
        print(f"Niveau {level} :\n")
        header = " | ".join(f"{name} hit@1 | {name} hit@5" for name in sets)
        print(f"| Configuration | {header} | total hit@1 | total hit@5 |")
        print("|---|" + "---|" * (2 * len(sets) + 2))
        for key, label, *_ in configs:
            cells = " | ".join(
                " | ".join(f"{spread([hit_at_k(r[key, name, level], k) for r in runs])}/{len(question_sets[name])}" for k in (1, 5))
                for name in sets
            )
            totals = " | ".join(f"{spread([sum(hit_at_k(r[key, name, level], k) for name in sets) for r in runs])}/{total}" for k in (1, 5))
            print(f"| {label} | {cells} | {totals} |")
        print()

    print("Rang du premier article attendu, puis du paragraphe précisé s'il diffère (— = pas dans les 20 premiers) :\n")
    print("| Question | " + " | ".join(label for _, label, *_ in configs) + " |")
    print("|---|" + "---|" * len(configs))
    for name, questions in question_sets.items():
        for index, question in enumerate(questions):
            cells = []
            for key, *_ in configs:
                cell = spread([r[key, name, "article"][index] or "—" for r in runs])
                if question.expected != article_level(question.expected):
                    cell += f" (§ {spread([r[key, name, 'paragraphe'][index] or '—' for r in runs])})"
                cells.append(cell)
            print(f"| {question.id} | {' | '.join(cells)} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())

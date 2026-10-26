"""Compare several search configurations on the v0 and v1 questions (hit@1, hit@5, hit@8, ranks).

Two levels: the article, and the paragraph when a question names the one that matters (session 6).
Prints Markdown tables. The question vectors computed by Ollama on the CPU vary very slightly
from one run to the next, which can swap two passages with almost the same score: with
--repeat N, everything is measured N times and a varying result is shown as a range ("11–12").
The hybrid configurations, rejected at session 5, are no longer measured (see eval/results_v1.md).
Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_retrieval.py [--repeat 3]
"""

import argparse
import sys

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import article_level, first_hit_rank, hit_at_k, load_questions
from compliance_copilot.index import IndexNotReadyError, search

DEPTH = 20
CONFIGS = [  # (label, mode, lexicon, at most N chunks of the same article, first paragraph of a split article added)
    ("vecteurs seuls (départ)", "vector", "off", None, False),
    ("vecteurs + lexique", "vector", "all", None, False),
    ("vecteurs + lexique + 2 par article", "vector", "all", 2, False),
    ("vecteurs + lexique + 2 par article + 1er paragraphe", "vector", "all", 2, True),
]
LEVELS = [("article", True), ("paragraphe", False)]
SETS = [("v0", "questions_v0.jsonl"), ("v1", "questions_v1.jsonl")]


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
    parser = argparse.ArgumentParser(description="Compare les configurations de recherche sur v0 et v1.")
    parser.add_argument("--repeat", type=int, default=1, help="nombre de mesures complètes (3 recommandé)")
    args = parser.parse_args()
    settings = load_settings()
    question_sets = {name: [q for q in load_questions(EVAL_DIR / file) if q.expected] for name, file in SETS}
    runs: list[dict[tuple[str, str, str], list[int | None]]] = []
    for run in range(args.repeat):
        embedder = CachedEmbedder(make_embedder(settings, settings.query_embedding_device))  # fresh vectors each run
        ranks: dict[tuple[str, str, str], list[int | None]] = {}
        for label, mode, lexicon, limit, first_paragraph in CONFIGS:
            print(f"… mesure {run + 1}/{args.repeat} : {label}", file=sys.stderr, flush=True)
            for name, questions in question_sets.items():
                try:
                    found = [
                        [r.id for r in search(q.question, INDEX_DIR, embedder, k=DEPTH, mode=mode, lexicon=lexicon, max_per_article=limit,
                                              first_paragraph=first_paragraph)]
                        for q in questions
                    ]
                except (IndexNotReadyError, EmbeddingError) as error:
                    print(f"[ERREUR] {error}")
                    return 1
                for level, by_article in LEVELS:
                    ranks[label, name, level] = [
                        first_hit_rank(ids, article_level(q.expected) if by_article else q.expected) for ids, q in zip(found, questions)
                    ]
        runs.append(ranks)

    print(f"Mesures répétées {args.repeat} fois ; « a–b » = résultat variable d'une mesure à l'autre.\n")
    for level, _ in LEVELS:
        print(f"Niveau {level} :\n")
        header = " | ".join(f"{name} hit@1 | {name} hit@5 | {name} hit@8" for name, _ in SETS)
        print(f"| Configuration | {header} |")
        print("|---|" + "---|" * (3 * len(SETS)))
        for label, *_ in CONFIGS:
            cells = " | ".join(
                " | ".join(f"{spread([hit_at_k(r[label, name, level], k) for r in runs])}/{len(question_sets[name])}" for k in (1, 5, 8))
                for name, _ in SETS
            )
            print(f"| {label} | {cells} |")
        print()

    print("Rang du premier article attendu, puis du paragraphe précisé s'il diffère (— = pas dans les 20 premiers) :\n")
    print("| Question | " + " | ".join(label for label, *_ in CONFIGS) + " |")
    print("|---|" + "---|" * len(CONFIGS))
    for name, questions in question_sets.items():
        for index, question in enumerate(questions):
            cells = []
            for label, *_ in CONFIGS:
                cell = spread([r[label, name, "article"][index] or "—" for r in runs])
                if question.expected != article_level(question.expected):
                    cell += f" (§ {spread([r[label, name, 'paragraphe'][index] or '—' for r in runs])})"
                cells.append(cell)
            print(f"| {question.id} | {' | '.join(cells)} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())

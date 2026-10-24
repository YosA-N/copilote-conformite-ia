"""Compare several search configurations on the v0 and v1 questions (hit@1, hit@5, ranks).

Prints Markdown tables. The question vectors computed by Ollama on the CPU vary very slightly
from one run to the next, which can swap two passages with almost the same score: with
--repeat N, everything is measured N times and a varying result is shown as a range ("11–12").
Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_retrieval.py [--repeat 3]
"""

import argparse
import sys

from compliance_copilot.config import EVAL_DIR, INDEX_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.evaluation import first_hit_rank, hit_at_k, load_questions
from compliance_copilot.index import IndexNotReadyError, search

DEPTH = 20
CONFIGS = [  # (label, mode, lexicon)
    ("vecteurs seuls (départ)", "vector", "off"),
    ("vecteurs + lexique", "vector", "all"),
    ("hybride", "hybrid", "off"),
    ("hybride + lexique (mots-clés)", "hybrid", "keywords"),
    ("hybride + lexique (partout)", "hybrid", "all"),
]
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
    runs: list[dict[tuple[str, str], list[int | None]]] = []
    for run in range(args.repeat):
        embedder = CachedEmbedder(make_embedder(settings, settings.query_embedding_device))  # fresh vectors each run
        ranks: dict[tuple[str, str], list[int | None]] = {}
        for label, mode, lexicon in CONFIGS:
            print(f"… mesure {run + 1}/{args.repeat} : {label}", file=sys.stderr, flush=True)
            for name, questions in question_sets.items():
                try:
                    ranks[label, name] = [
                        first_hit_rank([r.id for r in search(q.question, INDEX_DIR, embedder, k=DEPTH, mode=mode, lexicon=lexicon)], q.expected)
                        for q in questions
                    ]
                except (IndexNotReadyError, EmbeddingError) as error:
                    print(f"[ERREUR] {error}")
                    return 1
        runs.append(ranks)

    print(f"Mesures répétées {args.repeat} fois ; « a–b » = résultat variable d'une mesure à l'autre.\n")
    header = " | ".join(f"{name} hit@1 | {name} hit@5" for name, _ in SETS)
    print(f"| Configuration | {header} |")
    print("|---|" + "---|" * (2 * len(SETS)))
    for label, _, _ in CONFIGS:
        cells = " | ".join(
            f"{spread([hit_at_k(r[label, name], 1) for r in runs])}/{len(question_sets[name])} | "
            f"{spread([hit_at_k(r[label, name], 5) for r in runs])}/{len(question_sets[name])}"
            for name, _ in SETS
        )
        print(f"| {label} | {cells} |")

    print("\nRang du premier article attendu (— = pas dans les 20 premiers) :\n")
    print("| Question | " + " | ".join(label for label, _, _ in CONFIGS) + " |")
    print("|---|" + "---|" * len(CONFIGS))
    for name, questions in question_sets.items():
        for index, question in enumerate(questions):
            cells = " | ".join(spread([r[label, name][index] or "—" for r in runs]) for label, _, _ in CONFIGS)
            print(f"| {question.id} | {cells} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())

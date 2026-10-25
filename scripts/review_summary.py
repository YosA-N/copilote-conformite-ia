"""Count the verdicts of the human reviews: eval/reviews/<version>.jsonl, defined in eval/rubric.md.

Prints a Markdown table (one row per reviewed version), then the questions that are not "juste".
With --check, every review must cover exactly the questions answered in eval/answers_<version>.md,
and every reviewed id must be a question of one of the eval/questions_*.jsonl files (the author's
questions included, once eval/questions_author.jsonl exists).

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\review_summary.py [--check]
"""

import argparse
import re
import sys
from pathlib import Path

from compliance_copilot.config import EVAL_DIR
from compliance_copilot.evaluation import VERDICTS, ReviewError, answered_question_ids, load_questions, load_reviews, verdict_counts

REVIEWS_DIR = EVAL_DIR / "reviews"


def version_order(path: Path) -> tuple:
    """v0, v1, v2… first, in numeric order, then the other versions (heldout_v3…) by name."""
    number = re.fullmatch(r"v(\d+)", path.stem)
    return (0, int(number.group(1)), "") if number else (1, 0, path.stem)


def check(version: str, reviewed: list[str], known: set[str]) -> list[str]:
    problems = [f"{version} : {review_id} n'est dans aucun fichier eval/questions_*.jsonl" for review_id in reviewed if review_id not in known]
    answers = EVAL_DIR / f"answers_{version}.md"
    if not answers.exists():
        return problems + [f"{version} : {answers.name} introuvable"]
    answered = answered_question_ids(answers)
    problems += [f"{version} : {q} est répondue dans {answers.name} mais pas relue" for q in answered if q not in reviewed]
    problems += [f"{version} : {q} est relue mais absente de {answers.name}" for q in reviewed if q not in answered]
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Tableau des verdicts des relectures humaines.")
    parser.add_argument("--check", action="store_true", help="vérifier que chaque relecture couvre les questions répondues")
    args = parser.parse_args()

    files = sorted(REVIEWS_DIR.glob("*.jsonl"), key=version_order)
    if not files:
        print(f"[ERREUR] Aucune relecture dans {REVIEWS_DIR}")
        return 1
    try:
        reviews = {path.stem: load_reviews(path) for path in files}
    except ReviewError as error:
        print(f"[ERREUR] {error}")
        return 1

    print("| Version | Questions | " + " | ".join(verdict.capitalize() for verdict in VERDICTS) + " |")
    print("|---|---|" + "---|" * len(VERDICTS))
    for version, version_reviews in reviews.items():
        counts = verdict_counts(version_reviews)
        print(f"| {version} | {len(version_reviews)} | " + " | ".join(str(counts[verdict]) for verdict in VERDICTS) + " |")

    print("\nQuestions qui ne sont pas justes :\n")
    for version, version_reviews in reviews.items():
        groups = [
            f"{verdict} {', '.join(r.id for r in version_reviews if r.verdict == verdict)}"
            for verdict in VERDICTS[1:]
            if any(r.verdict == verdict for r in version_reviews)
        ]
        print(f"- {version} : {' · '.join(groups) if groups else 'aucune'}")

    if args.check:
        known = {q.id for path in EVAL_DIR.glob("questions_*.jsonl") for q in load_questions(path)}
        problems = [problem for version, version_reviews in reviews.items() for problem in check(version, [r.id for r in version_reviews], known)]
        print()
        for problem in problems:
            print(f"[ERREUR] {problem}")
        if problems:
            return 1
        print(f"[OK] {len(reviews)} relecture(s) cohérente(s) avec les réponses et les questions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

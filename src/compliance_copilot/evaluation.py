"""Measure how well the search finds the expected articles (rank of the first hit, hit@k), and count
the verdicts of the human reviews of the answers.

A reference names an article, an annex or a part of it, like the start of a chunk id:
"gdpr:art_37" (any chunk of GDPR article 37) or "ai_act:anx_III:pt_4" (point 4 of AI Act annex III).
A review gives one verdict per answered question, as defined in eval/rubric.md.
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from compliance_copilot.sources import SOURCES

SOURCE_NAMES = {source.key: source.name for source in SOURCES}
LETTER_SUFFIXES = {"a": "bis", "b": "ter", "c": "quater", "d": "quinquies", "e": "sexies"}
PART_NAMES = {"par": "paragraphe", "def": "définition", "pt": "point", "sec": "section", "part": "partie"}
VERDICTS = ("juste", "partiel", "faux", "dangereux")  # eval/rubric.md, from the best to the worst
ANSWER_TITLE = re.compile(r"^## (\w+) — ", re.MULTILINE)  # "## q01 — Dois-je désigner un DPO ?" in eval/answers_*.md


@dataclass
class Question:
    id: str
    question: str
    expected: list[str]  # the search succeeds if one of these is found
    related: list[str] = field(default_factory=list)  # useful, but not enough to answer alone
    coverage: str = "complet"  # "partiel" when the corpus only holds part of the answer
    note: str = ""


@dataclass
class Review:
    id: str
    verdict: str  # one of VERDICTS
    comment: str = ""  # required for any verdict other than "juste"


class ReviewError(ValueError):
    """A review file that does not follow eval/rubric.md."""


def load_questions(path: Path) -> list[Question]:
    return [Question(**json.loads(line)) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_reviews(path: Path) -> list[Review]:
    """The human review of one version (eval/reviews/<version>.jsonl), checked against the rubric."""
    reviews: list[Review] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            review = Review(**json.loads(line))
        except (TypeError, ValueError) as error:
            raise ReviewError(f"{path.name}, ligne {number} : format invalide ({error})") from error
        where = f"{path.name}, ligne {number} ({review.id})"
        if review.verdict not in VERDICTS:
            raise ReviewError(f"{where} : verdict inconnu « {review.verdict} » (attendus : {', '.join(VERDICTS)})")
        if any(other.id == review.id for other in reviews):
            raise ReviewError(f"{where} : question relue deux fois")
        if review.verdict != "juste" and not review.comment.strip():
            raise ReviewError(f"{where} : un commentaire est obligatoire pour le verdict « {review.verdict} »")
        reviews.append(review)
    return reviews


def verdict_counts(reviews: list[Review]) -> dict[str, int]:
    """{"juste": 10, "partiel": 2, "faux": 0, "dangereux": 0}, always in the order of VERDICTS."""
    return {verdict: sum(1 for review in reviews if review.verdict == verdict) for verdict in VERDICTS}


def answered_question_ids(answers_path: Path) -> list[str]:
    """Ids of the questions answered in an eval/answers_<version>.md file, in order."""
    return ANSWER_TITLE.findall(answers_path.read_text(encoding="utf-8"))


def matches(chunk_id: str, reference: str) -> bool:
    """True if the chunk belongs to the referenced article, annex or part ("gdpr:art_3" ≠ "gdpr:art_37").

    A paragraph split by points belongs to its paragraph: "gdpr:art_9:par_2_a-i" matches "gdpr:art_9:par_2"
    (but "ai_act:art_5:par_1-bis" is another paragraph than "ai_act:art_5:par_1")."""
    return chunk_id == reference or chunk_id.startswith(reference + ":") or chunk_id.startswith(reference + "_")


def reference_unit(reference: str) -> str:
    """The article (or the annex point) of a reference: 'gdpr:art_9:par_1' → 'gdpr:art_9';
    'ai_act:anx_III:pt_4' stays as it is, an annex point being the unit of the annexes."""
    parts = reference.split(":")
    return ":".join(parts[:3] if parts[1].startswith("anx_") else parts[:2])


def article_level(expected: list[str]) -> list[str]:
    """The expected references at the article level, as measured before paragraphs were named (session 6)."""
    return list(dict.fromkeys(reference_unit(reference) for reference in expected))


def first_hit_rank(result_ids: list[str], expected: list[str]) -> int | None:
    """Rank (from 1) of the first result that belongs to an expected reference, or None."""
    for rank, chunk_id in enumerate(result_ids, start=1):
        if any(matches(chunk_id, reference) for reference in expected):
            return rank
    return None


def hit_at_k(ranks: list[int | None], k: int) -> int:
    """Number of questions whose first expected result is among the k first results."""
    return sum(1 for rank in ranks if rank is not None and rank <= k)


def describe_reference(reference: str) -> str:
    """'gdpr:art_37' → 'RGPD art. 37'; 'ai_act:anx_III:pt_4' → 'AI Act annexe III, point 4'."""
    key, anchor, *parts = reference.split(":")
    article = re.fullmatch(r"art_(\d+)([a-z]?)", anchor)
    if article:
        number, letter = article.groups()
        label = f"art. {number}" + (f" {LETTER_SUFFIXES.get(letter, letter)}" if letter else "")
    else:
        label = f"annexe {anchor.removeprefix('anx_')}"
    for part in parts:
        kind, _, value = part.partition("_")
        label += f", {PART_NAMES.get(kind, kind)} {value.replace('-', ' ')}"
    return f"{SOURCE_NAMES.get(key, key)} {label}"

"""Offline tests for the retrieval measures, the files of test questions and the human reviews."""

import re

import pytest

from compliance_copilot.config import EVAL_DIR
from compliance_copilot.evaluation import (
    ReviewError,
    answered_question_ids,
    describe_reference,
    first_hit_rank,
    hit_at_k,
    load_questions,
    load_reviews,
    matches,
    verdict_counts,
)

REFERENCE = re.compile(r"^(gdpr|ai_act):(art_\d+[a-z]?|anx_[IVXLC]+)(:[\w-]+)*$")


def test_a_reference_matches_its_whole_article_and_nothing_else():
    assert matches("gdpr:art_37", "gdpr:art_37")
    assert matches("gdpr:art_12:par_3", "gdpr:art_12")
    assert matches("ai_act:anx_III:pt_4", "ai_act:anx_III")
    assert not matches("gdpr:art_37", "gdpr:art_3")
    assert not matches("gdpr:art_3", "gdpr:art_37")
    assert not matches("ai_act:anx_III:pt_4", "ai_act:anx_III:pt_1")


def test_first_hit_rank_and_hit_at_k():
    results = ["gdpr:art_38", "gdpr:art_37:par_1", "gdpr:art_39"]

    assert first_hit_rank(results, ["gdpr:art_37"]) == 2
    assert first_hit_rank(results, ["gdpr:art_30", "gdpr:art_39"]) == 3
    assert first_hit_rank(results, ["gdpr:art_30"]) is None
    ranks = [1, 2, None, 6, 5]
    assert hit_at_k(ranks, 1) == 1
    assert hit_at_k(ranks, 5) == 3


def test_describe_reference():
    assert describe_reference("gdpr:art_37") == "RGPD art. 37"
    assert describe_reference("ai_act:art_4a") == "AI Act art. 4 bis"
    assert describe_reference("ai_act:anx_III:pt_4") == "AI Act annexe III, point 4"
    assert describe_reference("gdpr:art_12:par_3") == "RGPD art. 12, paragraphe 3"


def test_questions_file_is_well_formed():
    questions = load_questions(EVAL_DIR / "questions_v0.jsonl")

    assert len(questions) == 10
    assert len({question.id for question in questions}) == 10
    for question in questions:
        assert question.question.strip()
        assert question.expected, question.id
        assert all(REFERENCE.match(ref) for ref in question.expected + question.related), question.id
        assert question.coverage in {"complet", "partiel"}


def test_measure_questions_v1_are_well_formed_and_new():
    v1 = load_questions(EVAL_DIR / "questions_v1.jsonl")
    earlier = load_questions(EVAL_DIR / "questions_v0.jsonl") + load_questions(EVAL_DIR / "questions_offtopic_v0.jsonl")

    assert len(v1) == 20
    assert not {q.id for q in v1} & {q.id for q in earlier}  # new ids
    assert not {q.question for q in v1} & {q.question for q in earlier}  # new questions
    for question in v1:
        assert all(REFERENCE.match(ref) for ref in question.expected + question.related), question.id
        if question.coverage == "hors corpus":
            assert question.expected == [], question.id
        else:
            assert question.expected and question.coverage in {"complet", "partiel"}, question.id
    assert sum(1 for question in v1 if not question.expected) == 3


def check_question_format(questions):
    for question in questions:
        assert question.question.strip(), question.id
        assert all(REFERENCE.match(ref) for ref in question.expected + question.related), question.id
        if question.coverage == "hors corpus":
            assert question.expected == [], question.id
        else:
            assert question.expected and question.coverage in {"complet", "partiel"}, question.id


def test_final_exam_questions_v2_are_well_formed_and_new():
    # format only: these questions are frozen and must not be used to tune anything before the end of the project
    v2 = load_questions(EVAL_DIR / "questions_v2.jsonl")
    earlier = [q for name in ("questions_v0.jsonl", "questions_offtopic_v0.jsonl", "questions_v1.jsonl") for q in load_questions(EVAL_DIR / name)]

    assert len(v2) == 20 and len({q.id for q in v2}) == 20
    assert not {q.id for q in v2} & {q.id for q in earlier}
    assert not {q.question for q in v2} & {q.question for q in earlier}
    assert sum(1 for q in v2 if not q.expected) == 3
    check_question_format(v2)


def test_author_questions_are_well_formed_if_present():
    path = EVAL_DIR / "questions_author.jsonl"
    if not path.exists():
        pytest.skip("eval/questions_author.jsonl n'existe pas encore (ajouté par l'auteur à la fin du projet)")
    others = [q for other in EVAL_DIR.glob("questions_*.jsonl") if other != path for q in load_questions(other)]
    author = load_questions(path)

    assert len({q.id for q in author}) == len(author)
    assert not {q.id for q in author} & {q.id for q in others}
    check_question_format(author)


# ---------------------------------------------------------------- human reviews (eval/rubric.md)

# Totals of the author's reviews (eval/review_v*.md, then the review of v3), with the two
# reclassifications decided at session 6: v0 q01 and v2 q08 become "dangereux".
AUTHOR_TOTALS = {
    "v0": {"juste": 5, "partiel": 1, "faux": 3, "dangereux": 3},
    "v1": {"juste": 9, "partiel": 2, "faux": 0, "dangereux": 1},
    "v2": {"juste": 6, "partiel": 5, "faux": 0, "dangereux": 1},
    "v3": {"juste": 10, "partiel": 2, "faux": 0, "dangereux": 0},
}


def test_review_files_follow_the_rubric_and_cover_the_answered_questions():
    paths = sorted((EVAL_DIR / "reviews").glob("*.jsonl"))
    assert paths

    for path in paths:
        reviews = load_reviews(path)  # raises ReviewError if a verdict, an id or a comment is wrong
        answers = EVAL_DIR / f"answers_{path.stem}.md"
        assert answers.exists(), path.name
        assert sorted(r.id for r in reviews) == sorted(answered_question_ids(answers)), path.name


@pytest.mark.parametrize("version", AUTHOR_TOTALS)
def test_converted_reviews_keep_the_author_verdicts(version):
    assert verdict_counts(load_reviews(EVAL_DIR / "reviews" / f"{version}.jsonl")) == AUTHOR_TOTALS[version]


@pytest.mark.parametrize(
    ("lines", "message"),
    [
        (['{"id": "q01", "verdict": "bof", "comment": "?"}'], "verdict inconnu"),
        (['{"id": "q01", "verdict": "juste"}', '{"id": "q01", "verdict": "juste"}'], "relue deux fois"),
        (['{"id": "q01", "verdict": "faux", "comment": " "}'], "commentaire est obligatoire"),
        (['{"id": "q01", "verdict": "juste", "note": "?"}'], "format invalide"),
    ],
)
def test_invalid_reviews_are_rejected(tmp_path, lines, message):
    path = tmp_path / "v9.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pytest.raises(ReviewError, match=message):
        load_reviews(path)


def test_answered_question_ids_reads_the_titles_of_an_answers_file(tmp_path):
    path = tmp_path / "answers_v9.md"
    path.write_text("# Réponses\n\n## q01 — Dois-je désigner un DPO ?\n\ntexte\n\n## h01 — Quel est le taux de TVA ?\n", encoding="utf-8")

    assert answered_question_ids(path) == ["q01", "h01"]

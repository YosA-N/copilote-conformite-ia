"""The word-for-word check tolerates typographic characters, on both sides, and nothing more.

The sentences come from the real answers of `openai/gpt-oss-120b` (session 7, eval/answers_heldout_v4_big_gptoss.md,
questions q11, q12 and q15) and from the passages they cite (RGPD articles 15, 17, 28…), copied once into
tests/fixtures/typographic_extracts.json so that the tests never read data/.
"""

import json
from pathlib import Path

import pytest

from compliance_copilot.index import SearchResult
from compliance_copilot.rag import _comparable, finalize_answer, found_word_for_word, parse_extracts, verify_extracts

FIXTURE = json.loads((Path(__file__).parent / "fixtures" / "typographic_extracts.json").read_text(encoding="utf-8"))
ARTICLE_28_3 = FIXTURE["passages"]["gdpr:art_28:par_3"]


def passages_of(question: str) -> list[SearchResult]:
    return [
        SearchResult(id=cid, text=FIXTURE["passages"][cid], score=0.9, metadata={}, rank=rank)
        for rank, cid in enumerate(FIXTURE["extracts"][question]["passage_ids"], start=1)
    ]


def extracts_of(question: str):
    return verify_extracts(FIXTURE["extracts"][question]["raw_extracts_part"], passages_of(question))


# ---------------------------------------------------------------- the normalisation, character by character


@pytest.mark.parametrize(
    ("written", "official"),
    [
        ("le traitement par un sous‑traitant est régi", "le traitement par un sous-traitant est régi"),  # non-breaking hyphen
        ("celui‐ci fait uniquement appel à des sous–traitants", "celui-ci fait uniquement appel à des sous-traitants"),
        ("des motifs suivants s'applique : a) les données", "des motifs suivants s'applique: a) les données"),  # space before :
        ("un traitement illicite ; e) les données", "un traitement illicite; e) les données"),
        ("informations suivantes : a) les finalités", "informations suivantes: a) les finalités"),  # narrow no-break space
        ("« violation de données à caractère personnel », une violation", "«violation de données à caractère personnel», une violation"),
        ("violation de données à caractère personnel, une violation", "«violation de données à caractère personnel», une violation"),
        ("qu’il en soit autrement", "qu'il en soit autrement"),
        ("Sous réserve des droits", "sous réserve des droits"),
    ],
)
def test_typographic_variants_compare_equal(written, official):
    assert _comparable(written) == _comparable(official)


def test_words_are_never_changed():
    assert _comparable("sous-traitant") != _comparable("sous traitant")
    assert _comparable("un contrat ou un autre acte juridique") != _comparable("un contrat écrit ou un autre acte juridique")
    assert _comparable("ne s'appliquent pas") != _comparable("s'appliquent")


# ---------------------------------------------------------------- the real rejected extracts of gpt-oss-120b


def test_q15_extracts_with_non_breaking_hyphens_and_inner_quotes_are_found():
    extracts = extracts_of("q15")

    assert len(extracts) == 4 and all(extract.verified for extract in extracts)
    assert extracts[0].text.startswith("le traitement par un sous‑traitant")  # the extract itself is kept as written
    assert extracts[1].text.startswith("a) « ne traite les données")  # inner quotes around the point


def test_q11_extracts_with_a_space_before_the_colon_are_found():
    extracts = extracts_of("q11")

    assert len(extracts) == 2 and all(extract.verified for extract in extracts)
    assert "s'applique : a)" in extracts[0].text


def test_q12_citation_repeated_after_the_closing_quote_is_dropped_but_a_skipped_point_stays_rejected():
    parsed = parse_extracts(FIXTURE["extracts"]["q12"]["raw_extracts_part"])
    assert [text.endswith(end) for (_, text), end in zip(parsed, ("la logique sous‑jacent…", "il en soit autrement."))] == [True, True]  # no « »**[2]** left

    extracts = extracts_of("q12")

    assert [extract.verified for extract in extracts] == [False, True]
    assert "contrôle; h) l'existence" in _comparable(extracts[0].text)  # point g) skipped without « … »: not word for word


def test_a_reworded_extract_stays_rejected():
    official = "le traitement par un sous-traitant est régi par un contrat ou un autre acte juridique au titre du droit de l'Union"
    assert found_word_for_word(official, ARTICLE_28_3)
    assert found_word_for_word(official.replace("sous-", "sous‑"), ARTICLE_28_3)
    assert not found_word_for_word(official.replace("un contrat", "un contrat écrit"), ARTICLE_28_3)
    assert not found_word_for_word(official.replace("est régi par", "doit être régi par"), ARTICLE_28_3)


def test_q15_answer_is_no_longer_replaced_by_a_refusal():
    raw = FIXTURE["extracts"]["q15"]["raw_extracts_part"] + "\n\nRÉPONSE :\nOui, un contrat est nécessaire [1]."
    text, extracts, refused = finalize_answer(raw, passages_of("q15"))

    assert not refused and text.startswith("Oui, un contrat est nécessaire") and sum(e.verified for e in extracts) == 4

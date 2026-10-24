"""Offline tests for the answer pipeline, with the fake embedding model and the fake language model."""

import pytest
from conftest import FakeChatModel

from compliance_copilot.index import search
from compliance_copilot.rag import (
    DISCLAIMER,
    REFUSAL,
    SYSTEM_PROMPT,
    AnswerStream,
    CitationStream,
    answer_from_passages,
    answer_question,
    build_messages,
    check_citations,
    found_word_for_word,
    normalize_citations,
    parse_extracts,
    render_footer,
)

QUESTION = "Dois-je désigner un délégué ?"
# a sentence of article 37 of the GDPR, as it appears in tests/fixtures/gdpr_sample.xhtml
ARTICLE_37 = "Le responsable du traitement et le sous-traitant désignent en tout état de cause un délégué à la protection des données"
GOOD_REPLY = f"EXTRAITS :\n- [1] « {ARTICLE_37} »\n\nRÉPONSE :\nOui, dans certains cas [1b]."
CLEAN_REFUSAL = f"EXTRAITS : aucun\n\nRÉPONSE : {REFUSAL}"


@pytest.fixture
def passages(index_dir, fake_embedder):
    """Three passages; the first one is article 37 of the GDPR."""
    found = search("désignation délégué", index_dir, fake_embedder, k=3)
    assert found[0].id == "gdpr:art_37"
    return found


# ---------------------------------------------------------------- prompt and citations


def test_prompt_gives_the_rules_and_numbers_the_passages_in_order(passages):
    system, user = build_messages(QUESTION, passages)

    assert system["role"] == "system" and system["content"] == SYSTEM_PROMPT
    for rule in ("UNIQUEMENT", "N'invente jamais", "EXTRAITS :", "RÉPONSE :", "mot pour mot", REFUSAL):
        assert rule in SYSTEM_PROMPT
    assert user["content"].startswith("Passages :\n\n[1] RGPD — règlement (UE) 2016/679 — Article 37")
    assert user["content"].index("[1] ") < user["content"].index("[2] ") < user["content"].index("[3] ")
    assert user["content"].endswith(f"Question : {QUESTION}")


def test_citation_variants_are_written_as_plain_numbers():
    text = "Oui [1b], voir [2, 3c] et [1][2]. Mais [sic] et [lien](https://exemple.fr) ne changent pas."

    assert normalize_citations(text) == "Oui [1], voir [2, 3] et [1][2]. Mais [sic] et [lien](https://exemple.fr) ne changent pas."


def test_streamed_citations_are_normalised_even_when_cut_in_pieces():
    shown = []
    stream = CitationStream(shown.append)

    for piece in ["Oui [", "1", "b] et [2", "c]. Fin"]:
        stream.feed(piece)
    stream.close()

    assert "".join(shown) == "Oui [1] et [2]. Fin"


def test_citation_check_finds_unknown_passages():
    check = check_citations("Oui [1]. Selon [9], non [2, 3].", passage_count=5)

    assert check.cited == [1, 2, 3]
    assert check.unknown == [9]


# ---------------------------------------------------------------- verified extracts


def test_word_for_word_check_tolerates_only_spacing_quotes_case_and_ellipsis():
    law = "Le responsable du traitement l’informe  de la prolongation et des motifs du report dans un délai d'un mois."

    assert found_word_for_word("le responsable du traitement l'informe de la prolongation", law)  # case, ’, spaces
    assert found_word_for_word("Le responsable du traitement … dans un délai d'un mois.", law)  # skipped part
    assert not found_word_for_word("Le responsable du traitement l'informe de la prolongation dans un délai de deux mois", law)
    assert not found_word_for_word("dans un délai d'un mois … Le responsable du traitement", law)  # wrong order
    assert not found_word_for_word("un délai d'un mois", law)  # too short to prove anything


def test_extracts_are_read_with_their_passage_number_and_inner_quotes():
    part = (
        "**EXTRAITS :**\n"
        "[1] *« «données à caractère personnel», toute information se rapportant à une personne physique »*\n"
        "- [2] « une phrase écrite\n  sur deux lignes »\n"
        "- « sans numéro de passage »\n"
        "---"
    )

    assert parse_extracts(part) == [
        (1, "«données à caractère personnel», toute information se rapportant à une personne physique"),
        (2, "une phrase écrite … sur deux lignes"),  # each line must be found as written, in order
        (None, "sans numéro de passage"),
    ]


def test_verified_extract_keeps_the_answer(passages):
    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=GOOD_REPLY))

    assert not answer.refused
    assert answer.text == "Oui, dans certains cas [1]."
    assert [(extract.passage, extract.verified) for extract in answer.extracts] == [(1, True)]
    assert answer.warnings == []
    assert f"[1] « {ARTICLE_37} »" in render_footer(answer)


def test_answer_without_verified_extract_is_replaced_by_the_refusal(passages):
    paraphrase = "EXTRAITS :\n- [1] « Les associations doivent toujours désigner un délégué à la protection des données »\n\nRÉPONSE :\nOui, toujours [1]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=paraphrase))

    assert answer.refused and answer.text == REFUSAL
    assert any("remplacée par un refus" in warning for warning in answer.warnings)
    assert not any(source.cited for source in answer.sources)


def test_extract_attributed_to_the_wrong_passage_is_rejected(passages):
    wrong_number = f"EXTRAITS :\n- [2] « {ARTICLE_37} »\n- [1] « {ARTICLE_37} »\n\nRÉPONSE :\nOui [1]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=wrong_number))

    assert [extract.verified for extract in answer.extracts] == [False, True]
    assert any("introuvable(s) mot pour mot dans le passage cité ([2])" in warning for warning in answer.warnings)


def test_clean_refusal_of_an_off_topic_question_gets_no_citation_warning(passages):
    answer = answer_from_passages("Quel est le taux de TVA ?", passages, FakeChatModel(reply=CLEAN_REFUSAL))

    assert answer.refused and answer.text == REFUSAL
    assert answer.warnings == []
    assert "Attention" not in render_footer(answer)


def test_extract_copied_on_several_lines_is_checked_line_by_line(passages):
    lines = f"EXTRAITS :\n[1] {ARTICLE_37} lorsque:\nle traitement est effectué par une autorité publique ou un organisme public\n\nRÉPONSE :\nOui [1]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=lines))

    assert [extract.verified for extract in answer.extracts] == [True]


def test_answer_missing_after_verified_extracts_is_explained(passages):
    cut = f"EXTRAITS :\n- [1] « {ARTICLE_37} »\n"  # the model stopped before writing its answer

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=cut, truncated=True))

    assert answer.refused and answer.text == REFUSAL
    assert any("n'a pas rédigé de réponse" in warning for warning in answer.warnings)
    assert not any("Aucun des" in warning for warning in answer.warnings)  # its extract was verified


def test_citation_without_verified_extract_is_reported(passages):
    reply = f"EXTRAITS :\n- [1] « {ARTICLE_37} »\n\nRÉPONSE :\nOui [1], et aussi selon [2]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=reply))

    assert any("cite [2] sans extrait vérifié" in warning for warning in answer.warnings)


def test_stream_shows_the_answer_only_after_its_extracts_are_verified(passages):
    shown = []
    stream = AnswerStream(shown.append, passages)

    for start in range(0, len(GOOD_REPLY), 4):
        stream.feed(GOOD_REPLY[start : start + 4])
        if "RÉPONSE" not in GOOD_REPLY[: start + 4]:
            assert shown == []  # nothing is shown while the extracts are being written
    stream.close()

    assert "".join(shown) == "Oui, dans certains cas [1]."


def test_stream_shows_the_refusal_when_no_extract_is_verified(passages):
    shown = []
    stream = AnswerStream(shown.append, passages)

    for piece in ["EXTRAITS :\n- [1] « une phrase inventée de toutes pièces »\n\nRÉP", "ONSE :\nOui, toujours", " [1]."]:
        stream.feed(piece)
    stream.close()

    assert "".join(shown) == REFUSAL


# ---------------------------------------------------------------- whole answer


def test_sources_come_from_the_metadata_not_from_the_model(passages):
    reply = f"EXTRAITS :\n- [1] « {ARTICLE_37} »\n\nRÉPONSE :\nSelon l'article 99 du règlement, oui [1]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=reply))

    first = answer.sources[0]
    assert first.cited and first.number == 1
    assert first.label == "RGPD — règlement (UE) 2016/679, article 37 : Désignation du délégué à la protection des données"
    assert first.url.endswith("#art_37") and first.version_date == "2016-05-04"
    assert not any("99" in source.label for source in answer.sources)
    assert [source.cited for source in answer.sources] == [True, False, False]


def test_every_answer_gets_the_legal_warning(index_dir, fake_embedder):
    for reply in [GOOD_REPLY, CLEAN_REFUSAL, "Réponse sans aucun format."]:
        answer = answer_question(QUESTION, index_dir, fake_embedder, FakeChatModel(reply=reply))
        assert render_footer(answer).endswith(DISCLAIMER)
    assert DISCLAIMER.startswith("Information, pas un conseil juridique")


def test_truncated_answer_is_reported(passages):
    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=GOOD_REPLY, truncated=True))

    assert any("Réponse coupée" in warning and "700" in warning for warning in answer.warnings)
    assert "Attention : Réponse coupée" in render_footer(answer)


def test_passages_that_do_not_fit_in_the_context_are_dropped(index_dir, fake_embedder):
    small_model = FakeChatModel(num_ctx=1800, max_tokens=300)

    answer = answer_question(QUESTION, index_dir, fake_embedder, small_model, k=5)

    assert 1 <= len(answer.passages) < 5
    assert any("retiré(s) faute de place" in warning for warning in answer.warnings)
    assert small_model.messages[1]["content"].count("\n\n[") == len(answer.passages)  # only the kept passages are sent


def test_answer_is_streamed_and_timed(index_dir, fake_embedder):
    shown = []

    answer = answer_question("désignation délégué", index_dir, fake_embedder, FakeChatModel(reply=GOOD_REPLY), on_text=shown.append)

    assert "".join(shown) == answer.text == "Oui, dans certains cas [1]."
    assert answer.search_seconds >= 0 and answer.generation_seconds >= 0
    assert answer.generation.tokens_per_second == 20.0

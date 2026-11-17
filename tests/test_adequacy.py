"""Adequacy decisions are not in the corpus (session 7 bis): the prompt forbids saying whether a third country has one,
and the code adds a fixed note, with the official link, under any answer that cites RGPD articles 44 to 49."""

from conftest import FakeChatModel

from compliance_copilot.index import SearchResult
from compliance_copilot.rag import (
    ADEQUACY_DECISIONS_URL,
    ADEQUACY_NOTE,
    REFUSAL,
    SYSTEM_PROMPT,
    answer_from_passages,
    cites_transfer_articles,
    fixed_notes,
    render_footer,
)

ART_46 = ("Le responsable du traitement ou le sous-traitant ne peut transférer des données à caractère personnel vers un pays "
          "tiers ou à une organisation internationale que s'il a prévu des garanties appropriées et à la condition que les "
          "personnes concernées disposent de droits opposables et de voies de droit effectives.")
QUESTION = "Puis-je stocker les fichiers de mon association chez un hébergeur situé hors de l'Union ?"


def passage(chunk_id: str, regulation: str, number: str, text: str = "Texte du passage.", unit_type: str = "article") -> SearchResult:
    metadata = {"regulation": regulation, "regulation_ref": "règlement", "unit_type": unit_type, "number": number,
                "title": "Titre", "part": None, "source_url": "https://eur-lex.europa.eu/x", "version_date": "2016-05-04"}
    return SearchResult(rank=1, score=0.7, id=chunk_id, text=f"En-tête\n\n{text}", metadata=metadata)


def test_the_note_needs_a_cited_passage_of_rgpd_articles_44_to_49():
    gdpr_46 = passage("gdpr:art_46", "RGPD", "46")
    others = [passage("gdpr:art_43", "RGPD", "43"), passage("gdpr:art_50", "RGPD", "50"), passage("ai_act:art_46", "AI Act", "46"),
              passage("ai_act:anx_IV", "AI Act", "IV", unit_type="annexe")]

    assert cites_transfer_articles([gdpr_46], cited=[1])
    assert cites_transfer_articles([passage("gdpr:art_44", "RGPD", "44"), passage("gdpr:art_49:par_1", "RGPD", "49")], cited=[2])
    assert not cites_transfer_articles([gdpr_46], cited=[])  # consulted but not cited: no note
    assert not cites_transfer_articles(others, cited=[1, 2, 3, 4])  # neighbouring GDPR articles, AI Act article 46, an annex
    assert not cites_transfer_articles([gdpr_46], cited=[7])  # a number that matches no passage
    assert fixed_notes([gdpr_46], [1]) == [ADEQUACY_NOTE] and fixed_notes(others, [1, 2]) == []


def test_the_note_is_shown_under_an_answer_that_cites_article_46_and_not_after_a_refusal():
    passages = [passage("gdpr:art_46", "RGPD", "46", ART_46)]
    reply = f"EXTRAITS :\n- [1] « {ART_46} »\n\nRÉPONSE :\nOui, si des garanties appropriées sont prévues (RGPD, article 46) [1]."

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=reply))
    footer = render_footer(answer)
    assert answer.notes == [ADEQUACY_NOTE]
    assert f"Note : {ADEQUACY_NOTE}" in footer and ADEQUACY_DECISIONS_URL in footer
    assert footer.index("Note :") < footer.index("Information, pas un conseil juridique")

    refused = answer_from_passages(QUESTION, passages, FakeChatModel(reply=f"EXTRAITS : aucun\n\nRÉPONSE :\n{REFUSAL}"))
    assert refused.notes == [] and "Note :" not in render_footer(refused)


def test_the_prompt_rule_and_the_note_name_no_country():
    assert "n'affirmez jamais qu'un pays tiers a ou n'a pas de décision d'adéquation" in SYSTEM_PROMPT
    assert "RGPD, article 45" in SYSTEM_PROMPT and "RGPD, article 46" in SYSTEM_PROMPT and "Commission européenne" in SYSTEM_PROMPT
    assert ADEQUACY_DECISIONS_URL.startswith("https://commission.europa.eu/") and ADEQUACY_DECISIONS_URL.endswith("adequacy-decisions_en")
    for text in (SYSTEM_PROMPT, ADEQUACY_NOTE):
        for country in ("États-Unis", "Etats-Unis", "Royaume-Uni", "Suisse", "Japon", "Canada", "Chine", "Inde", "USA"):
            assert country not in text

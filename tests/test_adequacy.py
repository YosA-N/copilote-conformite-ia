"""Adequacy decisions are not in the corpus (session 7 bis): the prompt forbids saying whether a third country has one,
and the code adds a fixed note, with the official link, under any answer that cites RGPD articles 44 to 49."""

from pathlib import Path

from conftest import FakeChatModel

from compliance_copilot.adequacy import REDACTED, is_country_adequacy_claim, redact_adequacy_claims
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


# ---------------------------------------------------------------- control (c): a claim about a country is removed

# The real wrong sentences of q16 (copied from the answer files), judged dangerous by the author.
KNOWN_DANGEROUS = {
    "heldout_v4": "Cela suppose que le niveau de protection des données dans les États-Unis soit jugé adéquat par la Commission européenne, ce qui n’est pas le cas selon les éléments de l’article 5 [5], puisque les États-Unis ne disposent pas d’un système de protection des données adéquat reconnu par la Commission [1].",
    "heldout_v4_big_gptoss": "Vous devrez donc soit obtenir une décision d’adéquation (qui n’existe pas pour les États‑Unis), soit mettre en place l’une des garanties prévues à l’article 46 du RGPD (clauses contractuelles types, code de conduite, mécanisme de certification, etc.) avant de pouvoir transférer les données.",
    "heldout_v4_rerank": "Les règles de l'article 45, [3], concernant l'évaluation du niveau de protection, montrent que les États-Unis ne sont pas explicitement mentionnés comme assurant un niveau de protection adéquat, ce qui implique que le transfert ne peut pas être fondé sur cette base.",
    # answers_q16_adequacy.md, local, 3rd try (rule 12 of the prompt not followed)
    "q16_adequacy_local_3": "Les États-Unis ne sont pas reconnus comme assurant un niveau de protection adéquat par une décision de la Commission, donc le transfert ne peut être effectué que sous garanties appropriées (article 46, [2]).",
}
# Known false alarms (measured in eval/results_v4.md, section 8.4): correct, prudent sentences that the check removes too.
# Kept here on purpose, so that a change of the check that fixes or worsens them is seen.
KNOWN_FALSE_ALARMS = [
    "Vous ne pouvez pas simplement stocker les fichiers de votre association chez un hébergeur situé aux États-Unis sans vérifier une décision d’adéquation ou mettre en place des garanties appropriées.",
    "La décision de la Commission sur le niveau de protection des États-Unis n’est pas mentionnée dans les extraits, donc la situation reste incertaine sans preuve d’une décision d’adéquation.",
]
# Correct sentences of the recorded answers that must stay: the rule under a condition, what the passages do not say…
NOT_CLAIMS = [
    "Si les États-Unis ont été reconnus comme assurant un niveau de protection adéquat par la Commission européenne (article 45, [1]), le transfert est autorisé sans autorisation spécifique.",
    "Les passages trouvés ne précisent pas que les États-Unis ont une décision d’adéquation en vigueur, donc la possibilité dépend de l’existence d’un tel avis, qui n’est pas indiquée ici.",
    "Les passages trouvés ne permettent pas de savoir si une décision d'adéquation est actuellement en vigueur pour les États-Unis ; la liste des pays reconnus est publiée par la Commission européenne.",
    "Ce transfert est autorisé si la Commission européenne a constaté que le pays tiers assure un niveau de protection adéquat, auquel cas « Un tel transfert ne nécessite pas d'autorisation spécifique » [1].",
    "À défaut de cette décision d'adéquation, vous ne pouvez transférer les données que si vous avez prévu des « garanties appropriées » [2].",
    "La liste des pays reconnus comme offrant un niveau de protection adéquat est publiée par la Commission européenne.",
    "Les États membres ne peuvent pas restreindre les transferts lorsque la Commission a adopté une décision d'adéquation [1].",
    "Oui, vous pouvez stocker les fichiers de votre association chez un hébergeur situé aux États-Unis, à condition de respecter les règles du RGPD [3].",
]


def test_the_known_dangerous_sentences_of_q16_are_claims():
    for name, sentence in KNOWN_DANGEROUS.items():
        assert is_country_adequacy_claim(sentence), name


def test_correct_sentences_are_not_claims_and_the_known_false_alarms_are_documented():
    for sentence in NOT_CLAIMS:
        assert not is_country_adequacy_claim(sentence), sentence
    for sentence in KNOWN_FALSE_ALARMS:
        assert is_country_adequacy_claim(sentence), "false alarm no longer raised: update eval/results_v4.md, section 8.4"


def test_only_the_claiming_sentence_is_replaced_and_the_rest_of_the_answer_is_kept():
    before = "Oui, si des garanties appropriées sont prévues (RGPD, article 46) [2]."
    after = "La liste des pays reconnus est publiée par la Commission européenne."
    for sentence in KNOWN_DANGEROUS.values():
        text, removed = redact_adequacy_claims(f"{before} {sentence} {after}")
        assert text == f"{before} {REDACTED} {after}"
        assert removed == [sentence]
    listed, removed = redact_adequacy_claims(f"{before}\n- {KNOWN_DANGEROUS['q16_adequacy_local_3']}\n- {after}")
    assert listed == f"{before}\n- {REDACTED}\n- {after}" and len(removed) == 1  # the list marker is kept
    assert redact_adequacy_claims(f"{before} {after}") == (f"{before} {after}", [])


def test_the_answer_shown_never_holds_the_claim_neither_at_the_end_nor_while_it_is_written():
    passages = [passage("gdpr:art_46", "RGPD", "46", ART_46)]
    claim = KNOWN_DANGEROUS["q16_adequacy_local_3"].replace("[2]", "[1]")
    reply = (f"EXTRAITS :\n- [1] « {ART_46} »\n\nRÉPONSE :\nOui, si des garanties appropriées sont prévues (RGPD, article 46) [1]. "
             f"{claim} Les personnes concernées doivent disposer de droits opposables [1].")

    answer = answer_from_passages(QUESTION, passages, FakeChatModel(reply=reply))
    assert REDACTED in answer.text and "ne sont pas reconnus" not in answer.text
    assert answer.text.startswith("Oui, si des garanties appropriées") and answer.text.endswith("droits opposables [1].")
    assert any(w.startswith("Phrase retirée de la réponse") and "Les États-Unis ne sont pas reconnus" in w for w in answer.warnings)
    assert answer.notes == [ADEQUACY_NOTE]

    shown: list[str] = []
    streamed = answer_from_passages(QUESTION, passages, FakeChatModel(reply=reply), on_text=shown.append)  # 3 characters at a time
    assert "".join(shown) == streamed.text
    assert REDACTED in "".join(shown) and "ne sont pas reconnus" not in "".join(shown)


def test_the_check_names_no_country():
    source = (Path(__file__).resolve().parents[1] / "src" / "compliance_copilot" / "adequacy.py").read_text(encoding="utf-8")
    for country in ("États-Unis", "Etats-Unis", "Royaume-Uni", "Suisse", "Japon", "Canada", "Chine", "Inde", "USA", "Unis"):
        assert country not in source

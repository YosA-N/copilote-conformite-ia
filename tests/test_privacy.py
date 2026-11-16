"""The guard of the remote mode: personal data is recognised by simple patterns, legal questions are not blocked."""

import pytest

from compliance_copilot.privacy import PERSONAL_DATA, PersonalDataError, personal_data_found, refusal_message, refuse_personal_data


@pytest.mark.parametrize(
    ("question", "kind"),
    [
        ("Puis-je envoyer la newsletter à jean.dupont@example.org sans son accord ?", "une adresse e-mail"),
        ("Un client (prenom-nom+pro@mail.asso.fr) demande l'accès à ses données.", "une adresse e-mail"),
        ("Un adhérent joignable au 06 12 34 56 78 veut être effacé de nos fichiers.", "un numéro de téléphone"),
        ("Rappeler le +33 6 12 34 56 78 est-il de la prospection ?", "un numéro de téléphone"),
        ("Son numéro est 0612345678, puis-je le garder ?", "un numéro de téléphone"),
        ("Puis-je conserver l'IBAN FR76 3000 6000 0112 3456 7890 189 d'un donateur ?", "un IBAN"),
        ("Le RIB FR7630006000011234567890189 doit-il être chiffré ?", "un IBAN"),
        ("Un bénévole né en 1985, NIR 1 85 05 78 006 084 36, demande sa fiche.", "un numéro de sécurité sociale"),
        ("Numéro de sécurité sociale 285057800608436 : combien de temps le garder ?", "un numéro de sécurité sociale"),
        ("Corse : 1 90 12 2A 004 123 45", "un numéro de sécurité sociale"),
    ],
)
def test_each_kind_of_personal_data_is_found(question, kind):
    assert personal_data_found(question) == [kind]


def test_several_kinds_are_all_named_in_a_fixed_order():
    found = personal_data_found("Écrire à a@b.fr ou appeler le 06 12 34 56 78 ?")
    assert found == ["une adresse e-mail", "un numéro de téléphone"]
    assert list(PERSONAL_DATA) == ["une adresse e-mail", "un numéro de téléphone", "un IBAN", "un numéro de sécurité sociale"]


@pytest.mark.parametrize(
    "question",
    [
        "Dois-je désigner un DPO ?",
        "Que dit l'article 30 du règlement (UE) 2016/679 sur le registre des traitements ?",
        "L'AI Act (règlement (UE) 2024/1689) s'applique-t-il à un chatbot ?",
        "Combien de temps garder les données : 3 ans, 5 ans ou 10 ans après le dernier contact ?",
        "Une amende peut-elle atteindre 20 000 000 EUR ou 4 % du chiffre d'affaires ?",
        "Le délai de réponse est-il de 1 mois, prolongeable de 2 mois (article 12, paragraphe 3) ?",
        "Notre association compte 250 salariés et 12 000 adhérents : faut-il un registre ?",
        "La décision d'exécution (UE) 2023/1795 vaut-elle adéquation pour les États-Unis ?",
        "Puis-je filmer l'entrée du local, ouvert de 09h00 à 18h30 ?",
    ],
)
def test_ordinary_legal_questions_are_not_blocked(question):
    assert personal_data_found(question) == []


def test_refusal_message_names_the_kinds_and_the_way_out_without_the_data():
    message = refusal_message(["une adresse e-mail", "un IBAN"], "Groq")
    assert message.startswith("La question contient une adresse e-mail et un IBAN : en mode distant, rien n'a été envoyé à Groq.")
    assert "--backend ollama" in message and "@" not in message
    three = refusal_message(["une adresse e-mail", "un numéro de téléphone", "un IBAN"], "Groq")
    assert "une adresse e-mail, un numéro de téléphone et un IBAN" in three


class Remote:
    remote, provider = True, "Groq"


class Local:
    remote, provider = False, "Ollama"


def test_the_guard_refuses_only_a_remote_model_and_never_repeats_the_data():
    refuse_personal_data("Dois-je désigner un DPO ?", Remote())  # nothing to refuse
    refuse_personal_data("Écrire à a@b.fr ?", Local())  # local: nothing leaves the computer

    with pytest.raises(PersonalDataError) as error:
        refuse_personal_data("Écrire à a@b.fr ?", Remote())
    assert error.value.kinds == ["une adresse e-mail"] and error.value.provider == "Groq"
    assert str(error.value).startswith("La question contient une adresse e-mail : en mode distant, rien n'a été envoyé à Groq.")
    assert "a@b.fr" not in str(error.value)

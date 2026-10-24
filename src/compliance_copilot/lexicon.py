"""Small lexicon that adds the legal wording to everyday words in a question.

« mention d'information » → « informations à fournir à la personne concernée… »

The entries come only from the failures of eval/questions_v0.jsonl, from the examples given
when the project was planned and from common acronyms. They must NOT be written from the
questions of eval/questions_v1.jsonl, which are kept to measure the effect fairly.
"""

import re
import unicodedata

LEXICON: list[tuple[str, str]] = [
    # (pattern, accents ignored) → legal wording added to the question
    (r"\bdpo\b", "délégué à la protection des données"),
    (r"\baipd\b", "analyse d'impact relative à la protection des données"),
    (r"mentions? d.information|informer les personnes", "informations à fournir à la personne concernée lors de la collecte des données"),
    (r"duree de conservation|combien de temps .*(garder|conserver)", "limitation de la conservation : durée n'excédant pas celle nécessaire au regard des finalités"),
    (r"fuite de donnees|piratage", "violation de données à caractère personnel"),
    (r"registre", "registre des activités de traitement"),
    (r"delai pour repondre|repondre a une demande", "modalités de l'exercice des droits de la personne concernée"),
    (r"\bcv\b|recrutement|candidat", "recrutement ou sélection de personnes physiques, filtrer les candidatures"),
    (r"chatbot|agent conversationnel", "système d'IA destiné à interagir directement avec des personnes physiques"),
    (r"form(er|ation) .*\bia\b|ia generative|utilisent une ia", "maîtrise de l'IA du personnel et des personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA"),
    (r"clients?|adherents?|benevoles?|salaries?", "personne concernée"),
    (r"\bpme\b|entreprise|association", "responsable du traitement"),
]


def _plain(text: str) -> str:
    return "".join(char for char in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(char) != "Mn")


def expand_query(question: str) -> str:
    """The question followed by the legal wording of the everyday words it contains, if any."""
    plain = _plain(question)
    additions = [wording for pattern, wording in LEXICON if re.search(pattern, plain)]
    return f"{question} ({' ; '.join(additions)})" if additions else question

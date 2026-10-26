"""Small lexicon that adds the legal wording to everyday words in a question.

« mention d'information » → « informations à fournir à la personne concernée… »

Sessions 5 to 6, part 1: the entries came only from the failures of eval/questions_v0.jsonl, from
the examples given when the project was planned and from common acronyms. Since session 6, part 2,
the v1 questions have been reviewed and may be used too (CLAUDE.md): the last entries come from the
failures of v1, always as general « everyday word → legal wording » pairs. They must NEVER come
from eval/questions_v2.jsonl, the final exam.
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
    # session 6, part 2: from the failures of v1 (q14, q15, q16, q18, q21, q24, q27)
    (r"sante|medical|maladie|handicap", "données concernant la santé, catégories particulières de données à caractère personnel"),
    (r"lettre d.information|newsletter|prospection|publicit|e-?mails? (commercia|promotion)", "prospection, droit d'opposition de la personne concernée"),
    (r"proteger .*donnees|securi[st]", "sécurité du traitement : mesures techniques et organisationnelles appropriées"),
    (r"prestataire|sous-traitan", "sous-traitant qui traite des données pour le compte du responsable du traitement"),
    (r"etats-unis|hors (de l.)?(ue|union|europe)|pays tiers|a l.etranger", "transfert de données vers un pays tiers, décision d'adéquation, garanties appropriées"),
    (r"emotion", "systèmes de reconnaissance des émotions, pratiques interdites en matière d'IA"),
    (r"amendes?|sanctions?", "amendes administratives"),
]


def _plain(text: str) -> str:
    return "".join(char for char in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(char) != "Mn")


def expand_query(question: str) -> str:
    """The question followed by the legal wording of the everyday words it contains, if any."""
    plain = _plain(question)
    additions = [wording for pattern, wording in LEXICON if re.search(pattern, plain)]
    return f"{question} ({' ; '.join(additions)})" if additions else question

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
    # (pattern, accents ignored, matched on WHOLE words only: see expand_query) → legal wording added to the question.
    # Word families are written out (plural, feminine, derived words), since a pattern no longer matches inside a word.
    (r"dpo", "délégué à la protection des données"),
    (r"aipd", "analyse d'impact relative à la protection des données"),
    (r"mentions? d.information|informer les personnes", "informations à fournir à la personne concernée lors de la collecte des données"),
    (r"duree de conservation|combien de temps .*(garder|conserver)", "limitation de la conservation : durée n'excédant pas celle nécessaire au regard des finalités"),
    (r"fuites? de donnees|piratages?", "violation de données à caractère personnel"),
    (r"registres?", "registre des activités de traitement"),
    (r"delai pour repondre|repondre a une demande", "modalités de l'exercice des droits de la personne concernée"),
    (r"cv|recrutements?|candidat(e|es|s|ure|ures)?", "recrutement ou sélection de personnes physiques, filtrer les candidatures"),
    (r"chatbots?|agents? conversationnels?", "système d'IA destiné à interagir directement avec des personnes physiques"),
    (r"form(er|ation|ations) .*\bia|ia generatives?|utilisent une ia", "maîtrise de l'IA du personnel et des personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA"),
    (r"client(e|es|s)?|adherent(e|es|s)?|benevoles?|salarie(e|es|s)?", "personne concernée"),
    (r"pme|entreprises?|associations?", "responsable du traitement"),
    # session 6, part 2: from the failures of v1 (q14, q15, q16, q18, q21, q24, q27)
    (r"sante|medica(l|le|les|ux)|maladies?|handicap(e|es|ee|ees|s)?", "données concernant la santé, catégories particulières de données à caractère personnel"),
    (r"lettres? d.information|newsletters?|prospection|publicit(e|es|aire|aires)|e-?mails? (commercia\w*|promotion\w*)", "prospection, droit d'opposition de la personne concernée"),
    (r"proteger .*donnees|securi(te|tes|taire|taires|ser|sation|se|ses|sez)", "sécurité du traitement : mesures techniques et organisationnelles appropriées"),
    (r"prestataires?|sous-traitan(t|ts|te|tes|ce|ces)", "sous-traitant qui traite des données pour le compte du responsable du traitement"),
    (r"etats-unis|hors (de l.)?(ue|union|europe)|pays tiers|a l.etranger", "transfert de données vers un pays tiers, décision d'adéquation, garanties appropriées"),
    # the lexicon translates words, it never gives the conclusion: emotion recognition is only forbidden at work and in education
    (r"emotions?|emotionnel(le|les|s)?", "systèmes de reconnaissance des émotions"),
    (r"amendes?|sanctions?", "amendes administratives"),
    # Measured and NOT kept (session 7 bis, eval/results_v4.md, section 6): « ai-je le droit » → « pratique interdite
    # ou autorisée ». It only helped q24 and, with the local model, turned a harmless abstention into an inverted answer.
]


def _plain(text: str) -> str:
    return "".join(char for char in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(char) != "Mn")


# session 7 ter: an entry is triggered by whole words only (« enregistre » no longer triggers « registre »)
WHOLE_WORDS = r"(?<![a-z0-9])(?:{})(?![a-z0-9])"


def expand_query(question: str) -> str:
    """The question followed by the legal wording of the everyday words it contains, if any."""
    plain = _plain(question)
    additions = [wording for pattern, wording in LEXICON if re.search(WHOLE_WORDS.format(pattern), plain)]
    return f"{question} ({' ; '.join(additions)})" if additions else question

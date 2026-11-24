"""Query rewriting (session 7 ter): before the search, the language model gives the legal wording of the question.

A question in everyday words (« géolocalisation des véhicules ») is often far from the words of the law
(« données de localisation »). The model is asked for a few legal terms only, added to the question like the
lexicon additions; the code then drops any term that holds a conclusion (interdit, autorisé, obligatoire,
oui, non…), a number (article, date) or too many words, so that the search gets vocabulary, never an answer.

SEARCH_REWRITE=auto (the default): on in remote mode together with the reranker, off in local mode. It uses the model of the chosen mode (local or remote), after the
personal-data guard of the remote mode. Measured in eval/results_v6.md.
"""

import re

REWRITE_PROMPT = """Vous aidez un moteur de recherche dans le RGPD et le règlement européen sur l'IA (AI Act).
On vous donne une question écrite avec des mots de tous les jours. Donnez les termes juridiques que ces textes emploient pour les mêmes choses (par exemple, pour « géolocalisation des véhicules » : « données de localisation »).
Règles :
- au plus 6 termes, séparés par des points-virgules, sur une seule ligne ;
- des termes de quelques mots, jamais une phrase ;
- jamais de réponse ni de conclusion : n'écrivez pas « interdit », « autorisé », « obligatoire », « oui » ni « non » ;
- jamais de numéro d'article ni de date.
Écrivez uniquement les termes."""
MAX_TERMS = 6
MAX_WORDS = 8
# a term that holds a conclusion or a judgment is dropped: the search gets vocabulary, never an answer
CONCLUSION = re.compile(
    r"\b(?:oui|non|pas|aucun|aucune|jamais|interdit|interdits|interdite|interdites|interdiction|interdictions|autorisé|autorisée|"
    r"autorisés|autorisées|obligatoire|obligatoires|permis|permise|permises|légal|légale|légaux|illégal|illégale|illégaux|licite|"
    r"illicite|doit|doivent|devez|peut|peuvent|pouvez|vous)\b",
    re.IGNORECASE,
)
SEPARATORS = re.compile(r"[;\n•]+|\s+-\s+")
TRIM = " \t\"'«»“”.,:*-_()[]"


def parse_terms(text: str) -> list[str]:
    """The legal terms of the model's reply, filtered: no conclusion, no number, at most MAX_WORDS words each,
    no duplicates, at most MAX_TERMS."""
    text = re.sub(r"^\s*(?:termes?(?: juridiques?)?\s*:)", "", text.strip(), flags=re.IGNORECASE)
    terms, seen = [], set()
    for piece in SEPARATORS.split(text):
        term = " ".join(piece.strip(TRIM).split())
        if not term or re.search(r"\d", term) or CONCLUSION.search(term) or len(term.split()) > MAX_WORDS:
            continue
        if term.lower() in seen:
            continue
        seen.add(term.lower())
        terms.append(term)
        if len(terms) == MAX_TERMS:
            break
    return terms


def rewrite_terms(question: str, chat_model) -> list[str]:
    """Ask the model for the legal wording of the question (one short call), then filter its reply."""
    messages = [{"role": "system", "content": REWRITE_PROMPT}, {"role": "user", "content": f"Question : {question}"}]
    return parse_terms(chat_model.generate(messages).text)

"""Adequacy decisions (session 7 bis, q16): they are NOT in the corpus, so the copilot cannot know which third
countries have one. No country is named in this module: the checks only look at the shape of the sentences.

- fixed_notes(): the note the code adds, with the official link, under any answer that cites RGPD articles 44 to 49;
- redact_adequacy_claims(): each sentence that asserts that a NAMED place has, or has not, an adequacy decision or
  an adequate level of protection is replaced by REDACTED (the rest of the answer is kept), and the code warns.

The sentence check is a simple signal, measured in eval/results_v4.md (section 8.4): it caught the 4 known wrong
sentences of q16 and made 2 false alarms on prudent, correct sentences (documented in tests/test_adequacy.py).
"""

import re

ADEQUACY_DECISIONS_URL = "https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en"
ADEQUACY_NOTE = (
    "La liste des pays bénéficiant d'une décision d'adéquation n'est pas dans les textes utilisés par le copilote : "
    f"consultez la page de la Commission européenne sur les décisions d'adéquation (en anglais) : {ADEQUACY_DECISIONS_URL}"
)
TRANSFER_ARTICLES = range(44, 50)  # RGPD, chapter V: articles 44 to 49
REDACTED = "[phrase retirée : le copilote ne peut pas savoir si ce pays bénéficie d'une décision d'adéquation]"

# Sentences end with . ! ? followed by a space, or with a line break; « art. 45 » and « al. 2 » do not end a sentence.
SENTENCE_END = re.compile(r"(?<=[.!?])(?<!\bart\.)(?<!\bal\.)(?<!\bp\.)\s+|\n+")
CITATION = re.compile(r"\[[^\[\]\n]{1,30}\]")
LEADING_MARKS = re.compile(r"^[\s>*•-]*")

ADEQUACY = re.compile(r"adéquat|adéquation", re.IGNORECASE)
NEGATION = re.compile(
    r"\b(?:ne|n['’])\s*\w+(?:\s+\w+){0,3}?\s+(?:pas|aucun|aucune|jamais|plus)\b|\baucune décision\b|\bpas de décision\b|\bn['’]existe pas\b",
    re.IGNORECASE,
)
AFFIRMATION = re.compile(
    r"\b(?:bénéficie|bénéficient|dispose|disposent)\s+d['’]une décision|\bfait l['’]objet d['’]une décision|\bont une décision|\ba une décision|"
    r"\bassurent? un niveau de protection adéquat|\best reconnu",
    re.IGNORECASE,
)
# a claim made under a condition is the rule itself, not a statement about a country
CONDITION = re.compile(r"\b(?:si|s['’]ils?|lorsque|lorsqu['’]|à condition|sauf|à défaut|en l['’]absence|quand)\b", re.IGNORECASE)
# what the passages do not say may be said (rule 8 of the prompt): not a claim about a country
HEDGE = re.compile(r"\b(?:ne|n['’])\s*(?:permettent|permet|disent|dit|précisent|précise|traitent|traite|mentionnent|indiquent)\s+pas\b", re.IGNORECASE)
# capitalised words that are not places: institutions, legal texts, « État(s) membre(s) »…
NOT_A_PLACE = {
    "Commission", "Union", "Conseil", "Parlement", "Comité", "Cour", "CJUE", "RGPD", "AI", "Act", "Règlement", "Data", "Privacy",
    "Framework", "Article", "Annexe", "Chapitre", "Section", "EEE", "UE", "CNIL", "État", "États", "Espace",
}
CAPITALISED = re.compile(r"\b([A-ZÉÈÀÂÎÔÛÇ][\wéèêàâîôûç]+(?:[-‑][A-ZÉÈÀÂÎÔÛÇ][\wéèêàâîôûç]+)?)")


def cites_transfer_articles(passages: list, cited: list[int]) -> bool:
    """True when a cited passage comes from RGPD articles 44 to 49 (transfers of data to third countries)."""
    for number in cited:
        if not 1 <= number <= len(passages):
            continue
        metadata = passages[number - 1].metadata
        if metadata.get("regulation") == "RGPD" and metadata.get("unit_type") == "article":
            try:
                if int(metadata.get("number", "")) in TRANSFER_ARTICLES:
                    return True
            except ValueError:
                continue
    return False


def fixed_notes(passages: list, cited: list[int]) -> list[str]:
    """The notes the code adds under an answer, whatever the model wrote."""
    return [ADEQUACY_NOTE] if cites_transfer_articles(passages, cited) else []


def _named_places(sentence: str) -> list[str]:
    """Capitalised words that are neither the first word of the sentence nor an institution or a legal text."""
    return [m.group(1) for m in CAPITALISED.finditer(sentence) if m.start() > 0 and m.group(1) not in NOT_A_PLACE]


def is_country_adequacy_claim(sentence: str) -> bool:
    """A sentence that asserts, outside any condition, that a named place has or has not an adequacy decision
    (or an adequate level of protection)."""
    plain = LEADING_MARKS.sub("", CITATION.sub("", sentence)).strip()
    if not ADEQUACY.search(plain) or HEDGE.search(plain) or not _named_places(plain):
        return False
    claim = NEGATION.search(plain) or AFFIRMATION.search(plain)
    return bool(claim) and not CONDITION.search(plain[: claim.start()])


def _sentence_spans(text: str) -> list[tuple[int, int]]:
    spans, start = [], 0
    for match in SENTENCE_END.finditer(text):
        spans.append((start, match.start()))
        start = match.end()
    spans.append((start, len(text)))
    return [(a, b) for a, b in spans if b > a]


def redact_adequacy_claims(text: str) -> tuple[str, list[str]]:
    """(text with each claiming sentence replaced by REDACTED, the removed sentences). A list marker is kept."""
    removed, pieces, last = [], [], 0
    for start, end in _sentence_spans(text):
        sentence = text[start:end]
        if is_country_adequacy_claim(sentence):
            marks = LEADING_MARKS.match(sentence).group(0)
            pieces += [text[last:start], marks, REDACTED]
            removed.append(sentence[len(marks):].strip())
            last = end
    pieces.append(text[last:])
    return "".join(pieces), removed


class SentenceRedactor:
    """For an answer shown while it is written: holds back each sentence until it is complete, then passes it on,
    or REDACTED instead. The text shown is thus the same as the final answer."""

    def __init__(self, write):
        self.write = write
        self.buffer = ""

    def feed(self, piece: str) -> None:
        self.buffer += piece
        complete = 0
        for match in SENTENCE_END.finditer(self.buffer):
            if match.end() < len(self.buffer):  # the separator is followed by text: the sentence before it is complete
                complete = match.end()
        if complete:
            self.write(redact_adequacy_claims(self.buffer[:complete])[0])
            self.buffer = self.buffer[complete:]

    def close(self) -> None:
        if self.buffer:
            self.write(redact_adequacy_claims(self.buffer)[0])
            self.buffer = ""

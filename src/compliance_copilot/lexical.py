"""Keyword search (BM25) on the chunks, to complement the search by meaning (embeddings).

Words are lower-cased, stripped of accents and reduced to their stem ("conservation",
"conserver" → "conserv"); very common French words are ignored. Rankings from several searches are
combined by reciprocal rank fusion (RRF).
"""

import math
import re
import unicodedata
from collections import Counter, defaultdict

import snowballstemmer

STOPWORDS = {
    "a", "afin", "ai", "au", "aux", "avec", "ce", "ces", "cet", "cette", "dans", "de", "des", "doit", "dois",
    "donc", "du", "elle", "elles", "en", "est", "et", "etre", "il", "ils", "je", "la", "le", "les", "leur",
    "leurs", "lorsque", "mais", "me", "mes", "mon", "ma", "ne", "nos", "notre", "nous", "on", "ou", "par",
    "pas", "peut", "peuvent", "pour", "puis", "qu", "que", "quel", "quelle", "quelles", "quels", "qui", "sa",
    "sans", "se", "ses", "si", "son", "sont", "sur", "ta", "te", "tes", "ton", "tout", "toute", "toutes",
    "tous", "tu", "un", "une", "vos", "votre", "vous", "y",
}
_stemmer = snowballstemmer.stemmer("french")


def _strip_accents(text: str) -> str:
    return "".join(char for char in unicodedata.normalize("NFD", text) if unicodedata.category(char) != "Mn")


def tokenize(text: str) -> list[str]:
    """'Les données conservées' → ['donne', 'conserv'] (stems without accents, no stop words).

    Accents are removed before stemming, so that a question typed without accents
    ("donnees") gives the same stems as the law ("données").
    """
    words = [word for word in re.findall(r"\w+", _strip_accents(text.lower())) if len(word) > 1 and word not in STOPWORDS]
    # without accents, the stemmer keeps a final "e" ("conservees" → "conserve"): drop it
    return [stem[:-1] if stem.endswith("e") and len(stem) > 3 else stem for stem in _stemmer.stemWords(words)]


class BM25:
    """Okapi BM25 ranking over a fixed set of documents."""

    def __init__(self, ids: list[str], texts: list[str], k1: float = 1.5, b: float = 0.75):
        self.ids = ids
        self.k1, self.b = k1, b
        self.documents = [Counter(tokenize(text)) for text in texts]
        self.lengths = [sum(document.values()) for document in self.documents]
        self.average_length = sum(self.lengths) / max(len(self.lengths), 1)
        frequencies = Counter(term for document in self.documents for term in document)
        count = len(texts)
        self.idf = {term: math.log(1 + (count - df + 0.5) / (df + 0.5)) for term, df in frequencies.items()}

    def search(self, query: str, k: int) -> list[tuple[str, float]]:
        """The k best (id, score) pairs; documents sharing no word with the query are left out."""
        terms = tokenize(query)
        scored = []
        for index, document in enumerate(self.documents):
            norm = self.k1 * (1 - self.b + self.b * self.lengths[index] / self.average_length)
            score = sum(
                self.idf[term] * document[term] * (self.k1 + 1) / (document[term] + norm) for term in terms if term in document
            )
            if score > 0:
                scored.append((score, index))
        scored.sort(reverse=True)
        return [(self.ids[index], score) for score, index in scored[:k]]


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    """Combine several rankings: each id scores 1 / (k + rank) in every ranking where it appears."""
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, item in enumerate(ranking, start=1):
            scores[item] += 1 / (k + rank)
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)

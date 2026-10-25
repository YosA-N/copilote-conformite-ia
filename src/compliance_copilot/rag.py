"""Answer a question from the passages of the corpus (RAG: Retrieval-Augmented Generation).

The language model first copies the exact sentences of the passages that answer the question
(EXTRAITS), then writes its answer from those sentences only (RÉPONSE). The code checks that
every copied sentence really exists, word for word, in the passage it cites; without any
verified sentence, the answer is replaced by a standard refusal. The code also checks the
citations, builds the list of sources from the metadata and adds the legal warning: none of
these depend on what the model writes.
"""

import re
import time
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from compliance_copilot.embeddings import Embedder
from compliance_copilot.index import SearchResult, search
from compliance_copilot.lexical import tokenize
from compliance_copilot.llm import ChatModel, Generation

# Written with "vous" from start to end: a prompt that says "tu" to the model makes it say "tu" to the user.
SYSTEM_PROMPT = """Vous êtes le copilote de conformité : vous aidez les PME et les associations à comprendre le RGPD et l'AI Act.

Répondez toujours en deux parties, dans cet ordre :

EXTRAITS :
- [numéro du passage] « phrase recopiée mot pour mot dans ce passage »
(six extraits au plus, chacun sur sa ligne ; chaque extrait est une seule phrase ou un seul point a), b)…, jamais un paragraphe entier ; prenez d'abord un extrait de chaque passage qui répond à une partie de la question, avant un deuxième extrait d'un même passage ; recopiez exactement, sans modifier ni résumer ; si vous sautez une partie d'une phrase, remplacez-la par « … »)

RÉPONSE :
la réponse, écrite uniquement à partir des extraits ci-dessus, avec le numéro du passage entre crochets à la fin de chaque phrase qui s'appuie sur lui.

Exemple de forme (contenu fictif) :
EXTRAITS :
- [2] « Le responsable du traitement tient un document X, sauf si l'organisme compte moins de dix membres. »
- [4] « Les fournisseurs informent l'autorité Z. »
RÉPONSE :
Oui : en tant que responsable du traitement, vous devez tenir le document X (RGPD, article N), « sauf si l'organisme compte moins de dix membres » [2]. L'information de l'autorité Z (AI Act, article N) vise les fournisseurs, pas l'organisation qui utilise l'outil [4].

Règles à respecter :
1. Utilisez UNIQUEMENT les passages fournis, numérotés [1], [2]… N'utilisez aucune autre connaissance.
2. Si aucun passage ne répond à la question, écrivez « EXTRAITS : aucun » puis « RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question. »
3. N'inventez jamais de numéro d'article, de date, de durée ni de délai : reprenez uniquement ceux des passages et des extraits.
4. Pour chaque obligation, nommez le règlement (RGPD ou AI Act), l'article et qui est visé (responsable du traitement, sous-traitant, fournisseur, déployeur…), comme dans le passage. N'attribuez pas à la personne une obligation qui vise un autre acteur. Ne réunissez jamais sous un même nom deux obligations de textes différents, même si elles se ressemblent.
5. Distinguez ce qui est obligatoire (« doit ») de ce qui est permis (« peut »).
6. Exceptions et conditions (« sauf si », « à moins que », « lorsque », « sous réserve de », « à condition que ») : recopiez-les mot pour mot entre « », telles qu'elles figurent dans un extrait. Ne les reformulez jamais : n'ajoutez ni ne retirez jamais un « ne … pas ».
7. Quand un extrait annonce une liste de cas (a), b), c)…), recopiez chaque cas comme un extrait et reprenez-les tous dans la réponse. Si vous n'en citez qu'une partie, écrivez-le clairement : « parmi d'autres cas (liste complète à l'article N) ».
8. Ne concluez jamais qu'il n'y a « aucune obligation » ou que quelque chose « ne s'applique pas » parce que les passages n'en parlent pas : écrivez plutôt « les passages trouvés ne traitent pas de ce point ». N'affirmez une absence d'obligation que si un extrait le dit explicitement.
9. Répondez à chaque partie de la question (par exemple « qui », « quoi » et « quand »), avec chaque passage utile et pas seulement le premier. Quand les extraits ne donnent qu'un principe général (par exemple, une durée de conservation « pas plus longue que nécessaire »), dites-le et précisez que les règles concrètes (durées, montants, modalités) peuvent venir d'autres textes, comme le droit national ou les recommandations de la CNIL.
10. Vouvoyez toujours la personne : jamais « tu », « toi », « ton », « ta », « tes ». Écrivez en français simple, pour une personne qui n'est pas juriste. Commencez par la réponse directe en une ou deux phrases, puis expliquez brièvement.
11. Ne donnez aucun conseil qui ne figure pas dans les extraits."""

REFUSAL = "Les textes trouvés ne permettent pas de répondre à cette question."
DISCLAIMER = (
    "Information, pas un conseil juridique : vérifiez les textes officiels cités et, en cas de doute, "
    "demandez l'avis d'un professionnel ou de la CNIL."
)

CHARS_PER_TOKEN = 3  # cautious estimate for French text, to check that the prompt fits in the context
SAFETY_TOKENS = 200
MIN_EXTRACT_WORDS = 6  # shorter quotes prove nothing
CITATION = re.compile(r"\[([^\[\]\n]{1,30})\]")
CITED_ITEM = re.compile(r"^\s*(\d+)\s*[a-z]?\s*$", re.IGNORECASE)  # "1", "1b" (point b of passage 1)
ANSWER_HEADER = re.compile(r"^[\s*#>_-]*R[ÉE]PONSE\s*[*_]*\s*:?[*_]*", re.IGNORECASE | re.MULTILINE)
EXTRACTS_HEADER = re.compile(r"^[\s*#>_-]*EXTRAITS?\s*[*_]*\s*:?[*_]*", re.IGNORECASE | re.MULTILINE)
ITEM_START = re.compile(r"^[\s>*•-]*(?:-|•|\[\d+)")  # a new extract: "- …" or "[2] …"
ITEM = re.compile(r"^[\s>*•-]*(?:\[(\d+)[a-z]?\])?\s*[:–-]?\s*(.*)$", re.DOTALL)
ELLIPSIS = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]|\(\s*(?:…|\.\.\.)\s*\)|…|\.\.\.")

# Checks of the answer text (session 5 bis). The 35 % threshold was chosen by the author after
# measuring: at 60 %, 19 of 27 correct-looking answers got an alert; at 35 %, the three known wrong
# sentences (tests/test_rag.py) are still flagged.
SUPPORT_THRESHOLD = 0.35
MIN_SENTENCE_STEMS = 4  # "Oui." or "Voici les cas :" prove nothing either way
TUTOIEMENT = re.compile(r"\b(?:tu|toi|te|ton|ta|tes)\b|\bt['’](?=\w)", re.IGNORECASE)
ABSENCE_CLAIM = re.compile(
    r"\baucune?s? (?:obligation|règle|exigence|formalité)"
    r"|\bpas (?:d['’]obligation|obligatoire|tenue?s? de|soumise?s? à)"
    r"|\bne (?:vous )?(?:s['’]appliquen?t|concernen?t) pas"
    r"|\bn['’](?:est|êtes|sont|avez|y a) (?:pas|aucun)"
    r"|\bne (?:pouvez|pouvons|peut|peuvent|devez|doit) pas",
    re.IGNORECASE,
)
NEGATION = re.compile(r"\b(?:ne|n['’])\b[^.;:]{0,80}?\b(?:pas|ni|aucune?)\b|\baucune?s?\b|\binterdite?s?\b|\bn['’]\w+ pas\b", re.IGNORECASE)
ABOUT_PASSAGES = re.compile(r"\b(?:passages?|extraits?|textes? trouvés)\b", re.IGNORECASE)

# Checks of exceptions, quotes, lists of cases and roles (session 5 ter). Measured on the saved v2
# and session 5 answers before adoption: see eval/results_v1.md.
EXCEPTION = re.compile(
    r"\b(?:sauf (?:si|lorsque|lorsqu['’]|dans|en cas)|à moins qu(?:e|['’])|sous réserve d[eu]|à condition qu(?:e|['’])|à l['’]exception d[eu])",
    re.IGNORECASE,
)
CONDITION = re.compile(EXCEPTION.pattern + r"|\blorsqu(?:e\b|['’])", re.IGNORECASE)
CLAUSE_NEGATION = re.compile(
    r"\b(?:ne|n['’])\s*(?:\w+['’]?\s+){0,4}?(?:pas|plus|jamais|aucune?|ni|point)\b|\baucune?\b|\bnon\b|\bsans\b",
    re.IGNORECASE,
)
CLAUSE_WORDS = 12  # an exception is compared on its first 12 words…
LONG_CLAUSE_WORDS = 24  # …with up to 24 words of the extract, so that a shorter wording is not taken for a flip
QUOTE = re.compile(r"«\s*([^«»]+?)\s*»")
MIN_QUOTE_WORDS = 3  # « déployeur » alone proves nothing
EXCEPTION_SUPPORT = 0.6  # share of the words of an exception that must come from one extract
LIST_ITEM = re.compile(r"^\s*(?:[a-z]|[ivx]+|\d+)\)\s")
CASE_LIST_INTRO = re.compile(r"(?:\blorsqu|\bcas suivants|\bconditions? suivantes?|\bl['’]une (?:ou l['’]autre )?des|\bsi\b)[^:]*:\s*$", re.IGNORECASE)
CONTENT_LIST_INTRO = re.compile(r"informations suivantes|éléments suivants|\bcomporte\b|\bcontient\b|\bcomprenant\b", re.IGNORECASE)
CASE_COVERED = 0.4  # share of the first words of a case that the answer must repeat
PARTIAL_LIST = re.compile(r"\bparmi\b|\bentre autres\b|liste complète|autres cas|\bl['’]un des\b|\bcertains des\b", re.IGNORECASE)
OTHER_ACTOR = re.compile(r"\b(?:fournisseurs?|importateurs?|distributeurs?|mandataires?)\b", re.IGNORECASE)
USER_ROLE = re.compile(r"déployeurs?|responsables? du traitement|sous-traitants?", re.IGNORECASE)
REGULATION_NAMES = {
    "RGPD": re.compile(r"\bRGPD\b|2016/679|protection des données", re.IGNORECASE),
    "AI Act": re.compile(r"\bAI Act\b|2024/1689|intelligence artificielle|\bIA\b", re.IGNORECASE),
}


@dataclass
class Extract:
    number: int | None  # passage number written by the model, None if it gave none
    text: str
    verified: bool  # found word for word in the passage it cites (or, without a number, in one passage)
    passage: int | None = None  # passage where the sentence was found


@dataclass
class CitationCheck:
    cited: list[int]  # passages cited in the answer
    unknown: list[int]  # cited numbers that match no passage, e.g. [9] when 5 passages were given


@dataclass
class Source:
    number: int  # the passage number used in the answer: [1], [2]...
    label: str
    url: str
    version_date: str
    cited: bool


@dataclass
class RagAnswer:
    question: str
    text: str  # the answer shown to the user (the standard refusal if nothing was verified)
    raw_text: str  # everything the model wrote, extracts included
    extracts: list[Extract]
    refused: bool
    passages: list[SearchResult]
    sources: list[Source]
    citations: CitationCheck
    warnings: list[str]
    generation: Generation
    search_seconds: float
    generation_seconds: float

    @property
    def verified_extracts(self) -> list[Extract]:
        return [extract for extract in self.extracts if extract.verified]


# ---------------------------------------------------------------- citations [n]


def _cited_numbers(content: str) -> list[int] | None:
    """[1], [1, 3], [1b] or [1 et 2] → their numbers; None for other brackets such as [sic]."""
    numbers: list[int] = []
    for item in re.split(r"[,;]| et ", content):
        match = CITED_ITEM.match(item)
        if not match:
            return None
        if int(match.group(1)) not in numbers:
            numbers.append(int(match.group(1)))
    return numbers


def normalize_citations(text: str) -> str:
    """Write every citation as [n]: '[1b]' becomes '[1]', '[2, 3c]' becomes '[2, 3]'."""

    def rewrite(match: re.Match) -> str:
        numbers = _cited_numbers(match.group(1))
        return match.group(0) if numbers is None else "[" + ", ".join(map(str, numbers)) + "]"

    return CITATION.sub(rewrite, text)


class CitationStream:
    """Pass streamed text on to `write`, holding back a '[' until its ']' arrives, so that
    citations are already normalised when they are displayed."""

    MAX_PENDING = 32  # a '[' not closed after this many characters is not a citation

    def __init__(self, write: Callable[[str], None]):
        self.write = write
        self.pending = ""

    def feed(self, piece: str) -> None:
        self.pending += piece
        ready = ""
        while self.pending:
            start = self.pending.find("[")
            if start == -1:
                ready, self.pending = ready + self.pending, ""
                break
            ready, self.pending = ready + self.pending[:start], self.pending[start:]
            end = self.pending.find("]")
            if end == -1:
                if len(self.pending) <= self.MAX_PENDING and "\n" not in self.pending:
                    break  # wait for the end of the citation
                ready, self.pending = ready + self.pending[0], self.pending[1:]
            else:
                ready, self.pending = ready + normalize_citations(self.pending[: end + 1]), self.pending[end + 1 :]
        if ready:
            self.write(ready)

    def close(self) -> None:
        if self.pending:
            self.write(normalize_citations(self.pending))
            self.pending = ""


def check_citations(text: str, passage_count: int) -> CitationCheck:
    cited, unknown = set(), set()
    for match in CITATION.finditer(text):
        for number in _cited_numbers(match.group(1)) or []:
            (cited if 1 <= number <= passage_count else unknown).add(number)
    return CitationCheck(cited=sorted(cited), unknown=sorted(unknown))


# ---------------------------------------------------------------- verified extracts


def _comparable(text: str) -> str:
    """Ignore only what does not change the words: spaces, apostrophe and quote styles, case."""
    text = unicodedata.normalize("NFC", text).replace("­", "")
    for variant, plain in (("’", "'"), ("‘", "'"), ("«", '"'), ("»", '"'), ("“", '"'), ("”", '"')):
        text = text.replace(variant, plain)
    return re.sub(r"\s+", " ", text).strip().casefold()


def found_word_for_word(extract: str, passage_text: str, min_words: int = MIN_EXTRACT_WORDS) -> bool:
    """True if the extract appears in the passage; '…' may skip a part, the pieces staying in order."""
    pieces = [_comparable(piece).strip(" .,;:") for piece in ELLIPSIS.split(extract)]
    pieces = [piece for piece in pieces if piece]
    if not pieces or sum(len(piece.split()) for piece in pieces) < min_words:
        return False
    haystack, position = _comparable(passage_text), 0
    for piece in pieces:
        position = haystack.find(piece, position)
        if position == -1:
            return False
        position += len(piece)
    return True


def split_answer(text: str) -> tuple[str, str | None]:
    """(extracts part, answer part); the answer part is None if the model wrote no 'RÉPONSE :'."""
    match = ANSWER_HEADER.search(text)
    if not match:
        return text, None
    return text[: match.start()], text[match.end() :].strip(" \n:*_")


def parse_extracts(extracts_part: str) -> list[tuple[int | None, str]]:
    """'- [2] « phrase »' lines → (2, 'phrase'). The text runs from the first opening quote to the
    last closing one, so that quotes inside the law (« données à caractère personnel ») are kept."""
    items: list[str] = []
    for line in EXTRACTS_HEADER.sub("", extracts_part, count=1).splitlines():
        if ITEM_START.match(line):
            items.append(line)
        elif items and line.strip():
            # an extract written on several lines: each line must be found as written, in order,
            # as if the model had put "…" between them (it often skips the lines in between)
            items[-1] += " … " + line.strip()
    parsed = []
    for item in items:
        number, text = ITEM.match(item).groups()
        text = re.sub(r"^[«\"“]\s*", "", text.strip(" *_"))  # also drop Markdown emphasis: *« … »*
        text = re.sub(r"\s*[»\"”]\s*[.;,]?\s*$", "", text.strip(" *_")).strip(" *_")
        if text and text.casefold() not in {"aucun", "aucune", "aucun extrait"}:
            parsed.append((int(number) if number else None, text))
    return parsed


def verify_extracts(extracts_part: str, passages: list[SearchResult]) -> list[Extract]:
    """Every quoted sentence of the extracts part, checked against the passage it cites."""
    extracts = []
    for number, text in parse_extracts(extracts_part):
        if number is not None:
            verified = 1 <= number <= len(passages) and found_word_for_word(text, passages[number - 1].text)
            extracts.append(Extract(number, text, verified, number if verified else None))
        else:  # no passage number: accept the sentence if it is found in one of the passages
            found = next((i for i, passage in enumerate(passages, start=1) if found_word_for_word(text, passage.text)), None)
            extracts.append(Extract(None, text, found is not None, found))
    return extracts


def finalize_answer(raw_text: str, passages: list[SearchResult]) -> tuple[str, list[Extract], bool]:
    """(answer shown to the user, extracts, refused): the standard refusal replaces any answer
    that rests on no verified extract."""
    extracts_part, answer = split_answer(raw_text)
    extracts = verify_extracts(extracts_part, passages)
    if not answer or not any(extract.verified for extract in extracts):
        return REFUSAL, extracts, True
    return normalize_citations(answer), extracts, False


class AnswerStream:
    """Show the answer while it is written, but only once its extracts are verified: the
    extracts are held back, then either the answer is passed on, or the standard refusal."""

    def __init__(self, write: Callable[[str], None], passages: list[SearchResult]):
        self.write = write
        self.passages = passages
        self.buffer = ""
        self.state = "extracts"  # then "answer" or "refused"
        self.citations = CitationStream(write)

    def feed(self, piece: str) -> None:
        if self.state == "answer":
            self.citations.feed(piece)
            return
        if self.state == "refused":
            return
        self.buffer += piece
        match = ANSWER_HEADER.search(self.buffer)
        if match and len(self.buffer) > match.end() + 1:  # the header is complete
            extracts = verify_extracts(self.buffer[: match.start()], self.passages)
            if any(extract.verified for extract in extracts):
                self.state = "answer"
                self.citations.feed(self.buffer[match.end() :].lstrip(" \n:*_"))
            else:
                self.state = "refused"
                self.write(REFUSAL)

    def close(self) -> None:
        if self.state == "answer":
            self.citations.close()
        elif self.state == "extracts":  # the model never started its answer
            self.write(REFUSAL)


# ---------------------------------------------------------------- prompt and sources


def passage_label(metadata: dict) -> str:
    """'RGPD — règlement (UE) 2016/679, article 37, paragraphe 2 : Titre'."""
    kind = "article" if metadata["unit_type"] == "article" else "annexe"
    part = f", {metadata['part']}" if metadata.get("part") else ""
    return f"{metadata['regulation']} — {metadata['regulation_ref']}, {kind} {metadata['number']}{part} : {metadata['title']}"


def build_messages(question: str, passages: list[SearchResult], system_prompt: str = SYSTEM_PROMPT) -> list[dict]:
    """System prompt, then the numbered passages and the question."""
    numbered = "\n\n".join(f"[{number}] {passage.text}" for number, passage in enumerate(passages, start=1))
    user = f"Passages :\n\n{numbered}\n\nQuestion : {question}"
    return [{"role": "system", "content": system_prompt}, {"role": "user", "content": user}]


def fit_passages(question: str, passages: list[SearchResult], chat_model: ChatModel) -> list[SearchResult]:
    """Drop the lowest-ranked passages until the prompt and the answer fit in the model context."""
    budget = chat_model.num_ctx - chat_model.max_tokens - SAFETY_TOKENS
    kept = list(passages)
    while len(kept) > 1:
        prompt_chars = sum(len(message["content"]) for message in build_messages(question, kept))
        if prompt_chars / CHARS_PER_TOKEN <= budget:
            break
        kept.pop()
    return kept


def build_sources(passages: list[SearchResult], cited: list[int]) -> list[Source]:
    """The sources come from the metadata of the passages, never from the text of the model."""
    return [
        Source(
            number=number,
            label=passage_label(passage.metadata),
            url=passage.metadata["source_url"],
            version_date=passage.metadata["version_date"],
            cited=number in cited,
        )
        for number, passage in enumerate(passages, start=1)
    ]


# ---------------------------------------------------------------- checks of the answer text


def answer_sentences(text: str) -> list[str]:
    """The sentences and list items of an answer, without the [n] citations; very short ones are left out."""
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    sentences = [re.sub(r"^[\s>*•-]+", "", CITATION.sub("", part)).strip() for part in parts]
    return [sentence for sentence in sentences if len(tokenize(sentence)) >= MIN_SENTENCE_STEMS]


def support_ratio(sentence: str, extracts: list[str]) -> float:
    """Share of the significant words (stems) of the sentence that appear in the verified extracts."""
    words = set(tokenize(sentence))
    pool = set().union(*(set(tokenize(extract)) for extract in extracts)) if extracts else set()
    return len(words & pool) / len(words) if words else 1.0


def unsupported_sentences(text: str, extracts: list[str], threshold: float = SUPPORT_THRESHOLD) -> list[str]:
    """Sentences of the answer that share too few words with the verified extracts."""
    return [sentence for sentence in answer_sentences(text) if support_ratio(sentence, extracts) < threshold]


def unbacked_absence_claims(text: str, extracts: list[str]) -> list[str]:
    """Sentences that state an absence or an impossibility ("aucune obligation", "ne s'applique pas",
    "vous ne pouvez pas"…) while no verified extract says anything negative."""
    if any(NEGATION.search(extract) for extract in extracts):
        return []
    # "les passages trouvés ne traitent pas de ce point" speaks of the passages, not of the law: it is the wording the prompt asks for
    return [sentence for sentence in answer_sentences(text) if ABSENCE_CLAIM.search(sentence) and not ABOUT_PASSAGES.search(sentence)]


def uses_tu(text: str) -> bool:
    """True if the answer says "tu", "ton", "ta"… to the person instead of "vous"."""
    return bool(TUTOIEMENT.search(text))


def _first_words(text: str, count: int) -> str:
    return " ".join(text.split()[:count])


def _clauses(text: str, marker: re.Pattern) -> list[tuple[str, str]]:
    """(marker, what follows it up to the end of the sentence) for each "sauf si", "lorsque"…"""
    return [(match.group(0), re.split(r"[.;!?]", text[match.end():], maxsplit=1)[0].strip()) for match in marker.finditer(text)]


def flipped_negations(text: str, extracts: list[str]) -> list[str]:
    """Conditions and exceptions of the answer that add or drop a « ne … pas » compared with the extract they repeat.

    The closest extract clause must share at least half of the words; its negation is looked for on
    24 words (one the answer would have added) or 12 words (one it would have dropped)."""
    flips = []
    for marker, clause in _clauses(text, CONDITION):
        short = _first_words(clause, CLAUSE_WORDS)
        words = set(tokenize(short))
        if len(words) < 3:
            continue
        overlaps = [
            (len(words & set(tokenize(_first_words(other, LONG_CLAUSE_WORDS)))) / len(words), other)
            for extract in extracts
            for _, other in _clauses(extract, CONDITION)
        ]
        overlap, closest = max(overlaps, default=(0.0, ""))
        if overlap < 0.5:
            continue
        added = CLAUSE_NEGATION.search(short) and not CLAUSE_NEGATION.search(_first_words(closest, LONG_CLAUSE_WORDS))
        dropped = not CLAUSE_NEGATION.search(short) and CLAUSE_NEGATION.search(_first_words(closest, CLAUSE_WORDS))
        if added or dropped:
            flips.append(f"{marker} {short}")
    return flips


def quotes_not_in_extracts(text: str, extracts: list[str]) -> list[str]:
    """Texts written between « » in the answer that no verified extract contains."""
    missing = []
    for quote in QUOTE.findall(text):
        if len(quote.split()) < MIN_QUOTE_WORDS or ABOUT_PASSAGES.search(quote) or PARTIAL_LIST.search(quote):
            continue  # the wordings asked by the prompt are not quotes of the law
        if not any(found_word_for_word(quote, extract, min_words=MIN_QUOTE_WORDS) for extract in extracts):
            missing.append(quote)
    return missing


def unquoted_exceptions(text: str, extracts: list[str], already_flagged: list[str] = ()) -> list[str]:
    """Exceptions ("sauf si"…) written outside « » with too few words of any verified extract."""
    unquoted = []
    for marker, clause in _clauses(QUOTE.sub(" ", text), EXCEPTION):
        words = set(tokenize(_first_words(clause, CLAUSE_WORDS)))
        if len(words) < 3 or f"{marker} {_first_words(clause, CLAUSE_WORDS)}" in already_flagged:
            continue
        if not any(len(words & set(tokenize(extract))) / len(words) >= EXCEPTION_SUPPORT for extract in extracts):
            unquoted.append(f"{marker} {_first_words(clause, CLAUSE_WORDS)}")
    return unquoted


def _case_list(extract: Extract, passages: list[SearchResult]) -> tuple[int, list[str]] | None:
    """(passage number, cases) if the extract announces a list of cases a), b)… or is one of them."""
    lines = passages[extract.passage - 1].text.split("\n")
    start = _comparable(_first_words(ELLIPSIS.split(extract.text)[0], 8))
    index = next((i for i, line in enumerate(lines) if start and start in _comparable(line)), None)
    if index is None:
        return None
    intro = index
    while intro > 0 and LIST_ITEM.match(lines[intro]):
        intro -= 1
    announcement = re.split(r"(?<=\.)\s", lines[intro])[-1]
    if not CASE_LIST_INTRO.search(announcement) or CONTENT_LIST_INTRO.search(announcement):
        return None  # a list of contents (« les informations suivantes ») is not a list of cases
    if intro == index and not ELLIPSIS.sub("", extract.text).rstrip(" .»").endswith(":"):
        return None  # the extract is another sentence of the same paragraph
    cases = []
    for line in lines[intro + 1:]:
        if not LIST_ITEM.match(line):
            break
        cases.append(line)
    return (extract.passage, cases) if len(cases) >= 2 else None


def incomplete_case_lists(text: str, extracts: list[Extract], passages: list[SearchResult]) -> list[tuple[int, int, int]]:
    """(passage, cases repeated, cases listed) for the lists of cases the answer only partly repeats, without saying so."""
    if PARTIAL_LIST.search(text):
        return []
    answer_words = set(tokenize(text))
    incomplete = set()
    for extract in extracts:
        if not extract.verified or not extract.passage:
            continue
        found = _case_list(extract, passages)
        if not found:
            continue
        number, cases = found
        heads = [set(tokenize(case)[:15]) for case in cases]
        repeated = sum(1 for head in heads if head and len(head & answer_words) / len(head) >= CASE_COVERED)
        if repeated < len(cases):
            incomplete.add((number, repeated, len(cases)))
    return sorted(incomplete)


def _sentences_with_citations(text: str) -> list[tuple[str, list[int]]]:
    sentences = []
    for part in re.split(r"(?<=[.!?])\s+|\n+", text):
        numbers = [number for match in CITATION.finditer(part) for number in (_cited_numbers(match.group(1)) or [])]
        sentence = re.sub(r"\s+([.,;:!?])", r"\1", re.sub(r"^[\s>*•-]+", "", CITATION.sub("", part))).strip()
        if sentence:
            sentences.append((sentence, numbers))
    return sentences


def other_actor_duties(text: str, extracts: list[Extract]) -> list[str]:
    """Sentences that rely on an extract addressed to a provider, importer… without naming that actor."""
    by_passage: dict[int, list[str]] = {}
    for extract in extracts:
        if extract.verified and extract.passage:
            by_passage.setdefault(extract.passage, []).append(_first_words(extract.text, 6))
    unnamed = []
    for sentence, numbers in _sentences_with_citations(text):
        subjects = [subject for number in numbers for subject in by_passage.get(number, [])]
        if any(USER_ROLE.search(subject) for subject in subjects):
            continue  # the extract also speaks to the deployer or the controller
        if any(OTHER_ACTOR.search(subject) for subject in subjects) and not OTHER_ACTOR.search(sentence):
            unnamed.append(sentence)
    return unnamed


def unnamed_regulations(text: str, extracts: list[Extract], passages: list[SearchResult]) -> list[str]:
    """In an answer that relies on both the RGPD and the AI Act, sentences that do not say which one they use."""
    regulations = {passages[extract.passage - 1].metadata["regulation"] for extract in extracts if extract.verified and extract.passage}
    if len(regulations) < 2:
        return []
    unnamed = []
    for sentence, numbers in _sentences_with_citations(text):
        for number in numbers:
            name = passages[number - 1].metadata["regulation"] if 1 <= number <= len(passages) else None
            if name in REGULATION_NAMES and not REGULATION_NAMES[name].search(sentence) and sentence not in unnamed:
                unnamed.append(sentence)
    return unnamed


def _short(sentence: str, length: int = 120) -> str:
    return sentence if len(sentence) <= length else sentence[:length].rsplit(" ", 1)[0] + " …"


def _more(found: list) -> str:
    return f" (et {len(found) - 1} autre(s))" if len(found) > 1 else ""


# ---------------------------------------------------------------- answer


def _warnings(found: int, passages: list[SearchResult], chat_model: ChatModel, generation: Generation,
              extracts: list[Extract], refused: bool, citations: CitationCheck, answer_written: bool,
              answer_text: str) -> list[str]:
    warnings = []
    if len(passages) < found:
        warnings.append(
            f"{found - len(passages)} passage(s) retiré(s) faute de place dans le contexte du modèle (LLM_NUM_CTX = {chat_model.num_ctx})."
        )
    if generation.truncated:
        warnings.append(
            f"Réponse coupée : le modèle a atteint la limite de {chat_model.max_tokens} tokens (LLM_MAX_TOKENS), "
            "la fin de la réponse manque. Posez une question plus précise ou augmentez LLM_MAX_TOKENS dans .env."
        )
    rejected = [extract for extract in extracts if not extract.verified]
    if refused:
        if not answer_written and (extracts or generation.text.strip()):
            warnings.append(
                "Le modèle n'a pas rédigé de réponse après ses extraits (réponse coupée ou format EXTRAITS / RÉPONSE "
                "non respecté) : un refus est affiché par prudence."
            )
        elif extracts and not any(extract.verified for extract in extracts):
            warnings.append(
                f"Aucun des {len(extracts)} extrait(s) recopié(s) par le modèle n'a été retrouvé mot pour mot dans "
                "les passages : sa réponse a été remplacée par un refus."
            )
        return warnings
    if rejected:
        numbers = ", ".join(f"[{extract.number}]" if extract.number else "sans numéro" for extract in rejected)
        warnings.append(f"{len(rejected)} extrait(s) introuvable(s) mot pour mot dans le passage cité ({numbers}) : ignoré(s).")
    if citations.unknown:
        unknown = ", ".join(f"[{number}]" for number in citations.unknown)
        warnings.append(f"Citation vers un passage inexistant : {unknown} (seuls les passages [1] à [{len(passages)}] ont été fournis).")
    verified_passages = {extract.passage for extract in extracts if extract.verified}
    unsupported = [number for number in citations.cited if number not in verified_passages]
    if unsupported:
        listed = ", ".join(f"[{number}]" for number in unsupported)
        warnings.append(f"La réponse cite {listed} sans extrait vérifié de ce(s) passage(s) : vérifiez ces affirmations.")
    verified_texts = [extract.text for extract in extracts if extract.verified]
    if not citations.cited and not citations.unknown:
        # without [n], the answer must at least repeat the words of the verified extracts
        weak = unsupported_sentences(answer_text, verified_texts)
        if weak:
            warnings.append(
                f"La réponse ne cite aucun passage et une phrase ne reprend pas les extraits vérifiés : « {_short(weak[0])} »{_more(weak)}. "
                "Vérifiez-la dans les textes."
            )
    for claim in unbacked_absence_claims(answer_text, verified_texts):
        warnings.append(f"La réponse affirme une absence ou une impossibilité qu'aucun extrait ne dit : « {_short(claim)} ». Vérifiez ce point.")
    flips = flipped_negations(answer_text, verified_texts)
    if flips:
        warnings.append(
            f"La réponse change le sens d'une condition ou d'une exception (négation ajoutée ou retirée par rapport à l'extrait) : "
            f"« {_short(flips[0])} »{_more(flips)}. Vérifiez ce point."
        )
    missing = quotes_not_in_extracts(answer_text, verified_texts)
    if missing:
        warnings.append(f"La réponse met entre « » un texte introuvable dans les extraits vérifiés : « {_short(missing[0])} »{_more(missing)}.")
    unquoted = unquoted_exceptions(answer_text, verified_texts, already_flagged=flips)
    if unquoted:
        warnings.append(
            f"La réponse formule une exception qui ne reprend pas les extraits vérifiés : « {_short(unquoted[0])} »{_more(unquoted)}. "
            "Vérifiez-la dans les textes."
        )
    lists = incomplete_case_lists(answer_text, extracts, passages)
    if lists:
        number, repeated, listed = lists[0]
        warnings.append(
            f"La réponse ne reprend que {repeated} des {listed} cas énumérés au passage [{number}], sans dire qu'elle n'en cite "
            f"qu'une partie{_more(lists)}. Vérifiez la liste complète."
        )
    others = other_actor_duties(answer_text, extracts)
    if others:
        warnings.append(
            f"La réponse s'appuie sur un extrait qui vise un fournisseur, un importateur ou un distributeur, sans nommer cet acteur : "
            f"« {_short(others[0])} »{_more(others)}. Vérifiez qui est concerné."
        )
    unnamed = unnamed_regulations(answer_text, extracts, passages)
    if unnamed:
        warnings.append(
            f"La réponse s'appuie sur le RGPD et l'AI Act sans dire de quel règlement vient chaque obligation : "
            f"« {_short(unnamed[0])} »{_more(unnamed)}."
        )
    if uses_tu(answer_text):
        warnings.append("La réponse tutoie la personne (« tu », « ton »…) alors que le copilote doit toujours vouvoyer.")
    return warnings


def answer_question(
    question: str,
    index_dir: Path,
    embedder: Embedder,
    chat_model: ChatModel,
    k: int = 5,
    on_text: Callable[[str], None] | None = None,
    mode: str = "vector",
    lexicon: str = "off",
    max_per_article: int | None = None,
) -> RagAnswer:
    """Search the closest passages, have the model quote them and answer, then check everything."""
    start = time.perf_counter()
    found = search(question, index_dir, embedder, k=k, mode=mode, lexicon=lexicon, max_per_article=max_per_article)
    search_seconds = time.perf_counter() - start
    passages = fit_passages(question, found, chat_model)
    return answer_from_passages(question, passages, chat_model, on_text, search_seconds, found=len(found))


def answer_from_passages(
    question: str,
    passages: list[SearchResult],
    chat_model: ChatModel,
    on_text: Callable[[str], None] | None = None,
    search_seconds: float = 0.0,
    found: int | None = None,
    system_prompt: str = SYSTEM_PROMPT,
) -> RagAnswer:
    """Have the model answer from the given passages (also used to compare models or prompts on the same passages)."""
    stream = AnswerStream(on_text, passages) if on_text else None
    start = time.perf_counter()
    generation = chat_model.generate(build_messages(question, passages, system_prompt), on_text=stream.feed if stream else None)
    generation_seconds = time.perf_counter() - start
    if stream:
        stream.close()

    text, extracts, refused = finalize_answer(generation.text, passages)
    answer_written = bool(split_answer(generation.text)[1])
    citations = check_citations(text, len(passages)) if not refused else CitationCheck(cited=[], unknown=[])
    cited = sorted(set(citations.cited) | {extract.passage for extract in extracts if extract.verified}) if not refused else []
    return RagAnswer(
        question=question,
        text=text,
        raw_text=generation.text,
        extracts=extracts,
        refused=refused,
        passages=passages,
        sources=build_sources(passages, cited),
        citations=citations,
        warnings=_warnings(
            found if found is not None else len(passages), passages, chat_model, generation, extracts, refused, citations, answer_written,
            text,
        ),
        generation=generation,
        search_seconds=search_seconds,
        generation_seconds=generation_seconds,
    )


def render_footer(answer: RagAnswer) -> str:
    """Verified extracts, sources, warnings and the legal warning, added by the code after every answer."""
    lines = []
    verified = answer.verified_extracts
    if verified:
        lines.append("Extraits vérifiés (recopiés mot pour mot des textes) :")
        for extract in verified:
            lines.append(f"  [{extract.passage}] « {extract.text} »")
        lines.append("")
    lines.append("Sources citées :")
    cited = [source for source in answer.sources if source.cited]
    if not cited:
        lines.append("  aucune")
    for source in cited:
        lines += [f"  [{source.number}] {source.label} (version du {source.version_date})", f"      {source.url}"]
    others = [source for source in answer.sources if not source.cited]
    if others:
        lines.append("Passages consultés mais non cités :")
        for source in others:
            lines += [f"  [{source.number}] {source.label}", f"      {source.url}"]
    for warning in answer.warnings:
        lines.append(f"Attention : {warning}")
    lines += ["", DISCLAIMER]
    return "\n".join(lines)

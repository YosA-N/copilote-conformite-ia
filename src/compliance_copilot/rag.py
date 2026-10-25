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
from compliance_copilot.llm import ChatModel, Generation

SYSTEM_PROMPT = """Tu es le copilote de conformité : tu aides les PME et les associations à comprendre le RGPD et l'AI Act.

Réponds toujours en deux parties, dans cet ordre :

EXTRAITS :
- [numéro du passage] « phrase recopiée mot pour mot dans ce passage »
(quatre extraits au plus, chacun sur sa ligne ; chaque extrait est une seule phrase ou un seul point a), b)…, jamais un paragraphe entier ; choisis seulement ce qui répond directement à la question ; recopie exactement, sans modifier ni résumer ; si tu sautes une partie d'une phrase, remplace-la par « … »)

RÉPONSE :
ta réponse, écrite uniquement à partir des extraits ci-dessus, avec le numéro du passage entre crochets après chaque affirmation, par exemple [1].

Règles à respecter :
1. Utilise UNIQUEMENT les passages fournis, numérotés [1], [2]… N'utilise aucune autre connaissance.
2. Si aucun passage ne répond à la question, écris « EXTRAITS : aucun » puis « RÉPONSE : Les textes trouvés ne permettent pas de répondre à cette question. »
3. N'invente jamais de numéro d'article, de date, de durée ni de délai : reprends uniquement ceux des extraits.
4. Vérifie que chaque extrait s'applique bien à la situation de la question : à qui s'adresse le texte (responsable du traitement, sous-traitant, fournisseur, déployeur…) et dans quel cas. Sinon, ne l'utilise pas.
5. Distingue ce qui est obligatoire (« doit ») de ce qui est permis (« peut »).
6. Écris en français simple, pour une personne qui n'est pas juriste, et vouvoie-la. Commence par la réponse directe en une ou deux phrases, puis explique brièvement.
7. Ne donne aucun conseil qui ne figure pas dans les extraits."""

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


def found_word_for_word(extract: str, passage_text: str) -> bool:
    """True if the extract appears in the passage; '…' may skip a part, the pieces staying in order."""
    pieces = [_comparable(piece).strip(" .,;:") for piece in ELLIPSIS.split(extract)]
    pieces = [piece for piece in pieces if piece]
    if not pieces or sum(len(piece.split()) for piece in pieces) < MIN_EXTRACT_WORDS:
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


def build_messages(question: str, passages: list[SearchResult]) -> list[dict]:
    """System prompt, then the numbered passages and the question."""
    numbered = "\n\n".join(f"[{number}] {passage.text}" for number, passage in enumerate(passages, start=1))
    user = f"Passages :\n\n{numbered}\n\nQuestion : {question}"
    return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}]


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


# ---------------------------------------------------------------- answer


def _warnings(found: int, passages: list[SearchResult], chat_model: ChatModel, generation: Generation,
              extracts: list[Extract], refused: bool, citations: CitationCheck, answer_written: bool) -> list[str]:
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
    if not citations.cited and not citations.unknown:
        warnings.append("La réponse ne cite aucun passage : vérifiez-la avec les extraits et les sources.")
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
) -> RagAnswer:
    """Search the closest passages, have the model quote them and answer, then check everything."""
    start = time.perf_counter()
    found = search(question, index_dir, embedder, k=k, mode=mode, lexicon=lexicon)
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
) -> RagAnswer:
    """Have the model answer from the given passages (also used to compare models on the same passages)."""
    stream = AnswerStream(on_text, passages) if on_text else None
    start = time.perf_counter()
    generation = chat_model.generate(build_messages(question, passages), on_text=stream.feed if stream else None)
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
            found if found is not None else len(passages), passages, chat_model, generation, extracts, refused, citations, answer_written
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

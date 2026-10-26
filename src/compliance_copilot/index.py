"""Search index: the chunks and their embeddings, stored in a local Chroma database.

The index folder (data/index/) holds the Chroma files and manifest.json, which records what
the index was built from: the fingerprint (SHA-256) of chunks.jsonl and the embedding model.
An unchanged corpus is therefore never embedded twice.
"""

import hashlib
import json
import re
import time
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import chromadb
from chromadb.config import Settings as ChromaSettings

from compliance_copilot.embeddings import Embedder
from compliance_copilot.lexical import BM25, reciprocal_rank_fusion
from compliance_copilot.lexicon import expand_query

COLLECTION_NAME = "chunks"
MANIFEST_NAME = "manifest.json"
BATCH_SIZE = 16  # chunks sent to the embedding model at once
SEARCH_MODES = ("vector", "hybrid")
LEXICON_TARGETS = ("off", "keywords", "all")
HYBRID_CANDIDATES = 50  # chunks taken from each ranking before fusion
_KEYWORD_INDEXES: dict[tuple, BM25] = {}
_FIRST_PARAGRAPHS: dict[tuple, dict[str, str]] = {}


class IndexNotReadyError(RuntimeError):
    """The index is missing or does not match the configuration; the message says what to do."""


@dataclass
class BuildReport:
    status: str  # "built" or "unchanged"
    chunk_count: int
    seconds: float


@dataclass
class SearchResult:
    rank: int
    score: float  # cosine similarity between the question and the chunk: 1 = same meaning
    id: str
    text: str
    metadata: dict


def load_chunks(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_manifest(index_dir: Path) -> dict | None:
    path = index_dir / MANIFEST_NAME
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def _client(index_dir: Path):
    # Chroma sends anonymous usage statistics unless told not to: everything stays local here.
    return chromadb.PersistentClient(path=str(index_dir), settings=ChromaSettings(anonymized_telemetry=False))


def open_collection(index_dir: Path):
    """The Chroma collection of an index that has already been built."""
    return _client(index_dir).get_collection(COLLECTION_NAME, embedding_function=None)


def _metadata(chunk: dict) -> dict:
    """Chunk fields stored next to its vector; Chroma rejects None, so empty fields are left out."""
    return {key: value for key, value in chunk.items() if key not in ("id", "text") and value is not None}


def build_index(
    chunks_path: Path,
    index_dir: Path,
    embedder: Embedder,
    force: bool = False,
    progress: Callable[[int, int], None] | None = None,
) -> BuildReport:
    """Embed every chunk and store it in Chroma, unless the corpus and the model are unchanged."""
    chunks = load_chunks(chunks_path)
    if not chunks:
        raise ValueError(f"{chunks_path} ne contient aucun chunk.")
    fingerprint = {"corpus_sha256": file_sha256(chunks_path), "embedding_model": embedder.model}
    manifest = read_manifest(index_dir)
    if not force and manifest and all(manifest.get(key) == value for key, value in fingerprint.items()):
        return BuildReport("unchanged", manifest["chunk_count"], 0.0)

    start = time.perf_counter()
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / MANIFEST_NAME).unlink(missing_ok=True)  # an interrupted build must not look complete
    client = _client(index_dir)
    if COLLECTION_NAME in {collection.name for collection in client.list_collections()}:
        client.delete_collection(COLLECTION_NAME)  # on Windows, deleting the folder itself fails while it is open
    collection = client.create_collection(
        name=COLLECTION_NAME,
        configuration={"hnsw": {"space": "cosine"}},
        embedding_function=None,  # vectors always come from our embedder, never from a model Chroma would download
    )
    dimension = 0
    for first in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[first : first + BATCH_SIZE]
        vectors = embedder.embed([chunk["text"] for chunk in batch])
        dimension = len(vectors[0])
        collection.add(
            ids=[chunk["id"] for chunk in batch],
            embeddings=vectors,
            documents=[chunk["text"] for chunk in batch],
            metadatas=[_metadata(chunk) for chunk in batch],
        )
        if progress:
            progress(first + len(batch), len(chunks))
    seconds = time.perf_counter() - start

    manifest = {
        **fingerprint,
        "chunk_count": len(chunks),
        "dimension": dimension,
        "built_at": datetime.now().isoformat(timespec="seconds"),
        "build_seconds": round(seconds, 1),
    }
    (index_dir / MANIFEST_NAME).write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return BuildReport("built", len(chunks), seconds)


def _keyword_index(index_dir: Path, manifest: dict) -> BM25:
    """BM25 over every chunk of the index, built once per index version and kept in memory."""
    key = (str(index_dir), manifest["corpus_sha256"], manifest["built_at"])
    if key not in _KEYWORD_INDEXES:
        stored = open_collection(index_dir).get(include=["documents"])
        _KEYWORD_INDEXES[key] = BM25(stored["ids"], stored["documents"])
    return _KEYWORD_INDEXES[key]


def _first_paragraphs(index_dir: Path, manifest: dict) -> dict[str, str]:
    """{article: id of its first paragraph} for the articles split into paragraphs, built once per index version."""
    key = (str(index_dir), manifest["corpus_sha256"], manifest["built_at"])
    if key not in _FIRST_PARAGRAPHS:
        ids = open_collection(index_dir).get(include=[])["ids"]
        firsts: dict[str, str] = {}
        for chunk_id in sorted(ids):  # 'par_1' < 'par_1_a-e' < 'par_1_f-h'
            if paragraph_number(chunk_id) == 1:
                firsts.setdefault(article_of(chunk_id), chunk_id)
        _FIRST_PARAGRAPHS[key] = firsts
    return _FIRST_PARAGRAPHS[key]


def article_of(chunk_id: str) -> str:
    """'gdpr:art_37:par_1' → 'gdpr:art_37': the article or annex a chunk belongs to."""
    return ":".join(chunk_id.split(":")[:2])


def paragraph_number(chunk_id: str) -> int | None:
    """'gdpr:art_9:par_2_a-i' → 2; None for a whole article, a definition, an annex point or 'par_1-bis'."""
    parts = chunk_id.split(":")
    match = re.fullmatch(r"par_(\d+)(?:_[\w-]+)?", parts[2]) if len(parts) > 2 else None
    return int(match.group(1)) if match else None


def with_first_paragraphs(chunk_ids: list[str], first_paragraphs: dict[str, str]) -> list[str]:
    """After the first kept chunk of an article that is a later paragraph, add the article's first
    paragraph, which often states the rule (art. 9, § 1: the prohibition), if it is not already there.
    It comes in second place for its article, or third if two of its chunks were already kept."""
    kept, present = [], set(chunk_ids)
    for chunk_id in chunk_ids:
        kept.append(chunk_id)
        first = first_paragraphs.get(article_of(chunk_id))
        part = chunk_id.split(":")[2] if chunk_id.count(":") >= 2 else ""
        is_later_paragraph = part.startswith("par_") and paragraph_number(chunk_id) != 1  # 'par_3', 'par_1-bis'…
        if first and first not in present and is_later_paragraph:
            kept.append(first)
            present.add(first)
    return kept


def limit_per_article(chunk_ids: list[str], limit: int | None) -> list[str]:
    """Keep at most `limit` chunks of each article, in order, so that one long article cut into
    paragraphs cannot fill all the places (None: no limit)."""
    if not limit:
        return chunk_ids
    kept, counts = [], {}
    for chunk_id in chunk_ids:
        article = article_of(chunk_id)
        if counts.get(article, 0) < limit:
            kept.append(chunk_id)
            counts[article] = counts.get(article, 0) + 1
    return kept


def search(
    question: str,
    index_dir: Path,
    embedder: Embedder,
    k: int = 5,
    mode: str = "vector",
    lexicon: str = "off",
    max_per_article: int | None = None,
    first_paragraph: bool = False,
) -> list[SearchResult]:
    """The k chunks closest to the question, best first.

    mode "vector" ranks by meaning only; "hybrid" also ranks by keywords (BM25) and fuses both
    rankings (RRF). lexicon "keywords" adds legal wording to the keyword query, "all" to both
    queries. max_per_article keeps at most that many chunks of the same article; first_paragraph
    adds the first paragraph of an article when a later one is kept (see with_first_paragraphs).
    The score is always the cosine similarity between the question and the chunk.
    """
    if mode not in SEARCH_MODES or lexicon not in LEXICON_TARGETS:
        raise ValueError(f"mode doit valoir {SEARCH_MODES} et lexicon {LEXICON_TARGETS}")
    manifest = read_manifest(index_dir)
    if manifest is None:
        raise IndexNotReadyError("L'index n'existe pas encore : lancez d'abord scripts\\build_index.py.")
    if manifest["embedding_model"] != embedder.model:
        raise IndexNotReadyError(
            f"L'index a été construit avec le modèle {manifest['embedding_model']}, mais .env demande "
            f"{embedder.model} : relancez scripts\\build_index.py."
        )
    expanded = expand_query(question) if lexicon != "off" else question
    vector = embedder.embed([expanded if lexicon == "all" else question])[0]
    collection = open_collection(index_dir)

    if mode == "vector":
        candidates = k * 4 if max_per_article else k  # room to skip the extra chunks of an article
        found = collection.query(query_embeddings=[vector], n_results=candidates, include=["distances"])
        ranked = found["ids"][0]
        distances = dict(zip(ranked, found["distances"][0]))
    else:
        distances = {}
        by_meaning = collection.query(query_embeddings=[vector], n_results=HYBRID_CANDIDATES, include=[])["ids"][0]
        by_keywords = [chunk_id for chunk_id, _ in _keyword_index(index_dir, manifest).search(expanded, HYBRID_CANDIDATES)]
        ranked = [chunk_id for chunk_id, _ in reciprocal_rank_fusion([by_meaning, by_keywords])]
    best = limit_per_article(ranked, max_per_article)
    if first_paragraph:
        best = with_first_paragraphs(best, _first_paragraphs(index_dir, manifest))
    best = best[:k]
    stored = collection.get(ids=best, include=["documents", "metadatas", "embeddings"])
    found = dict(zip(stored["ids"], zip(stored["documents"], stored["metadatas"], stored["embeddings"])))
    results = []
    for rank, chunk_id in enumerate(best, start=1):
        text, metadata, embedding = found[chunk_id]
        if chunk_id in distances:
            similarity = 1 - distances[chunk_id]
        else:  # fused ranking or added first paragraph: both vectors are normalised
            similarity = float(sum(a * b for a, b in zip(vector, embedding)))
        results.append(SearchResult(rank=rank, score=similarity, id=chunk_id, text=text, metadata=metadata))
    return results

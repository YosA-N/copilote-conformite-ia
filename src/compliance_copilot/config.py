"""Application settings, read from environment variables and the local .env file."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_LLM_MODEL = "qwen3:4b-instruct"  # chosen in session 5 (eval/results_v1.md); before: ministral-3:3b
DEFAULT_EMBEDDING_MODEL = "bge-m3"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
INDEX_DIR = PROJECT_ROOT / "data" / "index"
EVAL_DIR = PROJECT_ROOT / "eval"


@dataclass(frozen=True)
class Settings:
    ollama_base_url: str
    llm_model: str
    embedding_model: str
    index_embedding_device: str = "gpu"  # "gpu" or "cpu", used to build the index
    query_embedding_device: str = "cpu"  # used for questions, to leave the GPU to the language model
    llm_num_ctx: int = 8192  # context size in tokens: passages + question + answer
    llm_num_gpu: int | None = 99  # model layers on the GPU (99 = all); None lets Ollama decide
    llm_temperature: float = 0.1
    llm_max_tokens: int = 2000  # room for the verbatim extracts, then the answer (1500 until session 6)
    search_mode: str = "vector"  # "vector" or "hybrid" (vectors + BM25, measured worse in session 5)
    search_lexicon: str = "all"  # "off", "keywords" or "all": add legal wording to the question
    search_max_per_article: int | None = 2  # at most 2 chunks of the same article among the passages
    search_k: int = 5  # passages given to the language model (8 measured at session 6: slower, no gain with the lexicon)
    search_first_paragraph: bool = True  # add the first paragraph of an article when a later one is kept (session 6)
    answer_judge: bool = True  # second short call: do the verified extracts answer the question directly?


def optional_int(value: str | None) -> int | None:
    """'' or None → None; '20' → 20."""
    return int(value) if value and value.strip() else None


def load_settings() -> Settings:
    """Load settings from .env (if present), falling back to the defaults above."""
    load_dotenv()
    return Settings(
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL).rstrip("/"),
        llm_model=os.getenv("LLM_MODEL", DEFAULT_LLM_MODEL),
        embedding_model=os.getenv("EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL),
        index_embedding_device=os.getenv("INDEX_EMBEDDING_DEVICE", "gpu").strip().lower(),
        query_embedding_device=os.getenv("QUERY_EMBEDDING_DEVICE", "cpu").strip().lower(),
        llm_num_ctx=int(os.getenv("LLM_NUM_CTX", "8192")),
        llm_num_gpu=optional_int(os.getenv("LLM_NUM_GPU", "99")),
        llm_temperature=float(os.getenv("LLM_TEMPERATURE", "0.1")),
        llm_max_tokens=int(os.getenv("LLM_MAX_TOKENS", "2000")),
        search_mode=os.getenv("SEARCH_MODE", "vector").strip().lower(),
        search_lexicon=os.getenv("SEARCH_LEXICON", "all").strip().lower(),
        search_max_per_article=optional_int(os.getenv("SEARCH_MAX_PER_ARTICLE", "2")),
        search_k=int(os.getenv("SEARCH_K", "5")),
        search_first_paragraph=os.getenv("SEARCH_FIRST_PARAGRAPH", "on").strip().lower() in {"on", "1", "true", "oui"},
        answer_judge=os.getenv("ANSWER_JUDGE", "on").strip().lower() in {"on", "1", "true", "oui"},
    )

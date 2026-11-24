"""Optional reranker: a cross-encoder scores (question, passage) pairs and reorders the candidates of the search.

On by default in remote mode only (SEARCH_RERANK=auto, session 7 ter); off in local mode. The model (BAAI/bge-reranker-v2-m3, Apache-2.0, 568 million parameters,
about 2.3 GB downloaded once into the Hugging Face cache) runs on the CPU with torch and transformers, which
are NOT required by the copilot: they are imported only when the reranker is switched on, so everything else
works without them. Measured in session 7 bis (eval/results_v4.md).
"""

import importlib.util
from collections.abc import Callable
from dataclasses import replace
from typing import Protocol

from compliance_copilot.config import Settings

DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"
MAX_LENGTH = 512  # tokens of question + passage given to the model; longer passages are cut at the end
INSTALL_HINT = "pip install -e .[rerank]"


class Reranker(Protocol):
    model: str

    def score(self, question: str, texts: list[str]) -> list[float]:
        """One relevance score per text, higher = more relevant to the question; any scale."""
        ...


class RerankerError(RuntimeError):
    """The reranker was asked for but cannot run; the message can be shown to the user as is."""


class CrossEncoderReranker:
    """BAAI/bge-reranker-v2-m3 (or another sequence-classification cross-encoder) on the CPU, loaded on first use."""

    def __init__(self, model: str = DEFAULT_RERANKER_MODEL, max_length: int = MAX_LENGTH, batch_size: int = 8):
        self.model = model
        self.max_length = max_length
        self.batch_size = batch_size
        self._tokenizer = self._network = None
        self.load_seconds = 0.0

    def _load(self) -> None:
        if self._network is not None:
            return
        import time

        start = time.perf_counter()
        try:
            import torch
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
        except ImportError as error:  # torch or transformers missing: the copilot itself does not need them
            raise RerankerError(
                f"Reranker demandé (SEARCH_RERANK=on) mais {error.name} n'est pas installé : installez les dépendances "
                f"optionnelles avec {INSTALL_HINT}, ou mettez SEARCH_RERANK=auto ou off."
            ) from None
        torch.set_num_threads(max(1, torch.get_num_threads()))
        self._torch = torch
        self._tokenizer = AutoTokenizer.from_pretrained(self.model)
        self._network = AutoModelForSequenceClassification.from_pretrained(self.model)
        self._network.eval()
        self.load_seconds = time.perf_counter() - start

    def score(self, question: str, texts: list[str]) -> list[float]:
        if not texts:
            return []
        self._load()
        scores: list[float] = []
        with self._torch.inference_mode():
            for start in range(0, len(texts), self.batch_size):
                batch = texts[start : start + self.batch_size]
                encoded = self._tokenizer([question] * len(batch), batch, padding=True, truncation=True,
                                          max_length=self.max_length, return_tensors="pt")
                logits = self._network(**encoded).logits.view(-1).float()
                scores.extend(logits.tolist())
        return scores


FALLBACK_NOTICE = (
    "Reformulation et reranker prévus par défaut en mode distant, mais torch ou transformers n'est pas installé : "
    "recherche sans reformulation ni reranker (configuration validée avant la séance 7 ter). "
    f"Pour les activer : {INSTALL_HINT}. Pour ne plus voir ce message : SEARCH_RERANK=off dans .env."
)


def reranker_installed() -> bool:
    """True if torch and transformers can be imported (checked without importing them)."""
    try:
        return all(importlib.util.find_spec(name) is not None for name in ("torch", "transformers"))
    except (ImportError, ValueError):
        return False


def resolve_search(settings: Settings, installed: Callable[[], bool] = reranker_installed) -> tuple[Settings, str]:
    """The settings with SEARCH_RERANK and SEARCH_REWRITE decided (on or off) for this run, and a notice to show.

    In remote mode, auto turns both on. If torch is missing, auto falls back to the configuration validated before
    session 7 ter, without the reranker AND without the rewriting: never the rewriting alone, which set back v0 and
    v1. SEARCH_RERANK=on written in .env is kept: the reranker then stops with its clear error on first use."""
    rerank, rewrite, notice = settings.search_rerank, settings.search_rewrite, ""
    if rerank and settings.search_rerank_mode == "auto" and not installed():
        rerank, rewrite, notice = False, False, FALLBACK_NOTICE
    decided = {True: "on", False: "off"}
    return replace(settings, search_rerank_mode=decided[rerank], search_rewrite_mode=decided[rewrite]), notice


def make_reranker(settings: Settings) -> CrossEncoderReranker | None:
    """The reranker configured in .env, or None when it is not used (local mode by default)."""
    if not settings.search_rerank:
        return None
    return CrossEncoderReranker(settings.reranker_model)

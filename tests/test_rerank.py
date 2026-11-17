"""The optional reranker: off by default, nothing imported then (the copilot runs without torch), and when a
reranker is given, the candidates of the search are reordered by its scores before the per-article limit."""

import subprocess
import sys

from conftest import FakeEmbedder

from compliance_copilot.config import Settings
from compliance_copilot.index import search
from compliance_copilot.rerank import CrossEncoderReranker, RerankerError, make_reranker


class FakeReranker:
    """Scores a text by the number of times a wanted word appears in it; records what it was asked."""

    model = "fake-reranker"

    def __init__(self, wanted: str):
        self.wanted = wanted
        self.calls: list[tuple[str, int]] = []

    def score(self, question, texts):
        self.calls.append((question, len(texts)))
        return [float(text.lower().count(self.wanted)) for text in texts]


def test_reranker_is_off_by_default_and_nothing_heavy_is_imported():
    assert make_reranker(Settings(ollama_base_url="", llm_model="m", embedding_model="e")) is None
    code = ("import sys; import compliance_copilot.rerank, compliance_copilot.index, compliance_copilot.rag; "
            "print(sorted(m for m in ('torch', 'transformers') if m in sys.modules))")
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "[]"


def test_reranker_reorders_the_candidates_before_the_per_article_limit(index_dir, fake_embedder: FakeEmbedder):
    plain = search("désignation délégué", index_dir, fake_embedder, k=3)
    reranker = FakeReranker("haut risque")
    reranked = search("désignation délégué", index_dir, fake_embedder, k=3, reranker=reranker, rerank_candidates=6)

    assert [r.id for r in plain] != [r.id for r in reranked]
    assert {reranked[0].id, reranked[1].id} == {"ai_act:art_4a", "ai_act:anx_III"}  # the two chunks that say « haut risque »
    assert reranked[0].rerank_score and reranked[0].rerank_score >= (reranked[1].rerank_score or 0)
    assert reranked[0].score <= 1.0  # the shown score stays the cosine similarity
    assert reranker.calls == [("désignation délégué", 6)]
    assert [r.rank for r in reranked] == [1, 2, 3]


def test_missing_torch_gives_a_clear_error(monkeypatch):
    import builtins

    real_import = builtins.__import__

    def no_torch(name, *args, **kwargs):
        if name == "torch":
            raise ImportError("No module named 'torch'", name="torch")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", no_torch)
    try:
        CrossEncoderReranker("any/model").score("q", ["t"])
    except RerankerError as error:
        assert "torch" in str(error) and "pip install -e .[rerank]" in str(error) and "SEARCH_RERANK=off" in str(error)
    else:
        raise AssertionError("RerankerError expected")

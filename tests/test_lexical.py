"""Offline tests for the keyword search (BM25), the rank fusion (RRF) and the lexicon."""

import pytest

from compliance_copilot.index import search
from compliance_copilot.lexical import BM25, reciprocal_rank_fusion, tokenize
from compliance_copilot.lexicon import expand_query


def test_words_are_stemmed_without_accents_and_stop_words():
    assert tokenize("Les données conservées") == tokenize("donnees conserver")
    assert "le" not in tokenize("le délégué") and "de" not in tokenize("le délai de réponse")


def test_bm25_ranks_the_document_that_shares_the_rare_words_first():
    index = BM25(
        ["a", "b", "c"],
        [
            "Le responsable du traitement tient un registre des activités de traitement.",
            "Le délégué à la protection des données est désigné sur la base de ses qualités.",
            "Les données sont traitées de manière licite.",
        ],
    )

    results = index.search("désigner un délégué", k=3)

    assert results[0][0] == "b"
    assert all(score > 0 for _, score in results)
    assert "a" not in [doc for doc, _ in results]  # no shared word, no result


def test_rank_fusion_rewards_documents_found_by_both_searches():
    fused = dict(reciprocal_rank_fusion([["x", "y", "z"], ["y", "w"]], k=60))

    assert fused["y"] == pytest.approx(1 / 62 + 1 / 61)
    assert max(fused, key=fused.get) == "y"


def test_lexicon_adds_the_legal_wording_of_everyday_words():
    assert "délégué à la protection des données" in expand_query("Dois-je désigner un DPO ?")
    assert "informations à fournir" in expand_query("Que mettre dans la mention d'information ?")
    assert expand_query("Quel temps fait-il ?") == "Quel temps fait-il ?"


def test_hybrid_search_returns_the_best_chunks_with_their_similarity(index_dir, fake_embedder):
    results = search("désignation délégué", index_dir, fake_embedder, k=3, mode="hybrid", lexicon="keywords")

    assert [result.rank for result in results] == [1, 2, 3]
    assert results[0].id == "gdpr:art_37"
    assert all(-1 <= result.score <= 1 for result in results)


def test_unknown_search_options_are_rejected(index_dir, fake_embedder):
    with pytest.raises(ValueError):
        search("DPO", index_dir, fake_embedder, mode="magic")

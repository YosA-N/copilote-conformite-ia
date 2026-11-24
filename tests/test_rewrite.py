"""Query rewriting (session 7 ter): the model adds legal terms to the question before the search, never a conclusion."""

import pytest
from conftest import FakeChatModel

from compliance_copilot.index import search
from compliance_copilot.llm import Generation
from compliance_copilot.privacy import PersonalDataError
from compliance_copilot.rag import answer_question
from compliance_copilot.rewrite import MAX_TERMS, REWRITE_PROMPT, parse_terms, rewrite_terms


def test_terms_are_kept_only_when_they_hold_no_conclusion_no_number_and_few_words():
    reply = ("Termes : données biométriques ; traitement interdit ; article 9 ; consentement explicite ; Données biométriques ; "
             "une phrase beaucoup trop longue avec bien plus de huit mots dedans ; « obligation d'information » ; oui")
    assert parse_terms(reply) == ["données biométriques", "consentement explicite", "obligation d'information"]
    assert parse_terms("- sous-traitant\n- contrat de sous-traitance\n- 25 mai 2018") == ["sous-traitant", "contrat de sous-traitance"]
    assert len(parse_terms(" ; ".join(f"terme {chr(97 + i)}" for i in range(10)))) == MAX_TERMS
    assert parse_terms("pratiques interdites ; autorisé ; vous devez informer") == []


def test_the_model_gets_the_question_and_the_rules_in_one_short_call():
    model = FakeChatModel(reply="données biométriques ; données à caractère personnel")
    assert rewrite_terms("Une pointeuse à empreinte digitale ?", model) == ["données biométriques", "données à caractère personnel"]
    assert model.messages[0] == {"role": "system", "content": REWRITE_PROMPT}
    assert model.messages[1]["content"] == "Question : Une pointeuse à empreinte digitale ?"


class SpyEmbedder:
    """Records the texts it is asked to embed, and delegates to the fake embedder."""

    def __init__(self, inner):
        self.inner, self.model, self.texts = inner, inner.model, []

    def embed(self, texts):
        self.texts += texts
        return self.inner.embed(texts)


def test_the_terms_are_added_to_the_query_like_the_lexicon(index_dir, fake_embedder):
    spy = SpyEmbedder(fake_embedder)
    search("Qui désigner ?", index_dir, spy, k=3, lexicon="all", extra_terms=["délégué à la protection des données"])
    assert spy.texts[-1] == "Qui désigner ? (délégué à la protection des données)"
    search("Qui désigner ?", index_dir, spy, k=3, lexicon="all")
    assert spy.texts[-1] == "Qui désigner ?"


class RewritingModel(FakeChatModel):
    """Answers the rewriting call with legal terms, then the question with the usual reply."""

    def __init__(self, terms: str, reply: str = "EXTRAITS : aucun\n\nRÉPONSE :\nLes textes trouvés ne permettent pas de répondre à cette question."):
        super().__init__(reply=reply)
        self.terms, self.calls = terms, []

    def generate(self, messages, on_text=None):
        self.calls.append(messages)
        if len(self.calls) == 1:
            return Generation(self.terms, prompt_tokens=50, completion_tokens=10, seconds=0.1, tokens_per_second=100.0, truncated=False)
        return super().generate(messages, on_text)


def test_answer_question_rewrites_first_when_asked_and_keeps_the_terms(index_dir, fake_embedder):
    model = RewritingModel("délégué à la protection des données ; traitement interdit")
    answer = answer_question("Qui désigner ?", index_dir, fake_embedder, model, k=3, rewrite=True)
    assert answer.rewrite_terms == ["délégué à la protection des données"]
    assert model.calls[0][0]["content"] == REWRITE_PROMPT and len(model.calls) == 2

    plain = RewritingModel("ignored")
    assert answer_question("Qui désigner ?", index_dir, fake_embedder, plain, k=3).rewrite_terms == []
    assert plain.calls[0][0]["content"] != REWRITE_PROMPT  # off by default: no rewriting call


def test_in_remote_mode_the_personal_data_guard_comes_before_the_rewriting(index_dir, fake_embedder):
    model = RewritingModel("données à caractère personnel")
    model.remote, model.provider = True, "Groq"
    with pytest.raises(PersonalDataError):
        answer_question("Puis-je garder jean.dupont@example.org ?", index_dir, fake_embedder, model, rewrite=True)
    assert model.calls == []  # nothing was sent, not even the rewriting

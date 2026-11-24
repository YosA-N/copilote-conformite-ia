"""Ask the copilot a question: the answer is written as it comes, then the sources and the times.

Local by default (Ollama). With --backend openai (or LLM_BACKEND=openai in .env), the question and the law
extracts are sent to the remote API (Groq, LLM_API_MODEL = qwen/qwen3.8-27b by default): a notice says so
before every answer, the model that wrote the answer is named under it, and a question that holds personal
data (e-mail, phone number, IBAN, social security number) is refused by the core (rag.answer_question) before
anything is sent; this script only shows the refusal. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\ask.py "Dois-je désigner un DPO ?" [--show-passages]
    .venv\\Scripts\\python scripts\\ask.py --backend openai "Dois-je désigner un DPO ?"
"""

import argparse
import dataclasses
import sys

from compliance_copilot.config import INDEX_DIR, LLM_BACKENDS, Settings, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.index import IndexNotReadyError
from compliance_copilot.llm import LLMError, make_chat_model, provider_name
from compliance_copilot.privacy import PersonalDataError
from compliance_copilot.rerank import RerankerError, make_reranker, resolve_search
from compliance_copilot.rag import answer_question, passage_label, render_footer


def write_now(text: str) -> None:
    print(text, end="", flush=True)


def remote_notice(settings: Settings) -> str:
    return (
        f"Mode distant : votre question et les extraits de loi sont envoyés à {provider_name(settings.llm_api_base_url)} "
        f"({settings.generation_model}). N'y mettez aucune donnée personnelle."
    )


def signature(settings: Settings) -> str:
    """Who wrote the answer, shown under every answer."""
    if settings.remote:
        return f"Réponse rédigée par {settings.generation_model}, modèle distant servi par {provider_name(settings.llm_api_base_url)}."
    return f"Réponse rédigée par {settings.generation_model}, modèle local (Ollama), sans sortie de votre ordinateur."


def apply_overrides(settings: Settings, backend: str | None, model: str | None) -> Settings:
    """--backend replaces LLM_BACKEND for this run; --model replaces the model of the chosen mode
    (LLM_API_MODEL in remote mode, LLM_MODEL in local mode)."""
    if backend:
        settings = dataclasses.replace(settings, llm_backend=backend)
    if model:
        settings = dataclasses.replace(settings, **{"llm_api_model" if settings.remote else "llm_model": model})
    return settings


def main() -> int:
    parser = argparse.ArgumentParser(description="Pose une question au copilote de conformité.")
    parser.add_argument("question", nargs="+", help="la question, de préférence entre guillemets")
    parser.add_argument("--show-passages", action="store_true", help="afficher les passages donnés au modèle")
    parser.add_argument("-k", type=int, help="nombre de passages donnés au modèle (par défaut : SEARCH_K du .env)")
    parser.add_argument("--backend", choices=LLM_BACKENDS, help="ollama (local, par défaut) ou openai (API distante), à la place de LLM_BACKEND")
    parser.add_argument("--model", help="modèle à utiliser, à la place de LLM_API_MODEL (mode distant) ou de LLM_MODEL (mode local)")
    args = parser.parse_args()
    question = " ".join(args.question)

    settings, notice = resolve_search(apply_overrides(load_settings(), args.backend, args.model))
    if notice:
        print(f"[INFO] {notice}\n")
    try:
        embedder = make_embedder(settings, settings.query_embedding_device)
        chat_model = make_chat_model(settings)
    except (EmbeddingError, LLMError) as error:
        print(f"[ERREUR] {error}")
        return 1
    if settings.remote:
        print(f"⚠️  {remote_notice(settings)}\n")
    print(f"Question : {question}\n")
    print("Réponse :" + (" (affichée après le contrôle de pertinence)" if settings.answer_judge else ""))
    try:
        answer = answer_question(
            question, INDEX_DIR, embedder, chat_model, k=args.k or settings.search_k, on_text=write_now,
            mode=settings.search_mode, lexicon=settings.search_lexicon, max_per_article=settings.search_max_per_article,
            first_paragraph=settings.search_first_paragraph,
            reranker=make_reranker(settings), rerank_candidates=settings.search_rerank_candidates, rewrite=settings.search_rewrite,
            judge=settings.answer_judge,
        )
    except PersonalDataError as refusal:  # raised by the core before the search and before anything is sent
        print(f"\n[REFUS] {refusal}")
        return 2
    except (IndexNotReadyError, EmbeddingError, LLMError, RerankerError) as error:
        print(f"\n[ERREUR] {error}")
        return 1

    if settings.answer_judge:  # nothing was streamed: the verdict of the judge comes after the answer
        print(answer.text)
    print("\n")
    if args.show_passages:
        print("Passages donnés au modèle :")
        for number, passage in enumerate(answer.passages, start=1):
            print(f"\n[{number}] (score {passage.score:.3f}) {passage_label(passage.metadata)}")
            print(passage.text.split("\n\n", 1)[-1])
        print()
    if answer.rewrite_terms:
        print(f"Reformulation de la question : {' ; '.join(answer.rewrite_terms)}\n")
    print(render_footer(answer))
    print(f"\n{signature(settings)}")
    generation = answer.generation
    print(
        f"\nTemps : recherche {answer.search_seconds:.1f} s · génération {answer.generation_seconds:.1f} s "
        f"({generation.completion_tokens} tokens, {generation.tokens_per_second:.1f} tokens/s) · "
        + (f"contrôle de pertinence {answer.judge_seconds:.1f} s · " if settings.answer_judge else "")
        + (f"reformulation {answer.rewrite_seconds:.1f} s · " if answer.rewrite_seconds else "")
        + f"total {answer.rewrite_seconds + answer.search_seconds + answer.generation_seconds + answer.judge_seconds:.1f} s"
        + (f" · attente des limites de l'API {answer.wait_seconds:.0f} s (non comptée)" if answer.wait_seconds else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

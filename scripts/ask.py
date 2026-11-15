"""Ask the copilot a question: the answer is written as it comes, then the sources and the times.

Local by default (Ollama). With --backend openai (or LLM_BACKEND=openai in .env), the question and the law
extracts are sent to the remote API (Groq, qwen/qwen3.8-27b): a notice says so before every answer, the
model that wrote the answer is named under it, and a question that holds personal data (e-mail, phone
number, IBAN, social security number) is never sent. Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\ask.py "Dois-je désigner un DPO ?" [--show-passages]
    .venv\\Scripts\\python scripts\\ask.py --backend openai --model qwen/qwen3.8-27b "Dois-je désigner un DPO ?"
"""

import argparse
import dataclasses
import sys
from urllib.parse import urlparse

from compliance_copilot.config import INDEX_DIR, LLM_BACKENDS, Settings, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.index import IndexNotReadyError
from compliance_copilot.llm import LLMError, make_chat_model
from compliance_copilot.privacy import personal_data_found, refusal_message
from compliance_copilot.rag import answer_question, passage_label, render_footer


def write_now(text: str) -> None:
    print(text, end="", flush=True)


def is_remote(settings: Settings) -> bool:
    return settings.llm_backend != "ollama"


def provider(settings: Settings) -> str:
    """'Groq' for api.groq.com, else the host name of the API."""
    host = urlparse(settings.llm_api_base_url).hostname or settings.llm_api_base_url
    return "Groq" if "groq" in host else host


def remote_notice(settings: Settings) -> str:
    return (
        f"Mode distant : votre question et les extraits de loi sont envoyés à {provider(settings)} ({settings.llm_model}). "
        "N'y mettez aucune donnée personnelle."
    )


def signature(settings: Settings) -> str:
    """Who wrote the answer, shown under every answer."""
    if is_remote(settings):
        return f"Réponse rédigée par {settings.llm_model}, modèle distant servi par {provider(settings)}."
    return f"Réponse rédigée par {settings.llm_model}, modèle local (Ollama), sans sortie de votre ordinateur."


def blocked_message(question: str, settings: Settings) -> str | None:
    """In remote mode, the refusal to send a question that holds personal data; None when it may be sent."""
    if not is_remote(settings):
        return None
    kinds = personal_data_found(question)
    return refusal_message(kinds, provider(settings)) if kinds else None


def apply_overrides(settings: Settings, backend: str | None, model: str | None) -> Settings:
    """--backend and --model replace LLM_BACKEND and LLM_MODEL of .env for this run only."""
    overrides = {}
    if backend:
        overrides["llm_backend"] = backend
    if model:
        overrides["llm_model"] = model
    return dataclasses.replace(settings, **overrides) if overrides else settings


def main() -> int:
    parser = argparse.ArgumentParser(description="Pose une question au copilote de conformité.")
    parser.add_argument("question", nargs="+", help="la question, de préférence entre guillemets")
    parser.add_argument("--show-passages", action="store_true", help="afficher les passages donnés au modèle")
    parser.add_argument("-k", type=int, help="nombre de passages donnés au modèle (par défaut : SEARCH_K du .env)")
    parser.add_argument("--backend", choices=LLM_BACKENDS, help="ollama (local, par défaut) ou openai (API distante), à la place de LLM_BACKEND")
    parser.add_argument("--model", help="modèle à utiliser, à la place de LLM_MODEL (par exemple qwen/qwen3.8-27b en mode distant)")
    args = parser.parse_args()
    question = " ".join(args.question)

    settings = apply_overrides(load_settings(), args.backend, args.model)
    blocked = blocked_message(question, settings)
    if blocked:  # checked before anything is built or sent
        print(f"[REFUS] {blocked}")
        return 2
    try:
        embedder = make_embedder(settings, settings.query_embedding_device)
        chat_model = make_chat_model(settings)
    except (EmbeddingError, LLMError) as error:
        print(f"[ERREUR] {error}")
        return 1
    if is_remote(settings):
        print(f"⚠️  {remote_notice(settings)}\n")
    print(f"Question : {question}\n")
    print("Réponse :" + (" (affichée après le contrôle de pertinence)" if settings.answer_judge else ""))
    try:
        answer = answer_question(
            question, INDEX_DIR, embedder, chat_model, k=args.k or settings.search_k, on_text=write_now,
            mode=settings.search_mode, lexicon=settings.search_lexicon, max_per_article=settings.search_max_per_article,
            first_paragraph=settings.search_first_paragraph,
            judge=settings.answer_judge,
        )
    except (IndexNotReadyError, EmbeddingError, LLMError) as error:
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
    print(render_footer(answer))
    print(f"\n{signature(settings)}")
    generation = answer.generation
    print(
        f"\nTemps : recherche {answer.search_seconds:.1f} s · génération {answer.generation_seconds:.1f} s "
        f"({generation.completion_tokens} tokens, {generation.tokens_per_second:.1f} tokens/s) · "
        + (f"contrôle de pertinence {answer.judge_seconds:.1f} s · " if settings.answer_judge else "")
        + f"total {answer.search_seconds + answer.generation_seconds + answer.judge_seconds:.1f} s"
        + (f" · attente des limites de l'API {answer.wait_seconds:.0f} s (non comptée)" if answer.wait_seconds else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

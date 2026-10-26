"""Ask the copilot a question: the answer is written as it comes, then the sources and the times.

Run scripts/build_index.py first.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\ask.py "Dois-je désigner un DPO ?" [--show-passages]
"""

import argparse
import sys

from compliance_copilot.config import INDEX_DIR, load_settings
from compliance_copilot.embeddings import EmbeddingError, make_embedder
from compliance_copilot.index import IndexNotReadyError
from compliance_copilot.llm import LLMError, make_chat_model
from compliance_copilot.rag import answer_question, passage_label, render_footer


def write_now(text: str) -> None:
    print(text, end="", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Pose une question au copilote de conformité.")
    parser.add_argument("question", nargs="+", help="la question, de préférence entre guillemets")
    parser.add_argument("--show-passages", action="store_true", help="afficher les passages donnés au modèle")
    parser.add_argument("-k", type=int, help="nombre de passages donnés au modèle (par défaut : SEARCH_K du .env)")
    args = parser.parse_args()
    question = " ".join(args.question)

    settings = load_settings()
    embedder = make_embedder(settings, settings.query_embedding_device)
    chat_model = make_chat_model(settings)
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
    generation = answer.generation
    print(
        f"\nTemps : recherche {answer.search_seconds:.1f} s · génération {answer.generation_seconds:.1f} s "
        f"({generation.completion_tokens} tokens, {generation.tokens_per_second:.1f} tokens/s) · "
        + (f"contrôle de pertinence {answer.judge_seconds:.1f} s · " if settings.answer_judge else "")
        + f"total {answer.search_seconds + answer.generation_seconds + answer.judge_seconds:.1f} s"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

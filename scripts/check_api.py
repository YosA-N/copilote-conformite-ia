"""One trial call to the OpenAI-compatible API of the session 7 experiment, before the test questions:
which models the key may use, one short fixed chat call through the copilot's own backend, and the real
rate limits of the account (x-ratelimit-* headers of the answer).

Nothing personal is sent: only a fixed question about the number of a regulation. The key is never printed.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\check_api.py --model qwen/qwen3.8-27b --reasoning-effort none
    .venv\\Scripts\\python scripts\\check_api.py --model openai/gpt-oss-120b --reasoning-effort low
"""

import argparse
import sys
import time

from compliance_copilot.config import load_settings
from compliance_copilot.llm import LLMError, OpenAICompatibleChatModel

TRIAL_MESSAGES = [
    {"role": "system", "content": "Vous répondez en français, en une phrase courte."},
    {"role": "user", "content": "Quel est le nom usuel du règlement (UE) 2016/679 ?"},
]
RETIRED_MODEL = "llama-3.3-70b-versatile"  # first planned for the experiment, retired by Groq on 16/08/2026
# What the x-ratelimit-* headers mean (Groq documentation): the request headers count the day, the token headers the minute.
HEADER_MEANINGS = [
    ("x-ratelimit-limit-requests", "requêtes par jour (RPD), limite"),
    ("x-ratelimit-remaining-requests", "requêtes par jour, restantes"),
    ("x-ratelimit-reset-requests", "requêtes par jour, remise à zéro dans"),
    ("x-ratelimit-limit-tokens", "tokens par minute (TPM), limite"),
    ("x-ratelimit-remaining-tokens", "tokens par minute, restants"),
    ("x-ratelimit-reset-tokens", "tokens par minute, remise à zéro dans"),
]
SERVER_TIMINGS = ("queue_time", "prompt_time", "completion_time", "total_time")


def describe_limits(rate_limits: dict[str, str]) -> list[str]:
    """One line per rate-limit header, with its meaning; unknown x-ratelimit-* headers are shown as they are."""
    lines = [f"  {meaning} : {rate_limits[name]}" for name, meaning in HEADER_MEANINGS if name in rate_limits]
    known = {name for name, _ in HEADER_MEANINGS}
    lines += [f"  {name} : {value}" for name, value in sorted(rate_limits.items()) if name not in known]
    if not lines:
        lines.append("  aucun en-tête x-ratelimit-* dans la réponse")
    lines.append("  (les tokens par jour, TPD, ne figurent pas dans les en-têtes : voir la page des limites de l'API)")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Un appel d'essai à l'API compatible OpenAI : modèles ouverts, limites du compte.")
    parser.add_argument("--model", help="modèle distant à essayer (par défaut : LLM_MODEL)")
    parser.add_argument("--reasoning-effort",
                        help="valeur de reasoning_effort à envoyer, par exemple none ou low (par défaut : LLM_API_REASONING_EFFORT)")
    args = parser.parse_args()
    settings = load_settings()
    model = args.model or settings.llm_model
    effort = settings.llm_api_reasoning_effort if args.reasoning_effort is None else args.reasoning_effort.strip().lower()
    chat_model = OpenAICompatibleChatModel(
        settings.llm_api_base_url, model, settings.llm_api_key_env, num_ctx=settings.llm_num_ctx,
        temperature=settings.llm_temperature, max_tokens=settings.llm_max_tokens, reasoning_effort=effort,
    )
    print(f"API : {settings.llm_api_base_url} · clé lue dans la variable {settings.llm_api_key_env} (jamais affichée)")

    try:
        models = chat_model.list_models()
    except LLMError as error:
        print(f"[ERREUR] {error}")
        return 1
    print(f"[OK] {len(models)} modèle(s) ouvert(s) à cette clé : {', '.join(models)}")
    listed = model in models
    print(f"[{'OK' if listed else 'ATTENTION'}] {model} {'est' if listed else 'n’est pas'} dans la liste")
    print(f"     {RETIRED_MODEL} : {'encore présent' if RETIRED_MODEL in models else 'absent (retiré par Groq le 16/08/2026)'}")

    print(
        f"\nAppel d'essai : {model}, reasoning_effort = {effort or 'non envoyé'}, température {settings.llm_temperature}, "
        f"{settings.llm_max_tokens} tokens au plus · question fixe : « {TRIAL_MESSAGES[1]['content']} »"
    )
    start = time.perf_counter()
    try:
        generation = chat_model.generate(TRIAL_MESSAGES)
    except LLMError as error:
        print(f"[ERREUR] {error}")
        return 1
    wall = time.perf_counter() - start - chat_model.waited_seconds
    print(f"[OK] Réponse : {' '.join(generation.text.split())}")
    print(
        f"     {generation.prompt_tokens} tokens lus, {generation.completion_tokens} écrits"
        + (f" (dont un raisonnement d'environ {len(generation.reasoning.split())} mots)" if generation.reasoning else "")
        + f", {generation.tokens_per_second:.0f} tokens/s, réponse {'coupée' if generation.truncated else 'complète'}"
    )
    usage = chat_model.last_usage
    timings = ", ".join(f"{name} {usage[name]:.2f} s" for name in SERVER_TIMINGS if isinstance(usage.get(name), (int, float)))
    print(
        f"     Temps mesuré ici {wall:.1f} s"
        + (f" · temps du serveur : {timings}" if timings else "")
        + (f" · attente des limites {chat_model.waited_seconds:.0f} s" if chat_model.waited_seconds else "")
    )
    print(f"\nLimites réelles du compte pour {model} (en-têtes x-ratelimit-* de la réponse) :")
    print("\n".join(describe_limits(chat_model.rate_limits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

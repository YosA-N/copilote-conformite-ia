"""Offline tests for scripts/scan_secrets.py. The fake keys are built at run time, so that this file
does not look like a secret to the scanner itself."""

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_secrets.py"
spec = importlib.util.spec_from_file_location("scan_secrets", SCRIPT)
scan_secrets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan_secrets)

GROQ_LIKE = "gsk_" + "A1b2" * 10
OPENAI_LIKE = "sk-" + "Z9y8" * 8


def test_key_shapes_are_found():
    assert scan_secrets.find_secrets(f"key: {GROQ_LIKE}", []) == ["clé Groq (gsk_…)"]
    assert "clé OpenAI (sk-…)" in scan_secrets.find_secrets(f"OPENAI={OPENAI_LIKE}", [])
    assert "affectation d'une clé" in scan_secrets.find_secrets('api_key = "' + "q" * 24 + '"', [])


def test_values_of_secret_variables_of_env_are_found_without_being_returned(tmp_path):
    secret = "my-own-" + "s3cr3t" * 4
    env = tmp_path / ".env"
    env.write_text(f"LLM_MODEL=qwen3:4b-instruct\nGROQ_API_KEY={secret}\nLLM_API_KEY_ENV=GROQ_API_KEY\n", encoding="utf-8")

    values = scan_secrets.secret_values(env)
    found = scan_secrets.find_secrets(f"oops {secret} committed", values)

    assert values == [secret]  # LLM_API_KEY_ENV holds a variable name, not a secret; LLM_MODEL is not secret
    assert found == ["valeur d'une variable secrète de .env"] and all(secret not in kind for kind in found)


def test_ordinary_code_is_not_taken_for_a_secret():
    code = (
        "tokens_per_second=completion_tokens / writing_seconds\n"
        "llm_api_key_env=os.getenv('LLM_API_KEY_ENV', DEFAULT_API_KEY_ENV)\n"
        "LLM_API_KEY_ENV=GROQ_API_KEY\n"
    )

    assert scan_secrets.find_secrets(code, []) == []

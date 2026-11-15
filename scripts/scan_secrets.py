"""Check that no secret is about to be committed: run it before every commit.

1. .env must be ignored by Git and never tracked.
2. The staged changes must contain no key-shaped text (gsk_…, sk-…, api_key = …) and none of the
   values of the *_KEY, *_TOKEN and *SECRET* variables of .env.

Nothing secret is ever printed: only the file name and the kind of match.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\scan_secrets.py
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY_SHAPES = {
    "clé Groq (gsk_…)": re.compile(r"gsk_[A-Za-z0-9]{20,}"),
    "clé OpenAI (sk-…)": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "affectation d'une clé": re.compile(r"(?i)\b(?:api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
}
SECRET_NAME = re.compile(r"(?:_KEY|_TOKEN|SECRET)", re.IGNORECASE)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")


def secret_values(env_path: Path) -> list[str]:
    """The values of the secret-looking variables of .env (never printed)."""
    if not env_path.exists():
        return []
    values = []
    for line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
        name, _, value = line.partition("=")
        value = value.strip().strip("'\"")
        names_a_variable = name.strip().endswith("_ENV") or re.fullmatch(r"[A-Z0-9_]+", value)  # LLM_API_KEY_ENV=GROQ_API_KEY
        if SECRET_NAME.search(name) and len(value) >= 8 and not names_a_variable:
            values.append(value)
    return values


def find_secrets(text: str, values: list[str]) -> list[str]:
    """The kinds of secret found in the text (never the secret itself)."""
    found = [kind for kind, pattern in KEY_SHAPES.items() if pattern.search(text)]
    if any(value in text for value in values):
        found.append("valeur d'une variable secrète de .env")
    return found


def main() -> int:
    problems = []
    if git("check-ignore", "-q", ".env").returncode != 0:
        problems.append(".env n'est pas ignoré par Git (ajoutez « .env » à .gitignore)")
    if git("ls-files", "--error-unmatch", ".env").returncode == 0:
        problems.append(".env est suivi par Git : retirez-le avec « git rm --cached .env »")

    values = secret_values(ROOT / ".env")
    staged = [name for name in git("diff", "--cached", "--name-only", "--diff-filter=ACMR").stdout.splitlines() if name]
    for name in staged:
        content = git("show", f":{name}").stdout  # the staged version of the file
        for kind in find_secrets(content, values):
            problems.append(f"{name} : {kind}")

    if problems:
        for problem in problems:
            print(f"[SECRET] {problem}")
        print("Commit bloqué : retirez le secret avant de commiter.")
        return 1
    print(f"[OK] Aucun secret dans les {len(staged)} fichier(s) prêts à être commités ; .env est ignoré et non suivi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

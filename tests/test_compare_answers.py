"""Offline tests for scripts/compare_answers.py: reading the answers files, and the comparison tables."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "compare_answers.py"
spec = importlib.util.spec_from_file_location("compare_answers", SCRIPT)
compare_answers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compare_answers)

Q01_ROW = "| q01 | Dois-je désigner un DPO ? | 2/2 | non | — | 55 s |"
Q02_ROW = ("| q02 | Dois-je tenir un registre ? | 1/3 | abstention | Contrôle de pertinence : les extraits retenus ne répondent pas "
           "directement à la question. | 37 s |")
Q01_TIMES = "Temps : recherche 2.4 s · génération 47.1 s (2880 tokens lus, 521 écrits, 35.6 tokens/s) · contrôle de pertinence 5.3 s"
LOCAL = f"""# Réponses du copilote — v4

| # | Question | Extraits vérifiés | Refus | Alertes du code | Temps total |
|---|---|---|---|---|---|
{Q01_ROW}
{Q02_ROW}
| h01 | Quel est le taux de TVA en France ? | 0/0 | oui | — | 14 s |

## q01 — Dois-je désigner un DPO ?

Article attendu : RGPD art. 37 — passage [1].

### Réponse du copilote

> Oui : vous devez désigner un délégué [1].
> Dans certains cas.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  [1] RGPD, article 37

Information, pas un conseil juridique.
```

<details><summary>Texte brut écrit par le modèle (extraits compris)</summary>

```text
Attention : ceci est écrit par le modèle, pas une alerte du code.
```

</details>

{Q01_TIMES}

## q02 — Dois-je tenir un registre ?

Article attendu : RGPD art. 30 — passage [1].

### Réponse du copilote

> Les passages trouvés ne traitent pas directement de votre question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune
Attention : 2 extrait(s) introuvable(s) mot pour mot dans le passage cité ([1], [2]) : ignoré(s).
Attention : Contrôle de pertinence : les extraits retenus ne répondent pas directement à la question.

Information, pas un conseil juridique.
```

Temps : recherche 5.0 s · génération 27.7 s (2915 tokens lus, 366 écrits, 35.6 tokens/s) · contrôle de pertinence 3.9 s

## h01 — Quel est le taux de TVA en France ?

Question hors sujet : aucun article attendu, le copilote devrait refuser.

### Réponse du copilote

> Les textes trouvés ne permettent pas de répondre à cette question.

### Extraits, sources, contrôles et avertissement (ajoutés par le code)

```text
Sources citées :
  aucune

Information, pas un conseil juridique.
```

Temps : recherche 1.0 s · génération 10.0 s (2000 tokens lus, 20 écrits, 30.0 tokens/s)
"""
CUT = ("Attention : Réponse coupée : le modèle a atteint la limite de 2000 tokens (LLM_MAX_TOKENS), la fin de la réponse manque. "
       "Son raisonnement (environ 300 mots, non affiché) a consommé une partie de cette limite.")
REMOTE = (
    LOCAL.replace("— v4", "— big")
    .replace(Q01_ROW, "| q01 | Dois-je désigner un DPO ? | 3/3 | non | Réponse coupée : … | 70 s |")
    .replace(Q01_TIMES, "Temps : recherche 2.4 s · génération 8.0 s (2900 tokens lus, 2000 écrits, raisonnement ≈ 300 mots, "
                        "400.0 tokens/s) · contrôle de pertinence 1.0 s · attente des limites de l'API 45 s (non comptée)")
    .replace("  [1] RGPD, article 37\n", f"  [1] RGPD, article 37\n{CUT}\n")
)


def test_records_are_read_from_the_summary_table_the_footer_and_the_times_line():
    records = {record.id: record for record in compare_answers.parse_answers(LOCAL)}

    q01, q02, h01 = records["q01"], records["q02"], records["h01"]
    assert (q01.verified, q01.extracts, q01.refusal, q01.total_seconds, q01.off_topic) == (2, 2, "non", 55.0, False)
    assert q01.words == 11 and q01.alerts == [] and q01.answered  # the « Attention » written by the model is not an alert
    assert (q01.search_seconds, q01.generation_seconds, q01.judge_seconds, q01.wait_seconds) == (2.4, 47.1, 5.3, 0.0)
    assert (q01.prompt_tokens, q01.completion_tokens, q01.reasoning_words) == (2880, 521, 0)
    assert q02.refusal == "abstention" and len(q02.alerts) == 2 and not q02.answered and not q02.truncated
    assert h01.off_topic and h01.refusal == "oui" and h01.judge_seconds == 0.0 and not h01.answered


def test_reasoning_waits_and_truncation_are_read():
    q01 = compare_answers.parse_answers(REMOTE)[0]

    assert (q01.reasoning_words, q01.wait_seconds, q01.completion_tokens, q01.generation_seconds) == (300, 45.0, 2000, 8.0)
    assert q01.truncated and q01.cut_by_reasoning and q01.alerts == [CUT[len("Attention : "):]]


def test_a_section_without_its_table_row_is_refused():
    with pytest.raises(ValueError, match="q02 : format non reconnu"):
        compare_answers.parse_answers(LOCAL.replace(Q02_ROW + "\n", ""))


def test_a_series_refuses_the_same_question_twice(tmp_path):
    path = tmp_path / "a.md"
    path.write_text(LOCAL, encoding="utf-8")

    with pytest.raises(ValueError, match="en double q01, q02, h01"):
        compare_answers.load_series(f"v4={path},{path}")


def test_tables_compare_the_series_without_judging_them(tmp_path, capsys):
    (tmp_path / "local.md").write_text(LOCAL, encoding="utf-8")
    (tmp_path / "remote.md").write_text(REMOTE, encoding="utf-8")
    series = [compare_answers.load_series(f"v4={tmp_path / 'local.md'}"), compare_answers.load_series(f"big={tmp_path / 'remote.md'}")]

    summary = compare_answers.summary_table(series)
    assert summary[2] == ("| v4 | 3 (2 + 1 hors sujet) | 1 / 2 | 1 | 1 / 1 | 3 / 5 | 0 (0) | 1 / 3 | 2 | 11 | 28 s · 47 s | "
                          "37 s · 55 s | 0 | 0 s sur 0 question(s) |")
    assert summary[3] == ("| big | 3 (2 + 1 hors sujet) | 1 / 2 | 1 | 1 / 1 | 4 / 6 | 1 (1) | 2 / 3 | 3 | 11 | 10 s · 28 s | "
                          "37 s · 70 s | 1 | 45 s sur 1 question(s) |")

    alerts = compare_answers.alerts_table(series)
    assert alerts[0] == "| Alerte (nombre de réponses) | v4 | big |"
    assert any(line.startswith("| Réponse coupée : le modèle a atteint la limite …") and line.endswith("| 0 | 1 |") for line in alerts)

    questions = compare_answers.question_table(series)
    assert questions[0] == "Valeurs dans l'ordre : v4 · big."
    assert "| q01 | 2/2 · 3/3 | non · non | 0 · 1 | 11 · 11 | 47 · 8 | 55 · 70 |" in questions
    assert "| q02 | 1/3 · 1/3 | abstention · abstention | 2 · 2 | — · — | 28 · 28 | 37 · 37 |" in questions

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr("sys.argv", ["compare_answers.py", f"v4={tmp_path / 'local.md'}", f"big={tmp_path / 'remote.md'}"])
        assert compare_answers.main() == 0
    out = capsys.readouterr().out
    assert summary[2] in out and "Alertes du code par type" in out and questions[-1] in out

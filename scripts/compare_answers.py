"""Compare series of answers (eval/answers_<version>.md files written by answer_questions.py), without judging them:
verified extracts, abstentions and refusals, code alerts, length, generation and total times, API waits.
The verdicts (right, partial, wrong, dangerous) only come from the human reviews (eval/reviews/).

A series is "label=file[,file…]": its questions are those of all its files, for example v0 + v1 = 32 questions.
The Markdown tables are printed, ready to be pasted in eval/results_*.md.

Usage, from the repository root:
    .venv\\Scripts\\python scripts\\compare_answers.py v4=eval\\answers_v4.md,eval\\answers_heldout_v4.md qwen27b=eval\\answers_v4_big_qwen27b.md,eval\\answers_heldout_v4_big_qwen27b.md
"""

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from statistics import median

from compliance_copilot.evaluation import alert_kind

SUMMARY_ROW = re.compile(
    r"^\| (?P<id>\w+) \| (?P<question>.*) \| (?P<verified>\d+)/(?P<extracts>\d+) \| (?P<refusal>oui|non|abstention) \| "
    r"(?P<alerts>.*) \| (?P<total>\d+) s \|$"
)
SECTION_TITLE = re.compile(r"^## (?P<id>\w+) — (?P<question>.*)$", re.MULTILINE)
TIMES = re.compile(
    r"^Temps : recherche (?P<search>[\d.]+) s · génération (?P<generation>[\d.]+) s "
    r"\((?P<prompt_tokens>\d+) tokens lus, (?P<completion_tokens>\d+) écrits(?:, raisonnement ≈ (?P<reasoning_words>\d+) mots)?, "
    r"(?P<tokens_per_second>[\d.]+) tokens/s\)"
    r"(?: · contrôle de pertinence (?P<judge>[\d.]+) s)?"
    r"(?: · reformulation (?P<rewrite>[\d.]+) s)?"
    r"(?: · attente des limites de l'API (?P<wait>\d+) s \(non comptée\))?$",
    re.MULTILINE,
)
ANSWER_HEADING = "### Réponse du copilote"
FOOTER_HEADING = "### Extraits, sources, contrôles et avertissement"
OFF_TOPIC = "Question hors sujet"
TRUNCATED = "Réponse coupée"
LONG_ANSWER_SECONDS = 60


@dataclass
class Record:
    id: str
    question: str
    off_topic: bool
    verified: int
    extracts: int
    refusal: str  # oui, non or abstention, as in the summary table
    alerts: list[str]
    words: int
    search_seconds: float
    generation_seconds: float
    judge_seconds: float
    wait_seconds: float
    prompt_tokens: int
    completion_tokens: int
    reasoning_words: int
    total_seconds: float  # search + generation + judge, as in the summary table (waits excluded)

    @property
    def answered(self) -> bool:
        return not self.off_topic and self.refusal == "non"

    @property
    def truncated(self) -> bool:
        return any(TRUNCATED in alert for alert in self.alerts)

    @property
    def cut_by_reasoning(self) -> bool:
        return any(TRUNCATED in alert and "raisonnement" in alert for alert in self.alerts)


@dataclass
class Series:
    label: str
    records: list[Record]

    def by_id(self) -> dict[str, Record]:
        return {record.id: record for record in self.records}


def _answer_words(body: str) -> int:
    """Words of the answer shown to the user: the quoted lines after the answer heading."""
    if ANSWER_HEADING not in body:
        return 0
    quoted = []
    for line in body.split(ANSWER_HEADING, 1)[1].splitlines():
        if line.startswith("###"):
            break
        if line.startswith(">"):
            quoted.append(line[1:].strip())
    return len(" ".join(quoted).split())


def _alerts(body: str) -> list[str]:
    """The 'Attention : …' lines of the footer written by the code (not the raw text of the model)."""
    if FOOTER_HEADING not in body:
        return []
    footer = body.split(FOOTER_HEADING, 1)[1].split("<details>", 1)[0]
    return [line[len("Attention : "):].strip() for line in footer.splitlines() if line.startswith("Attention : ")]


def parse_answers(text: str, name: str = "answers") -> list[Record]:
    """The records of one eval/answers_<version>.md file, in the order of its sections."""
    rows = {match["id"]: match for match in map(SUMMARY_ROW.match, text.splitlines()) if match}
    titles = list(SECTION_TITLE.finditer(text))
    records = []
    for index, title in enumerate(titles):
        end = titles[index + 1].start() if index + 1 < len(titles) else len(text)
        body = text[title.end():end]
        row, times = rows.get(title["id"]), TIMES.search(body)
        if row is None or times is None:
            raise ValueError(f"{name}, {title['id']} : format non reconnu (ligne du tableau ou ligne « Temps » absente)")
        records.append(Record(
            id=title["id"], question=title["question"].strip(), off_topic=OFF_TOPIC in body,
            verified=int(row["verified"]), extracts=int(row["extracts"]), refusal=row["refusal"], alerts=_alerts(body),
            words=_answer_words(body), search_seconds=float(times["search"]), generation_seconds=float(times["generation"]),
            judge_seconds=float(times["judge"] or 0), wait_seconds=float(times["wait"] or 0),
            prompt_tokens=int(times["prompt_tokens"]), completion_tokens=int(times["completion_tokens"]),
            reasoning_words=int(times["reasoning_words"] or 0), total_seconds=float(row["total"]),
        ))
    return records


def load_series(argument: str) -> Series:
    """'label=file1,file2' → the series of all the records of these files (an id may appear only once)."""
    label, _, files = argument.partition("=")
    if not files:
        raise ValueError(f"série « {argument} » : attendu label=fichier[,fichier…]")
    records = [record for file in files.split(",") for record in parse_answers(Path(file).read_text(encoding="utf-8"), file)]
    duplicates = [item for item, count in Counter(record.id for record in records).items() if count > 1]
    if duplicates:
        raise ValueError(f"série « {label} » : question(s) en double {', '.join(duplicates)}")
    return Series(label.strip(), records)


def _median_max(values: list[float]) -> str:
    return f"{median(values):.0f} s · {max(values):.0f} s" if values else "—"


def summary_table(series: list[Series]) -> list[str]:
    lines = [
        "| Série | Questions | Réponses données | Abstentions | Hors sujet refusés | Extraits vérifiés / recopiés | "
        "Réponses coupées (par le raisonnement) | Réponses avec alerte | Alertes | Mots par réponse (médiane) | "
        "Génération : médiane · max | Total : médian · max | Au-delà de 60 s | Attente API (non comptée) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for one in series:
        records = one.records
        in_corpus = [r for r in records if not r.off_topic]
        off_topic = [r for r in records if r.off_topic]
        answered = [r for r in records if r.answered]
        words = f"{median([r.words for r in answered]):.0f}" if answered else "—"
        lines.append(
            f"| {one.label} | {len(records)} ({len(in_corpus)} + {len(off_topic)} hors sujet) | {len(answered)} / {len(in_corpus)} | "
            f"{sum(r.refusal == 'abstention' for r in in_corpus)} | {sum(r.refusal != 'non' for r in off_topic)} / {len(off_topic)} | "
            f"{sum(r.verified for r in records)} / {sum(r.extracts for r in records)} | "
            f"{sum(r.truncated for r in records)} ({sum(r.cut_by_reasoning for r in records)}) | "
            f"{sum(bool(r.alerts) for r in records)} / {len(records)} | {sum(len(r.alerts) for r in records)} | "
            f"{words} | {_median_max([r.generation_seconds for r in records])} | "
            f"{_median_max([r.total_seconds for r in records])} | {sum(r.total_seconds > LONG_ANSWER_SECONDS for r in records)} | "
            f"{sum(r.wait_seconds for r in records):.0f} s sur {sum(r.wait_seconds > 0 for r in records)} question(s) |"
        )
    return lines


def alerts_table(series: list[Series]) -> list[str]:
    counts = [Counter(kind for r in one.records for kind in set(map(alert_kind, r.alerts))) for one in series]
    kinds = sorted({kind for count in counts for kind in count}, key=lambda kind: (-sum(count[kind] for count in counts), kind))
    lines = ["| Alerte (nombre de réponses) | " + " | ".join(one.label for one in series) + " |", "|---|" + "---|" * len(series)]
    for kind in kinds:
        lines.append(f"| {kind} | " + " | ".join(str(count[kind]) for count in counts) + " |")
    return lines


def _cell(values) -> str:
    return " · ".join(values)


def question_table(series: list[Series]) -> list[str]:
    """One row per question found in every series; each cell gives the values in the order of the series."""
    maps = [one.by_id() for one in series]
    ids = [r.id for r in series[0].records if all(r.id in m for m in maps)]
    lines = [
        f"Valeurs dans l'ordre : {' · '.join(one.label for one in series)}.",
        "",
        "| # | Extraits vérifiés | Refus | Alertes | Mots | Génération (s) | Total (s) |",
        "|---|---|---|---|---|---|---|",
    ]
    for id_ in ids:
        records = [m[id_] for m in maps]
        lines.append(
            f"| {id_} | {_cell(f'{r.verified}/{r.extracts}' for r in records)} | {_cell(r.refusal for r in records)} | "
            f"{_cell(str(len(r.alerts)) for r in records)} | {_cell(str(r.words) if r.answered else '—' for r in records)} | "
            f"{_cell(f'{r.generation_seconds:.0f}' for r in records)} | {_cell(f'{r.total_seconds:.0f}' for r in records)} |"
        )
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare des séries de réponses (eval/answers_*.md) sans les juger.")
    parser.add_argument("series", nargs="+", help="label=fichier[,fichier…], par exemple v4=eval/answers_v4.md,eval/answers_heldout_v4.md")
    args = parser.parse_args()
    try:
        series = [load_series(argument) for argument in args.series]
    except (OSError, ValueError) as error:
        print(f"[ERREUR] {error}")
        return 1
    print("\n".join(summary_table(series)))
    print("\nAlertes du code par type :\n")
    print("\n".join(alerts_table(series)))
    print("\nPar question :\n")
    print("\n".join(question_table(series)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

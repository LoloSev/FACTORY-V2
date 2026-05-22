#!/usr/bin/env python3
"""
Audit TOKEN ECONOMY / machine-first.

But:
- repérer prose longue dans markdown
- repérer duplications de concepts runtime hors lexique
- repérer XLSX/CSV potentiellement non runtime-table
- produire un rapport court dans _FACTORY/_STATE

Ce script ne modifie aucun fichier.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
FACTORY = ROOT / "_FACTORY"
STATE = FACTORY / "_STATE"
LEXICON = FACTORY / "_STANDARDS" / "_GLOBAL" / "FACTORY_RUNTIME_LEXICON.md"

FLOATING_WORDS = [
    "culture", "territoire", "vivant", "émotion", "emotion",
    "poétique", "poetique", "authentique", "surprise culturelle",
    "anti-school", "anti scolaire", "anti-scolaire"
]

RUNTIME_CONCEPTS = [
    "PAYOFF_TYPE", "RUNTIME_SIGNAL", "MECHANIC", "FLAG_TYPE",
    "DECISION_RUNTIME", "STATUT_B2", "RICHESSE"
]

IGNORE_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
REPORT_MAX = 80


def is_ignored(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def iter_text_files():
    for path in FACTORY.rglob("*"):
        if is_ignored(path) or not path.is_file():
            continue
        if path.suffix.lower() in {".md", ".txt", ".json", ".py"}:
            yield path


def count_long_lines(text: str) -> int:
    total = 0
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("|") or stripped.startswith("#"):
            continue
        if len(stripped) > 180:
            total += 1
    return total


def main() -> int:
    findings = []
    lex_text = LEXICON.read_text(encoding="utf-8") if LEXICON.exists() else ""

    for path in iter_text_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        long_lines = count_long_lines(text)
        if long_lines:
            findings.append({
                "type": "LONG_PROSE",
                "file": rel,
                "count": long_lines,
            })

        lower = text.lower()
        hits = [w for w in FLOATING_WORDS if w.lower() in lower]
        if hits:
            findings.append({
                "type": "FLOATING_WORDS",
                "file": rel,
                "hits": sorted(set(hits)),
            })

        if path != LEXICON:
            duplicated = [c for c in RUNTIME_CONCEPTS if c in text and c in lex_text]
            if duplicated:
                findings.append({
                    "type": "LEXICON_DUPLICATION_RISK",
                    "file": rel,
                    "concepts": duplicated,
                })

    xlsx_files = [p.relative_to(ROOT).as_posix() for p in FACTORY.rglob("*.xlsx") if not is_ignored(p)]
    result = {
        "audit": "TOKEN_ECONOMY",
        "status": "WARN" if findings else "PASS",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "lexicon_present": LEXICON.exists(),
        "xlsx_count": len(xlsx_files),
        "xlsx_files": xlsx_files[:REPORT_MAX],
        "findings_count": len(findings),
        "findings": findings[:REPORT_MAX],
    }

    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / "TOKEN_ECONOMY_AUDIT.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md_lines = [
        "# TOKEN ECONOMY AUDIT",
        "",
        f"STATUS: {result['status']}",
        f"LEXICON_PRESENT: {result['lexicon_present']}",
        f"XLSX_COUNT: {result['xlsx_count']}",
        f"FINDINGS_COUNT: {result['findings_count']}",
        "",
        "## FINDINGS",
        "",
    ]
    if findings:
        for item in findings[:REPORT_MAX]:
            md_lines.append(f"- {item}")
    else:
        md_lines.append("- aucun warning détecté")

    (STATE / "TOKEN_ECONOMY_AUDIT.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

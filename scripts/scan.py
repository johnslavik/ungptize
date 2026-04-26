#!/usr/bin/env python3
"""Scan English prose for AI-writing tells catalogued in Wikipedia's
"Signs of AI writing" article. Emits a JSON report.

Non-interactive: reads from --file PATH or stdin, writes JSON to stdout.

English-only. The lexicon and most regexes are English-specific; for
non-English prose, skip this script and apply the rule categories from
SKILL.md using your knowledge of the input language.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from typing import Any


# The 24+ words Wikipedia identifies as overused in AI English prose.
# Stored lowercase; matched as whole words, case-insensitive.
AI_VOCAB = [
    "additionally",
    "align",  # match "align with"
    "boasts",
    "bolstered",
    "concrete",
    "crucial",
    "delve",
    "emphasizing",
    "enduring",
    "enhance",
    "fostering",
    "garner",
    "highlight",
    "interplay",
    "intricate",
    "intricacies",
    "key",
    "landscape",
    "meticulous",
    "meticulously",
    "pivotal",
    "robust",
    "showcase",
    "showcasing",
    "tapestry",
    "testament",
    "underscore",
    "valuable",
    "vibrant",
]

# Phrases that substitute for "is/are/has" — naive, line-level flags.
COPULATIVE_AVOIDANCE = [
    r"\bserves as\b",
    r"\bstands as\b",
    r"\brepresents\b",
    r"\bboasts\b",
    r"\bfeatures\b",
    r"\bmaintains\b",
    r"\boffers\b",
    r"\bmarks\b",
]

# Decorative negative-parallelism shapes.
NEG_PARALLELISM = [
    r"\bnot only\b[^.]*\bbut\b",
    r"\bnot just\b[^.]*\b(it'?s|its|but)\b",
    r"\bno\s+\w+,\s*no\s+\w+,\s*just\b",
]

EM_DASH_PATTERN = re.compile(r"[—–]")  # em + en dash
CURLY_QUOTE_PATTERN = re.compile(r"[‘’“”]")
WORD_PATTERN = re.compile(r"\b[A-Za-z'-]+\b")


def scan(text: str) -> dict[str, Any]:
    lower = text.lower()

    # Vocabulary hits.
    word_counts: Counter[str] = Counter()
    for match in WORD_PATTERN.finditer(lower):
        word = match.group(0)
        if word in AI_VOCAB:
            word_counts[word] += 1

    # Per-line line-numbered findings, useful for the change log.
    findings: list[dict[str, Any]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        line_lower = line.lower()
        for pattern in COPULATIVE_AVOIDANCE:
            for m in re.finditer(pattern, line_lower):
                findings.append({
                    "category": "copulative-avoidance",
                    "line": lineno,
                    "match": line[m.start():m.end()],
                })
        for pattern in NEG_PARALLELISM:
            for m in re.finditer(pattern, line_lower):
                findings.append({
                    "category": "negative-parallelism",
                    "line": lineno,
                    "match": line[m.start():m.end()],
                })

    em_dashes = len(EM_DASH_PATTERN.findall(text))
    curly_quotes = len(CURLY_QUOTE_PATTERN.findall(text))

    # Cluster heuristic: how many distinct vocab words appeared at least once.
    distinct_vocab = len(word_counts)
    total_vocab_hits = sum(word_counts.values())

    return {
        "vocabulary": {
            "hits": dict(word_counts),
            "distinct_words": distinct_vocab,
            "total_hits": total_vocab_hits,
        },
        "structural_findings": findings,
        "punctuation": {
            "em_dashes": em_dashes,
            "curly_quotes": curly_quotes,
        },
        "cluster_signal": {
            "distinct_vocab_words": distinct_vocab,
            "structural_finding_count": len(findings),
            "note": (
                "Multiple categories with hits = stronger AI-writing signal. "
                "Single isolated hits are usually not tells."
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Scan English prose for AI-writing tells. Emits JSON. "
            "Reads from --file PATH or stdin."
        )
    )
    parser.add_argument(
        "--file",
        help="Path to a text file. If omitted, reads from stdin.",
    )
    parser.add_argument(
        "--language",
        default="en",
        help="Language of the input (default: en). Only 'en' is supported.",
    )
    args = parser.parse_args()

    if args.language.lower() not in ("en", "english"):
        print(
            f"Error: lexical scan only supported for English, got "
            f"--language={args.language!r}. For non-English input, skip "
            f"this script and apply the rule categories from SKILL.md "
            f"directly.",
            file=sys.stderr,
        )
        return 2

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    if not text.strip():
        print("Error: no input prose provided.", file=sys.stderr)
        return 1

    report = scan(text)
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

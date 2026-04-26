#!/usr/bin/env python3
"""Mechanical fact sheet for English prose suspected of being AI-shaped.

What the script does well (and only this):
- Counts literal hits of the AI-overused vocabulary list (whole-word, case-
  insensitive). Useful as a vocabulary census, not a verdict.
- Counts em dashes and reports per-paragraph density. Em-dash flooding is
  one of the few AI tells that's genuinely a count phenomenon.
- Counts curly vs. straight quotes so the agent can spot a mismatched
  convention.
- Reports paragraph and line stats so the agent can see cadence at a glance
  (e.g., one-sentence paragraphs is a LinkedIn-AI tell).

What the script intentionally does NOT do:
- It does not try to detect negative parallelism, antithesis, copulative
  avoidance, tricolons, elegant variation, or "cadence" tells via regex.
  Those are recognition tasks, and the agent reading the prose is the right
  detector. Earlier versions had regex matchers for them; they produced
  false confidence on miss-prone shapes (e.g., "isn't X — it's Y") and over-
  fired on legitimate antithesis. The structural pass belongs in SKILL.md.

English-only. The vocabulary list is English; for non-English prose, skip
this script and apply the categories from SKILL.md using the input
language directly.

Non-interactive: reads from --file PATH or stdin, writes JSON to stdout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from typing import Any


# Words Wikipedia identifies as overused in AI English prose.
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

EM_DASH_PATTERN = re.compile(r"[—–]")
CURLY_QUOTE_PATTERN = re.compile(r"[‘’“”]")
WORD_PATTERN = re.compile(r"\b[A-Za-z'-]+\b")
SENTENCE_END = re.compile(r"[.!?]+(\s|$)")


def split_paragraphs(text: str) -> list[str]:
    """Split on blank lines. Trim each paragraph."""
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def scan(text: str) -> dict[str, Any]:
    lower = text.lower()

    word_counts: Counter[str] = Counter()
    for match in WORD_PATTERN.finditer(lower):
        word = match.group(0)
        if word in AI_VOCAB:
            word_counts[word] += 1

    paragraphs = split_paragraphs(text)
    paragraph_stats = []
    for idx, para in enumerate(paragraphs, start=1):
        em = len(EM_DASH_PATTERN.findall(para))
        sentences = max(1, len(SENTENCE_END.findall(para)))
        words = len(WORD_PATTERN.findall(para))
        paragraph_stats.append({
            "paragraph": idx,
            "sentences": sentences,
            "words": words,
            "em_dashes": em,
        })

    em_dashes = len(EM_DASH_PATTERN.findall(text))
    curly_quotes = len(CURLY_QUOTE_PATTERN.findall(text))

    distinct_vocab = len(word_counts)
    total_vocab_hits = sum(word_counts.values())
    total_words = len(WORD_PATTERN.findall(text))

    one_sentence_paragraphs = sum(
        1 for p in paragraph_stats if p["sentences"] == 1
    )

    return {
        "vocabulary": {
            "hits": dict(word_counts),
            "distinct_words": distinct_vocab,
            "total_hits": total_vocab_hits,
        },
        "punctuation": {
            "em_dashes": em_dashes,
            "curly_quotes": curly_quotes,
        },
        "structure": {
            "paragraphs": len(paragraphs),
            "total_words": total_words,
            "one_sentence_paragraphs": one_sentence_paragraphs,
            "per_paragraph": paragraph_stats,
        },
        "note": (
            "This is a fact sheet, not a verdict. Structural patterns "
            "(negative parallelism, tricolons, elegant variation, "
            "copulative avoidance, cadence) are detected by the agent "
            "reading the prose, not by this script. Use the inventory "
            "phase in SKILL.md to enumerate them."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Mechanical fact sheet for English prose. Reports vocabulary "
            "hits, em-dash and curly-quote counts, and paragraph stats. "
            "Reads from --file PATH or stdin. Emits JSON."
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

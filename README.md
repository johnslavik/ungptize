# ungptize

[![Cooked with skillcook](https://img.shields.io/badge/cooked_with-skillcook-d97757)](https://github.com/johnslavik/skillcook)

An [Agent Skill](https://agentskills.io) that strips AI-writing tells from prose. Source: the [*Language and grammar*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Language_and_grammar) section of Wikipedia's *Signs of AI writing*, plus the punctuation tells from the adjacent *Style* section.

## What it does

Given prose the user suspects is AI-shaped, the skill:

1. Identifies the input language. If English, runs `scripts/scan.py` for a mechanical pass over the catalogued vocabulary, em-dash density, curly quotes, and naive structural matches.
2. Categorises candidate tells across the five language-and-grammar patterns Wikipedia documents — overused vocabulary, copulative avoidance, negative parallelisms, the rule of three, and elegant variation.
3. Applies the *clustering* rule (single neutral usages stay; clusters get rewritten) to avoid scrubbing prose that just happens to use a flagged word.
4. Rewrites while preserving meaning, voice, and register. Doesn't invent content to fill gaps.
5. Returns the rewrite with a tell-by-tell change log.

For non-English input, the lexical scan is skipped. The structural rules (negative parallelism, rule of three, elegant variation, copulative avoidance, em-dash flooding) generalise across languages — the agent applies them using its own multilingual fluency. The change log notes the skipped lexical scan.

## Install

Drop the directory wherever your agent client picks up skills.

For Claude Code:
```bash
git clone git@github.com:johnslavik/ungptize.git ~/.claude/skills/ungptize
```

## Trigger phrases

`ungptize`, `remove AI tells`, `make this less ChatGPT-y`, `de-AI this`, `this sounds like AI / GPT / an LLM`, `rewrite to sound human`, `scrub the GPT-isms`, `less corporate`, `too polished`, or pasting prose and asking for a more human voice.

## Files

```
ungptize/
├── SKILL.md
├── references/
│   ├── VOCABULARY.md      # 24-word AI-overused list + replacements + era timeline
│   ├── EXAMPLES.md        # before/after rewrites per category, ambiguous cases
│   └── PUNCTUATION.md     # em dashes, curly quotes
├── scripts/
│   └── scan.py            # English-only mechanical scan, JSON report on stdout
├── evals/
│   └── evals.json         # 3 cases: dense English, near-miss neutral, non-English structural
├── LICENSE
└── README.md
```

## License

MIT — see `LICENSE`.

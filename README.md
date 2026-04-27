# ungptize

[![Cooked with skillcook](https://img.shields.io/badge/cooked_with-skillcook-d97757)](https://github.com/johnslavik/skillcook)

An [Agent Skill](https://agentskills.io) that strips AI-writing tells from prose. Source: the [*Language and grammar*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Language_and_grammar) section of Wikipedia's *Signs of AI writing*, plus the punctuation tells from the adjacent *Style* section.

## What it does

Given prose the user suspects is AI-shaped, the skill:

1. Reads the input. The agent — not a regex scanner — does the detection. AI tells are about *register* and *cluster density*, which substring matchers miss and false-positive on.
2. Spawns a detector subagent (phase 1) that produces an exhaustive inventory of candidate tells across the categories: vocabulary, copulative avoidance, negative parallelisms, rule-of-three tricolons, elegant variation, pre-emptive concession blocks, LinkedIn-style cadence, em-dash flooding, and curly-quote conventions.
3. Applies the *clustering* rule (single neutral usages stay; clusters get rewritten) to avoid scrubbing prose that just happens to use a flagged word.
4. Rewrites (phase 2) while preserving meaning, voice, and register. Doesn't invent content to fill gaps.
5. Returns the inventory, the rewrite, and a tell-by-tell change log.

The English vocabulary list in `references/VOCABULARY.md` is English-specific. The structural categories generalise across languages — for non-English input, the agent applies them using its own multilingual fluency.

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
├── evals/
│   └── evals.json         # 3 cases: dense English, near-miss neutral, non-English structural
├── LICENSE
└── README.md
```

## License

MIT — see `LICENSE`.

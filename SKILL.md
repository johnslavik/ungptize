---
name: ungptize
description: Use this skill when the user wants to strip AI-writing tells from prose — triggers include "ungptize", "remove AI tells", "make this less ChatGPT-y", "de-AI this", "this sounds like AI / GPT / an LLM", "rewrite to sound human", "scrub the GPT-isms", "less corporate", "too polished", or simply pasting prose and asking for a more human voice. Detects and rewrites the patterns Wikipedia catalogues as signs of AI writing — overused vocabulary (delve, pivotal, tapestry, robust, vibrant, etc.), avoidance of basic copulatives ("serves as" / "stands as" replacing "is" or "has"), negative parallelisms ("not just X, but Y"), rule-of-three tricolons, elegant variation, em-dash flooding, curly-quote conventions. English-first with multilingual structural fallback — also trigger when the input is in another language and the user asks for the same kind of cleanup, even if they don't say "AI".
metadata:
  cooked-with: johnslavik/skillcook
  cooked-with-version: "85270c7"
---

# ungptize

Take prose the user suspects is AI-shaped and rewrite it to remove the linguistic tells while preserving meaning, voice, and register. Source: the *Language and grammar* section of Wikipedia's [*Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (plus the punctuation tells from the adjacent *Style* section).

## Workflow

- [ ] **1. Read the input.** Identify the language. If non-English, set the `LEX_AVAILABLE=false` flag for yourself and skip step 2.
- [ ] **2. Run `scripts/scan.py`** on the input (English only). Pipe the prose to stdin; read the JSON report. Use it to back the change log with line numbers, not to dictate every fix.
- [ ] **3. Categorise candidate tells** into the five categories below + punctuation. For non-English input, do this from your own knowledge of the language's idiomatic AI-shaped phrasings — the categories generalise; the lexicon does not.
- [ ] **4. Decide what to rewrite.** Apply the clustering rule: rewrite when tells cluster or when a phrase clearly leans on a pattern. Leave isolated, neutrally-used instances alone.
- [ ] **5. Rewrite.** Preserve meaning, voice, register. Prefer the simplest copulative ("is"/"has") to a fancier verb. Don't invent content to fill gaps.
- [ ] **6. Verify** that meaning is preserved and the rewrite reads in the user's voice (or in a neutral human voice if the user is anonymous).
- [ ] **7. Output** the rewritten prose followed by a tell-by-tell change log.

## Inputs

The user pastes prose. They may also specify aggressiveness ("light pass", "scrub it hard"). Default: conservative — fix clusters, leave isolated-and-neutral instances.

If the input is a fragment without context (e.g., one sentence with no surrounding paragraph), ask whether to assume formal or casual register before rewriting. Don't guess silently.

Do **not** invent: project-specific terminology, names, facts, or claims to "replace" content removed during de-tell-ing. If removing a tell leaves the sentence shorter, that's fine.

## The five language-and-grammar patterns

Each rule: what to look for, then a one-line before/after.

**1. High-density AI vocabulary.** Words like *delve, pivotal, tapestry, robust, vibrant, intricate, meticulous, crucial, key, fostering, enhance, align with, showcase, underscore, testament, garner, bolstered, landscape, interplay, enduring, additionally, boasts, valuable, highlight, emphasizing*. Rewrite when several appear together or when one clearly carries no weight. Full list with replacements + era timeline: `references/VOCABULARY.md`.
- *Before:* "This pivotal release boasts a vibrant tapestry of features."
- *After:* "This release adds the features listed below."

**2. Avoidance of basic copulatives.** *Serves as, stands as, marks, represents, boasts, features, maintains, offers* in place of *is/are/has*.
- *Before:* "The library serves as the foundation of the framework."
- *After:* "The library is the foundation of the framework."

**3. Negative parallelisms.** *Not only X, but Y* / *Not just X, it's Y* / *Not X, but Y* / *No X, no Y, just Z*. Tell when the form is decorative; legitimate when the contrast carries actual meaning.
- *Before:* "It's not just a tool, it's an experience."
- *After:* "It's a good tool." (or whatever is actually true)

**4. Rule of three.** Adj/adj/adj or phrase/phrase/and-phrase tricolons. Tell when decorative and unsupported by surrounding rhythm; legitimate in slogans, quoted speech, and rhetorically grounded prose.
- *Before:* "a meticulous, robust, intricate experience"
- *After:* "a careful experience" (pick the one adjective that's actually doing work)

**5. Elegant variation.** Renaming the subject ("the protagonist", "the eponymous character", "the key player") instead of repeating the noun. Repeat the noun unless variation genuinely clarifies.
- *Before:* "Linus created Linux. The eponymous creator…"
- *After:* "Linus created Linux. Linus then…"

**6. Punctuation tells** (covered in `references/PUNCTUATION.md`). Em-dash flooding and curly quotes substituted into prose where straight quotes are the local default.

## Defaults

- **Voice preservation:** match the surrounding text's register. If the input is the user's own writing, lean toward less rather than more change.
- **Conservative pass:** rewrite clusters and decorative cases; leave isolated neutral usages.
- **No filler invention:** if a sentence gets shorter, leave it shorter.
- **Show your work:** every rewrite appears in the change log with its category and the original phrasing.

## Gotchas

- **Don't strip every flagged word.** *Key, crucial, additionally* appear in legitimate prose. Wikipedia explicitly notes that clustering — not single tokens — is the AI signal. Single neutral hits stay.
- **Don't invent content to fill the gap.** Removing "serves as the foundation of modern X" yields "is the foundation of modern X" — not a longer rewrite that reintroduces filler.
- **Preserve voice.** A rewrite that sounds like a different LLM's house style is still a tell, just a different one. Match the user's register.
- **Tricolons aren't always AI.** Quoted speech, slogans, established rhetoric ("life, liberty, and the pursuit of happiness") use the rule of three for a reason. Flag only decorative ones.
- **Negative parallelism has legitimate uses.** "Not the man we knew, but the man he had become" is prose. The tell is the shallow decorative form ("not just a tool, it's an experience").
- **Em dashes are not banned.** A few em dashes are normal. The tell is *flooding* — many per paragraph for over-emphasis. The script reports counts so you can decide.
- **Curly quotes can be intentional.** Print, ebook, and some CMS pipelines want curly quotes. Convert only if the surrounding document uses straight quotes (or vice versa); never silently flip a convention the user picked.
- **Non-English input: lexicon is unavailable, categories still apply.** Skip `scripts/scan.py`. Don't translate the English vocabulary list into the target language and pattern-match — invent nothing the source doesn't cover. Apply categories (negative parallelism, rule of three, elegant variation, copulative avoidance, em-dash flooding) using your own knowledge of the language. Note in the change log that the lexical scan was skipped.
- **The script is a pointer, not a verdict.** `scripts/scan.py` flags candidates; you decide. A high "key" count with all uses being neutral means no rewrite.
- **Don't sanitise the user's intentional voice.** If a sentence is florid because the user *wants* it florid, leave it. Ask if unsure.

## References

- **`references/VOCABULARY.md`** — read when you need a neutral replacement for a flagged word, or when the script reports a word you don't immediately recognise as a tell. Includes the era timeline (which words dominated 2023→mid-2024 vs. mid-2024→mid-2025 vs. mid-2025→).
- **`references/EXAMPLES.md`** — read when you're unsure whether a candidate is actually a tell vs. legitimate prose. Extended before/after rewrites for each category, including ambiguous cases.
- **`references/PUNCTUATION.md`** — read when the input has noticeable em-dash density or mixed quote styles, or when the user explicitly asks about punctuation.

## Available scripts

- **`scripts/scan.py`** — English-only mechanical scan. Pipe prose to stdin (or pass `--file PATH`); receive a JSON report with vocabulary hits, em-dash count, curly-quote count, candidate negative-parallelism matches, and copulative-avoidance flags. Run with `--help` for usage. For non-English input, skip this script — its lexicon is English-only and it will exit with a clear message if given `--language` other than `en`.

## Output

A rewritten copy of the prose, followed by a brief change log. Format:

```
<rewritten prose>

---
Changes:
- [vocabulary] "pivotal" → removed (decorative)
- [copulative] "serves as" → "is"
- [negative-parallelism] "not just X, but Y" → "X" (decorative form)
- [tricolon] "meticulous, robust, intricate" → "careful" (decorative)
- [punctuation] 7 em dashes → 2 (flooding)

Lexical scan: <ran on English | skipped, input is <language>>
```

State facts. Don't market the result.

---

<sub>[![Cooked with skillcook](https://img.shields.io/badge/cooked_with-skillcook-d97757)](https://github.com/johnslavik/skillcook)</sub>

# EXAMPLES

Extended before/after rewrites for each of the five language-and-grammar categories, including ambiguous cases the inline rules in `SKILL.md` don't cover.

Read this when you're unsure whether a candidate is actually a tell vs. legitimate prose.

---

## 1. High-density AI vocabulary

**Decorative cluster — rewrite hard.**
- *Before:* "This pivotal release boasts a vibrant tapestry of features, fostering not just productivity, but a meticulous, robust, intricate experience."
- *After:* "This release adds the features below."
- *Why:* Every adjective is decorative. The sentence makes no factual claim that survives stripping the tells.

**Isolated word, doing real work — leave it.**
- *Before:* "The key insight is that recursion bottoms out at the base case."
- *After:* "The key insight is that recursion bottoms out at the base case."
- *Why:* "Key" is the most natural word here. Replacing it with "main" or "important" is sideways motion. Single neutral usage; no cluster.

**Single decorative word — delete it.**
- *Before:* "The library provides a robust API for HTTP requests."
- *After:* "The library provides an API for HTTP requests."
- *Why:* "Robust" is doing no work. The reader learns nothing from it. Prefer deletion to substitution.

---

## 2. Avoidance of basic copulatives

**Stock substitution — restore "is".**
- *Before:* "The Eiffel Tower stands as a symbol of Paris."
- *After:* "The Eiffel Tower is a symbol of Paris."

**Genuinely doing work — leave it.**
- *Before:* "The committee serves as the appellate body for trademark disputes."
- *After:* "The committee serves as the appellate body for trademark disputes."
- *Why:* "Serves as" here describes a *role*, not just identity. "Is the appellate body" reads slightly differently. Edge case; prefer "is" only if the sentence still reads true.

**"Boasts" replacing "has" — almost always strip.**
- *Before:* "The new model boasts 200B parameters."
- *After:* "The new model has 200B parameters."

**"Features" replacing "has" — almost always strip.**
- *Before:* "The kitchen features granite countertops."
- *After:* "The kitchen has granite countertops."

---

## 3. Negative parallelisms

**Decorative — rewrite or delete.**
- *Before:* "It's not just a tool, it's an experience."
- *After:* "It's a useful tool." (or whatever is actually true; the original makes no real claim)
- *Why:* The contrast is empty — there's no actual content being negated. Pure rhetorical filler.

**Decorative tricolon negative — collapse.**
- *Before:* "No fluff, no jargon, just clarity."
- *After:* "Clear writing."

**Genuine contrast — leave it.**
- *Before:* "She wasn't the candidate I expected, but the candidate I needed."
- *After:* "She wasn't the candidate I expected, but the candidate I needed."
- *Why:* Real semantic contrast — both halves carry meaning. Not a tell.

**"Not only X, but Y" — judge by content of Y.**
- *Before:* "The library is not only fast, but also memory-safe."
- *After:* "The library is fast and memory-safe."
- *Why:* The "not only" framing is decorative when both halves are simple adjectives. Plain conjunction reads cleaner.

---

## 4. Rule of three (tricolon)

**Decorative adjective triple — pick the one that works.**
- *Before:* "a meticulous, robust, intricate experience"
- *After:* "a careful experience" (or just delete the adjective)

**Phrase triple — collapse.**
- *Before:* "We design for users, build for scale, and optimize for performance."
- *After:* "We build scalable systems for our users."

**Established rhetoric — leave it.**
- *Before:* "Life, liberty, and the pursuit of happiness."
- *After:* "Life, liberty, and the pursuit of happiness."
- *Why:* Quoted, established. Not a tell.

**Real list of three things — leave it.**
- *Before:* "The compiler runs three passes: lexer, parser, and codegen."
- *After:* "The compiler runs three passes: lexer, parser, and codegen."
- *Why:* These are actual three discrete things, not adjectival decoration.

---

## 5. Elegant variation

**Pointless re-naming — repeat the noun.**
- *Before:* "Linus Torvalds created Linux. The eponymous developer also wrote git."
- *After:* "Linus Torvalds created Linux. He also wrote git."

**Genuine clarification — leave it.**
- *Before:* "Linus Torvalds created Linux. The Finnish-American engineer was 21 at the time."
- *After:* "Linus Torvalds created Linux. The Finnish-American engineer was 21 at the time."
- *Why:* The variation adds biographical context, not just a synonym for the name.

**Subject re-naming as ornament — strip.**
- *Before:* "Hamlet kills Polonius. The prince of Denmark then…"
- *After:* "Hamlet kills Polonius. He then…"

---

## Cross-cutting: when the rewrite makes the prose shorter

This is correct. AI-shaped prose is often *longer* than it needs to be precisely because the tells are filler. A rewrite that drops 30% of the words and preserves all the meaning is the right outcome. Don't add new content to make the rewrite the same length.

## Cross-cutting: when the input has no real tells

If you scan the prose and find isolated, neutrally-used vocabulary and no structural patterns — say so. Output: "No clear tells found at the cluster level. Isolated uses of [words] but each reads natural in context." A skill that's honest about producing no rewrite is more useful than one that fabricates fixes.

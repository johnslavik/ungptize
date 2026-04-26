# EXAMPLES

Extended before/after rewrites for each category, plus worked-example inventories on long-form prose.

Read this when you're unsure whether a candidate is actually a tell vs. legitimate prose, or when you want a model of how the inventory should look on a real piece.

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
- *Why:* "Robust" is doing no work. Prefer deletion to substitution.

---

## 2. Avoidance of basic copulatives

**Stock substitution — restore "is".**
- *Before:* "The Eiffel Tower stands as a symbol of Paris."
- *After:* "The Eiffel Tower is a symbol of Paris."

**Genuinely doing work — leave it.**
- *Before:* "The committee serves as the appellate body for trademark disputes."
- *After:* "The committee serves as the appellate body for trademark disputes."
- *Why:* "Serves as" here describes a *role*, not just identity. Edge case; prefer "is" only if the sentence still reads true.

**"Boasts" replacing "has" — almost always strip.**
- *Before:* "The new model boasts 200B parameters."
- *After:* "The new model has 200B parameters."

**"Features" replacing "has" — almost always strip.**
- *Before:* "The kitchen features granite countertops."
- *After:* "The kitchen has granite countertops."

---

## 3. Negative parallelisms

This category is where the skill missed tells before the rewrite. The full shape inventory:

> **Rewriting principle: escape the shape, don't compress it.** When you rewrite a negative parallelism, do not just produce a shorter or tighter antithesis. State the affirmative half directly and drop the negation. If you can't restate the thought without the `not X` half, the negation was decorative — find a different sentence that says what's true. A semicolon-parallel `X is A; Y is B` is the same tell at clause level: pick one half, or rewrite as plain prose.

### `not only X, but Y`
- *Before:* "The library is not only fast, but also memory-safe."
- *After:* "The library is fast and memory-safe."
- *Why:* The "not only" framing is decorative when both halves are simple adjectives. Plain conjunction reads cleaner.

### `not just X, it's Y`
- *Before:* "It's not just a tool, it's an experience."
- *After:* "It's a useful tool." (or whatever is actually true)
- *Why:* The contrast is empty — there's no actual content being negated.

### `X, not Y` (trailing antithesis)
- *Before:* "The fix is a rule, not a patch."
- *After:* "The fix is a rule."
- *Why:* If "not a patch" doesn't add information the reader didn't already have from "is a rule," it's decoration. Watch for this everywhere — it's small, easy to miss, and pure LLM cadence.

### `isn't/wasn't X — it's/it was Y` (em-dash antithesis)
- *Before:* "It isn't that the AI is smart — it's that the knowledge is finally written down."
- *After:* "What's new is that the knowledge is finally written down."
- *Why:* The em-dash antithesis is the LLM signature. Note the *bad* fix: rewriting this as "The AI isn't smart; the knowledge is written down" or "The AI isn't smart. The knowledge is written down." Both are still antitheses, just punctuated differently. The honest rewrite drops the negation entirely and says what's true.

### `wasn't X; it was Y` (semicolon antithesis)
- *Before:* "The fix wasn't a new library; it was two paragraphs in a Markdown file."
- *After:* "The fix was two paragraphs in a Markdown file."
- *Why:* Naming what something *isn't* is filler unless the misconception is one the reader genuinely held.

### `doesn't X; it Y` (semicolon antithesis, verb form)
- *Before:* "It doesn't need a script; it needs guidance."
- *After:* "It needs guidance."
- *Why:* "Not a script" only adds information if the reader was about to write a script. If they weren't, the negation is decorative. Notice the *bad* fix: "It needs guidance, not a script" — that's the same antithesis with a comma instead of a semicolon.

### `X is A; Y is B` (parallel antithesis)
- *Before:* "A script is a leaky abstraction; a skill file is the actual intent."
- *After:* "A skill file states the intent directly."
- *Why:* The parallel-clause shape is decorative when one half is a setup for the other. The bad fix is "A script leaks; a skill file states the intent" — that's the same parallel structure compressed. The honest fix picks one clause and drops the other.

### `Don't X. Y.` (imperative antithesis)
- *Before:* "Don't write a script. Write a set of instructions."
- *After:* "Write a set of instructions."
- *Why:* The two-sentence imperative form is LLM rhythm. The bad fix is "Write a set of instructions instead of a script" — that's the same antithesis collapsed into one sentence. If "instead of a script" doesn't carry information, drop it.

### `doesn't mean X. It means Y.`
- *Before:* "This doesn't mean I don't care about quality. It means I care more about speed."
- *After:* "Speed matters more to me than polish."
- *Why:* The double negative + reframe is one of the most recognisable LinkedIn-AI shapes. The bad fix is "I care about quality, but I care more about speed" — that mirrors the same comparative shape. The honest rewrite states the actual position once and drops the negation theatre entirely.

### `no X, no Y, just Z` (negative tricolon)
- *Before:* "No fluff, no jargon, just clarity."
- *After:* "Clear writing."

### Genuine contrast — leave it
- *Before:* "She wasn't the candidate I expected, but the candidate I needed."
- *After:* "She wasn't the candidate I expected, but the candidate I needed."
- *Why:* Real semantic contrast — both halves carry meaning. Not a tell.

---

## 4. Rule of three (tricolon)

**Decorative adjective triple — pick the one that works.**
- *Before:* "a meticulous, robust, intricate experience"
- *After:* "a careful experience"

**Decorative phrase triple — collapse.**
- *Before:* "We design for users, build for scale, and optimize for performance."
- *After:* "We build scalable systems for our users."

**Parallel-sentence triple (the long-form version) — collapse or pick one.**
- *Before:* "The runner who shows up tired beats the one who waits for ideal weather. The recipe you cook tonight beats the one you bookmark for next month. The page you write at lunch beats the chapter you outline forever."
- *After:* "The page you write at lunch beats the chapter you outline forever."
- *Why:* Three parallel sentences making the same point is decoration. Pick the strongest example or condense to one general statement.

**Established rhetoric — leave it.**
- *Before:* "Life, liberty, and the pursuit of happiness."
- *After:* "Life, liberty, and the pursuit of happiness."

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

---

## 6. Cadence

The category Wikipedia's catalogue misses but every LinkedIn-style AI post is built on. Recognise the cluster, not individual cues.

### Cues to look for, together

- **One-sentence paragraphs.** Most of the post.
- **Pivot phrases.** "Here's the thing:" / "Let me explain:" / "The reality is:"
- **Fake interlocutor.** A quoted objection in scare quotes that the writer immediately refutes.
- **Fragment-as-emphasis.** "Every time." / "Especially now."
- **Aphorism drop.** A maxim sentence that summarises the post.
- **Rhetorical-question + emoji closer.** Final paragraph asking a question, often + emoji.

A single cue is not a tell. Three or more together is.

### Worked example: cadence cluster

**Before** (AI-shaped post on houseplant care):

> Most people kill houseplants the same way.
>
> They overwater. They underwater. They move the pot every week chasing the perfect light.
>
> Here's the thing: plants don't want perfect. They want predictable.
>
> The fiddle-leaf in the dim corner that gets watered every Sunday outlives the one rotated daily under a grow lamp. The pothos on the bookshelf that nobody fusses over outgrows the one in the kitchen window. The succulent ignored for two weeks beats the one prodded for moisture every morning.
>
> "But what about light? What about humidity?"
>
> Light and humidity matter. Consistency matters more.
>
> What's one plant you've been micro-managing? 🌿

**Inventory:**

```
P1-P7 · cadence      · 7 paragraphs, 5 one-sentence              · rewrite   · LinkedIn cadence cluster
P3    · cadence      · "Here's the thing:" pivot                 · rewrite   · explicit reframe phrase
P4    · tricolon     · "The fiddle-leaf… The pothos… The succulent…" · rewrite · parallel-sentence triple, no new info per row
P5    · cadence      · "But what about light? What about humidity?" · rewrite · fake interlocutor
P3    · neg-parallel · "don't want perfect. They want predictable" · rewrite  · `not X. They want Y.` antithesis
P6    · neg-parallel · "Light and humidity matter. Consistency matters more." · rewrite · `X matter. Y matters more.` antithesis
P7    · cadence      · rhetorical-question + 🌿 closer            · rewrite   · LinkedIn closer signature
L2    · tricolon     · "They overwater. They underwater. They move…" · rewrite · decorative parallel triple
```

**After:**

> Most people kill houseplants by trying too hard. Plants do best on a steady routine. A pothos on a bookshelf that gets watered every Sunday will usually outlast one rotated daily under a grow lamp.

*Why this rewrite:* the original makes one observation (a steady routine helps houseplants) and dresses it up with a pivot phrase, a parallel triple, a fake interlocutor, antithesis ("X matter. Y matters more."), and a rhetorical-question closer. The rewrite states the observation once with one example, in three plain sentences with no antithesis structure. Note: an early draft of this rewrite said "Plants want predictable conditions more than optimal ones" — that's still a comparative antithesis, just compressed. The principle is to escape the shape entirely, not compress it.

---

### Worked example: dense neg-parallel cluster

**Before** (AI-shaped post on learning an instrument):

> When my piano teacher fired me, I thought I'd failed.
>
> Looking back, the firing wasn't a failure — it was the beginning of progress.
>
> The problem wasn't that I couldn't play the étude. It was that I'd stopped listening to it.
>
> I didn't need a new teacher; I needed a new ear.
>
> So I stopped drilling the passage and started listening to it. Don't repeat. Hear.
>
> The musician who listens beats the one who repeats.

**Inventory:**

```
P2 · neg-parallel · "wasn't a failure — it was the beginning of progress" · rewrite · em-dash antithesis, decorative
P3 · neg-parallel · "wasn't that I couldn't play the étude. It was that I'd stopped listening" · rewrite · `wasn't that X. It was that Y.` antithesis
P4 · neg-parallel · "didn't need a new teacher; I needed a new ear"        · rewrite · semicolon antithesis with verb
P5 · neg-parallel · "Don't repeat. Hear."                                  · rewrite · imperative antithesis (decorative)
P6 · cadence      · aphorism drop "The musician who listens beats the one who repeats" · rewrite · maxim closer
P1-P6 · cadence   · 6 one-sentence paragraphs                              · rewrite · LinkedIn cadence
```

**After:**

> When my piano teacher fired me, I thought I'd failed. Looking back, it was when I started making real progress. I'd been drilling the étude for weeks without actually hearing it. So I spent the next month listening to recordings, and that changed how I played.

*Why this rewrite:* the original story is fine; the rhetorical scaffolding is the AI part. An early draft of this rewrite kept "the problem wasn't the étude, it was that I'd stopped listening to what I was playing" — *and that's still a `wasn't X, it was Y` antithesis*, just shorter. It's the same tell. The fix is to escape the shape entirely: state directly that the writer had been drilling without listening. No `wasn't / it was`. No `not / instead`. Same content; different sentence shape.

---

## Cross-cutting: when the rewrite makes the prose shorter

This is correct. AI-shaped prose is often *longer* than it needs to be precisely because the tells are filler. A rewrite that drops 50%+ of the words and preserves all the meaning is the right outcome. Don't add new content to make the rewrite the same length.

## Cross-cutting: when the input has no real tells

If the inventory comes back with mostly `keep` rows and no clusters — say so. Output: "No clear tells found at the cluster level. Isolated uses of [words] but each reads natural in context." A skill that's honest about producing no rewrite is more useful than one that fabricates fixes.

# VOCABULARY

The 24+ words Wikipedia identifies as overused in AI-generated English prose, with neutral replacements you can default to. **Don't blanket-replace.** Use the clustering rule from `SKILL.md`: rewrite when several appear together or the word is decorative; leave isolated neutral usages alone.

## The list (English)

| AI-overused word | Neutral replacements (pick by context, or just delete) |
|---|---|
| Additionally | (delete) / Also / And |
| align with | match / fit / agree with |
| boasts | has |
| bolstered | strengthened / supported / backed |
| crucial | important / needed / required (or delete) |
| delve (into) | look at / examine / study |
| emphasizing | stressing / pointing out |
| enduring | lasting / long |
| enhance | improve / increase / strengthen |
| fostering | building / growing / encouraging |
| garner | get / earn / win |
| highlight (v.) | show / point out |
| interplay | interaction / mix |
| intricate / intricacies | complex / detail / detailed |
| key | important / main (or delete) |
| landscape | field / area / scene |
| meticulous / meticulously | careful / carefully |
| pivotal | important / central |
| robust | strong / solid / reliable |
| showcase (v.) | show / display |
| tapestry | mix / range / collection |
| testament (to) | proof (of) / sign (of) |
| underscore | stress / show |
| valuable | useful / helpful |
| vibrant | lively / colourful / active |

## Special case: "concrete"

The Wikipedia article notes "concrete" appears with unusual frequency when AI is *defending itself against* the accusation of being AI ("concrete evidence", "concrete examples"). If the prose is the AI's reply to "are you an AI?" — that's a strong tell on its own. In normal prose, "concrete" is fine.

## Era timeline (signal strength shifts over time)

The dominant overused words have rotated as model generations changed. Words from earlier eras are now weaker tells (they've leaked into human writing); words from the current era are stronger.

- **2023 → mid-2024:** *delve, boasts, intricate* — these were the canonical tells of the GPT-3.5/4 era. Still overused but humans now use them too.
- **mid-2024 → mid-2025:** *align with, enhance, fostering* — the Claude/GPT-4o-era replacements.
- **mid-2025 →:** *emphasizing, highlighting, showcasing* (gerund forms) — current dominant pattern.

When you see a cluster from a single era, that's a strong signal the prose was generated in that era's style. The change log should note the era when calling out vocabulary tells.

## How to use this list

1. While reading the input, note words from this list that appear.
2. For each hit, ask: *Is this word doing real work in this sentence?* If yes, leave it. If no — if removing it doesn't change the meaning — replace or delete.
3. Prefer **delete** over **replace** when the word is purely decorative. "This crucial improvement" → "This improvement" beats "This important improvement".
4. Don't replace one tell with another tell. Going from *delve* to *explore* is sideways motion; both are AI-shaped. Use the plain replacements above.

## Non-English

This list is English-only. Wikipedia's source enumerates English words. For other languages, the skill relies on your own knowledge of the target language's idiomatic AI-shaped vocabulary — do not translate this list into the target language and pattern-match against it.

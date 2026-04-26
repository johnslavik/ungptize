# PUNCTUATION

Punctuation tells from the *Style* section of Wikipedia's [*Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Adjacent to the language-and-grammar patterns this skill targets, and the script reports counts so you can decide.

Read this file when the input has noticeable em-dash density or mixed quote styles, or when the user asks specifically about punctuation.

---

## Em dashes

LLMs use em dashes more frequently than human writers do, especially in a *formulaic, pat way* and to over-emphasise clauses. The tell is **flooding**, not the dash itself.

**How to judge:**
- Count em dashes per paragraph (the script reports this). Two or three across a long paragraph is normal. Five-plus in a paragraph or one in nearly every sentence is the tell.
- Look at *what* the dash interrupts. The AI pattern: "X — and this is important — Y". A dash inserted to add a meta-emphasis the surrounding sentence doesn't need. The human pattern: a real parenthetical or genuine break in thought.

**Rewrite options:**
1. Replace the em-dash clause with a parenthetical (`( … )`) — slightly less emphatic, fine in most prose.
2. Promote the em-dash clause to its own sentence.
3. Demote it: drop the clause entirely if it adds no information.

**Don't:** mass-replace em dashes with hyphens or commas. The result is choppy and reads as another kind of edit-tell.

---

## Curly / smart quotes

ChatGPT and DeepSeek typically emit curly quotation marks (`" " ' '`) and apostrophes (`'`) instead of straight ones (`" " ' '`).

**How to judge:**
- Look at the surrounding document or codebase. If everything else uses straight quotes, the curly ones in the AI-generated chunk stand out.
- If the document is meant for print, ebook, or a CMS that prefers curly quotes — leave them alone.

**Rewrite:**
- Convert curly to straight (or vice versa) only if it matches the user's existing convention. If you're not sure what the convention is, ask.
- Don't silently flip a convention the user picked.

**Common curly characters to look for:**
- `"` (left double) and `"` (right double) — replace with `"` if needed
- `'` (left single) and `'` (right single, also used as apostrophe) — replace with `'`
- `–` (en dash) and `—` (em dash) — these are not the curly-quote issue, but worth noting in the same scan

---

## Other punctuation tells (lower signal)

The Wikipedia article doesn't dwell on these, but they sometimes appear alongside the bigger tells:

- **Title-case headings** in body prose where sentence case is the convention.
- **Bold-then-explanation** sentence structure ("**Performance:** The library is fast.") repeated for every list item.
- **Exclamation marks** at the end of every paragraph in cheerful corporate prose.

Treat these as weak signals — they show up in legitimate human writing too. Only act on them when they cluster with stronger tells.

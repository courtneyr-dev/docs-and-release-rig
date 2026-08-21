> Adapted from [Diátaxis](https://diataxis.fr) (reference page), © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is CC BY-SA 4.0. Autodoc and provenance rules adapted from Peter Knego's diataxis-docs-skill (CC BY-SA 4.0 layer). Changes: unified rule sheet, 2026-08-20.

# Reference — rule sheet

**Purpose.** Information-oriented technical description of the machinery, consulted (not read) by the user at work. Uniquely among the four types, reference is **led by the product it describes**, not by user needs. Users need truth and certainty — firm platforms to stand on — so reference must be austere, consistent, and wholly authoritative: no doubt, no ambiguity. Like a map: it tells you about the territory without your having to go verify the territory yourself, and the seriousness food-label law applies to packaging information applies here.

## Enforced

- **Describe and only describe.** Neutral description is the whole imperative — and it is genuinely hard, because explaining, instructing, and opining are what come naturally. Where those are needed, link to their homes.
- **Structure mirrors the machinery.** Module/class/method (or endpoint/resource) relationships appear identically in the docs so the user navigates product and documentation simultaneously. Don't force unnatural structure; let the product's logical arrangement make sense of the docs.
- **One consistent entry pattern per kind of entry:** name → signature → parameters → returns → errors/exceptions → defaults/limits → example. Omit fields that don't apply to a kind (an env var has no signature) rather than writing "N/A", and keep the remaining order; every entry of the same kind carries the same fields. Reference is not the place to demonstrate vocabulary range.
- **Completeness within scope** is a reference virtue (unlike how-to guides): all parameters, return values, exceptions, constraints, warnings, error codes.
- **Examples are illustration only.** A succinct usage example illuminates without teaching; watch the drift where an example develops into explanation.
- **Language:** state facts ("X inherits Y's defaults; defined in `path`"), list ("Sub-commands are: a, b, c"), warn ("You must use a. You must not apply b unless c. Never d."). Precise types and constraints ("string, max 255 characters", "Must be a valid ISO 8601 datetime"), documented defaults, documented side effects.
- **Verify every claim against source.** While drafting, note file:line per claim in the working plan (not the published page).
- **Measured numbers carry provenance.** A benchmark or measured figure cites a dated, archived run record; a number with no artifact behind it does not go in.

## Forbidden

Instruction ("to do X, first…") → link the how-to guide · explanation (any *why*) → link the explanation · opinion/recommendation → editorial has no home here (or the explanation) · narrative flow and first-person voice · **invented or assumed API** · inconsistent formats across entries.

## The autodoc rule

Where a reference generator already exists (Sphinx autodoc, typedoc, godoc, rustdoc, OpenAPI pipelines…): **improve the docstrings and structure feeding that pipeline; never write parallel pages** — they drift from the generated output. This applies at section level too: don't restate doc-comment content in hand-written tables. Hand-written reference carries only what no single API item can — cross-cutting matrices, legal combinations, wire formats — and links to the generated docs for per-item detail.

Generation is a powerful way to keep reference faithful to code — but auto-generated reference is never *all* the documentation required, and generated output still gets human review against this sheet's structure and consistency demands.

## Closing self-check

Compass every section and the whole: must land in informs-cognition / application. Anything instructing, explaining, or opining is moved (parked in the plan), never deleted. Is every entry of a kind in the same shape? Does every claim have a source note? Does every measured number have provenance?

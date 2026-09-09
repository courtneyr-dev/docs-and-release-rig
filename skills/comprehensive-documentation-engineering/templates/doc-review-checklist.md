# Pre-delivery review checklist (one document)

> Run before handing over or committing any single doc. Universal rows always apply; profile rows apply when a site profile is loaded (`templates/site-profile.md`). Checklist form after Chris Reynolds' pantheon-docs-writer (MIT), generalized. A row you did not check stays unchecked — never tick on faith.

**Document:** _____  **Type (compass):** _____ · confidence _____  **Profile:** _____ / none

## Universal

**Type purity**
- [ ] Serves one Diátaxis need; the type sheet's closing self-check ran (section and whole-doc scale)
- [ ] Anything belonging to another type was moved or linked out, not left inline
- [ ] Title says what the reader achieves ("How to …" for how-tos; the built thing for tutorials)

**Accuracy and evidence**
- [ ] Every technical claim carries its marker (`observed` / `reproduced` / `inferred` / `reported` / `disputed` / `unverified`)
- [ ] Code samples ran in a sandbox, or are marked `unverified`
- [ ] UI labels, menu paths, and option sets match the running interface (label-diff done if the doc names controls)
- [ ] Version, path, and default values checked against the current build, not memory

**Style (default Diátaxis voice unless an overlay is chosen)**
- [ ] Second person for instructions, active voice, present tense
- [ ] One term per concept, matched to the product's own label
- [ ] Sentence-case headings unless the profile says otherwise; no skipped levels; no trailing punctuation on headings
- [ ] Bold reserved for UI elements and paths; code font for files, commands, values
- [ ] Descriptive link text; internal links relative and section-deep
- [ ] Numbered lists for sequences, bullets otherwise, parallel construction
- [ ] ≤2–3 admonitions on the page
- [ ] Reader oriented (where they are) before any "click" instruction
- [ ] Shell variables declared once up front and reused (lowercase variables, uppercase constants)
- [ ] Acronyms spelled out on first use; no idioms; inclusive language (table in `references/accessibility-and-localization.md`)

**Structure and links**
- [ ] Prerequisites at the top, next steps at the bottom, related links across types; no dead ends
- [ ] Troubleshooting entries keyed by symptom, error text verbatim
- [ ] No template padding; sections that don't apply are deleted

**Images and accessibility**
- [ ] Every image has descriptive alt text; no personal data (names, emails, IDs) in screenshots; no drawn-on arrows or circles
- [ ] Terminal output is a code block, never an image
- [ ] Meaning never carried by color alone

**Mechanics**
- [ ] No trailing whitespace; single newline at end of file
- [ ] Blank line after frontmatter and around every heading and fenced block
- [ ] Every fence has a language tag

## Profile-supplied (only with a site profile)

- [ ] Correct page species and directory; filename rule honored where it is load-bearing
- [ ] Frontmatter complete per the species schema; review-date field set per profile
- [ ] Site opening and closing sections present under their exact headings
- [ ] Heading case per species (docs vs release notes may differ)
- [ ] Reusable snippets searched before writing new content; correct callout type per profile
- [ ] Page registered in navigation the way the profile specifies
- [ ] Any moved or removed URL has a redirect entry (one per old URL, sub-pages included), the PR carries the redirect label, and a From/To table is in the PR body
- [ ] Release notes only: filename date = go-live date; publish timestamp accurate; description is a full sentence; `action-required` category present if readers must act; links to the relevant docs

## Not checked (say why)
- _____

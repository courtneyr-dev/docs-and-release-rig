# Workflow: write or revise one document

For a single document — new or improved. For set-level work use `plan-new-docs.md`; for moving files use `restructure-docs.md`.

## 1 · Identify the need and type
- Who is the reader (learner or practitioner)? What do they need (do something or understand something)? Where are they (studying or working)?
- **Inputs to gather if not given** (after jazzsequence's pantheon-docs-writer, MIT): topic · audience facet · platform or variant scope (which CMS, product, or integration it applies to) · new document or edit of an existing one · when a site profile is loaded, which page species the site uses for this need (single page vs paginated guide vs release note).
- **If the docs target a specific site or docs repo**, load its profile (`templates/site-profile.md`; shape in `references/site-profiles.md`) before drafting, or build one from the repo first. Profile facts are claims about the build and carry evidence markers.
- Run the compass (`references/compass-and-classification.md`) → one type. Report **type + confidence + evidence**.
- **Generation policy:** before writing, the type is either stated by the user or classified by you and confirmed. If a request would require blending types, say so and recommend a split — refusal-to-blend is a successful outcome, not a failure.

## 2 · Load the one relevant sheet
Tutorial → `references/tutorials.md` · how-to → `references/how-to-guides.md` · reference → `references/reference.md` · explanation → `references/explanation.md`. Other species (quickstart, migration, troubleshooting, runbook, changelog, integration, SDK/config reference, architecture, glossary) → `references/content-types.md`. Grab the skeleton from `templates/content-templates.md`. Don't load sheets for types you're not writing.

## 3 · Draft to the quality bar
Apply the authoring quality bar (SKILL.md) and the type sheet's *enforced* list. Default voice is Diátaxis per-quadrant style (`references/style-overrides.md`); apply an override only if the user or repo chose one. Use the product's own terminology and UI labels (verify against the UI via `verify-ui.md` when the doc names controls). Every concept gets a concrete example; every code sample is complete and realistic.

## 4 · Verify what you assert
- Code samples and documented procedures: run them where possible (`references/evidence-and-validation.md`, `scripts/verify_examples.py`) in a disposable sandbox; mark side-effecting/unrunnable steps `unverified`. Never imply verification that didn't happen.
- Technical claims about the product: check against source/tests/schemas (shipped target) or against the source hierarchy (moving target); mark each claim.

## 5 · Boundary self-check
Does any part serve a different need? Explanation in the tutorial → extract + link. Instruction in reference → move to how-to. Reference detail in how-to → link. Then run the type sheet's **closing self-check** (compass at section and whole-doc scale; the type-specific test — fork check / human-project check / describe-only check / bath test).

## 6 · Cross-link and finish
Add prerequisites, next steps, and related links across types (no dead ends). If this doc creates or needs a target in another type that doesn't exist yet, note it (don't scaffold an empty type). State any assumption or unverified claim explicitly. Run `templates/doc-review-checklist.md` (universal rows always; profile rows when a site profile is loaded) and report unchecked rows as unchecked.

## For revising an existing document (the iterative loop)
Choose the piece → challenge it (what need? how well served? right type? language fit? anything belonging elsewhere?) → decide the single improvement that helps now → do it and treat it complete → repeat. Structure emerges from improving pieces; don't rewrite the whole set to "fix structure".

---
*Provenance: generation policy from Keith Patton's diataxis-agent-skill (CC BY-SA 4.0); review loop from Sam McLeod's agentic-coding (Apache-2.0) and diataxis.fr; inputs-to-gather, site-profile step, and pre-delivery checklist from Chris Reynolds' pantheon-docs-writer (MIT). Full attribution: `references/source-provenance.md`.*

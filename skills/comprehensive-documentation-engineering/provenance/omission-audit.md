# Omission audit

Performed after the package was complete: re-read the full prompt, re-read the capability ledger, and re-compared the skill against every source. This records anything from the prompt or a source not incorporated, and why. Accidental omissions found during the audit were corrected before finishing (noted inline).

## Method
1. Walked the prompt's Phase 3 operating model (18 modes) → each maps to a workflow and/or reference.
2. Walked the prompt's required-deliverables list (8) → each exists.
3. Walked the authoring-quality, scripts, and testing requirement lists → each mapped to a capability + file.
4. Walked each of the nine sources' unique-contributions column in `research-report.md` §3 → each traced to a destination in `traceability-matrix.md`.
5. Walked the "Definition of done" checklist → each satisfied.

## Phase 3 — the 18 modes (all present)

| # | Mode | Home |
|---|---|---|
| 1 | Documentation triage | SKILL.md router "Triage" + `compass-and-classification.md` |
| 2 | Repository documentation audit | `workflows/audit-existing-docs.md` + `documentation-audits.md` |
| 3 | New documentation-system planning | `workflows/plan-new-docs.md` |
| 4 | Tutorial authoring | `references/tutorials.md` |
| 5 | How-to guide authoring | `references/how-to-guides.md` |
| 6 | Reference authoring | `references/reference.md` |
| 7 | Explanation authoring | `references/explanation.md` |
| 8 | Document refactoring and migration | `workflows/restructure-docs.md` |
| 9 | Change-driven documentation | `workflows/document-a-change.md` |
| 10 | UI verification and label-diff | `workflows/verify-ui.md` + `ui-verification.md` |
| 11 | Release tracking | `references/release-documentation.md` |
| 12 | Beta and RC testing | `references/beta-rc-testing.md` + `workflows/test-release.md` |
| 13 | Evidence and claim validation | `workflows/validate-claims.md` + `evidence-and-validation.md` |
| 14 | Security-sensitive documentation | `security-documentation.md` + `workflows/security-audit-handoff.md` |
| 15 | Developer-experience analysis | `references/developer-experience.md` |
| 16 | Documentation governance | `references/governance-and-freshness.md` |
| 17 | Diagrams and visual explanation | `references/diagrams.md` |
| 18 | Safe execution | SKILL.md safety rules + gates in every mutating workflow |

## Required deliverables (all 8 present)

1. Research report — `provenance/research-report.md`
2. Atomic capability ledger — `provenance/capability-ledger.md`
3. Coverage and traceability matrix — `provenance/traceability-matrix.md`
4. Architecture rationale — `provenance/architecture-rationale.md`
5. Complete skill package — the shipped tree (66 files)
6. Validation report — `provenance/validation-report.md`
7. Omission audit — this file
8. Final handoff — README.md § Install/Verify/Supported + the session's closing summary

## Prompt-specified content checks (spot audit of easily-dropped items)

- Diátaxis site pages required by name: Start here, Applying, Tutorials, How-to, Reference, Explanation, the compass, Workflow, Foundations, the map, Quality, Tutorials-vs-how-to, Reference-vs-explanation, **Complex hierarchies**, Translation/localization — **all inspected** (complex-hierarchies recovered from git history; see `research-report.md` §5 C10) and reflected in `diataxis-foundations.md`, `compass-and-classification.md`, the type sheets, `information-architecture.md`, and `accessibility-and-localization.md`.
- Authoring-quality list (17 items) — all mapped: one-need (WRITE-ONE-1), outcomes-first (WRITE-OUT-1), active voice/second person (WRITE-STYLE-1), consistent terminology (WRITE-STYLE-2), global language (WRITE-STYLE-3), scannable headings (WRITE-STYLE-6), accurate prerequisites (how-to sheet + quality bar), working tested examples (WRITE-CODE-1), accessible text/visuals (GOV-A11Y-1, DGM-1), minimal admonitions (WRITE-STYLE-4), fact/instruction/interpretation separation (the four type sheets + boundary checks), tone-by-type (WRITE-STYLE-5), links-between-needs-without-blending (ARCH-LINK-1), product terminology over synonyms (WRITE-TERM-1), no template padding (WRITE-PAD-1), no forced four types (WRITE-PAD-1/DIA-WORK-3).
- Scripts "potential functions" list — implemented the load-bearing ones (inventory, link/anchor checking, mixed-doc detection, code-block extraction+testing, command verification, UI-label comparison, skill-structure validation, plus a scrub checker the security workflow needs). The remaining "potential" items are covered as method rather than a dedicated binary: **frontmatter inspection** (validate_skill inspects SKILL frontmatter), **terminology linting** (GOV-TERM-1 method + the repo-specific-lint pattern GOV-LINT-1), **stale-version detection** (freshness cadences + last-updated stamps in GOV-FRESH-1), **coverage-receipt generation** (`templates/change-coverage-receipt.md` + the workflow). These are deliberately not scripted because they are judgment- or repo-specific and a heuristic binary would overclaim — consistent with the prompt's "don't pretend a heuristic classifier can determine intent" instruction. Recorded here as a deliberate scope decision, not an accidental omission.
- Testing coverage (23 required areas) — all mapped in `validation-report.md`; positive/negative/ambiguous/adversarial all present.

## Source-by-source (nothing dropped)

Each source's unique contributions (`research-report.md` §3) were re-checked against `traceability-matrix.md` index A. All nine sources have every listed contribution landing in a concrete file. Confirmed specifically for the easily-lost specialized items:
- **rlespinasse:** git-history reclassification respect, docs-tooling adaptation, eval harness — all present.
- **keithpatton:** confidence+evidence output contract, refusal-as-success, blur-zone table, non-goals — all present.
- **peterknego:** plan-file lifecycle, not-created reason+remedy, autodoc rule at section level, tutorial execution verification, C4 rules, license split — all present.
- **sammcj:** approach-not-template, why-exactly-four, flow articulation, minimalist-docs, "what Diátaxis cannot do", British-English house-style example — all present.
- **anivar:** all 27 rules, 14 content types, 6 style overlays, maturity model, adoption funnel, audience matrix, partner both-sides + production-readiness, measurement metrics, localization, templates — all present.
- **diataxis.fr:** full doctrine incl. quality theory, both comparison pages, complex hierarchies, translation program — all present.
- **docs-and-release-rig:** source hierarchy, 48h decay, coverage map, change-coverage receipt, UI label-diff, beta/RC runbook + DoD, environment fidelity, public-tooling pattern, external-PR audit, evidence ladder + 20-step loop + controls + null-result + escape hatch + safe-proof, audit-handoff standard + scrubbing + accuracy labels, repo-docs split — all present.

## Attribution completeness pass (added 2026-08-20, second review)

On the question "is everything appropriately credited?", a grep audit found credit complete at four levels — per-reference attribution headers (all 22, incl. license + author + changes for every CC BY-SA adaptation), `LICENSE` §3, `CITATION.cff`, and `references/source-provenance.md` + the traceability matrix — but the 9 workflows, 12 templates, and `tests/check_evals.py` carried no *in-file* credit. Legally compliant (CC0 requires nothing; MIT/Apache material is re-expressed with package-level notice; all CC BY-SA adaptations live in references/ with headers), but under-credited relative to how closely several of those files follow one identifiable source. Fixed: every workflow and template now ends with a one-line provenance footer naming its principal source(s) and license, and `check_evals.py`'s docstring credits the rlespinasse eval schema. Verified by re-grep: zero workflow/template/test files without an in-file credit.

## Corrections made during this audit

- **`references/diagrams.md` licensing header:** confirmed correct (MIT + CC BY 4.0 for C4), and the structural validator was fixed to stop wrongly demanding a CC BY-SA header on it (it had produced a false failure). Documented in `validation-report.md`.
- **`(#)` placeholder anchors** in templates were being reported as broken links; the link checker was corrected to skip them, and a runnable fixture was added so the example-verification smoke test also demonstrates a clean pass. Documented in `validation-report.md`.
- No content-level omissions were found requiring a capability to be added; the ledger's four dispositions (retained/merged/adapted/optionalized) already covered every source element, and the only non-retained items are the two justified scope decisions at the foot of `capability-ledger.md` (non-documentation sibling skills in agent-skills; WordPress-specific literal values generalized to their methods).

## Result

No unexplained gaps. Every prompt-required mode, deliverable, and quality/scripts/testing item maps to a concrete file; every source's distinct contributions are traceable to a destination; the two exclusions are justified with their reasons (not "redundant"). The four Diátaxis types remain distinct and are never mechanically required. Broad changes are gated; audits inventory before judging; claims use evidence; verified and unverified are separated; code samples are verified where possible; release, UI, security, governance, and documentation workflows all remain present.

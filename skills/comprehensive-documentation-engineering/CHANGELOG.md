# Changelog

All notable changes to this skill are documented here. Format loosely follows
Keep a Changelog; this skill versions its own behavior (see `governance-and-freshness.md`
on why that matters).

## [1.2.0] — 2026-09-09

### Added
- Tenth source: Chris Reynolds' (jazzsequence) [claude-skill-pantheon-docs-writer](https://github.com/jazzsequence/claude-skill-pantheon-docs-writer) (`78451e5`, MIT per README, no LICENSE file), read in full and re-expressed. Row 10 in `references/source-provenance.md`; S10 in the ledger and traceability matrix; CITATION.cff reference.
- `references/site-profiles.md`: the site-profile concept — the build-specific mechanics (frontmatter schema, page species, file locations, components, fence metadata, navigation registration, redirects, terminology, contribution workflow, review-date field) that a specific docs site imposes, kept out of the method sheets and loaded only when the docs target that site. Pantheon kept as the credited worked example. Router row and reference-index entry.
- `templates/site-profile.md`: fill-in profile with `observed`/`inferred` evidence per slot.
- `templates/doc-review-checklist.md`: single-document pre-delivery checklist, universal rows plus profile-supplied rows; wired into `write-or-revise.md` step 6.
- `references/content-types.md`: release-note authoring rules (belongs/doesn't, go-live dating, filename-as-URL, feed-order timestamp, message-carrying headings, sentence case, three body shapes, action-required tagging); troubleshooting headings carry the error verbatim.
- `references/accessibility-and-localization.md`: inclusive-language substitution table (ableist, violent, gendered, racial, exclusionary framing).
- `references/how-to-guides.md`: procedural mechanics (orient before instructing, variables declared once, `1.` numbering, verbatim error text, output as code).
- `references/evidence-and-validation.md`: "a declared field is not a consumed field" — find the code that reads a metadata field before documenting its effect.
- `workflows/restructure-docs.md`: one redirect per old URL including sub-pages, path form, PR redirect table and label.
- `workflows/write-or-revise.md`: inputs to gather, site-profile load step.
- Evals `site-01..03` (profile load before drafting, release-note divergence, declared-vs-consumed metadata).

### Fixed
- Version drift: `SKILL.md` frontmatter and `CITATION.cff` still said 1.0.0 while this changelog was at 1.1.1. Both now carry the current version; bump all three on every change (rule adopted from source 10's maintenance notes).

### Notes
- Behavioral eval run for the new evals **not performed** in this release; only the structural validators (`scripts/validate_skill.py`, `tests/check_evals.py`) ran. Record a run in `provenance/eval-run-report.md` before relying on `site-*` assertions.

## [1.1.1] — 2026-08-20

### Fixed
- `scripts/check_links.py`: heading-anchor slugifier now matches GitHub's algorithm — each whitespace character becomes a hyphen without collapsing runs, so headings with a dropped separator (e.g. `## 1 · Prompts and skills` → `#1--prompts-and-skills`) resolve instead of false-flagging. Surfaced while vendoring the skill into `docs-and-release-rig`, whose `·`-separated SETUP headings use exactly this pattern.

## [1.1.0] — 2026-08-20

### Added
- `references/repo-workflow-practices.md`: the six sibling skills from rlespinasse/agent-skills, read in full and incorporated at user direction — conventional commits (incl. fixup guardrails and execution safety), PR CI-log diagnosis (incl. log prompt-injection defense), GitHub Actions SHA pinning (incl. API-injection defense and Dependabot grouping), branch-status reporting, Draw.io export tooling decisions, and non-English content enforcement (French worked example).
- Router row and reference-index entry for the new sheet; cross-link from `accessibility-and-localization.md`.
- Ledger AUX-* capabilities, traceability entries, and three behavioral evals (aux-01..03); the 1.0.0 exclusion note for the sibling skills is rescinded.
- Behavioral eval run: the eval suite executed against live subagents (with a no-skill baseline for the adversarial trio); results in `provenance/eval-run-report.md`.

## [1.0.0] — 2026-08-20

### Added
- Initial release. A synthesis of nine sources into one documentation-engineering skill.
- `SKILL.md` with a compass, a 12-row task router, mandatory safety/approval rules, a two-regime evidence standard, an authoring quality bar, and progressive-disclosure loading.
- 21 reference sheets: Diátaxis foundations, compass/classification, the four type sheets, anti-patterns, information architecture, 14 content types, pluggable style overrides, documentation audits, developer experience, governance/freshness, release documentation, beta/RC testing, evidence/validation, UI verification, security documentation, diagrams (incl. evidence-traced C4), accessibility/localization, and source provenance.
- 9 workflows: audit, plan/generate (gated), write/revise, restructure (gated), document-a-change, validate-claims, verify-ui, test-release, security-audit-handoff.
- 12 templates: inventory, classification matrix, coverage map, gap analysis, migration/plan file, change-coverage receipt, release-test report, evidence bundle, UI label-diff, security finding, audit handoff, content skeletons.
- 7 scripts (Python 3 stdlib, safe/dry-run by default, machine-readable output, clear exit codes): inventory_docs, check_links, detect_mixed_docs, verify_examples, compare_ui_labels, scrub_check, validate_skill.
- Test suite: `tests/evals.json` (behavioral scenarios across activation, classification, workflows, safety, evidence, governance, DX, style, localization, diagrams, and adversarial cases), a schema validator, and fixtures.
- `provenance/`: research report (source inventory, inspection record, conflict-resolution log), atomic capability ledger (~180 capabilities), and traceability matrix.

### Notes
- Dual-licensed by file (MIT + CC BY-SA 4.0); see `LICENSE`.
- Diátaxis is the work of Daniele Procida; this skill adapts it and is not endorsed by him or any source author.

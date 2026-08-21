# Changelog

All notable changes to this skill are documented here. Format loosely follows
Keep a Changelog; this skill versions its own behavior (see `governance-and-freshness.md`
on why that matters).

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

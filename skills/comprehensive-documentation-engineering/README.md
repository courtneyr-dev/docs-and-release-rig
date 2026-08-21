# comprehensive-documentation-engineering

An agent skill that treats documentation as an engineering practice. It combines the Diátaxis framework with documentation auditing, information architecture, developer experience, governance, release testing, UI verification, evidence discipline, and security-safe reporting — one coherent skill an agent can use to plan, write, audit, restructure, synchronize, verify, test, and hand off documentation.

It is a synthesis of nine sources (see `references/source-provenance.md` and `provenance/`), reconciled and de-duplicated into canonical rules with full traceability.

## What it helps an agent do

- **Classify and improve** documentation with the Diátaxis compass (tutorials, how-to guides, reference, explanation) — at sentence, section, and document scale.
- **Audit** an existing doc set: inventory before judging, classify with confidence + evidence, gap-analyze against needs/content-types/adoption-funnel, and assess maturity.
- **Plan or generate** a documentation system for a codebase — gated, phased, approval-first, never scaffolding empty types.
- **Write and revise** any of 14 content types with per-type rule sheets and skeletons.
- **Restructure** docs safely — move, never delete; preserve and verify; keep links intact; approval-gated.
- **Keep docs synchronized** with code changes and releases, producing a change-coverage receipt.
- **Verify** technical claims, code samples, and procedures against reality — prove by firing, mark every claim.
- **Validate UI labels** against the running interface (label-diff report).
- **Test releases** (beta/RC/GA) with an environment-timed runbook and a definition of done.
- **Package audit/security findings** responsibly — honest gaps, accuracy labels, confidentiality scrubbing.
- **Govern** documentation: ownership, freshness cadences, versioning, localization, diagrams.

## Structure

```
comprehensive-documentation-engineering/
├── SKILL.md                 # router, compass, safety rules, evidence standards, quality bar
├── README.md · LICENSE · CHANGELOG.md · CITATION.cff
├── references/              # 21 on-demand reference sheets (doctrine, practice areas, provenance)
├── workflows/               # 9 step-by-step workflows, one per mode
├── templates/               # 12 fill-in artifacts (inventory, plan, receipt, reports, handoff, skeletons)
├── scripts/                 # 7 safe/dry-run tools (inventory, links, mixed-doc, examples, ui-labels, scrub, validate)
├── tests/                   # evals.json + structural validators + fixtures
└── provenance/              # research report, capability ledger, traceability matrix
```

Progressive disclosure: `SKILL.md` routes; each mode loads only the references it needs. Nothing else loads until required.

## Install

Personal skill (Claude Code):

```bash
cp -R comprehensive-documentation-engineering ~/.claude/skills/
```

Or symlink a clone so edits/pulls take effect live (remove any existing dir first):

```bash
ln -s "$(pwd)/comprehensive-documentation-engineering" ~/.claude/skills/comprehensive-documentation-engineering
```

Other runtimes recognize `.cursor/skills/`, `.codex/skills/`, and the cross-runtime `~/.agents/skills/`. Project-scoped installs go under `.claude/skills/` in the repo. Verify by asking the agent a documentation question and confirming the skill activates.

## Verify the package

```bash
python3 scripts/validate_skill.py
python3 tests/check_evals.py tests/evals.json
```

## Supported environments

Claude Code, Cursor, and other agents that read the agentskills.io SKILL.md format. Scripts require Python 3 (standard library only; no dependencies). Nothing here makes network requests by default.

## Licensing

Dual-licensed by file — MIT for original workflow/logic/tooling, CC BY-SA 4.0 for reference sheets that adapt Diátaxis doctrine (each carries an attribution header). See `LICENSE` and `references/source-provenance.md`. Diátaxis is the work of Daniele Procida; this skill adapts the framework and is not endorsed by him or by any source author.

## Author

Synthesized for Courtney Robertson, 2026-08-20. Sources credited in `references/source-provenance.md`.

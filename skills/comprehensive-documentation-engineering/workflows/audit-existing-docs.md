# Workflow: audit existing documentation

Read-only. Produces an assessment; changes it recommends go through `restructure-docs.md` or `write-or-revise.md` after approval. Reference depth: `references/documentation-audits.md`.

**Iron rule: inventory before any verdict.** Never say "the docs are reference-heavy" or "this is a mess" before the inventory exists.

## 1 · Inventory (write nothing to the docs)
- Locate all documentation, not just `/docs`: READMEs, wikis, blog posts, support articles, `examples/`, generated reference, inline docs/docstrings, contributor docs (CONTRIBUTING/TESTING/DEPLOYMENT/BRANCHING/SECURITY), release notes/changelog, interface text, and docs-tooling config (`mkdocs.yml`, `conf.py`, `docusaurus.config.*`, `antora.yml`, `hugo.toml`; `.rst`/`.adoc`/`.txt`). Run `scripts/inventory_docs.py <root>` for a machine-readable first pass, then hand-verify.
- One row per page in `templates/documentation-inventory.md`: path · title · content type (or unknown/mixed) · owner · last-updated · accuracy estimate · traffic · notes.
- If nothing exists: say so and route to `plan-new-docs.md`.

## 2 · Classify
- Compass every page **and its sections** (`references/compass-and-classification.md`); record type + confidence + evidence in `templates/classification-matrix.md`.
- Flag mixed pages with a proposed per-section split (don't split mechanically).
- Check location and title signal; **check git history for prior deliberate reclassifications and respect them** (`git log --all --oneline --diff-filter=R -- '<docs>/**'`).

## 3 · Gap analysis (`templates/gap-analysis.md`)
- Coverage grid: four needs × 14 content types × the product's features and audiences.
- Health checks: duplication, contradictions, obsolete claims, orphan pages, dead links (`scripts/check_links.py`), weak navigation, missing prerequisites.
- Imbalances reported as such; funnel cross-reference (Discover→…→Upgrade) and name the **bottleneck stage** to fix first.

## 4 · Maturity (`references/documentation-audits.md`)
Assess Seeds → Foundation → Integration → Excellence honestly; partial completion = the lower level; name the next achievable level.

## 5 · Claims audit (when the docs make testable claims)
For anything that asserts behavior (feature lists, "supports X", API contracts), spot-check the highest-risk claims against reality via `workflows/validate-claims.md`; a full release-claims sweep is `workflows/test-release.md`.

## 6 · Report
Deliver: inventory → classification matrix → gap analysis → maturity → **prioritized recommendations** (immediate / short / medium / long). State what you did **not** examine. Mark every accuracy judgment with its evidence marker. Recommend, don't execute — restructuring needs the approval gate.

## Guardrails
- Don't force the framework: a small project with one good README may be fine — say so (`SAFE-SMALL-1`).
- Nothing is deleted or moved in this workflow.
- Distinguish observed from inferred; a claim you didn't verify is `reported` or `inferred`, never stated as fact.

---
*Provenance: audit sequence synthesized from Anivar Aravind's developer-docs-framework (MIT; Google OpenDocs-derived, Apache-2.0), Romain Lespinasse's agent-skills diataxis skill (MIT), and Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

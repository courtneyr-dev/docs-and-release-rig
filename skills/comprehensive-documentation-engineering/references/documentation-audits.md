> Synthesized from Anivar Aravind's developer-docs-framework (MIT; audit rules and maturity model derive from Google OpenDocs, Apache-2.0), rlespinasse/agent-skills (MIT), Keith Patton's diataxis-agent-skill (CC BY-SA 4.0 — imbalance reporting), and Courtney Robertson's docs-and-release-rig (CC0 — coverage-map method). 2026-08-20. Operational steps: `workflows/audit-existing-docs.md`.

# Documentation audits — reference

An audit answers three different questions, and a complete audit answers all three:

1. **What exists and what shape is it in?** (inventory + classification)
2. **What's missing for the users this product has?** (gap analysis, funnel, maturity)
3. **Which of its claims are actually true?** (coverage/claims audit — see `evidence-and-validation.md`)

## Inventory (always first — no verdict before it exists)

One row per page: URL/path · title · content type (or "unknown"/"mixed") · owner · last-updated · accuracy estimate (current / possibly stale / likely outdated) · traffic if available · notes. Template: `templates/documentation-inventory.md`; `scripts/inventory_docs.py` produces a machine-readable draft to hand-verify.

What people get wrong: skipping the inventory ("let's just rewrite everything"); inventorying only official docs while missing READMEs, wikis, blog posts, support articles, examples, generated reference, inline docs, contributor docs, release notes, and interface text that readers actually use; not recording ownership (unowned docs stale first). When to audit: before any restructure; on inheriting docs; when support tickets say people can't find things; annually as a health check.

## Classification

Compass every page **and its sections** (`compass-and-classification.md`); record type + confidence + evidence per row; flag mixed pages with proposed per-section splits; check location (a tutorial filed under reference won't be found) and title signal ("Authentication" is ambiguous; "How to set up authentication" is not); respect prior deliberate reclassifications found in git history. Output: `templates/classification-matrix.md`.

## Gap analysis

- **Coverage grid:** the four needs × the 14 content types × the product's actual features and audiences. Which types have zero coverage? Which features have none? Which audience rows (see `developer-experience.md`) are unserved?
- **Health checks:** duplication · contradictions · obsolete claims · orphan pages · dead links (`scripts/check_links.py`) · weak navigation/dead ends · missing prerequisites.
- **Imbalances, reported as such:** "reference-heavy, tutorial-poor." The classic findings: ~70% reference and ~5% tutorials; "tutorials" that are how-to guides; explanation scattered through guides instead of centralized; missing migration guides for past majors; no troubleshooting despite heavy support volume.
- **Funnel cross-reference:** for each adoption stage (Discover → Evaluate → Start → Build → Operate → Upgrade) check whether the required types exist and are adequate; **prioritize the bottleneck stage** — more reference never fixes a broken quickstart.

Output: `templates/gap-analysis.md`, prioritized: immediate fixes (broken links, wrong facts, critical gaps) → short-term (missing how-tos, incomplete reference) → medium (tutorials, explanation, partner docs) → long-term (interactivity, localization, analytics).

## Maturity model (Seeds → Foundation → Integration → Excellence)

A roadmap, not a judgment. Partial completion of a level = still the previous level; finish the current level before advancing; use items as sprint tasks; reassess quarterly.

- **1 · Seeds** — findable and installable: README with purpose · install/setup instructions · ≥1 usage example · license · contribution guidelines if open source.
- **2 · Foundation** — core use documented, organized: quickstart (<10 min) · API reference complete for core endpoints · ≥3 how-to guides for common tasks · error docs with resolutions · consistent formatting · working examples in the primary language.
- **3 · Integration** — docs inside the development process: docs-as-code (VCS, CI/CD, PR review) · docs in the definition of done · tutorials for major use cases · multi-language examples · versioned docs · changelog every release · usage analytics · automated link checking · examples tested in CI.
- **4 · Excellence** — a strategic asset: interactive examples/sandboxes · comprehensive explanation · partner program docs · migration guides for every major · troubleshooting driven by support data · localization for key markets · quality metrics tracked and improved · user research informing priorities · community contributions accepted and reviewed.

## Project archetypes (name the kind of docs project you're in)

**The Manual** (write new guides from scratch) · **The Edit** (improve existing for accuracy/style/goals) · **The Audit** (assess condition and gaps) · **The Migration** (change platform/format/hosting) · **The Factory** (automation, CI/CD, tooling) · **The Translation** (i18n/l10n) · **The Rules** (contributor guidelines and standards) · **The Study** (investigate user needs and usage). Naming the archetype scopes the work and the deliverable.

## The claims audit (coverage map)

For products/releases that publish claims, the structural audit is only half; the other half asks: **which claims did we verify, and which are we repeating on faith?** Harvest every claim from *all* describing documents, attach a verification status to each, and publish the gaps as gaps. Method and template: `templates/coverage-map.md`, `workflows/test-release.md`, and `evidence-and-validation.md`. Rule underneath: *a gap you have written down is a task; a gap you haven't is a future correction.*

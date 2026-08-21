> Synthesized from Anivar Aravind's developer-docs-framework (MIT — governance rules, cadences, docs-as-code, versioning) and Courtney Robertson's docs-and-release-rig (CC0 — lint pattern, decision recording, CI shape). 2026-08-20.

# Governance and freshness — documentation as an ongoing product

Documentation is a product with owners, cadences, versions, and metrics — not a one-time writing project. Stale docs are worse than none: they actively mislead. A small fresh set beats a large decaying one.

## Documentation is part of "done"

A feature is not shipped until its documentation is written, reviewed, and published. Enforce structurally, not aspirationally: definition of done includes docs · PR template carries a docs checklist · release checklist verifies docs · career ladders and performance reviews recognize documentation contributions (the single most effective culture lever). Per-change requirements:

| Change type | Documentation required |
|---|---|
| New feature | how-to guide + API reference updates |
| Breaking change | migration guide + changelog entry |
| User-facing bug fix | troubleshooting update |
| Deprecation | notice + migration path (a notice without a path is an abandonment notice) |
| Configuration change | config reference update |

## Ownership and review

Every document has a named owner (ownership follows product ownership); unowned docs go stale first. Review triggers: on change (docs PR with code PR) · quarterly accuracy audit against current behavior · on deprecation (update everything affected, add migration links) · after incidents (runbooks and troubleshooting).

## Freshness cadences

| Content type | Maximum staleness / trigger |
|---|---|
| API / SDK / configuration reference | must match current release — every release |
| Changelog | updated with every release |
| Quickstart, tutorials | verified/tested quarterly |
| How-to guides | reviewed quarterly |
| Runbooks | reviewed after every incident |
| Troubleshooting | monthly, against support data |
| Migration guides | verified at release time |
| Explanation, architecture guides | semi-annually |
| Glossary | annually |

Automate the enforcement: link checking (daily/weekly) · code-example testing in CI every release · visible last-updated stamps · staleness alerts when a page exceeds its cadence · analytics cross-reference flagging high-traffic stale pages.

## Docs-as-code

Write (Markdown, +MDX/Mermaid/frontmatter) → review (PR: accuracy, completeness, clarity, **content-type purity**, style) → build (CI: links, examples compile/run, spelling/style linting, required metadata, image alt text) → deploy (CD) → measure. Docs live in version control; co-locate reference/SDK docs with the code they describe when practical; generator choice (Docusaurus, MkDocs, Sphinx, Hugo, Starlight) matters less than the workflow; generate API reference from specs/annotations, then review and enhance — generation is a starting point.

**The repo-specific lint rule:** once a reviewer has caught the same class of problem twice, encode it as an automated repo-specific gate (a custom lint target for recurring data-leak/i18n/style findings). Automating recurring review findings is the same move as packaging a method into a skill, one level down.

## Versioning

Version what describes versioned behavior: API reference, SDK reference, config reference, migration guides (each tied to one transition), usually how-to guides, sometimes tutorials. **Don't** version explanation, architecture (unless it fundamentally changed), or glossaries. Patterns: URL-versioned paths (bookmarkable, SEO-friendly) · version selector (unified UX, parallel maintenance cost) · version banner (cheapest). Lifecycle: **Preview** (labeled draft) → **Current** (default) → **Supported** (security updates) → **Deprecated** (prominent migration link) → **Archived** (read-only, clearly marked). Docs always say which version they describe.

## Terminology control

The glossary is a governance instrument: one term per concept, matched to the UI; terminology linting where available; renames propagate through *all* docs, not just new pages.

## Contribution and decision records

Keep contribution requirements proportionate to the project; consistent structure lowers review burden — methodology embedded in tooling/skills holds regardless of contributor, human or AI. Record trade-off decisions (e.g., "fork the test suite for this cycle, generalize after") *with rationale and intended follow-up* so they don't read as negligence later; ADR template in `templates/content-templates.md`. Living documentation (fast-moving, many contributors) benefits most from clear per-type contribution categories — it's obvious where new content belongs.

## Measurement

See `developer-experience.md` § Measuring documentation. Governance closes the loop: metrics feed the quarterly review; failed searches and ticket topics feed the gap backlog; tutorial completion feeds the testing cadence.

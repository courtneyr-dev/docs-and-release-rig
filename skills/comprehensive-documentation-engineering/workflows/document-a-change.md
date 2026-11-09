# Workflow: document a code/product change

Keep documentation synchronized with a change — a PR, a diff, a feature, a breaking change, a release. Produces a **change-coverage receipt** so "we documented everything" becomes an artifact someone can check, not an opinion.

## 1 · Establish the change surface
- Baseline → target (commits/tags/releases). Enumerate changed files, public APIs, hooks, routes, schemas, dependencies, deprecations, removals, feature flags.
- For a moving/pre-release target, apply the source hierarchy (`references/release-documentation.md`): runtime test > dev note > diff > roundup > memory; a dev note supersedes anything inferred from code.

## 2 · Determine which documentation types the change affects
Per the governance table (`references/governance-and-freshness.md`):

| Change | Docs required |
|---|---|
| New feature | how-to guide + API reference |
| Breaking change | migration guide + changelog |
| User-facing bug fix | troubleshooting update |
| Deprecation | notice + migration path |
| Config change | config reference |

Also: does user-facing behavior change? which existing documents describe the affected behavior?

## 3 · Reconcile — the completeness checklist
Reconcile two independent representations of the change; disagreement means something is undocumented:
- [ ] git changes ↔ release notes
- [ ] source ↔ released packages
- [ ] documented deprecations ↔ `@deprecated` annotations **and** runtime behavior
- [ ] API changes ↔ tests
- [ ] dependency changes ↔ lockfiles
- [ ] feature flags ↔ shipped defaults
- [ ] internal plans ↔ what shipped
- [ ] shipped-but-unannounced changes — identified
- [ ] announced-but-didn't-ship — identified
- [ ] reverted/partially-reverted work — identified
- [ ] generated-artifact-only changes — identified

The last four catch the real documentation bugs (e.g. a dependency upgrade that was announced, felt sourced, but never shipped).

## 4 · Update the affected docs
Apply `write-or-revise.md` per affected document, in dependency order where several change. Verify claims and run samples (`references/evidence-and-validation.md`). For compatibility statements ("Tested up to X"), treat them as runtime claims: run the real suite, diff the bent surfaces, probe per finding, and state the evidence ceiling (`references/release-documentation.md`).

If the change alters what users see, also run `workflows/verify-ui.md` steps 3–6 on the changed screens; the screenshots and the label-diff report are part of this mode's output.

## 5 · Emit the change-coverage receipt (`templates/change-coverage-receipt.md`)
Fill every field: baseline→target, counts (commits, files, APIs, hooks, routes, schemas, dependencies, deprecations, removals), undocumented changes found, **and "entries NOT fully reviewed, and why"**. The receipt states, for the change: what changed · which user-facing behavior changed · which documents were evaluated · which were updated · which were intentionally left unchanged · evidence · remaining uncertainty.

Put the filled receipt in the final message, or write it to a file and link it there; a summary table is not the receipt. For a PR-scoped docs sync, a checklist box that can't apply (no release, no lockfile change) gets `n/a — <reason>`, which counts as checked; a box with nothing beside it does not.

## 6 · The gate
If any receipt row is blank or any checklist box is unchecked, the review is **not complete** — record the shortfall as a named untested area; don't paper over it. A blank row is a legitimate, honest place to stop; a blank row nobody noticed is a future correction. "Looks done" is not a stop condition.

---
*Provenance: change-coverage receipt method from Courtney Robertson's docs-and-release-rig (CC0); per-change-type table from Anivar Aravind's developer-docs-framework (MIT). Full attribution: `references/source-provenance.md`.*

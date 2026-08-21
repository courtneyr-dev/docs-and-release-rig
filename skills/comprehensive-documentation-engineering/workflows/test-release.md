# Workflow: test and document a release (beta / RC / GA)

Support development, alpha, beta, release-candidate, and stable-release documentation and testing. Produces a coverage map and a release-test report. Reference depth: `references/release-documentation.md` (knowledge rules) and `references/beta-rc-testing.md` (the loop).

## 1 · Re-anchor before touching any deliverable (the daily sweep)
Mid-cycle knowledge decays in ~48 hours. Each session, **first**: sweep the last 24–48h of authoritative sources (dev-note tag, core/test channels, the release milestone, repo compare views, chat) → diff the sweep against the current docs → correct and **date the delta** for anything already shared (readers need the delta, not a silent edit; correct your own prior errors explicitly with the correcting source) → re-verify changed features at runtime where testable → swap draft links for public ones as official docs publish. Re-point every test spec at the current dev notes before testing.

## 2 · Build the coverage map (`templates/coverage-map.md`)
Harvest every claim the release makes from **all** describing sources; put verification status beside each. Structure: dated update log on top · verified-first-hand list · gap table grouped by audience (item · own-words description · authoritative public reference · status) · quality-of-life cluster (grouped, not enumerated) · cross-links to gaps discovered in other deliverables. Anything without a status is a gap, published as a gap. Originality guardrail: own words/examples/screenshots; never reuse a roundup's phrasing; exclude preview-tokened/internal links.

## 3 · Group environments by update timing and run the four-phase loop
Environments (`references/beta-rc-testing.md`): immediate (local disposable, shell-access hosts, forceable managed production) vs deferred (managed staging on its own schedule). Per drop:
- **Phase 0 re-anchor** (the sweep, plus re-point specs).
- **Phase 1** update immediate environments and **confirm the landed version** (fidelity ladder caveats; the explicit-package upgrade gotcha).
- **Phase 2** audit the changed surface (`references/security-documentation.md`; private disclosure for security-classified findings).
- **Phase 3** functionality: unattended CLI battery / browser-driven editor+a11y scenarios (batched) / load+real-hosting.
- **Phase 4** regressions at the **top** of the summary; bank results in the same session (per-milestone results columns, run log, status notes).

## 4 · Honor the milestone triggers
Weekly betas: expect churn. **RC1:** reconcile the whole coverage map; feature freeze. **RC2:** bugfix only — confirm nothing documented got reverted. **GA:** final link swap; verify every claim against the shipped build. Standing re-checks each pass: does the feature actually engage on this tier or silently fall back? compatibility surfaces? integrity baseline still matches? previously-reported findings still present?

## 5 · Emit the release-test report (`templates/release-test-report.md`) and its definition of done
Include the definition of done and report against it: per drop — every P0 spec × all variations × every applicable immediate environment; P1 in ≥2; P2 exploratory in 1; every security surface audited and reconciled; deferred environments when the build propagates. The cycle ends at the last RC with a **go/no-go readiness summary**. A loop without an explicit stop condition ends when someone tires or never — "looks done" is not a stop condition.

## 6 · Compatibility claims and external PRs
Treat "Tested up to X" as a runtime claim (real-install suite, scoped source diff, per-finding probe, stated evidence ceiling). For contributor PRs during a cycle: approve held CI before judging (no red X ≠ green check); probe disputed contracts on both branches; make every new guard fail once against pre-fix code; separate diagnosis from implementation; credit the contributor in everything that ships (`references/beta-rc-testing.md`).

---
*Provenance: release-testing loop, sweep, and coverage discipline from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

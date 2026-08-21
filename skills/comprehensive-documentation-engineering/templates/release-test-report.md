# Release-test report — <product> <version>

**Tester:** _____ · **Date:** _____ · **Builds covered:** _____
**Confidentiality:** _(banner — e.g. "Public references only; any security-classified finding disclosed privately and withheld here.")_

## 1 · Context
Goal of this pass · what happened mid-cycle that shaped it · upgrade origins exercised.

## 2 · Regressions (top of the report)
> Anything changed versus the prior milestone goes first.

## 3 · Findings
Per finding: **mechanism → evidence → fix**, plus a sources line (dev note/announcement, issue/PR, tracker ticket). Marker per claim (`observed`/`reproduced`/…). Security-classified findings: bare acknowledgment only (see `templates/audit-handoff.md`).

## 4 · Stack facts (verified)
Builds, change surface (commits/files per repo), upgrade origins, real-hosting reference.

## 5 · Tested and cleared (non-issues — don't re-chase)
> Explicit negative results with what was examined and why it's clear.

## 6 · Not covered (honest gaps)
> Multisite, non-default configs, performance, i18n/RTL, unchanged legacy surface — whatever this pass did not exercise.

## 7 · Per-environment results

| Spec (P0/P1/P2) | Local sandbox | Containerized | Persistent local | Real hosting | Deferred staging |
|---|---|---|---|---|---|
| | | | | | |

## 8 · How this was tested
Methods in prose (change-intelligence first; source hierarchy; upgrade-path matrix; prove-by-firing on disposable local). **Prompts verbatim in code blocks** so they can be re-run. Tooling **labeled by actual use** (`used`/`available`/`staged`/`authored`) + a one-line accuracy note naming which component did the reasoning.

## 9 · Definition of done (report against it)
- [ ] Every P0 spec × all applicable variations × every applicable immediate environment
- [ ] P1 specs in ≥2 environments
- [ ] P2 exploratory in ≥1 environment
- [ ] Every security surface audited and reconciled
- [ ] Deferred environments completed (or scheduled with propagation note)

**Cycle status (at last RC):** ☐ GO ☐ NO-GO — rationale: _____

## 10 · Consolidated sources (all public)
_____

---
*Provenance: report shape and definition-of-done from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

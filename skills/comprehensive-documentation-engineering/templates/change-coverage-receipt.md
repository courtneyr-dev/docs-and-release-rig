# Change-coverage receipt

> Produced BEFORE declaring a change review complete. "We looked at everything" is an opinion; this turns it into an artifact someone else can check. A blank row is a legitimate stop — a blank row nobody noticed is a future correction.

## Completeness reconciliation checklist
- [ ] git changes reconciled with release notes
- [ ] source reconciled with the released packages
- [ ] documented deprecations reconciled with `@deprecated` annotations **and** runtime behavior
- [ ] API changes reconciled with tests
- [ ] dependency changes reconciled with lockfiles
- [ ] feature flags reconciled with shipped defaults
- [ ] internal plans reconciled with what actually shipped
- [ ] shipped changes absent from public notes — identified
- [ ] announced changes that did not ship — identified
- [ ] reverted or partially-reverted work — identified
- [ ] changes present only in generated artifacts — identified

## Receipt
| Field | Value |
|---|---|
| Baseline → target | |
| Commits / tags reviewed | |
| Releases reviewed | |
| Files changed | |
| Public APIs changed | |
| Hooks changed | |
| Routes changed | |
| Schemas changed | |
| Dependencies changed | |
| Deprecations reviewed | |
| Removals reviewed | |
| Undocumented changes found | |
| **Entries NOT fully reviewed, and why** | |

## Documentation impact
| Affected behavior | Documents evaluated | Updated | Intentionally unchanged | Evidence / marker |
|---|---|---|---|---|
| | | | | |

**Remaining uncertainty:** _____

## Gate
If any checklist box is unchecked or any receipt row is blank → review is **NOT complete**. Record the shortfall as a named untested area. "Looks done" is not a stop condition.

---
*Provenance: receipt and reconciliation checklist from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

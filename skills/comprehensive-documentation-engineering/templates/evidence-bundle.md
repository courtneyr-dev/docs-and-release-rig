# Evidence bundle — <claim / finding>

> Reproducible record for a validated claim, code sample, or finding. Every claim carries a marker; verified and unverified never mix without labels.

**Claim:** _____
**Marker:** `observed` / `reproduced` / `inferred` / `reported` / `disputed` / `unverified`  ·  **Process:** `fired` / `source-attested`
**Regime:** shipped-stable / moving-pre-release  ·  **Evidence-source rank used:** _____

## Reproduction record
| Field | Value |
|---|---|
| Environment (isolated? disposable?) | |
| Exact versions | |
| Commands run (verbatim) | |
| Expected result | |
| Actual result (normalized output) | |
| Negative control (external corpus) | |
| Role / capability control | |
| Independent verification | |
| Date | |

## For a documentation claim verified against code
| Claim / sub-claim | Status (Confirmed/Partial/Not found/Overstated) | Evidence (file:line) |
|---|---|---|

## For a code sample / procedure
| Sample / step | Ran? | Result | If skipped — why (side-effecting / unrunnable) → `unverified` |
|---|---|---|---|

## Untested areas (null-result honesty)
Configuration set actually fired: _____ · Anything outside it is **untested**, not clean: _____
Bounded-environment limitation (if any): _____

**Never imply verification that did not happen.**

---
*Provenance: fields from the evidence & validation standard in Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

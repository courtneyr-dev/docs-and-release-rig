# Documentation plan — <repo/project>

> The persistent plan file. Written at the repo root, **outside any published docs tree** (site generators must never render it). Presented for approval before any documentation is written; updated during writing; trimmed and committed at the end. On reruns it is read as established context. Sections marked *transient* are removed by the closing trim; *persistent* sections survive between runs.

## Header — *persistent*
Run date: _____ · Detected output location & format (tooling): _____ · Reference generator detected (autodoc rule applies?): _____

## Proposed documents — *persistent*
> One table per type. A type with no genuine material is NOT listed here — it goes to Not-created.

### Reference — approved scope: **_____** *(separately approvable; "document the API" is unbounded)*
| Document (path) | Need served | Source material |
|---|---|---|
| | | |

### How-to guides
| Document (path) | Need served | Source material |
|---|---|---|

### Explanation _(architecture page C4 levels, if any: System Context / Container)_
| Document (path) | Need served | Source material |
|---|---|---|

### Tutorials
| Document (path) | Need served | Source material |
|---|---|---|

## Not-created entries — *persistent*
> Each REQUIRES both fields or it cannot be approved.

| Type / diagram level | Reason (what material is missing) | Remedy (what would make it creatable) |
|---|---|---|

## Existing docs — keep/move/split annotations — *transient*
> Section granularity. Every move and every split-part names a destination type + document, or it cannot be approved.

| Existing page / section | Compass class | Action (keep/move/split) | Destination type | Destination document |
|---|---|---|---|---|

## Batched questions & answers — *persistent*
> One round, only what the repo can't answer. Not re-asked on reruns unless current evidence contradicts.

- Audiences: _____
- Top real-world goals: _____
- Decisions worth explaining: _____

## Diagram evidence notes — *transient*
| Diagram element | Evidence it traces to (manifest / dependency / API client / role) |
|---|---|

## Parking lot — *transient (must be empty at close)*
| Content | Belongs to type | Tagged for phase |
|---|---|---|

## Standing decisions — *persistent*
> Link policies, off-limits directories, scope limits. Re-verified against output before commit.

## Tutorial verification status — *persistent*
| Tutorial | verified (commands executed in a disposable copy, output captured) / unverified (reason) |
|---|---|

---
**Approval:** ☐ plan approved ☐ reference scope approved — by _____ on _____
*(Presenting the plan is not approval. Questions are not approval. Silence is not approval. "Looks fine" is not approval.)*

---
*Provenance: plan-file format and lifecycle from Peter Knego's diataxis-docs-skill (MIT workflow layer). Full attribution: `references/source-provenance.md`.*

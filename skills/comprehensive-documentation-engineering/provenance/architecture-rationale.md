# Architecture rationale

Why this skill is shaped the way it is, what lives where, and how context size is controlled without dropping capability.

## The core problem the structure solves

The mission bundles capabilities from nine sources spanning documentation strategy, authoring, auditing, IA, DX, governance, release testing, security validation, evidence management, and UI verification — roughly 180 atomic capabilities (see `capability-ledger.md`). Loading all of that into every conversation would be both unusable (the agent can't act on 180 rules at once) and wasteful (most of it is irrelevant to any single task). The design answer is **one skill, one small always-on core, and mode-scoped progressive disclosure** — the pattern the strongest source skills (peterknego, anivar, rlespinasse) each use, generalized.

## What stays in SKILL.md

SKILL.md is the only file loaded on activation, so it holds exactly what's needed to *route correctly and behave safely*, and nothing that can wait:

- **The compass** — the one tool used in almost every mode, small enough to inline.
- **A task router** (12 rows) + a short decision tree — maps any request to a mode and the minimal file set to load.
- **Mandatory safety/approval rules** — these must bind before any workflow file is opened, so they can't live in a reference that a given mode might not load. This is deliberate: the approval gate, preservation rule, and "never claim verification that didn't happen" are the highest-stakes behaviors and must be unconditionally present.
- **Evidence standards** and the **authoring quality bar** — cross-cutting; every write/verify/audit mode leans on them, so they're stated once in the core rather than duplicated per sheet.
- **Output and completion criteria** — what "done" means, so the agent doesn't stop early.
- **A reference index** — the map to on-demand loading.

SKILL.md is kept to the routing-and-guardrails altitude; it never tries to teach how to write a tutorial or run a coverage map. It stays well under the spec's ~500-line guidance while remaining complete enough to route every mode and enforce every safety rule.

## What loads progressively

- **`references/` (21 sheets)** — the deep material, loaded only when a mode needs it. The router names the one or two sheets each mode requires. Critically, the four type sheets load **one at a time**: a run writing reference never carries tutorial pedagogy in context (peterknego's discipline, adopted because it measurably reduces cross-contamination of registers). Practice-area sheets (release, security, evidence, DX, governance, IA, localization, diagrams) load only in their modes.
- **`workflows/` (9)** — step sequences, loaded when a mode is entered. They cross-reference the reference sheets and templates rather than restating them, so each workflow file stays short.
- **`templates/` (12)** — loaded only when an artifact is produced.
- **`scripts/` (7)** — invoked, not read into context; they return machine-readable results.

This keeps any single task's working set to SKILL.md + one workflow + one or two references + maybe one template — a few thousand tokens, not the whole corpus.

## Why references are one level deep, not hundreds of tiny rule files

Anivar's source ships 27 individual rule files; peterknego ships 6 consolidated sheets. Both work, but hundreds of tiny always-discoverable files create two problems: an agent tempted to load many at once (context blow-up), and rule fragmentation (the same concern split across files). This skill **consolidates by concern** — one sheet per practice area, one per document type — so a mode loads a complete, self-contained unit. Rule *granularity* is preserved inside the sheets (every atomic capability is present and individually addressable), but *file* granularity is kept coarse enough that "load the sheet for this mode" is always the right move. Anivar's 27 discrete rules survive as the enforced/quick-reference lists inside `anti-patterns.md`, the type sheets, `style-overrides.md`, `governance-and-freshness.md`, and `developer-experience.md` — nothing was dropped, only regrouped.

## Why the two heavy modes are gated in the core, not just in their workflows

Plan/generate and restructure move or mass-produce files. If the gate lived only inside those workflow files, an agent could start the work before loading them. So the gate is stated in SKILL.md's safety rules and again in the workflows — defense in depth. The explicit-invocation requirement (heavy modes never self-trigger on incidental requests) is likewise in the core, because it governs whether a workflow is entered at all.

## How the four Diátaxis types stay distinct without being mandatory

The single most important doctrinal constraint (from diataxis.fr, reinforced by sammcj and peterknego) is that the four types are kept distinct **and** never mechanically required. The structure enforces both: distinctness comes from one-at-a-time type-sheet loading plus per-type closing self-checks; non-mandatoriness comes from the anti-scaffold rule in the core, the "not created (reason + remedy)" mechanism in the plan template, and the small-project pragmatism rule. The four types are never four required sections — they're four needs to serve when the material exists.

## How release/security/evidence/UI capability rides alongside documentation writing

These are not bolted on as a separate skill; they're modes of the same skill because the mission treats them as one practice ("documentation is a testable claim about behavior, and the test is the audit"). The evidence standard in the core is the connective tissue: the same marker system and prove-by-firing discipline govern a documented API claim, a tutorial step, a release feature, a UI label, and a security finding. That shared spine is why a coverage map (release), a change-coverage receipt (change-driven), a label-diff (UI), and an evidence bundle (validation) all feel like the same skill rather than four bolt-ons.

## Provenance kept separate from operation

`provenance/` (research report, capability ledger, traceability matrix, this file) is never loaded during operation — it exists for auditability and maintenance, mirroring how peterknego keeps `docs/superpowers/` engineering history out of the shipped skill. The shipped skill is `SKILL.md` + `references/` + `workflows/` + `templates/` + `scripts/` + `tests/`; provenance rides along for humans, not for the agent's context.

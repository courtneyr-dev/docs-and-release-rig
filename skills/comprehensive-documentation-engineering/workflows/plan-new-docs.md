# Workflow: plan or generate a documentation system (gated)

For planning a new documentation system, or generating a doc set from a codebase. **Gated and phased** — enter only on explicit request for that scale of work (never from an incidental "add a note" request). Writes a plan first and stops for approval before any documentation is written.

Central tension to hold throughout: only **reference** is derivable from source; tutorials, how-to guides, and explanation are led by **user needs**, which are not in the code. So treat the repository as *evidence* of needs (examples, e2e tests, issues, changelogs, ADRs) and ask the user only for the gaps. Never derive need-led docs from code alone — that produces the named how-to failure mode (tool inventories). And never scaffold an empty type.

## Phase 0 — survey (read-only, write nothing)
1. **Clean-tree gate** (if generating into a repo): confirm git + clean working tree. If not under git, offer `git init` **plus an initial commit** (init alone leaves files untracked and still fails). If dirty, offer commit/stash. Every later change must be revertable.
2. **Prior plan:** if a plan file exists from a previous run, read it as established context; you'll update it, not start blank.
3. **Docs-tooling + autodoc detection** (`references/information-architecture.md`, `references/reference.md`): fix output format/location; generator config beats a bare `docs/`; a reference generator triggers the autodoc rule.
4. **Product-surface mapping:** entry points, public exports, CLI commands, config options, module structure.
5. **Architecture-evidence harvest** (if an architecture page is in scope): deployable units, external systems, actors — from deploy manifests, entry points, API clients, documented roles — recording where each was found (feeds C4, `references/diagrams.md`).
6. **Need-evidence harvest:** README, CHANGELOG, ADRs, design docs, `examples/`, integration/e2e tests (best source of real user goals), commit history, PR/issue titles, docstrings.
7. **Classify existing docs** section-by-section with the compass.

## Phase 1 — plan and gap confirmation → `templates/migration-plan.md`
- Write the plan at the repo root, outside any published docs tree. Per proposed document: title · user need served · source material. Annotate existing docs **keep / move / split** at section granularity, each move/split naming its destination type and document (an annotation with no destination cannot be approved).
- **Reference scope** is its own approvable item ("public API only", "top-level modules") — "document the surface" is unbounded on a large codebase.
- A type with no genuine material is **not created** — reason (what's missing) + remedy (what would make it creatable). A bare "not created" cannot be approved. No empty directories, no placeholder landing pages.
- Architecture page: name proposed C4 levels; a level without evidence is a not-created entry.
- Ask the user **one batched round** of only what the repo can't answer: audiences, top real-world goals, decisions worth explaining. Don't re-ask anything a prior plan answered unless current evidence contradicts it. **Fold the answers into the plan before presenting it.**
- **STOP for explicit approval of the plan and the scope.** Presenting is not approval; questions are not approval; silence is not approval; "looks fine" is not approval — ask again. No Phase 2 without an explicit yes on this specific plan.

## Phases 2–5 — write, one type at a time
Order: **reference → how-to → explanation → tutorial** (reference is most derivable and becomes the link target; tutorial is most expensive/fragile and needs targets to link to). For each type: load only that type's sheet (plus `diagrams.md` for the architecture page), write its pages into their own directory, apply the plan's move/split annotations **as rewrites** (a move is held to the destination type's rules, not a relocation with fact fixes), park content belonging to a not-yet-written type in the plan, and run the type's closing self-check at section granularity before closing. Tutorials are execution-verified (`references/evidence-and-validation.md`); unrunnable/side-effecting steps are marked `unverified`. Single-type runs write only the requested type and link only to types that already exist.

## Phase 6 — assemble
Landing pages as overviews (not lists); apply the ~7-item list rule; wire cross-links so every "link out" target exists (`references/information-architecture.md`). Wire the README as the front door (a short docs section, one sentence per existing type — an overview, not a mirror). Re-verify the generated pages against every standing decision recorded in the plan. Then trim and commit the plan file with the docs: remove applied annotations and the (empty) parking lot; keep per-document need/source, the audience/goal/rationale answers, approved scope, not-created reasons+remedies, and tutorial verification status. A committed plan passes the next run's clean-tree gate and is the skill's memory.

## Reruns
Read the committed plan, keep recorded answers and scope, propose only the delta, re-ask only what current evidence contradicts, and pass the same approval gate.

---
*Provenance: gated, phased workflow adapted from Peter Knego's diataxis-docs-skill (MIT workflow layer), on diataxis.fr doctrine (CC BY-SA 4.0, adapted in references/). Full attribution: `references/source-provenance.md`.*

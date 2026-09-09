---
name: comprehensive-documentation-engineering
description: "Use when the user says 'write docs', 'document this', 'docs audit', 'Diátaxis', 'restructure the docs', 'release notes', 'field guide', 'verify the docs', or 'docs strategy', or when tutorials, how-tos, reference, or explanation need writing, review, or governance. Release testing goes to wp-release-party; audit handoffs to wordpress-audit-handoff."
license: MIT (workflow and original synthesis) AND CC-BY-SA-4.0 (Diátaxis-adapted reference sheets — see LICENSE)
metadata:
  version: 1.2.0
  provenance: provenance/source-provenance summary in references/source-provenance.md
---

# Comprehensive documentation engineering

Documentation is a testable claim about behavior, and the test is the audit. This skill combines the Diátaxis framework (the four user needs and how to serve them) with documentation auditing, information architecture, developer experience, governance, release testing, UI verification, evidence discipline, and security-safe reporting — as one coherent practice.

**Working stance:** Diátaxis is a guide, not a plan. Don't wait to understand everything before acting; pick the mode below that fits the task, load only the references it names, and iterate. Never manufacture structure (no empty tutorial/how-to/reference/explanation scaffolds — a section with no genuine material gets no directory, no landing page, no placeholder).

## The compass (always available)

Classify any content — or any user situation — with two questions:

1. Does it inform **action** (practical steps, doing) or **cognition** (propositional knowledge, thinking)?
2. Does it serve **acquisition** of skill (study) or **application** of skill (work)?

| If the content… | …and serves the user's… | …then it belongs to |
|---|---|---|
| informs action | acquisition of skill | a **tutorial** |
| informs action | application of skill | a **how-to guide** |
| informs cognition | application of skill | **reference** |
| informs cognition | acquisition of skill | **explanation** |

Apply it at every scale — sentence, section, whole document; a document can pass at a distance and fail close up. Classify by the reader's **need**, never by subject matter. When you classify, report **type + confidence (high/medium/low) + evidence** (specific phrases and structural signals). If signals conflict, that's usually mixed content: flag it, don't force it. Full tool, boundary cases (troubleshooting, FAQ, README, getting-started, migration), and blur diagnostics: `references/compass-and-classification.md`.

## Task router

Pick the row that matches the request; load the listed files; follow the listed workflow. Load nothing else until needed.

| The user wants… | Mode | Load |
|---|---|---|
| To figure out what kind of doc/work is needed | **Triage** | `references/compass-and-classification.md` (then route again) |
| An assessment of existing docs | **Audit** | `workflows/audit-existing-docs.md` + compass + `references/documentation-audits.md` |
| A documentation system planned/generated for a codebase | **Plan/generate** (gated) | `workflows/plan-new-docs.md` |
| One document written or improved | **Write/revise** | `workflows/write-or-revise.md` + the one relevant type sheet (`references/tutorials.md` \| `how-to-guides.md` \| `reference.md` \| `explanation.md`; other types: `references/content-types.md`) |
| Docs reorganized/moved/split | **Restructure** (gated) | `workflows/restructure-docs.md` |
| Docs updated for a code/product change | **Change-driven** | `workflows/document-a-change.md` |
| Claims, code samples, or procedures checked against reality | **Validate** | `workflows/validate-claims.md` + `references/evidence-and-validation.md` |
| Doc wording checked against the actual interface | **UI verify** | `workflows/verify-ui.md` |
| Release (beta/RC/GA) tested and documented | **Release** | `workflows/test-release.md` + `references/release-documentation.md` + `references/beta-rc-testing.md` |
| Audit/testing results packaged for someone else | **Handoff** | `workflows/security-audit-handoff.md` + `templates/audit-handoff.md` |
| Strategy: IA, DX, governance, style, localization, diagrams | **Advise** | the matching reference file (see index below) |
| Repo mechanics around docs work: committing changes, a failing CI run, pinning workflow actions, branch overview, diagram export, non-English content | **Repo workflow** | `references/repo-workflow-practices.md` |
| Docs for a named docs site or docs repo with its own frontmatter, components, navigation, or redirects | **Site profile** (then route again) | `references/site-profiles.md` + `templates/site-profile.md`, loaded before the mode's own files |

**Decision tree for ambiguous requests:** existing docs mentioned → Audit first (inventory before judging). A specific goal + a specific document → Write/revise. "Everything"/"the whole doc set"/"generate docs" → Plan/generate. A diff, PR, or release mentioned → Change-driven or Release. "Is this true / does this work" → Validate. When still unsure, ask which outcome they need — assessed, planned, written, moved, synchronized, verified, or reported.

**Mode gating:** the Plan/generate and Restructure modes move or mass-produce files. Enter them only when the user explicitly asks for that scale of work — an incidental request ("add a note to the README") never launches a multi-phase workflow. Generation policy: before writing any document, its target type is either stated by the user or classified by you and confirmed. Refusing to blend types — recommending a split instead — is a valid, successful outcome.

## Mandatory safety and approval rules

These bind every mode. Violating the letter is violating the spirit.

1. **Read-only before write.** Survey/audit phases write nothing. Proposals are presented before implementation.
2. **Explicit approval gates.** Broad restructuring, moves, deletions, mass rewrites, and generation runs proceed only after the user explicitly approves the specific plan **and its scope**. Presenting a plan is not approval. Questions are not approval. Silence is not approval. "Looks fine" that doesn't address plan and scope is not approval — ask again. Scope ("public API only", "just `docs/`") is its own approvable item.
3. **Preserve content.** Misplaced content is moved, never deleted. Never silently delete anything. After a move, **verify** preservation (diff or inventory comparison) — never claim it.
4. **Revertability.** Repo-modifying runs require a clean git tree (offer `git init` *plus an initial commit*, or commit/stash, before proceeding). Prefer incremental, single-section, reversible steps over big-bang changes.
5. **Link integrity.** Before moving anything, find inbound links and navigation config; update or redirect them; verify nothing broke.
6. **Respect the repo.** Existing conventions, tooling, style guides, prior user decisions, and prior deliberate reclassifications (check git history) win unless the user says otherwise. If the user rejects a suggestion, accept and adjust.
7. **Don't force the framework.** A small project with one good README may be done. Suggest the smallest useful improvement, not a scheme.
8. **Report honestly.** State assumptions, uncertainty, and gaps. **Never claim a verification, test, or scrub that did not occur** — not under time pressure, not "because it obviously works", not on request.

## Evidence standards

Every technical claim you write or evaluate gets an evidence posture:

- **Marker per claim:** `observed` · `reproduced` · `inferred` · `reported` · `disputed` · `unverified`. Verified and unverified claims never mix without labels. Lack of evidence is never evidence of absence.
- **Prove by firing.** A claim is a claim until something runs. Prefer executing the command, sample, or procedure (in a disposable sandbox; never with external side effects — mark those steps `unverified` instead) over re-reading reasoning. Capture real output; normalize paths/timestamps before presenting it as expected output.
- **Source regimes.** Shipped, stable target → code, tests, schemas, and runtime behavior outrank prose. Moving pre-release target → runtime test > official dev note > the diff > community roundups (discovery only) > memory; reading implementation code ranks *below* a published dev note. Details, gate ladder, and controls: `references/evidence-and-validation.md`.
- **No third door.** Don't declare something fine on reasoning alone, and don't dismiss claim B because it resembles disproven claim A.
- **A screenshot is not runtime proof** — it is evidence of appearance (and a free label audit).

## Default workflow (when no mode obviously fits)

The Diátaxis improvement loop: **choose** something small (the page in front of you is fine) → **assess** it (what user need? how well served? right type, tone, and language? anything belonging elsewhere?) → **decide** one action that improves it now → **do it** and treat it as complete → repeat. Structure emerges from the inside; don't work on the big picture.

## Authoring quality bar (all writing modes)

One primary need per document · outcomes before features (name docs for what the reader achieves) · show, don't tell (every concept gets a concrete example) · active voice, second person, present tense where natural · one term per concept, matched to the product's own labels · globally readable (no idioms; acronyms spelled out on first use; inclusive language) · scannable sentence-case headings and short functional sections · accurate prerequisites, next steps, and related links (no dead ends) · code samples complete, runnable, realistic, and tested where tools permit · accessible text and visuals · ≤2–3 admonitions per page · tone matches the type · no template padding — drop sections that don't apply, and never manufacture types the user's needs don't justify. Default voice is Diátaxis per-quadrant style; organization overlays (Google, Microsoft, Stripe, Canonical, Minimal) are explicit opt-ins: `references/style-overrides.md`.

## Output expectations

- **Audits** produce: inventory → classification matrix (with confidence + evidence) → gap analysis (needs × content types × adoption funnel) → maturity assessment → prioritized recommendations. Never a verdict before the inventory exists.
- **Plans** produce a persistent plan file (`templates/migration-plan.md` format): per-document need/source rows, keep/move/split annotations with destinations, scope statement, not-created entries with reason + remedy, batched questions and answers.
- **Change reviews** produce a change-coverage receipt; blank rows mean *not done*.
- **Validation** produces per-claim verdicts with markers and reproduction records; **release testing** produces the report in `templates/release-test-report.md` with a definition of done; **UI passes** produce a label-diff report; **handoffs** follow the required section order with honest gaps and accuracy labels (`used`/`available`/`staged`/`authored`).

## Completion criteria

A task in this skill is done when: the mode's output artifact exists and is filled in (no silent blanks); every claim carries its marker; approvals were obtained where required; preservation and links were verified after any move; verified/unverified separation is intact; gaps and untested areas are written down as such; and the user knows what was *not* covered.

## Reference index (load on demand)

Foundations & doctrine: `diataxis-foundations.md` · `compass-and-classification.md` · type sheets `tutorials.md`, `how-to-guides.md`, `reference.md`, `explanation.md` · `anti-patterns.md`
Architecture & content: `information-architecture.md` · `content-types.md` · `style-overrides.md` · `diagrams.md` · `site-profiles.md`
Practice areas: `documentation-audits.md` · `developer-experience.md` · `governance-and-freshness.md` · `release-documentation.md` · `beta-rc-testing.md` · `evidence-and-validation.md` · `ui-verification.md` · `security-documentation.md` · `accessibility-and-localization.md` · `repo-workflow-practices.md`
Provenance & licensing: `source-provenance.md`

Templates live in `templates/` (including `doc-review-checklist.md`, run before any single doc ships), deterministic tooling in `scripts/` (all safe/dry-run by default; heuristic outputs are candidates for review, never verdicts), and the skill's own test suite in `tests/`.

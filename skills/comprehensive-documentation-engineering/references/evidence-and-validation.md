> Synthesized from Courtney Robertson's docs-and-release-rig (CC0 — evidence ladder, 20-step loop, guardrails, safe-proof) and rlespinasse/agent-skills verify-readme-features (MIT — claim-status taxonomy) and Peter Knego's diataxis-docs-skill (CC BY-SA 4.0 layer — execution verification). 2026-08-20. Applies to any claim about behavior — a security finding *or* a documentation claim.

# Evidence and validation

The bar a claim clears before it is written down as true. Without an explicit ladder, "we tested it" and "it seemed fine" look identical in a report.

## Claim markers (label every claim)

`observed` · `reproduced` · `inferred` · `reported` · `disputed` · `unverified`. For validation processes specifically, also label `fired` (a harness genuinely executed it) vs `source-attested` (a reviewer worked a checklist) — **never imply a harness where there is only a checklist**; that's the easiest way for a report to become dishonest without anyone lying. Verified and unverified claims never mix without labels. **Lack of evidence is never evidence of absence.**

## The evidence hierarchy — two regimes

- **Shipped / stable target:** code, tests, schemas, product behavior, release artifacts, and authoritative maintainer sources outrank assumptions. Verify each claim against source (note file:line while drafting), then confirm by execution.
- **Moving / pre-release target:** runtime test on the current build > official dev note > the diff > community roundup (discovery only) > memory; reading implementation code ranks *below* a dev note (see `release-documentation.md`).

State which regime applies. When in the moving regime, a dev note landing supersedes anything you inferred from code before it.

## Prove by firing

A finding is a claim until something runs. Prefer re-deriving by execution — run the test, fire the case, reproduce the bug — over re-reading the reasoning. Opinions (human or model) set priority, never truth. And say when you're guessing: if the reason for dismissing something is "bounded", "harmless", "shouldn't reach", or "probably fine", that's an inference about runtime from source — test it instead.

- A **static observation** is not a finding.
- A **dynamic anomaly** is not automatically exploitable/impactful.
- A **screenshot is not runtime proof** (it's evidence of appearance).
- A **generated payload/output** is not evidence until reproduced and understood.

## No third door

Nothing is "not a problem" on reasoning alone — refuting a claim requires *fired-and-blocked* evidence, not an argument. **Consensus is not truth:** agreement between reviewers *deprioritizes* firing; disagreement *escalates* it; only firing writes a verdict. Never dismiss claim B because it resembles disproven claim A — test B.

## The gate ladder

A model, tool, or person may *propose* a transition; **evidence** justifies it.

| Status | Evidence to enter |
|---|---|
| idea | a named surface + a guessed weakness |
| hypothesis | a falsifiable statement (source, sink, broken invariant, required access/config) + one supporting and one disproving test |
| suspicious path | a source trace showing the invariant *can* break; no runtime evidence yet |
| verified primitive | dynamic reproduction of control over the effect, **with a passing negative control** and a role/capability control |
| verified issue | the primitive crosses a real boundary in a supported configuration, and an **independent verifier** (working from claim + evidence, not the narrative) reproduced it |
| chain candidate | ≥2 primitives linked on paper, ≥1 edge lacking runtime proof |
| verified chain | every edge has source, runtime, and test evidence end to end |
| remediated | fix present, failing-first regression test now passes, suite green on the shipped tree |
| regression protected | test in CI, asserts absence of side effects, covers the version matrix |

## The 20-step validation loop

Track state for each: 1 source · 2 sink/effect · 3 broken invariant · 4 required access · 5 required config · 6 exact supported versions · 7 execution path · 8 instrumentation · 9 smallest safe test · 10 expected result · 11 run in an isolated environment · 12 actual result · 13 **negative control** · 14 **role/capability control** · 15 a normal valid request · 16 patched/safe behavior · 17 repeat in a clean environment · 18 version-difference test · 19 **an independent agent tries to disprove it** · 20 store regression evidence.

## Controls and closure

- **Controls every run.** Fire known-good and known-bad fixtures first; a miscalibrated run is aborted and its findings discarded. Fixtures come from a **pre-registered, human-curated external corpus** — a self-authored negative control can't promote a finding on its own (a reviewer who misunderstands a mechanism writes a control that passes for the wrong reason).
- **Null-result rule (closing a surface without infinite testing).** A surface closes as *no finding* only when **both**: every input path traces in source to a correct control, **and** the bounded, enumerated set of supported configurations was fired with controls and none crossed a boundary. Record the exact configuration set fired; anything outside it is an **untested area**, recorded as such — not a clean bill of health.
- **Bounded-environment escape hatch.** What only reproduces under an unrecreatable production-like config is reported as a *hypothesis with a stated environmental limitation* — neither forced into a firing nor reasoned away. The one sanctioned exit from "no third door".
- **Record** commands, environments, dates, versions, and outcomes for every run; measured numbers carry a dated archived run record or are omitted. Produce reproducible evidence bundles (`templates/evidence-bundle.md`).

## Verifying documentation claims specifically

**A declared field is not a consumed field.** Schemas, type definitions, and frontmatter templates declare what *may* be set; only the code that reads a field proves it does anything. Before documenting a metadata field, option, or flag as controlling behavior, find the reader (grep the build, the theme, the handler) and cite it; until then the effect is `inferred` at best. Worked instance: a docs site whose page type declares an `innav` boolean while navigation is assembled from separate TypeScript files that never read it — documenting `innav` as "controls navigation" would be false (recorded in jazzsequence's pantheon-docs-writer maintenance notes, MIT; the same trap as a feature flag that exists but never engages).

**Feature-claim verification** (does the doc match the code?): extract every claim, including sub-claims ("X with A, B, and C" is four claims) → identify implementation keywords → search and **read** the code (don't trust file names) → classify each **Confirmed / Partial / Not found / Overstated** with file:line evidence → propose doc edits or flag implementation gaps → never auto-edit. Evidence order: source code > tests > config schemas > CSS/styles (for UI claims) > type definitions. **Docs never count as evidence for themselves.** For "configurable X", check both the config option and the code that reads it; for third-party claims, check the dependency is declared and used; for a11y/responsive claims, check ARIA attributes/breakpoints, not just the presence of a CSS file.

**Code-sample and procedure execution** (does the documented thing work?): extract code blocks / documented steps → run the runnable ones in a **disposable sandbox** (`git worktree`/temp clone), never the user's working tree → **never run commands with external side effects** (deploys, pushes, publishes, real-DB migrations, remote/credentialed calls) — mark those `unverified` → capture real output, normalize paths/timestamps/hostnames before presenting as expected output → if execution is impossible, mark the whole procedure `unverified`. **Never imply verification that did not happen** — an honest caveat is recoverable; a false promise is not. Wire runnable samples into CI where the repo allows. `scripts/verify_examples.py` extracts blocks and reports per-sample pass/fail/skipped-with-reason.

## Safe-proof standard (when proving a finding)

Prove **only** what's needed — reachability, control, required privilege, boundary violation, affected versions, practical impact, remediation, regression need — then stop. Prefer the least harmful proof: inert markers, synthetic sentinels, disposable records/directories, bounded rate-limited local measurement. Never add persistence, stealth, destruction, credential theft, public-target compatibility, shells, C2, or post-compromise steps. Destructive proofs run only on disposable local installs, never live sites.

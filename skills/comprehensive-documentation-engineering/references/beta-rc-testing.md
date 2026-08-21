> Synthesized from Courtney Robertson's docs-and-release-rig (CC0 — beta/RC runbook, environment fidelity, public tooling, external-PR audit). 2026-08-20. Generalized from a WordPress release cycle; the *methods* transfer to any release train with periodic drops.

# Beta / RC / release-candidate testing

Goal: thorough on functionality and security with the least human babysitting. Everything that can run unattended, runs unattended. `workflows/test-release.md` drives it; `templates/release-test-report.md` records it.

## Environments grouped by *when* they can be tested

The organizing insight: test environments do not all become testable at the same moment, and pretending otherwise makes release testing feel chaotic. Group by update timing, not importance.

**Immediate — testable the moment the release drops:**
1. Local disposable (in-browser sandbox, containerized at multiple runtime versions, persistent local app) — updates instantly, no human action.
2. Self-managed hosts with shell access — update on demand, no human action.
3. Managed hosting, production tier — updates when the platform propagates, or forced via CLI where allowed — one human connection per session.

**Deferred — always tested later:**
4. Managed hosting, staging tier — the platform takes time to surface a new build; test on its own schedule when it actually shows the release. The propagation delay is itself a finding worth documenting for site owners — a feature of the method, not a failure.

## The environment-fidelity ladder

Browser sandbox → containerized → persistent local → real hosting. Each rung has caveats that can silently produce **confidently wrong documentation**:
- Lower-fidelity environments substitute components (e.g. SQLite for the real database — can't model collation/charset/query specifics) and can **lag the release channel**, silently serving an older build.
- Some sandboxes block automation of complex editors (nested iframes).
- **Always confirm the version you actually landed on** (`⟨tool⟩ core version`-style check) — verifying a claim in an environment a version behind documents the old behavior with total confidence.
- Know the explicit-package upgrade gotcha class: a bare version flag can resolve to the latest *stable* offer instead of the beta, so the site never lands on the target unless you force the explicit release package URL. Reaching a beta from a stable install requires the explicit package.

## The four-phase per-drop loop

**Phase 0 — re-anchor (~10 min).** Sweep the drop's dev-note tag, the announcement, and the core/test channels for what changed. **Re-point every test spec at the current dev notes before any testing.** This is why the docs stay accurate: specs anchor to sources first, not after.

**Phase 1 — update immediate environments** and **confirm the landed version** (never assume an auto-updater landed where you think).

**Phase 2 — audit the changed surface** (see security, below).

**Phase 3 — functionality**, split by reach:
- *Unattended CLI battery, every immediate environment:* install/upgrade integrity, checksum verification, health checks, content CRUD across types, the media/asset pipeline, new-component markup validity and front-end asset loading, revisions, real-database integrity (charset/collation), scheduled tasks, routing/sitemap/robots against a real server.
- *Browser-driven, against real URLs:* editor scenarios a CLI can't reach — composer UIs, modals, interactive states, keyboard/screen-reader paths for new components, command palettes — plus a compatibility sweep needing the editor to load. Heavier — batch these.
- *Load and real hosting:* media at scale, batch operations under real resource limits, front-end rendering through a real cache.

**Phase 4 — regressions and banking.** Anything changed versus the prior milestone goes at the **top** of the session summary. Update every spec's results table (a column per milestone), the run log, and status notes **in the same session, while it's still true**.

## Definition of done

Write it down — a loop without an explicit stop condition ends when someone tires or never ends; "looks done" is not a stop condition. Per drop: every P0 spec run with all applicable variations in every applicable immediate environment; P1 specs in ≥2 environments; P2 exploratory in 1; every security surface audited and reconciled; deferred environments completed when the build propagates. Per cycle: ends at the last RC with a go/no-go readiness summary. The definition is deterministic — hand it to someone else and they can tell whether the pass is finished without asking you.

## Security audit of the changed surface

Change-intelligence first: diff the prior stable tag against the build, read the dev notes, monitor the issue channels — producing a ranked list of *changed* attack-surface families so the audit targets what moved. Optionally fan the diff to an independent multi-model panel (disagreement is signal; adversarial verification defaults to refute; compare against prior stable to confirm novelty). Security-classified findings route through **private** coordinated disclosure, never public trackers. Full discipline in `security-documentation.md` and `evidence-and-validation.md`.

## Public / community testing tooling

Lower the barrier to community testing: a pre-configured environment **blueprint** (a configured build in two clicks) removes setup cost; an interactive **checklist** removes not-knowing-what-to-check. A test tool's README **documents its own limitations** — what browser automation can't cover (genuinely simultaneous multi-user scenarios, custom server-side components, subjective UI assessment, server-side checks, accessibility, cross-browser) — so a manual exploratory layer is retained deliberately, not assumed covered. Record cycle-timing trade-offs (e.g. "fork the suite this cycle, generalize after") with rationale so the decision doesn't look accidental later.

## External-PR audit discipline

- **No red X is not a green check.** First-contributor CI is held (`action_required`) until a maintainer approves — a clean-looking checks area may have run *nothing*. Approve the held runs first; treat CI as one input, not the verdict.
- **A green suite only covers what someone thought to pin.** A full suite can pass on a real regression. Probe the disputed contract directly on both branches (pre- and post-change).
- **Make every new guard fail once on purpose.** Run each new regression test against the pre-fix code (check the old file into the test branch) so it fails before you trust it — a guard never watched failing is a decoration. Then restore and confirm green.
- **Separate diagnosis from implementation.** External contributors' *diagnosis* is often right while the *mechanism* is booby-trapped by undocumented core behavior; fix the mechanism, keep their diagnosis and their commits.
- **Credit is part of the merge.** Contributor commits stay intact; the changelog carries props by name; contributor attribution lands in the distribution listing. The audit protects the codebase; the credit protects why people send patches.

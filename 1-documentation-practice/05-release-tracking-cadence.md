# Release-tracking cadence — staying current on a moving release

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/release-documentation.md`](../skills/comprehensive-documentation-engineering/references/release-documentation.md) · [`references/evidence-and-validation.md`](../skills/comprehensive-documentation-engineering/references/evidence-and-validation.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


**Date:** July 24, 2026 · **Cycle:** WordPress 7.1 (Beta 1 July 15 → GA August 19)

The core lesson, stated plainly: **during an active beta → RC → GA cycle, our knowledge
decays in about 48 hours. Re-sweep authoritative sources at the start of every working
session, before editing any deliverable.**

That number is not a guess. Below is the retro that produced it.

---

## Retro — what went stale in two days (July 22 → 24)

By July 24, two things written on July 22 were wrong:

1. **Feature gating.** We had documented client-side media processing as gated on
   `is_ssl()`. The [dev note](https://make.wordpress.org/core/2026/07/22/client-side-media-processing-in-wordpress-7-1/)
   published July 22 says the real gate is a Chromium version floor, a
   `Document-Isolation-Policy` response header on editor screens, a CSP allowing
   `worker-src blob:`, and runtime checks on available memory, core count, and
   data-saver mode. Browsers outside that set fall back to server-side processing
   silently.
2. **A dependency upgrade we assumed had shipped.** We had written that React 19 landed
   in 7.1. It was [punted](https://make.wordpress.org/core/2026/07/24/react-19-punted-beyond-wordpress-7-1-experiment-in-gutenberg/);
   7.1 stays on React 18.3 and React 19 remains an opt-in experiment in the plugin.

Both errors came from the same root cause: **we had read the beta source code.** Reading
implementation is a legitimate research method, but what it produces is a *hypothesis*
about intended behavior, not documentation-grade truth. Code can be mid-refactor,
feature-flagged, or about to be reverted.

Two more lessons from the same window:

- **Attribute paths move between versions.** A screenshot took three attempts because
  the new support lives at `style.background.gradient`, not the older
  `style.color.gradient`. Build examples with the *current* attribute names, verified
  against the dev note or the block's own `block.json` — never from memory of the last
  release.
- **Environment fidelity is a documentation risk.** WordPress Playground lagged the beta
  channel, serving an older beta while real staging ran a newer one. If you verify a
  claim in an environment that is silently a version behind, you will document the old
  behavior with total confidence. Check what version you are actually looking at.

---

## The source hierarchy

This is the single most useful artifact in this file. When two sources conflict, the
higher one wins — no debate, no averaging:

1. **Our own runtime test on the current build.** Highest authority. It is the only
   source that describes what the software *does* rather than what someone believes it
   does.
2. **The dev note or field guide** on the project's official developer blog.
3. **The diff** — the actual commit range in the core and feature-plugin repositories.
4. **The community "source of truth" roundup.** Useful for discovering items you missed;
   never a citation, and never copy its phrasing.
5. **Our memory and older notes.** Lowest. Treat as a lead, not a fact.

Note where reading the beta source code sits: **below a dev note**. When a dev note
lands, go back and re-check everything you inferred from code before the note existed.
That single rule would have caught both of the July 22 errors.

---

## The daily sweep

Run this each working session during a release, **before** touching any deliverable:

1. **Sweep the last 24–48 hours** — the project's core blog and dev-note tag, the test
   team's blog, the release milestone in the issue tracker, the compare views for the
   core and feature-plugin repositories, and the relevant chat channels. Note anything
   dated since the last sweep.
2. **Diff the sweep against our docs.** Does anything new contradict, add to, or make
   public something currently written down?
3. **Correct, and date the delta.** For anything already shared with other people, log a
   dated update note that states explicitly what changed since the last shared version.
   Readers need the delta, not a silently-edited document.
4. **Re-verify changed features** on a current build where testable. Do not promote a
   reading of code or a dev note to "confirmed" without a runtime check.
5. **Swap draft links for public ones** as dev notes and the field guide publish.

## Milestone triggers — expect churn at each

- **Weekly betas:** features still get added, fixed, and punted. A large number of
  tickets remain milestoned late into the cycle.
- **RC1:** the field guide and dev notes finalize. Reconcile the entire coverage map
  here. The feature set should freeze at this point.
- **RC2:** bug fixes only. Confirm nothing previously documented got reverted.
- **GA:** final link swap; verify every claim against the shipped build.

## Standing re-checks, every pass

- Does the feature under test actually engage on this tier, or is it silently falling
  back? A silent fallback means the documented benefit does not exist for that reader.
- Plugin-compatibility surfaces: removed components and newly-unconditional behavior.
- Does the integrity/checksum baseline still match the new build?
- Are previously-reported findings still present in the latest build?

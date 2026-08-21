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

## The method this retro produced

The retro above earned three artifacts that are now canonical in the skill — read them
there, not here, so there's one copy to keep current:

- **The source hierarchy** (runtime test on the current build > official dev note > the
  diff > community roundup > memory; and crucially, *reading implementation code ranks
  below a published dev note* — the exact trap that made both July 22 errors) →
  [`references/release-documentation.md`](../skills/comprehensive-documentation-engineering/references/release-documentation.md)
  and the evidence regimes in [`references/evidence-and-validation.md`](../skills/comprehensive-documentation-engineering/references/evidence-and-validation.md).
- **The daily sweep** (sweep 24–48h of authoritative sources → diff against the docs →
  correct and *date the delta* → re-verify on a current build → swap draft links) →
  the re-anchor phase in [`workflows/test-release.md`](../skills/comprehensive-documentation-engineering/workflows/test-release.md).
- **Milestone triggers and standing re-checks** (RC1 reconcile + freeze, RC2 bugfix-only,
  GA final verify; and every pass: does the feature actually engage on this tier or
  silently fall back?) → [`references/release-documentation.md`](../skills/comprehensive-documentation-engineering/references/release-documentation.md).

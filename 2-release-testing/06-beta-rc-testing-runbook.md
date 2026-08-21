# Beta/RC testing runbook — how each release drop gets tested

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/beta-rc-testing.md`](../skills/comprehensive-documentation-engineering/references/beta-rc-testing.md) · [`workflows/test-release.md`](../skills/comprehensive-documentation-engineering/workflows/test-release.md) · [`templates/release-test-report.md`](../skills/comprehensive-documentation-engineering/templates/release-test-report.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


**Context:** written for the WordPress 7.1 cycle (Beta 3 → RC1 → RC2 → GA), and
generalizable to any release train with weekly drops.

> Generalized from production work. Hosting infrastructure, host names, and connection
> details are omitted, and platforms are described by *tier* rather than by name —
> the tier is what matters to the method.

Goal: thorough on security and functionality, with the smallest possible amount of
human babysitting. Everything that can run unattended, runs unattended.

## Environments, organized by when they can be tested

The organizing insight is that **test environments do not all become testable at the
same moment**, and pretending otherwise is what makes release testing feel chaotic.
Group them by update timing, not by importance:

**Immediate — testable the moment the release deploys**

1. **Local disposable environments** — a local-site app, containerized WordPress at
   multiple PHP versions, and WordPress Playground. Update instantly and
   automatically. No human action.
2. **Self-managed hosting with shell access** — a beta-channel plugin plus WP-CLI over
   key-based SSH. Updates on demand. No human action.
3. **Managed hosting, production tier** — updates when the platform propagates the
   build, or is forced via WP-CLI where the platform allows it. Needs a human to open
   the connection once per session.

**Deferred — always tested later**

4. **Managed hosting, staging tier** — the platform takes time to surface a new core
   version. Test it on its own schedule once it actually shows the release. This is a
   feature of the method, not a failure: staging propagation delay is itself a finding
   worth documenting for site owners.

## The method this insight drives

The deliberately-small human checklist, the four-phase automated loop (re-anchor → update
→ security audit of the changed surface → functionality, in three lanes), and the per-drop
definition of done are now canonical in the skill — one copy to keep current:
[`references/beta-rc-testing.md`](../skills/comprehensive-documentation-engineering/references/beta-rc-testing.md),
[`workflows/test-release.md`](../skills/comprehensive-documentation-engineering/workflows/test-release.md),
[`templates/release-test-report.md`](../skills/comprehensive-documentation-engineering/templates/release-test-report.md).
The one phase worth naming here, because it's what keeps the docs accurate: **Phase 0
re-anchors every test spec to the current dev notes *before* any testing happens, not
after.**

## Why the definition of done is written down

A release-testing loop without an explicit stop condition either ends early because
someone got tired, or never ends. "Looks done" is not a stop condition. The per-drop
definition of done — now in the skill — is deterministic: you can hand it to someone
else and they can tell you whether the pass is finished without asking you.

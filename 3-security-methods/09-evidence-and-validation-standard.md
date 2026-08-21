# Evidence & validation standard

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/evidence-and-validation.md`](../skills/comprehensive-documentation-engineering/references/evidence-and-validation.md) · [`templates/evidence-bundle.md`](../skills/comprehensive-documentation-engineering/templates/evidence-bundle.md) · [`templates/security-finding.md`](../skills/comprehensive-documentation-engineering/templates/security-finding.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


The bar a claim has to clear before it gets written down as true. This is the piece
that makes the rest of the process trustworthy: without an explicit evidence ladder,
"we tested it" and "it seemed fine" look identical in a report.

Written for security findings, but the ladder and the controls apply to any claim about
behavior — including a documentation claim.

## What this standard became

Every piece of this standard is now canonical, executable, and testable in the skill —
kept there as one copy so it can't drift from a second:

- **The gate ladder** (idea → hypothesis → suspicious path → verified primitive → verified
  issue → chain candidate → verified chain → remediated → regression protected) and the
  **20-step validation loop** → [`references/evidence-and-validation.md`](../skills/comprehensive-documentation-engineering/references/evidence-and-validation.md).
- **The guardrails that do the work** — prove-by-firing, no-third-door, controls-every-run
  from an external corpus, consensus-is-not-truth, a screenshot-is-not-runtime-proof,
  fired-vs-source-attested labelling, the null-result rule, and the bounded-environment
  escape hatch → same reference.
- **The safe-proof standard** (least-harmful proof per finding class; stop at the boundary)
  and the **reporting field order** → same reference.
- **The reusable templates** (hypothesis, blocked route, disproved hypothesis, finding,
  regression test) → [`templates/evidence-bundle.md`](../skills/comprehensive-documentation-engineering/templates/evidence-bundle.md)
  and [`templates/security-finding.md`](../skills/comprehensive-documentation-engineering/templates/security-finding.md).

The skill also generalizes the ladder past security to any documentation claim, via the
per-claim evidence markers (`observed` · `reproduced` · `inferred` · `reported` ·
`disputed` · `unverified`) in its `SKILL.md`.

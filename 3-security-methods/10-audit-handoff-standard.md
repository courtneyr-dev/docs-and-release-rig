# Audit handoff standard

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`workflows/security-audit-handoff.md`](../skills/comprehensive-documentation-engineering/workflows/security-audit-handoff.md) · [`references/security-documentation.md`](../skills/comprehensive-documentation-engineering/references/security-documentation.md) · [`templates/audit-handoff.md`](../skills/comprehensive-documentation-engineering/templates/audit-handoff.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


My standard for packaging audit or testing results for another human. It is written as
an executable specification — I keep it as an agent skill so the format is enforced
rather than remembered.

**This package was produced under this standard.** If you want to check the process, the
easiest audit is to verify that every link in every file here resolves for you as a
logged-out visitor.

## What this standard became

The standard is now enforced by the skill's handoff mode rather than remembered — one copy
to keep current:

- **Output rules** (one self-contained file, public links only, verify each repo link
  resolves logged-out before including it, a confidentiality banner, re-verify findings
  live) and the **required section order** (intro/context → findings as mechanism → evidence
  → fix → stack facts → tested-and-cleared → honest gaps → how-tested with verbatim prompts
  → consolidated sources) → [`workflows/security-audit-handoff.md`](../skills/comprehensive-documentation-engineering/workflows/security-audit-handoff.md)
  and [`templates/audit-handoff.md`](../skills/comprehensive-documentation-engineering/templates/audit-handoff.md).
- **The two rules easiest to get wrong** — reduce a privately-disclosed finding to a bare
  acknowledgment and *grep the finished file to prove zero traces remain*, and label every
  tool/skill/method by actual use (`used` · `staged` · `available` · `authored`) with an
  accuracy note naming which component did the reasoning → [`references/security-documentation.md`](../skills/comprehensive-documentation-engineering/references/security-documentation.md).

# Audit handoff standard

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`workflows/security-audit-handoff.md`](../skills/comprehensive-documentation-engineering/workflows/security-audit-handoff.md) · [`references/security-documentation.md`](../skills/comprehensive-documentation-engineering/references/security-documentation.md) · [`templates/audit-handoff.md`](../skills/comprehensive-documentation-engineering/templates/audit-handoff.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


My standard for packaging audit or testing results for another human. It is written as
an executable specification — I keep it as an agent skill so the format is enforced
rather than remembered.

**This package was produced under this standard.** If you want to check the process, the
easiest audit is to verify that every link in every file here resolves for you as a
logged-out visitor.

---

## Output rules

- **One file, fully self-contained.** No internal wiki-links, no local filesystem paths.
  The recipient has neither my notes system nor my machine. Inline the content, or link
  a public URL. The only acceptable links are public ones.
- **Verify every repository link is public *before* including it.** Check with an
  authenticated CLI query for the private flag, or an anonymous request expecting a 200
  and not a 404. **Never link a private repository** — the recipient gets a 404 and,
  worse, silently loses the evidence you meant to show them. If a tool lives in a private
  repository, describe it by name and author instead of linking it.
- **A confidentiality banner at the top**, matched to the audience.
- **Re-verify findings live** if the target is still reachable, so the document reports
  what is currently true rather than what was true when it was logged.

## Required sections, in order

1. **Intro and context** — target, environment and stack, versions, verification date.
2. **Findings** — one per finding, each structured as **mechanism → evidence → fix**,
   plus a sources line linking every feature to its authoritative reference: the
   official dev note or announcement, the issue or pull request, and the tracker ticket.
3. **Stack facts** — verified environment details.
4. **Tested and cleared** — non-issues, explicitly, so nobody re-chases them. This
   section saves the recipient more time than the findings do.
5. **Not covered — honest gaps.**
6. **How this was tested** — methods in prose; **prompts verbatim in code blocks**, so
   the recipient can re-run them; and tooling, each item labeled by actual use.
7. **Consolidated sources** — every public link gathered in one list at the bottom.

## The two rules that are easiest to get wrong

### Confidential and privately-disclosed findings

For anything under coordinated disclosure, or any unpatched security issue: reduce it to
a **bare acknowledgment.** For example — *"a separate security issue was identified and
responsibly disclosed through a private channel; details are withheld."*

Scrub **all** traces: the mechanism, endpoint and function names, severity scoring, the
reproduction, the specific commit or pull request, and even the name of the disclosure
platform. Then **grep the finished file to prove zero traces remain** before handing it
off. Believing you scrubbed it is not the same as checking.

If it is unclear which findings are confidential, ask before packaging — not after.

### Accuracy labels

Label every tool, skill, and method by **actual use**: `used`, `staged`, or `available`.
Never imply that a tool or model did work it did not do.

This matters more than it sounds. A methods section that lists an impressive tool chain
reads as authoritative, and a reader will reasonably assume every item in that list
touched the work. If the real analysis ran through a custom harness and the packaged
tools were merely installed, say so — and add a one-line accuracy note stating plainly
which component actually performed the reasoning.

Overstating your tooling is the most common quiet dishonesty in technical reports, and
it is entirely avoidable with a three-word label per line.

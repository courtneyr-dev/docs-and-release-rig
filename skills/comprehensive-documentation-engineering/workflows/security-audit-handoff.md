# Workflow: package audit/testing results as a handoff

Turn audit, testing, or validation results into one coworker- or SRE-ready document that's useful without leaking what shouldn't ship. Reference depth: `references/security-documentation.md`; output shape: `templates/audit-handoff.md`.

## 1 · Decide confidentiality first
Classify each finding: **confirmed vulnerability · weakness · hardening opportunity · speculative risk**, and **public vs privately-disclosed**. If it's unclear which findings are confidential, **ask before packaging** — not after.

## 2 · One self-contained file
No internal wiki-links, no local filesystem paths — the recipient has neither your notes system nor your machine. Inline the content or link a **public** URL. A confidentiality banner at the top matched to the audience.

## 3 · Required section order
1. **Intro & context** — target, environment/stack, versions, verification date.
2. **Findings** — one each, **mechanism → evidence → fix**, plus a sources line linking every item to its authoritative reference (dev note/announcement, issue/PR, tracker ticket).
3. **Stack facts** — verified environment details.
4. **Tested and cleared** — non-issues, explicitly, so nobody re-chases them (this section often saves the recipient more time than the findings do).
5. **Not covered — honest gaps.**
6. **How this was tested** — methods in prose; **prompts verbatim in code blocks** so the recipient can re-run them; tooling each labeled by actual use.
7. **Consolidated sources** — every public link in one list.

## 4 · Scrub privately-disclosed findings to a bare acknowledgment
Reduce anything under coordinated disclosure (or any unpatched security issue) to: *"a separate security issue was identified and responsibly disclosed through a private channel; details are withheld."* Scrub **all** traces — mechanism, endpoint/function names, severity scores, reproduction, the specific commit/PR, even the disclosure platform's name. Then **grep the finished file to prove zero traces remain** (`scripts/scrub_check.py <file>` flags common leak patterns; a manual grep confirms). Believing you scrubbed it is not checking it.

## 5 · Verify link hygiene (before including any link)
Every link must resolve for a **logged-out** visitor. Check each with an anonymous request expecting 200 (not 404) or an authenticated CLI query for the private flag. **Never link a private repository** — the recipient gets a 404 and silently loses the evidence; describe the tool by name and author instead. Re-verify findings **live** if the target is still reachable, so the document reports what is currently true (a citation's *state* is part of its accuracy — note if a ticket reopened).

## 6 · Accuracy labels
Label every tool, skill, and model `used` / `staged` / `available` / `authored` by **actual use**; never imply a tool or model did work it didn't. If the real analysis ran through one component and others were merely installed, add a one-line accuracy note naming which component actually performed the reasoning. Omit tools you can't currently verify are installed rather than citing from memory.

## Guardrails
- Redact secrets, PII, and production infrastructure specifics (hostnames, connection config, stack fingerprints, other people's names) — keep the transferable method.
- Include remediation with every finding; note remediation-verification status (fix present, regression test passing, suite green, CI-protected).
- Refuse to produce exploit-enabling detail for an unpatched issue in a shareable doc.

---
*Provenance: handoff standard, scrubbing, and accuracy-label rules from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

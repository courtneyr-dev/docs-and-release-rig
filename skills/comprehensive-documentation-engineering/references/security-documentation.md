> Synthesized from Courtney Robertson's docs-and-release-rig (CC0 — audit handoff standard, evidence/validation, methods report). 2026-08-20. Handoff mechanics: `workflows/security-audit-handoff.md` + `templates/audit-handoff.md`; evidence discipline: `evidence-and-validation.md`.

# Security-sensitive documentation

Documenting security findings responsibly is a distinct discipline: the goal is to be useful to maintainers and defenders without leaking what shouldn't ship, overstating what you found, or implying work you didn't do.

## Responsible language and classification

Separate, explicitly, four things and never blur them: **confirmed vulnerabilities** · **weaknesses** · **hardening opportunities** · **speculative risks**. Never overstate severity or exploitability. Where evidence exists, state it plainly; where it doesn't, label the item a **hypothesis** — never "it is possible that…" as a substitute for evidence. Record scope and preconditions (attacker access, required privileges, required configuration, exact affected versions) with every finding; a finding without its preconditions overstates its reach.

## Disclosure routing

- **Security-classified findings route through private coordinated-disclosure channels** — never public issue trackers or PRs.
- **Functional/integrity findings** go public, deduplicated against existing ticket clusters first.
- Provide the private channel before it's needed: a `SECURITY.md` routing reports to a private advisory channel, at both the project and single-repo scale — give people a private channel or they'll use the public one.

## Bare-acknowledgment scrubbing

Anything under coordinated disclosure, or any unpatched security issue, is reduced in shareable output to a **bare acknowledgment**: *"a separate security issue was identified and responsibly disclosed through a private channel; details are withheld."* Scrub **all** traces — mechanism, endpoint and function names, severity scoring, reproduction, the specific commit/PR, even the name of the disclosure platform. Then **grep the finished file to prove zero traces remain** before handing it off: believing you scrubbed it is not the same as checking. If it's unclear which findings are confidential, **ask before packaging**, not after.

## Redaction beyond security

Redact secrets and sensitive personal information generally; omit infrastructure specifics that came from production work (hostnames, connection configuration, stack fingerprints, other people's names). What's left is the transferable method.

## Safe proof and remediation verification

Prove only what's needed, with the least harmful proof, and stop (full safe-proof table in `evidence-and-validation.md`); never publish exploit-enabling detail prematurely. Remediation closes a finding only when: the fix is present, the failing-first regression test now passes, the suite is green on the shipped tree, and the test lands in CI asserting absence of side effects across the version matrix (gate-ladder rungs *remediated* / *regression protected*). Always include remediation guidance with a finding.

## Multi-model adversarial panel (optional, for changed-surface audits)

Change-intelligence first (diff prior stable → current; rank changed attack-surface families). Independent models audit the same diff separately — **disagreement is signal**. Every candidate runs through an adversarial verification pass that **defaults to refute**; a finding survives only if it can't be talked down and reproduces on a disposable install. Compare against the prior stable release to confirm novelty. Publish the verbatim, reusable panel prompts in the report so a reader can re-run them.

## Accuracy labels and the honest handoff

Label every tool, skill, and model by **actual use** — `used` / `staged` / `available` / `authored` — and never imply a tool or model did work it didn't. A methods section listing an impressive tool chain reads as authoritative, and a reader reasonably assumes every item touched the work; if the real analysis ran through a custom harness and the listed tools were merely installed, say so, and add a one-line accuracy note naming which component actually performed the reasoning. Overstating tooling is the most common quiet dishonesty in technical reports and is entirely avoidable with a three-word label per line. Omit tools you can no longer verify are installed rather than citing them from memory. **Document negative results** ("checked — not an issue", with what was examined and why it's clear) — the tested-and-cleared section saves the recipient more time than the findings do, and it's the part that most often gets deleted because it feels like admitting you were wrong.

Full handoff section order, confidentiality banner, link hygiene (public links verified logged-out; never link a private repo), and live re-verification live in `workflows/security-audit-handoff.md` and `templates/audit-handoff.md`.

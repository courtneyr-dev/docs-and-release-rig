# Workflow: validate technical claims, code samples, and procedures

Verify that what the docs assert is true and that what they tell the reader to do works. Reference depth: `references/evidence-and-validation.md`.

## 1 · Extract the claims
- Every factual assertion (signatures, defaults, behaviors, "supports X", limits), including **sub-claims** — "X with A, B, and C" is four claims.
- Every code sample and every documented procedure/step sequence.

## 2 · Pick the evidence regime and source order
- **Shipped/stable target:** code > tests > schemas > product behavior > maintainer docs; docs never verify themselves. Evidence order for feature claims: source code > tests > config schemas > CSS/styles (UI) > type definitions.
- **Moving/pre-release target:** runtime test > dev note > diff > community roundup (discovery only) > memory; reading code ranks below a dev note.
State which regime applies.

## 3 · Verify feature/fact claims
Search and **read** the implementing code (don't trust file names); classify each **Confirmed / Partial / Not found / Overstated** with **file:line** evidence. For "configurable X", check both the option and the code that reads it; for third-party claims, check the dependency is declared and used; for a11y/responsive claims, check ARIA/breakpoints, not just a CSS file's existence. Run `scripts/inventory_docs.py` output or a targeted grep to find the claims; the reading is manual.

## 4 · Verify code samples and procedures by firing
- Run runnable samples/steps in a **disposable sandbox** (`git worktree`/temp clone), never the user's working tree. `scripts/verify_examples.py <file>` extracts fenced blocks and reports per-sample pass/fail/skipped-with-reason.
- **Never run commands with external side effects** (deploys, pushes, publishes, real-DB migrations, remote/credentialed calls) — mark those steps `unverified`.
- Capture real output; normalize paths/timestamps/hostnames before presenting it as expected output.
- If execution is impossible in this environment, mark the whole procedure `unverified` — never imply verification that didn't happen.

## 5 · Apply the discipline
- **Prove by firing:** a claim is a claim until something runs; opinions set priority, not truth.
- **No third door:** don't declare something fine on reasoning alone; don't dismiss claim B because it resembles disproven claim A — test B.
- For findings that need it, walk the gate ladder and the 20-step loop with external-corpus controls (`references/evidence-and-validation.md`); close surfaces only via the null-result rule; use the bounded-environment escape hatch when a config can't be safely recreated.

## 6 · Report
Per claim/sample: verdict + marker (`observed`/`reproduced`/`inferred`/`reported`/`disputed`/`unverified`; `fired` vs `source-attested`) + evidence (file:line, command, captured output). Propose doc edits or flag implementation gaps; **never auto-edit** without approval. Produce a reproducible evidence bundle (`templates/evidence-bundle.md`) recording commands, environment, dates, versions, outcomes. Keep verified and unverified strictly separated.

---
*Provenance: feature-claim method from rlespinasse/agent-skills verify-readme-features (MIT); evidence discipline from docs-and-release-rig (CC0); execution protocol from Peter Knego's diataxis-docs-skill. Full attribution: `references/source-provenance.md`.*

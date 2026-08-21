# Tests

Two layers of testing for this skill.

## 1 · Structural validation (deterministic)

```bash
python3 scripts/validate_skill.py          # frontmatter, cross-refs, attribution, eval schema
python3 tests/check_evals.py tests/evals.json
```

Both exit non-zero on failure, so they drop into CI directly.

Script smoke checks against the bundled fixtures (each has a known outcome):

```bash
python3 scripts/inventory_docs.py tests/fixtures                 # exit 0: lists the fixtures
python3 scripts/detect_mixed_docs.py tests/fixtures              # exit 0: flags mixed-doc.md (4-type signals)
python3 scripts/check_links.py tests/fixtures                    # exit 0: no broken local links
python3 scripts/verify_examples.py tests/fixtures/runnable-sample.md --run python
# ^ exit 0: the self-contained block reports 'verified'
python3 scripts/verify_examples.py tests/fixtures/clean-reference.md --run python
# ^ exit 1 by design: the illustrative reference snippet references an undefined object and reports
#   'failed' — demonstrating the tool actually executes and captures failures (it never fakes a pass)
python3 scripts/compare_ui_labels.py tests/fixtures/draft-with-wrong-labels.md tests/fixtures/observed-labels.json
# ^ exit 1 by design: flags "Responsive editing" (invented menu) and "Pressed" (the real states are
#   Default/Hover/Focus/Focus-visible/Active) — exactly the label-diff the workflow catches
python3 scripts/scrub_check.py tests/fixtures/mixed-doc.md       # exit 0: no leak patterns present
```

Exit-code convention: `0` = clean/nothing to flag, `1` = issues found (the tool worked and has something to report), `2` = bad usage. `detect_mixed_docs` and `inventory` always exit 0 because their output is informational (heuristic candidates for review), never a pass/fail verdict.

## 2 · Behavioral evaluation (`evals.json`)

`evals.json` holds scenario evals covering the behaviors this skill must exhibit — activation and non-activation, classification (incl. compass, boundary cases, mixed docs), the writing/audit/plan/restructure/change/validate/UI/release/handoff workflows, evidence and security restraint, governance/DX/style/localization/diagrams advice, and adversarial cases (resisting false-verification, approval-skip, and unverified-preservation requests).

Each eval carries `id`, `category`, `prompt`, `expected_output`, `assertions[]`, and `files[]`. They are model-run: feed the `files[]` as context and the `prompt` as the task, then judge the response against the `assertions`. This mirrors the promptfoo + `claude -p` harness the schema is drawn from (≈2 model calls per eval). The evals are the RED/GREEN record for the skill — a change to a rule should be paired with a scenario that fails without it and passes with it.

**What to test is behavior, not mention.** An eval passes only when the agent *does* the thing (inventories before judging, holds the gate, marks a step unverified), not merely when it recites the rule.

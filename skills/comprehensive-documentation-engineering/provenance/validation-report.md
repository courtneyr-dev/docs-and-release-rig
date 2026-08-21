# Validation report

All commands run 2026-08-20 from the skill root, Python 3 standard library only, no network access.

## Structural validation

```
$ python3 scripts/validate_skill.py
✓ skill package structurally valid                     (exit 0)
```
Checks performed: SKILL.md frontmatter (`name` kebab-case ≤64 and matching, `description` present ≤1024, "Use when" phrasing); every `references/`, `workflows/`, `templates/`, `scripts/` path referenced by SKILL.md and by each workflow exists; the ten Diátaxis-adapted reference sheets each carry a CC BY-SA attribution header; `tests/evals.json` passes schema validation.

One issue was found and fixed during validation: the validator initially required a CC BY-SA header on `references/diagrams.md`, which is correctly MIT + CC BY 4.0 (C4 model), not CC BY-SA. The validator's required-set was corrected (diagrams.md removed, with a comment explaining why). Re-run: clean.

## Eval schema validation

```
$ python3 tests/check_evals.py tests/evals.json
✅ 53 evals validated across 19 categories             (exit 0)
   activation:4 adversarial:3 architecture:2 audit:2 classification:7
   diagrams:1 dx:2 evidence:4 governance:2 localization:1 packaging:1
   regression:2 release:3 safety:4 security:3 style:2 ui:2 workflow:2 writing:6
```
Every eval has a unique id, non-empty prompt/expected_output/assertions[]/files[], a known category, and files[] paths that all exist.

## Link validation

```
$ python3 scripts/check_links.py .
Scanned 54 files · checked 0 local links · skipped 20 external.
No broken local links.                                 (exit 0)
```
(Internal reference pointers in this package are written as backticked paths, not Markdown links, and are verified to exist by `validate_skill.py`; Markdown-link checking additionally confirmed no broken relative links or anchors.) One issue found and fixed: bare `(#)` placeholder anchors in templates were initially flagged as broken; the checker was corrected to skip the universal "fill-in-later" placeholder. Re-run: clean.

## Script smoke tests (against `tests/fixtures/`)

| Command | Expected | Result |
|---|---|---|
| `inventory_docs.py tests/fixtures` | lists 3 fixtures, heuristic type guesses labeled as candidates | ✓ exit 0 |
| `detect_mixed_docs.py tests/fixtures` | flags `mixed-doc.md` (tutorial+reference+explanation signals) | ✓ exit 0, flagged |
| `check_links.py tests/fixtures` | no broken local links | ✓ exit 0 |
| `verify_examples.py runnable-sample.md --run python` | the self-contained block reports `verified` | ✓ exit 0, verified |
| `verify_examples.py clean-reference.md --run python` | illustrative snippet reports `failed` (tool captures failures, never fakes a pass) | ✓ exit 1, failed-as-designed |
| `verify_examples.py clean-reference.md` (default) | extract-only, no execution | ✓ exit 0 |
| `compare_ui_labels.py draft-with-wrong-labels.md observed-labels.json` | flags "Responsive editing" (invented menu) and "Pressed" (real states are Default/Hover/Focus/Focus-visible/Active) | ✓ exit 1, both flagged |
| `scrub_check.py mixed-doc.md` | no leak patterns | ✓ exit 0 |

Exit-code convention verified: 0 = clean, 1 = issues found (tool worked, has something to report), 2 = bad usage. Heuristic tools (`inventory_docs`, `detect_mixed_docs`) always exit 0 because their output is advisory, not a verdict — and both label their output as candidates for human review, per the "don't pretend a heuristic classifier is certain" requirement.

```
$ python3 -m py_compile scripts/*.py tests/*.py
all compile OK
```

## Scenario evaluation

`tests/evals.json` is the behavioral test suite. It is model-run (feed `files[]` as context, `prompt` as the task, judge against `assertions[]`), so it is not executed by the deterministic tooling above; the schema validator confirms every eval is well-formed and its referenced files exist. Coverage against the prompt's required test areas:

| Required test area | Eval id(s) |
|---|---|
| Activation on direct + implicit tasks | act-01, act-02 |
| Non-activation on unrelated writing | act-04 |
| Heavy-mode not self-triggering | act-03 |
| Four-type distinction | class-01, class-10 |
| Compass for ambiguous cases | class-02 |
| Mixed-document diagnosis | class-12, class-05 |
| Boundary cases | class-11 |
| Preservation during restructuring | safe-preserve, adv-03 |
| Approval gating before broad changes | safe-approval-gate, adv-02 |
| Inventory before audit verdict | audit-01 |
| Documentation impact from a code change | rel-06 |
| Change-coverage receipt generation | rel-06 |
| UI-label verification | ui-01, ui-02 |
| Release-test reporting | rel-07 |
| Evidence classification | evid-04, verify-02 |
| Security claim restraint | sec-01 |
| Working-example verification | verify-03, verify-01 |
| Information-architecture recommendations | arch-04, arch-07 |
| Governance and freshness planning | gov-05, gov-04 |
| Diagram selection | dgm-02 |
| Accessibility and localization | loc-01 |
| Behavior when sources/tools unavailable | reg-tool-unavailable |
| Repo instructions conflicting with defaults | reg-repo-convention-conflict |
| Resistance to false-verification requests | adv-01 |
| Packaging/structure | pkg-01 |

Positive, negative, ambiguous, and adversarial cases are all represented (the `adversarial` category holds three: false-verification, approval-skip, and unverified-preservation).

## Remaining limitations

1. **Scenario evals are specified, not executed here.** They require a model runner (promptfoo + `claude -p`, ~2 calls each) or manual judging. The schema and file references are validated; the behavioral pass/fail is the deploying user's RED/GREEN gate. This is the intended split (deterministic structure now, behavioral judging at run time).
2. **Heuristic scripts are advisory by design.** `inventory_docs` and `detect_mixed_docs` guess types by keyword/signal and cannot determine user intent; their output is labeled candidates-for-review, never verdicts. The compass (by a human or the agent) is the authority.
3. **`check_links` is local-only.** It does not make network requests (deliberate, for CI speed/reliability). Public-URL-resolves-logged-out checks for handoffs are a manual step in `workflows/security-audit-handoff.md`.
4. **`scrub_check` is necessary, not sufficient.** It flags common leak patterns but cannot prove a file is clean; it requires `--term` for case-specific mechanism/endpoint/platform names and a human confirmation, and says so.
5. **Path note.** `~/.claude` on this machine is a symlink into a `claude-config` git repo, so absolute paths in script output show the resolved `claude-config` location; the skill functions identically under either path.

# 11 · External-PR audit: a worked case

One afternoon on [Post Formats for Block Themes](https://github.com/courtneyr-dev/post-formats-for-block-themes):
two pull requests from an outside contributor, both correct in diagnosis, one broken in
implementation — and every method in this rig got exercised on the way to merging them. This is the
worked case for the rig's thesis: **a claim is not evidence until something runs.**

The PRs: [#31](https://github.com/courtneyr-dev/post-formats-for-block-themes/pull/31) (a template
warning fix) and [#32](https://github.com/courtneyr-dev/post-formats-for-block-themes/pull/32)
(registering a PHP-only block in the editor via WordPress 7.0's `supports.autoRegister`).

---

## No red X is not a green check

Both PRs showed *no CI results at all*. Not failing — absent. GitHub holds workflow runs from
first-time contributors in an `action_required` state until a maintainer approves them, so an
external PR with a clean-looking checks area may have run **nothing**. The absence of a red X reads
as "fine" at a glance, and it means the opposite: zero of the matrix has executed.

The move: approve the held runs first (`gh api -X POST .../actions/runs/<id>/approve`), then treat
CI as one input — not the verdict.

## The suite passed green on a real regression

PR #32 passed the full test suite — 289 tests — and it shipped a regression anyway. It passed
`supports` through `register_block_type()` args, and core merges args over block.json metadata with
a **top-level** `array_merge()`: one key in args replaces the *entire* supports array from
block.json. Reading the core source said so; per the source hierarchy
([doc 05](../1-documentation-practice/05-release-tracking-cadence.md)), that still ranks below a
runtime test. So: a five-line probe dumping the registered block's supports, run on both branches.

- On the PR branch: `{"autoRegister":true}` — color, spacing, typography, border, anchor, all gone.
- On main: the full block.json set.

Two lessons stacked here. The suite was green because **nothing asserted the supports contract** —
a green suite only covers what someone thought to pin. And the diagnosis-vs-implementation split is
the normal case for external PRs: the contributor's analysis was right, the mechanism they reached
for was booby-trapped by a core behavior nobody documents loudly. The fix was one line in the right
place (declare the flag in block.json, where it merges cleanly), verified with the same probe.

## A regression test that never failed proves nothing

The follow-up PR added six integration tests pinning both contracts. Before trusting them, each was
run against the *pre-fix* code by checking out the old file into the test branch:

- template-contract test against pre-#31 code → fails (the leak it guards against)
- supports test against original #32 → fails (the wipe it guards against)

Then restored, both green. A guard that has never been watched failing is a decoration. The
checkout-swap takes about a minute and converts "the tests pass" into "the tests bite."

## "Tested up to" is a documentation claim — so it gets the audit

The same afternoon, WordPress 7.1 went stable. The temptation is to bump `Tested up to: 7.1` as a
version-string edit. It's not a version string; it's a **published claim about runtime behavior**,
and it earns the same treatment as any other doc claim in this rig:

1. Full suite against a real 7.1 install — locally, not just CI's `latest` lane (though checking
   the CI log to learn what `latest` actually resolved to is itself a source worth reading).
2. Core source diff 7.0 → 7.1 scoped to the surfaces the plugin bends — which found exactly one
   behavior change (`WP_Block_Template` grew a `date` property).
3. A runtime probe per finding: the plugin's synthetic template objects serialize the new field as
   `null` through the REST controller; the 7.0 auto-register bridge still picks up the block.
4. **The evidence ceiling, stated in the PR body:** the Playwright e2e/a11y suites were not run
   against a 7.1 environment. The bump ships with what it doesn't cover on the label.

## Credit is part of the merge

An external contributor whose diagnosis was right did the hardest part — finding the bug and caring
enough to fix it. The implementation correction is a footnote, not a demotion: their commits stay
intact on the merge, the changelog carries props by name, and `Contributors:` in `readme.txt` puts
the plugin on their WordPress.org profile. The audit protects the codebase; the credit protects the
reason people send patches at all.

---

**Steal this:** approve held CI before judging an external PR; probe the claim on both branches
before merging; make every new guard fail once on purpose; treat compatibility headers as testable
claims with a stated ceiling; and put the contributor's name in everything that ships.

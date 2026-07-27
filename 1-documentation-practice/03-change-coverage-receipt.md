# Change-coverage receipt

A deterministic completeness check, produced **before** declaring a change review
complete. It exists because "we looked at everything" is an opinion, and an opinion is
not a stop condition.

The receipt turns that opinion into an artifact someone else can check.

---

## Why a receipt and not a checklist

A reviewer who read 40 of 53 changed files and a reviewer who read all 53 produce
identical-sounding summaries. The difference only becomes visible when something in the
missing 13 ships undocumented and a reader hits it.

So the review does not end when someone feels finished. It ends when every row below has
a value in it. A blank row is not a failure — it is a recorded untested area, which is a
legitimate and honest place to stop. What is *not* legitimate is a blank row that nobody
noticed.

## Completeness reconciliation checklist

Each line is a reconciliation between two independent representations of the same
change. Where they disagree, something is undocumented:

- [ ] git changes reconciled with release notes
- [ ] source reconciled with the released packages
- [ ] documented deprecations reconciled with `@deprecated` annotations **and** runtime behavior
- [ ] API changes reconciled with tests
- [ ] dependency changes reconciled with lockfiles
- [ ] feature flags reconciled with shipped defaults
- [ ] internal plans reconciled with what actually shipped
- [ ] shipped changes absent from public notes — identified
- [ ] announced changes that did not ship — identified
- [ ] reverted or partially reverted work — identified
- [ ] changes present only in generated artifacts — identified

The last four are the ones that catch real documentation bugs. "Announced but did not
ship" is exactly the React 19 error described in the release-tracking file — the
announcement existed, so the claim felt sourced, but reconciling it against the shipped
tree would have caught it.

## The receipt

Filled in on each application:

| Field | Value |
|---|---|
| Baseline → target | |
| Commits / tags reviewed | |
| Releases reviewed | |
| Files changed | |
| Public APIs changed | |
| Hooks changed | |
| Routes changed | |
| Schemas changed | |
| Dependencies changed | |
| Deprecations reviewed | |
| Removals reviewed | |
| Undocumented changes found | |
| **Entries NOT fully reviewed, and why** | |

## The gate

If any row above is blank, or any checklist box is unchecked, the change review is
**not complete**. Record the shortfall as a named untested area. Do not paper over it.

A nondeterministic "looks done" is not a stop condition.

---

## Worked example

From the WordPress 7.1 beta cycle, the change surface for one audit range was roughly
53 commits across 95 files in the core repository, and 59 commits across 253 files in
the feature plugin. Reconciling git against the release notes on that range is what
surfaced a functional finding that the release notes never mentioned: a set of pruned
asset files was removed from the distribution but never added to the updater's
delete-list, so every *upgraded* site — not fresh installs — failed the canonical core
integrity check with roughly 243 "file should not exist" warnings.

The count matched the file-set delta exactly, which is what turned it from a suspicion
into a receipt. That finding is documented in full in
`../3-security-methods/08-methods-report-wordpress-7-1-beta.md`, and it was reported publicly
as a follow-up on the existing ticket after deduplicating against the known cluster.

It is a good illustration of the point: **nobody was hiding it.** It simply lived in the
space between the git history and the release notes, and only a reconciliation looks
there.

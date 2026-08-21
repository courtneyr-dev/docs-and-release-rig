# Change-coverage receipt

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`workflows/document-a-change.md`](../skills/comprehensive-documentation-engineering/workflows/document-a-change.md) · [`templates/change-coverage-receipt.md`](../skills/comprehensive-documentation-engineering/templates/change-coverage-receipt.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


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

## The reconciliation checklist, the receipt, and the gate

The 11-line reconciliation checklist, the fill-in receipt table, and the hard gate ("any
blank row = not complete") that used to be restated here are now the canonical, ready-to-fill
artifact in the skill: [`templates/change-coverage-receipt.md`](../skills/comprehensive-documentation-engineering/templates/change-coverage-receipt.md),
driven by [`workflows/document-a-change.md`](../skills/comprehensive-documentation-engineering/workflows/document-a-change.md).
Kept here is the one line that most often gets skipped and catches the most real
documentation bugs: **the last four reconciliations — shipped-but-unannounced, announced-but-did-not-ship,
reverted work, and changes present only in generated artifacts.** "Announced but did not
ship" is exactly the React 19 error described in the release-tracking file — the
announcement existed, so the claim felt sourced, but reconciling it against the shipped
tree would have caught it.

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

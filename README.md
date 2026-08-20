# Docs & release rig

**How I write developer documentation, test the releases that documentation describes, and report
what testing finds without leaking what shouldn't ship.**

Methods, standards, and reusable prompts — plus [**SETUP.md**](SETUP.md), which is how you install
and run the rig yourself.

> **The thesis:** documentation is a testable claim about behavior, and the test is the audit.
> Docs drift not because writers are careless, but because the source of truth moves faster than
> the doc and nobody re-runs the claim.

Everything here is drawn from real work — the WordPress 7.1 release cycle (July–August 2026) and
open-source plugins I maintain and ship. There's also a rendered version of this index:
open [`index.html`](index.html) locally, or enable GitHub Pages on this repo.

---

## Start here

If you have ten minutes, read these four in order:

1. **[The source hierarchy](1-documentation-practice/05-release-tracking-cadence.md)** — two facts
   we'd written down went stale in 48 hours. The retro explains why, and produces a ranking that
   resolves source conflicts deterministically: a runtime test beats a dev note beats the diff
   beats memory.
2. **[The audit that finds the gaps](1-documentation-practice/02-coverage-map-and-gap-analysis.md)** —
   everything a release claims, cross-referenced against what was actually verified, each gap
   carrying its authoritative source.
3. **[The loop that runs it](2-release-testing/06-beta-rc-testing-runbook.md)** — environments
   grouped by when they can actually be tested, a four-phase per-drop loop, and a definition of
   done you can hand to someone else.
4. **[The report at the end](3-security-methods/08-methods-report-wordpress-7-1-beta.md)** — what
   all of it produces: a self-contained document a stranger can act on, including the section most
   reports omit — what I did *not* cover.

---

## Contents

### 1 · Documentation practice

| Document | What it covers |
|---|---|
| [01 · Docs in my own projects](1-documentation-practice/01-docs-in-my-own-projects.md) | Four published docs sites, developer docs for the FAIR project, CI gates, release automation |
| [02 · Coverage map & gap analysis](1-documentation-practice/02-coverage-map-and-gap-analysis.md) | What the release claims vs. what I verified — with the gaps published as gaps |
| [03 · Change-coverage receipt](1-documentation-practice/03-change-coverage-receipt.md) | Reconciling release notes against git, packages, lockfiles, and shipped defaults |
| [04 · UI verification & label diff](1-documentation-practice/04-ui-verification-and-label-diff.md) | The pass that caught draft copy naming two controls that don't exist |
| [05 · Release-tracking cadence](1-documentation-practice/05-release-tracking-cadence.md) | The source hierarchy, and why knowledge decays in about 48 hours mid-beta |

### 2 · Release testing

| Document | What it covers |
|---|---|
| [06 · Beta/RC runbook](2-release-testing/06-beta-rc-testing-runbook.md) | Per-drop operating loop, environments grouped by update timing, definition of done |
| [07 · Public testing tooling](2-release-testing/07-public-testing-tooling.md) | A 123-step Playwright runner and a Playground blueprint, both shipped publicly |
| [11 · External-PR audit case](2-release-testing/11-external-pr-audit-case-study.md) | Two contributor PRs, worked end to end: held CI, a green suite hiding a regression, guards proven to bite, a runtime-backed compat bump |

### 3 · Security methods

| Document | What it covers |
|---|---|
| [08 · Methods report](3-security-methods/08-methods-report-wordpress-7-1-beta.md) | A complete real report: findings, honest gaps, verbatim reusable prompts, tooling labeled by actual use |
| [09 · Evidence & validation standard](3-security-methods/09-evidence-and-validation-standard.md) | Gate ladder, 20-step validation loop, required controls, safe-proof limits |
| [10 · Audit handoff standard](3-security-methods/10-audit-handoff-standard.md) | Link hygiene, confidentiality scrubbing, and labeling every tool by actual use |

### Reference

- [**SETUP.md**](SETUP.md) — install the rig: skills, testing tooling, environments, and the
  workflows that use them
- [**skills-and-tooling.md**](skills-and-tooling.md) — every tool and skill, labeled
  `used` / `available` / `authored`, with public links where public links exist

---

## The ideas worth stealing

Even if you never install any of it:

- **Rank your sources.** When two sources disagree, the higher one wins — no debate, no averaging.
  Reading implementation code sits *below* a published dev note, because code can be mid-refactor,
  feature-flagged, or about to be reverted.
- **Publish your gaps.** A gap you've written down is a task. A gap you haven't is a future
  correction.
- **A screenshot pass is a free documentation audit.** You're already looking at every control the
  doc names — take the label diff while you're there.
- **Say `used`, `available`, or `authored`.** Listing an impressive tool chain implies every item
  touched the work. Three words per line prevents the most common quiet dishonesty in technical
  reports.
- **Document your negative results.** "Checked — not an issue" saves the next person a full
  re-investigation, and it's the part that most consistently gets deleted because it feels like
  admitting you were wrong.
- **Write the definition of done.** A loop without an explicit stop condition either ends when
  someone gets tired or never ends.

---

## Scope and confidentiality

**Public references only.** Every external link resolves for a logged-out visitor, and every
referenced tracker ticket was checked against the tracker's own API.

One security-classified finding from the 7.1 work was responsibly disclosed through a private
channel. It appears here as a bare acknowledgment — no mechanism, location, severity, or
reproduction. That scrubbing procedure is itself documented in
[10 · Audit handoff standard](3-security-methods/10-audit-handoff-standard.md), because knowing how
to *not* publish something is part of the job.

Where a method came out of production work, infrastructure specifics — hostnames, connection
configuration, stack fingerprints, and other people's names — are omitted. What's left is the
transferable part.

## Related repositories

| Repo | What it is |
|---|---|
| [wp-dev-prompts](https://github.com/courtneyr-dev/wp-dev-prompts) | 11 skill modules + 6 portable prompts for WordPress development · CC0 |
| [developer-education-prompts](https://github.com/courtneyr-dev/developer-education-prompts) | Prompts for documentation and training material · CC0 |
| [wp7-test-automation](https://github.com/courtneyr-dev/wp7-test-automation) | Playwright runner, 123 test steps across 14 areas |
| [WP7-testing](https://github.com/courtneyr-dev/WP7-testing) | Test launcher + WordPress Playground blueprint |
| [fair-beacon-docs](https://github.com/courtneyr-dev/fair-beacon-docs) | Developer documentation for the FAIR ecosystem |

## License

[CC0 1.0 Universal](LICENSE) — public domain. Use it, adapt it, ship it. No attribution required,
though I'd enjoy hearing about it.

**Courtney Robertson** · [courtneyr.dev](https://courtneyr.dev) ·
[@courtneyr-dev](https://github.com/courtneyr-dev)

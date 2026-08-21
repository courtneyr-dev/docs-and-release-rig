# WordPress 7.1 Beta testing & security-audit methodology

<!-- canonical-source-banner -->
> **Provenance for the agent skill.** The transferable pattern in this page is generalized in the skill at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/security-documentation.md`](../skills/comprehensive-documentation-engineering/references/security-documentation.md) · [`references/evidence-and-validation.md`](../skills/comprehensive-documentation-engineering/references/evidence-and-validation.md) · [`references/beta-rc-testing.md`](../skills/comprehensive-documentation-engineering/references/beta-rc-testing.md). This page is the unique real-work record behind it.


**From:** Courtney Robertson
**Date:** July 22, 2026
**Builds covered:** WordPress 7.1 Beta 2 (July 17, 2026) and Beta 3 (July 22, 2026)

> *Originally written as a personal share for a member of the WordPress Security Team,
> and reproduced here unchanged. It is the best single example of how I test a release:
> what I found, how I proved it, what I did not cover, and the exact prompts anyone can
> re-run. Note §5 — the honest-gaps section is not optional in my reports.*

> **Confidentiality:** This document contains **public references only**. Every link resolves on the open web. One security-classified issue found during this work was **responsibly disclosed through a private channel and is withheld here** — no mechanism, location, or reproduction appears in this file. Everything else below is method and publicly-filed results.

---

## 1. Context

Goal: exercise each 7.1 beta the way a real site owner would upgrade into it, and independently audit each build's *changed* surface for security and integrity regressions before it reaches general availability. Two release-relevant things happened mid-cycle that shaped testing:

- **Beta 2 shipped early (July 17)** alongside the unplanned **7.0.2** security release, and the cycle gained an extra beta.
- **Beta 3 (July 22)** addressed 71+ issues since Beta 1.

Both were tested on the same day they dropped, against a real range of upgrade origins (6.8.5 → 7.1-beta3, etc.), not just clean installs.

**Sources:** [WordPress 7.1 Beta 1](https://wordpress.org/news/2026/07/wordpress-7-1-beta-1/) · [WordPress 7.1 Beta 3](https://wordpress.org/news/2026/07/wordpress-7-1-beta-3/) · [WordPress 7.0.2 Release](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) · [Make/Core 7.1 hub](https://make.wordpress.org/core/7-1/) · [What's new for developers (July 2026)](https://developer.wordpress.org/news/2026/07/whats-new-for-developers-july-2026/)

---

## 2. Findings

### Finding 1 (public, functional) — Upgrade leaves orphaned icon-library files; `verify-checksums` fails on every upgraded site

**Mechanism.** 7.1 prunes the `wp-includes/images/icon-library/` set (≈331 files in 7.0.x → ≈88 in 7.1). The removed SVG paths were **not** added to the `$_old_files` array in `wp-admin/includes/update-core.php`, so the update routine never deletes them. On a site that *upgrades* to 7.1 (rather than fresh-installs), ~243 old icons linger on disk.

**Evidence.** On a real upgraded 7.1 beta site, `wp core verify-checksums` reports ~243 `File should not exist: wp-includes/images/icon-library/<name>.svg` warnings. The count matches the file-set delta exactly (331 − 88 = 243). A clean 7.1 install is checksum-clean; only the upgrade path is affected. This is the same class as the collaboration/RTC file-removal issue that *was* added to `$_old_files` — the icon paths were simply missed.

**Impact.** No functional break (the orphans are unreferenced), but `verify-checksums` is the canonical core-integrity check, and host/third-party malware scanners compare against core checksums — so upgraded sites surface ~243 "unknown core files" fleet-wide as 7.1 rolls out. Reported publicly as a follow-up comment on the existing icon-pruning ticket rather than a new ticket (dedup'd against the known build-server file-removal cluster).

**Fix.** Add the removed `wp-includes/images/icon-library/*.svg` paths to `$_old_files` in `update-core.php`.

**Sources:** [Trac #65489 (icon-library pruning)](https://core.trac.wordpress.org/ticket/65489) · related file-removal cluster [Trac #65565](https://core.trac.wordpress.org/ticket/65565), [Trac #65325](https://core.trac.wordpress.org/ticket/65325) · [`wp core verify-checksums`](https://developer.wordpress.org/cli/commands/core/verify-checksums/)

### Finding 2 (security-classified) — withheld

A separate security issue was identified during the audit and **responsibly disclosed through a private channel**. Details — mechanism, location, reproduction, and severity — are withheld from this document by design. Happy to discuss it with you directly through the appropriate private channel.

---

## 3. Stack facts (verified)

- **Builds:** 7.1-beta2 (db_version 61833) and 7.1-beta3 (build 7.1-beta3-62828).
- **Change surface, Beta cycle:** ~53 commits / ~95 files in wordpress-develop and ~59 commits / ~253 files in Gutenberg across the audited range (see compare links in §7).
- **Upgrade origins exercised:** 6.8.5, 6.9.4, 7.0, 7.0.2, 7.1-beta2 — each fresh-installed, then upgraded in place to 7.1-beta3.
- **Real-hosting reference:** the orphan-icons finding was confirmed on a live host that auto-updated from a 7.0.x line into a 7.1 beta (PHP 8.4, real filesystem), not just in a container.

---

## 4. Tested and cleared (non-issues — don't re-chase)

- **Fresh installs, all versions.** 6.8.5 / 6.9.4 / 7.0 / 7.0.2 / 7.1-beta2 / 7.1-beta3 install clean and pass the full content smoke battery (§6).
- **Content lifecycle on beta3.** Posts, Pages, Comments (add/reply/edit/trash), custom post types, categories & tags, reusable blocks/patterns, media (upload/edit/delete with sub-size generation), theme switching, front-end rendering, and DB integrity all pass on 7.1-beta3 — both fresh and after in-place upgrade.
- **Global-styles custom-CSS input validation.** The nested block/element CSS path was examined for an output-injection bypass and **cleared**: the write path is gated by the `edit_css` capability (which maps to `unfiltered_html`), so any breakout crosses no privilege boundary, and the saved post is additionally kses-filtered. Not a vulnerability — at most a code-hygiene note to apply the guard uniformly.
- **Beta→beta upgrade.** 7.1-beta2 → 7.1-beta3 upgrades cleanly with the full battery passing.

---

## 5. Not covered (honest gaps)

- **Multisite / network-activated** scenarios were not exercised on the upgrade matrix (single-site only).
- **Non-default upload configurations** (date-organization disabled, custom upload paths) were not swept.
- **Performance/regression profiling** (Core Web Vitals, query counts) was out of scope here — this pass was security + upgrade-integrity focused.
- **Locale/i18n and RTL** upgrade paths not tested.
- The security audit prioritized the *changed* surface (diff-driven); unchanged legacy code was not re-audited from scratch.

---

## 6. How this was tested

### Methods (prose)

**Change-intelligence first.** Before touching a build, I diff the previous stable tag against the beta in both wordpress-develop and Gutenberg, read the dev notes / Make-Core posts for the cycle, and monitor `#core` and `#core-test` in the Making WordPress Slack for in-flight issues. That produces a ranked list of *changed* attack-surface families — REST dispatch/registration, media handling, the comment/Notes expansion, block render (URL/attribute handling), input-validation/sanitization guards, and SVG handling — so the audit targets what actually moved.

**Multi-model adversarial panel.** Each build's changed surface is audited by an independent panel of frontier models — Claude, OpenAI GPT/Codex, and Google Gemini — coordinated by a custom harness. Each model works the same diff independently; **disagreement is signal.** Every candidate finding is then run through an adversarial verification pass whose default is to **refute**: a finding survives only if it can't be talked down and can be reproduced. Behavior is always compared against the prior stable release to confirm novelty — a surface that behaves identically in the previous version is not a beta regression.

**Prove-by-firing, on disposable local only.** No finding is called a vulnerability on reasoning alone. It has to reproduce with a working proof on a **throwaway local install** — never on live hosting. If a proof can't be built, it's logged as "unconfirmed," not a vuln. Destructive proofs never run against real sites.

**Functional + upgrade-path testing.** Separately from security, every build goes through an upgrade matrix: fresh-install each origin version, run the content smoke battery, upgrade in place to the target beta, and re-run the battery. This is what surfaced the orphan-icons/`verify-checksums` issue — it only appears on the *upgrade* path, so clean-install testing alone would miss it. A practical gotcha worth passing on: reaching a *beta* from a *stable* install requires installing the **explicit release package** (`wp core update --version=<beta> --force <official-zip-url>`); a bare `--version=<beta>` resolves to the latest *stable* offer instead, so the origin never actually lands on the beta unless you force the package URL.

**Disclosure discipline.** Security-classified findings are routed **privately** through coordinated disclosure and never posted to public Trac or GitHub. Functional/integrity issues (like the orphan icons) go to public Trac, deduped against existing tickets first.

### Prompts (verbatim — reusable)

**Per-build security audit (one panel member):**
```
You are one model on an adversarial security panel auditing a WordPress beta build.
Scope: the diff between the previous stable tag and this beta, in wordpress-develop
and Gutenberg — do not re-audit unchanged legacy code.

1. Enumerate changed files touching: REST endpoints/dispatch/registration, media
   handling, the comment/Notes system, block render (URL/attribute handling),
   input validation & sanitization, and SVG handling.
2. For each, hypothesize a concrete abuse: a missing capability/ownership check,
   untrusted client input reaching a sink, an object-ownership or trust-boundary
   gap, or injection (kses/meta/output).
3. For every candidate, try to REFUTE it first. Compare the behavior to the prior
   stable release to confirm it is NEW. If you cannot build a working proof on a
   disposable local install, mark it "unconfirmed" — not a vulnerability.
4. Output per item: file:line, mechanism, reachability (which role/context),
   novelty vs prior release, suggested fix, and confidence.

Security-classified findings are disclosed privately. Do not post them publicly.
```

**Upgrade-path + content smoke matrix:**
```
For each origin version [6.8.5, 6.9.4, 7.0, 7.0.2, 7.1-beta2]:
  1. Fresh-install the version in a disposable local environment.
  2. Run the content smoke battery (below) and record pass/fail.
  3. Upgrade IN PLACE to the target beta by installing the exact release package:
       wp core update --version=<beta> --force <official-zip-url>
       wp core update-db
     (A bare --version=<beta> from a stable install resolves to the latest STABLE
      offer, not the beta — always force the explicit package URL.)
  4. Record which version the site ACTUALLY landed on.
  5. Re-run the content smoke battery on the upgraded site.

Content smoke battery:
  verify-checksums; Posts CRUD; Comments add/reply/edit/trash; Pages CRUD/trash;
  custom-post-type CRUD; Categories & Tags add/remove; create a reusable block/pattern;
  media upload/edit/delete (confirm sub-size generation); switch themes;
  front-end returns HTTP 200; database integrity check.
```

### Skills & tooling (labeled by actual use)

- **WP-CLI** — *used* throughout for install, upgrade, checksums, and content CRUD. <https://wp-cli.org/>
- **`@wordpress/env` (wp-env)** — *used* as the disposable local environment for installs, upgrades, and destructive proofs. <https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/>
- **WordPress Playground** — *available/cross-check* for quick throwaway version checks. <https://playground.wordpress.net/>
- **WordPress Studio** — *available* as an additional local environment. <https://developer.wordpress.com/studio/>
- **GitHub compare views** — *used* for the change-intelligence diff (links in §7).
- **Core Trac** — *used* for dedup and public disclosure of the functional finding.
- **Making WordPress Slack (`#core`, `#core-test`)** — *used* for in-flight issue monitoring. <https://make.wordpress.org/chat/>
- **Custom multi-model audit harness** (author: Courtney Robertson; private tooling — named, not linked) — *used* to fan the diff out to the model panel and run adversarial verification.
- **Model panel:** Claude (Opus), OpenAI GPT/Codex, Google Gemini — *used* as the independent auditors.

*Accuracy note:* the analysis ran through the custom harness + multi-agent orchestration coordinating the three model families — not a single packaged public "skill." Environment setup and content testing were WP-CLI + wp-env. No public skill performed the security reasoning; the named models did.

---

## 7. Consolidated sources (all public)

**Release / cycle**
- WordPress 7.1 Beta 1 — https://wordpress.org/news/2026/07/wordpress-7-1-beta-1/
- WordPress 7.1 Beta 3 — https://wordpress.org/news/2026/07/wordpress-7-1-beta-3/
- WordPress 7.0.2 Release — https://wordpress.org/news/2026/07/wordpress-7-0-2-release/
- Make/Core 7.1 hub — https://make.wordpress.org/core/7-1/
- What's new for developers (July 2026) — https://developer.wordpress.org/news/2026/07/whats-new-for-developers-july-2026/

**Change surface (diff)**
- wordpress-develop repo — https://github.com/WordPress/wordpress-develop
- Gutenberg repo — https://github.com/WordPress/gutenberg
- wordpress-develop compare range — https://github.com/WordPress/wordpress-develop/compare/1b957d710850a7a28eb4740c5ed5e308efb76460...trunk
- Gutenberg compare range — https://github.com/WordPress/gutenberg/compare/e73c3c481db0650183f092af157f6e42efe9ee2d...4997026b75c922d8a6f77a03d72ed7cad04c7073

**Functional finding (public)**
- Trac #65489 (icon-library pruning) — https://core.trac.wordpress.org/ticket/65489
- Trac #65565 — https://core.trac.wordpress.org/ticket/65565
- Trac #65325 — https://core.trac.wordpress.org/ticket/65325

**Tooling / docs**
- WP-CLI — https://wp-cli.org/
- `wp core verify-checksums` — https://developer.wordpress.org/cli/commands/core/verify-checksums/
- wp-env — https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/
- WordPress Playground — https://playground.wordpress.net/
- WordPress Studio — https://developer.wordpress.com/studio/
- Making WordPress Slack — https://make.wordpress.org/chat/

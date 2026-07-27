# Tooling & agent-skills index

Everything referenced in this package, labeled by **actual use** per the accuracy rule
in `3-security-methods/10-audit-handoff-standard.md`.

Labels:

- **used** — actually performed work described here
- **available** — installed and usable, but did not do the work described
- **authored** — I wrote it

Every link below was checked to resolve for a logged-out visitor at the time of
packaging. Ticket references were additionally verified against the tracker's own API —
see **Source verification** at the end of this file. Where a tool is private or
local-only, it is named and described rather than linked, because a link would 404 for
you.

---

## Testing & environment tooling

| Tool | Use | Link |
|---|---|---|
| **WP-CLI** | **used** — installs, upgrades, checksum verification, content CRUD, preference seeding | https://wp-cli.org/ |
| **`wp core verify-checksums`** | **used** — the canonical core-integrity check; the command that surfaced the orphaned-files finding | https://developer.wordpress.org/cli/commands/core/verify-checksums/ |
| **`@wordpress/env`** | **used** — disposable containerized environments across multiple PHP versions | https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/ |
| **WordPress Studio** | **used** — the persistent local capture rig for screenshots and label verification | https://developer.wordpress.com/studio/ |
| **WordPress Playground** | **available / cross-check** — fast throwaway version checks. Caveat documented in document 05 (release-tracking cadence): it can lag the beta channel | https://playground.wordpress.net/ |
| **Playwright** | **used** — end-to-end and accessibility testing in my own plugin repositories | https://playwright.dev/ |
| **axe-core** | **used** — automated accessibility testing in the Post Formats repository | https://github.com/dequelabs/axe-core |
| **PHPUnit** | **used** — unit and integration testing across my plugins | https://phpunit.de/ |
| **PHPStan** | **used** — static analysis, level 6 | https://phpstan.org/ |
| **PHP_CodeSniffer / WordPress Coding Standards** | **used** — coding-standards gates | https://github.com/WordPress/WordPress-Coding-Standards |
| **GitHub Actions** | **used** — CI on every pull request; automated WordPress.org deployment on release | https://github.com/features/actions |

## Sources & disclosure channels

| Source | Use | Link |
|---|---|---|
| **Make/Core dev notes** | **used** — rank 2 in the source hierarchy | https://make.wordpress.org/core/tag/dev-notes/ |
| **Make/Test** | **used** — official test calls and scrub schedules | https://make.wordpress.org/test/ |
| **Core Trac** | **used** — milestone as canonical shipped-vs-deferred; public disclosure of the functional finding | https://core.trac.wordpress.org/ |
| **wordpress-develop** | **used** — change-intelligence diffs | https://github.com/WordPress/wordpress-develop |
| **Gutenberg** | **used** — change-intelligence diffs | https://github.com/WordPress/gutenberg |
| **Making WordPress Slack** | **used** — in-flight issue monitoring in `#core` and `#core-test` | https://make.wordpress.org/chat/ |
| **Developer Blog** | **used** — "what's new for developers" monthly roundups | https://developer.wordpress.org/news/ |

## Agent skills — public

These are published under CC0 1.0 in my prompts toolkit, portable across Claude Code,
Cursor, Cline, Copilot and similar tools. Browse them all at
**https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/skills**

| Skill | Purpose | Use here |
|---|---|---|
| `wordpress-testing` | PHPUnit, WP_Mock, PHPCS, Playwright E2E, CI workflows | **authored · used** |
| `wordpress-security` | Sanitize, validate, escape; nonces, capabilities, queries, injection prevention | **authored · used** |
| `wordpress-dev` | Plugin architecture, block development, block themes, REST, Abilities API | **authored · used** |
| `wordpress-playground` | Browser-based test and demo environments via blueprints | **authored · available** |
| `wordpress-accessibility` | WCAG 2.1/2.2 AA, keyboard nav, screen-reader testing, ARIA, contrast | **authored · used** |
| `wordpress-performance` | Core Web Vitals, profiling, caching, asset loading | **authored · available** |
| `ui-ux-audit` | Interaction audit methodology and motion specifications | **authored · available** |
| `prompt-engineering` | Prompt structure and token optimization | **authored · used** |
| `engineering` | Planning, code review, git workflow | **authored · used** |
| `product-management` | Jobs-to-be-done, personas, positioning | **authored · available** |
| [`wp-screenshots`](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/skills/wp-screenshots) | Login-aware headless Chromium capture from a JSON brief; hides update bubbles and admin notices, defaults to 2× DPR, writes a standalone HTML gallery | **authored · used** |

The six portable prompts in the same repository — plugin scaffolding, block development, testing
setup, security review, accessibility check, and **documentation generation** — are at
https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/prompts , alongside
[agents](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/agents) and
[workflows](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/workflows).

A separate CC0 set covering documentation and training material — including an `agent-style.md`
defining voice constraints for generated content — lives at
**https://github.com/courtneyr-dev/developer-education-prompts**

## Public testing tooling (prior release cycle)

| Repository | What it is |
|---|---|
| [`wp7-test-automation`](https://github.com/courtneyr-dev/wp7-test-automation) | Node.js + Playwright runner, 123 test steps across 14 areas, cookie auth for 2FA/SSO sites, JSON results with an HTML reporter, screenshots on failure — and a README that documents its own coverage limits |
| [`WP7-testing`](https://github.com/courtneyr-dev/WP7-testing) | An [interactive test launcher](https://courtneyr-dev.github.io/WP7-testing/) plus a WordPress Playground blueprint, so a community tester gets a configured beta environment in two clicks |

Detail in `2-release-testing/07-public-testing-tooling.md`.

## Published documentation sites

| Project | Docs |
|---|---|
| Post Formats for Block Themes | https://courtneyr-dev.github.io/post-formats-for-block-themes/ |
| Post Kinds for IndieWeb | https://courtneyr-dev.github.io/post-kinds-for-indieweb/ |
| Outpost | https://courtneyr-dev.github.io/outpost/ |
| Link Extension for XFN | https://courtneyr-dev.github.io/link-extension-for-xfn/ |
| FAIR Beacon (developer docs, Markdown) | https://github.com/courtneyr-dev/fair-beacon-docs |

## Agent skills — local, named not linked

Private or local-only. Described so they can be discussed; not linked, because the link
would 404.

| Skill | Purpose | Use here |
|---|---|---|
| `wordpress-audit-handoff` | The packaging standard reproduced as document 10 — link hygiene, confidentiality scrubbing, accuracy labels, required section order | **authored · used** (this package was built with it) |
| `wp-audit` | Audits owned plugins, proves each finding by firing it against a disposable local site, and spawns a fix task per confirmed bug | **authored · available** |
| `wp-github-actions` | Sets up CI/CD for WordPress plugins — standards, linting, PHPUnit, PHPStan, dependency scanning, Playground PR previews, WordPress.org deployment | **authored · used** |
| `wp-readme-optimizer` | Structured audit and rewrite of WordPress.org `readme.txt` listings, scored by section against an inferred target keyword | **authored · available** |
| `wordpress-governance-wiki` | Maintains project-governance reference material | **authored · available** |
| `wp-training` | WordPress training material development | **authored · available** |
| `better-documents` | Document and presentation review against communication best practices; applied at generation time, not as an afterthought. Adapted from Anil Dash's [Make better documents](https://www.anildash.com/2024/03/10/make-better-documents/) | **available** |
| `technical-writing` | Drafts technical posts directly from a repository — reading commits, exploring files — while still in the code. Adapted from Rich Tabor's public collection at https://github.com/richtabor/agent-skills | **used** |
| `anti-slop-git-writing` | Commit messages, PR descriptions, and issue reports that read like a specific person wrote them under normal time pressure | **available** |
| `vault-hygiene-checker` | The checker half of a maker/checker split — independently verifies synthesis work rather than trusting it | **authored · available** |
| **Custom multi-model audit harness** | Fans a change surface out to an independent panel of frontier models and runs adversarial verification. Private repository (`wp-audit-pipeline`) | **authored · used** |

## Model panel

Claude (Opus), OpenAI GPT/Codex, and Google Gemini — **used** as independent auditors on
the changed surface, with disagreement treated as signal.

---

## Source verification

Re-verified **July 27, 2026**, per the "re-verify findings live if the target is
reachable" rule in the handoff standard. Every ticket cited anywhere in this package was
queried through the tracker's API and its title confirmed against how this package
describes it. Current status is reported because a citation's *state* is part of its
accuracy — a reader should not have to discover on their own that a referenced ticket
reopened.

| Ticket | Title as filed | Status | Milestone |
|---|---|---|---|
| [#65489](https://core.trac.wordpress.org/ticket/65489) | Icons: There are icon files that are not used in the icon registry | **reopened** | 7.1 |
| [#65565](https://core.trac.wordpress.org/ticket/65565) | Some files removed from `wordpress-develop` remain on the build server | closed | 7.1 |
| [#65325](https://core.trac.wordpress.org/ticket/65325) | Real-time collaboration files have shipped in 7.0 | closed | 7.0.3 |
| [#65564](https://core.trac.wordpress.org/ticket/65564) | Enable infinite scrolling in the Media Library grid view by default | closed | 7.1 |
| [#51006](https://core.trac.wordpress.org/ticket/51006) | Add a mechanism for accessible tooltips in core | closed | 7.1 |

Two notes from this pass:

- **#65489 is currently reopened**, which is consistent with the orphaned-files finding
  in document 08 having been filed as a follow-up on the existing ticket rather than as a
  new one. The three file-removal tickets — 65489, 65565, and 65325 — are the cluster
  that finding was deduplicated against before reporting.
- **#65564 is closed against 7.1**, meaning the media-library change shipped. It remains
  marked `untested` in the coverage map in document 02, because that column records *my*
  verification status, not the ticket's. Those are different claims and the map keeps
  them separate on purpose.

## Accuracy note

The security analysis in `../3-security-methods/08-methods-report-wordpress-7-1-beta.md` ran
through the custom harness coordinating the three model families — **not** through any
single packaged public skill. Environment setup and content testing were WP-CLI and
containerized WordPress. No public skill performed the security reasoning; the named
models did.

Two skills listed in my own working notes from July 2026 — a set of third-party
WordPress security and testing skills from other authors — are **no longer installed**
and are therefore omitted here rather than listed from memory. Verifying that before
writing this index is an instance of the same rule as the rest of the package: check the
current state, do not cite the note.

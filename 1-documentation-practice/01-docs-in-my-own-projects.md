# Documentation in my own projects

<!-- canonical-source-banner -->
> **Provenance for the agent skill.** The transferable pattern in this page is generalized in the skill at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/information-architecture.md`](../skills/comprehensive-documentation-engineering/references/information-architecture.md). This page is the unique real-work record behind it.


Published documentation sites, the repositories behind them, and the distribution listings they
support. **Every link below was verified for a logged-out visitor** — and for
WordPress.org plugin listings, verified against the plugins API
(`api.wordpress.org/plugins/info/1.2/`), because the listing URL for an unpublished slug
soft-redirects to a search page that still returns 200. A bare status-code check cannot
tell a real listing from that redirect; the API answers honestly.

These are where I set the documentation standard rather than inherit it, so they show what I
actually think good developer documentation looks like: **a real documentation site rather than a
long README**, separate living documents for testing, deployment, and branching, CI that gates
contributions, and a security policy that routes reports somewhere private.

---

## Quick index

| Project | Documentation site | Source | Distribution |
|---|---|---|---|
| Post Formats for Block Themes | [docs](https://courtneyr-dev.github.io/post-formats-for-block-themes/) | [repo](https://github.com/courtneyr-dev/post-formats-for-block-themes) | [WordPress.org](https://wordpress.org/plugins/post-formats-for-block-themes/) |
| Post Kinds for IndieWeb | [docs](https://courtneyr-dev.github.io/post-kinds-for-indieweb/) | [repo](https://github.com/courtneyr-dev/post-kinds-for-indieweb) | directory submission pending |
| Outpost | [docs](https://courtneyr-dev.github.io/outpost/) | [repo](https://github.com/courtneyr-dev/outpost) | directory submission pending |
| Link Extension for XFN | [docs](https://courtneyr-dev.github.io/link-extension-for-xfn/) | [repo](https://github.com/courtneyr-dev/link-extension-for-xfn) | [WordPress.org](https://wordpress.org/plugins/link-extension-for-xfn/) |
| FAIR Beacon | — | [repo (docs in `/docs`)](https://github.com/courtneyr-dev/fair-beacon-docs) | — |
| WordPress Dev Prompts | — | [repo](https://github.com/courtneyr-dev/wp-dev-prompts) | CC0 |
| Developer Education Prompts | — | [repo](https://github.com/courtneyr-dev/developer-education-prompts) | CC0 |

---

## Post Formats for Block Themes

**Docs: https://courtneyr-dev.github.io/post-formats-for-block-themes/**
Source: https://github.com/courtneyr-dev/post-formats-for-block-themes ·
Listing: https://wordpress.org/plugins/post-formats-for-block-themes/

Brings post-format behavior to block themes — automatic format detection, a mid-edit format switcher
that preserves content, a repair tool for legacy posts, and an integrated chat-log block.

**The documentation site's information architecture** is the thing worth looking at. Five sections,
ordered by who needs them and when:

1. **Start here** — installation, getting started
2. **Using post formats** — settings, common tasks, compatibility
3. **Reference** — screenshots, plus an interactive Playground preview so a reader can try the
   plugin without installing anything
4. **Help** — FAQ, troubleshooting, **accessibility**, and **privacy**
5. **For theme developers** — theme integration, design tokens, hooks

The progression runs user-facing → developer-facing, with search and a theme selector. Accessibility
and privacy get their own pages rather than a paragraph each, because those are the two questions
that block adoption for the people who have to ask them.

**Repository docs, each maintained separately:**

| Document | Reader |
|---|---|
| `TESTING.md` + `docs/TESTING-SUMMARY.md` | Contributors running the suite |
| `docs/DEPLOYMENT.md` | Whoever cuts the release |
| `BRANCHING-STRATEGY.md` | Anyone opening a pull request |
| `CONTRIBUTING.md` | First-time contributors |

Four documents rather than four sections of one, because each has a different reader and a
different update cadence.

**Testing:** Playwright end-to-end **and accessibility testing via axe-core**, visual regression,
performance benchmarking, PHPUnit. **Gates:** ESLint, Stylelint, PHP_CodeSniffer, PHPStan.
**Release automation:** `bin/prepare-release.sh` runs tests, builds assets, and updates versions;
publishing a GitHub release triggers automated deployment to the WordPress.org directory.

## Post Kinds for IndieWeb

**Docs: https://courtneyr-dev.github.io/post-kinds-for-indieweb/**
Source: https://github.com/courtneyr-dev/post-kinds-for-indieweb ·
Listing: not yet in the WordPress.org directory (submission pending)

Publishing what you read, watch, listen to, play, and where you check in — with correct
microformats2 markup on every post. A modern successor to the classic IndieWeb plugin: 36 kinds, 27 blocks,
integrations against several open media APIs, bulk import, and webhook support for real-time
scrobbling.

- **Docs:** Astro Starlight site, published as above
- **Testing:** PHPUnit (`composer test`), Playwright end-to-end (`npm run test:e2e`)
- **Gates:** PHPCS, PHPStan level 5 (`phpstan.neon`; baseline worked off incrementally), ESLint, Stylelint, GitHub Actions on every pull request
- **Governance:** `CONTRIBUTING.md` with branch-naming conventions, a dedicated `TESTING.md`, and a
  `SECURITY.md` routing vulnerability reports through **private GitHub Security Advisories** rather
  than public issues

That last point is the same discipline as the disclosure routing in `../3-security-methods/08-methods-report-wordpress-7-1-beta.md`,
at the scale of a single plugin: give people a private channel before they need it, or they'll use
the public one.

## Outpost

**Docs: https://courtneyr-dev.github.io/outpost/**
Source: https://github.com/courtneyr-dev/outpost ·
Listing: not yet in the WordPress.org directory (submission pending)

A mobile-first progressive web app composer for IndieWeb POSSE publishing — quick notes, replies,
likes, photos, and life-tracking from a phone, on your own domain, with one-tap syndication.
Offline queue, service worker, installable to the home screen.

- **An architecture rule, documented as a rule:** *"Plugin owns layout. Theme owns paint."* The
  plugin controls structure and interaction; themes control all visual styling through CSS custom
  properties. One sentence that resolves most "can I change this?" questions before they're asked.
- **Testing:** PHPUnit, Playwright end-to-end, Vitest
- **Gates:** PHPCS against WordPress-Extra, PHPStan, ESLint — plus a **custom repository-specific
  audit lint** (`composer lint:section5`) checking for data leaks, credential exposure,
  instance-handling problems, and internationalization gaps
- **Build:** Vite. **Docs:** `docs/`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`

The custom lint is the interesting part. It encodes review findings that kept recurring into an
automated gate, so they stop being things a reviewer has to remember — the same move as packaging a
method as a skill, one level down.

## Link Extension for XFN

**Docs: https://courtneyr-dev.github.io/link-extension-for-xfn/**
Source: https://github.com/courtneyr-dev/link-extension-for-xfn ·
Listing: https://wordpress.org/plugins/link-extension-for-xfn/

Integrates XFN relationship tagging into the block editor's link interface across every
link-supporting block, implementing the complete XFN 1.1 specification with validation that
prevents invalid relationship combinations.

- **Docs:** complete user guides — installation, settings, common tasks, troubleshooting — plus
  architecture, key functions, and hooks in the README
- **Testing:** PHPUnit under `tests/phpunit/`, plus a documented **manual** procedure covering all
  three interface locations, verification that relationships render into published `rel`
  attributes, keyboard and screen-reader accessibility, and compatibility against widely-used
  plugins and themes

**Honest gap:** this repository has the least automated coverage of the four, and its written manual
procedure carries the load. It's listed that way on purpose — the honest-gaps rule that governs
every report in this portfolio applies to my own projects, or it isn't a rule.

---

## Documentation written for someone else's project

### FAIR Beacon — developer documentation

**https://github.com/courtneyr-dev/fair-beacon-docs**

Developer documentation for the **FAIR** ecosystem (Federated API for Integrity and Resilience) — a
decentralized WordPress plugin distribution system built on Decentralized Identifiers. The docs
cover quick-start, architecture concepts, Git Updater integration, DID lifecycle management,
security considerations, and troubleshooting, as eight sequentially-numbered Markdown guides with a
README acting as the hub.

This is the closest analog to platform documentation work: **documenting a distributed system I did
not build, for developers who need to integrate with it.** The sequential numbering is deliberate —
the concepts have a dependency order, and a reader who takes them out of order gets stuck at DID
lifecycle without the architecture context.

The project is slated to move to the FAIR project's own GitHub organization at
[fair.pm](https://fair.pm), which is the intended outcome: docs written well enough to be adopted
by the project they describe.

### Developer Education Prompts

**https://github.com/courtneyr-dev/developer-education-prompts** · CC0 1.0

Prompts for creating documentation and training materials, aimed across the range from people new to
coding through experienced web developers. Includes an `agent-style.md` defining voice and style
constraints for generated material.

Released public domain for the same reason as the toolkit below: a documentation standard that only
I can apply is a bottleneck, not a standard.

### WordPress Development Prompts

**https://github.com/courtneyr-dev/wp-dev-prompts** · CC0 1.0

An AI-assisted toolkit for WordPress plugin, block, and theme development, portable across Claude
Code, Cursor, Cline, Copilot and others.

- **6 portable prompts:** plugin scaffolding, block development, testing setup (PHPUnit, PHPCS,
  PHPStan, CI), security review, accessibility audit, **documentation generation**
- **[11 skill modules](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/skills):**
  WordPress development, security, testing, Playground, accessibility, performance, prompt
  engineering, UI/UX audit, engineering practice, product management, and
  [wp-screenshots](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/skills/wp-screenshots)
- Plus [agents](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/agents) and
  [workflows](https://github.com/courtneyr-dev/wp-dev-prompts/tree/main/workflows)

Full index with usage labels in `../skills-and-tooling.md`.

---

## Named but not linked

Two repositories referenced in my working notes are **private**, so they're named and described
rather than linked — a link would 404 for you, which is worse than no link:

- **`wp-audit-pipeline`** — a multi-agent audit workflow that fans a change surface out across
  independent reviewers and reconciles the results adversarially. Author: Courtney Robertson.
- **`courtneyr-dev-site`** — the source for my personal site.

Happy to walk through either one live.

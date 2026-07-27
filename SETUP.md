# Setup — installing the rig

How to actually run this, rather than just read it. Four layers, each independently useful. Start
at layer 1; you can stop after any of them.

| Layer | What you get | Time |
|---|---|---|
| [1 · Prompts and skills](#1--prompts-and-skills) | The reusable methods, in your AI coding tool | 5 min |
| [2 · Test environments](#2--test-environments) | Disposable WordPress you can break | 10 min |
| [3 · Automated testing](#3--automated-testing) | A 123-step Playwright runner | 15 min |
| [4 · Docs sites and CI](#4--docs-sites-and-ci) | The documentation and pipeline setup | 30 min |

---

## 1 · Prompts and skills

The methods in this repo are packaged as **agent skills** — Markdown files with YAML frontmatter
that an AI coding tool loads on demand. They're portable across Claude Code, Cursor, Cline, Copilot,
and anything else that reads a prompt file.

```bash
git clone https://github.com/courtneyr-dev/wp-dev-prompts.git
```

**11 skill modules:** `wordpress-dev`, `wordpress-security`, `wordpress-testing`,
`wordpress-playground`, `wordpress-accessibility`, `wordpress-performance`, `prompt-engineering`,
`ui-ux-audit`, `engineering`, `product-management`, `wp-screenshots`.

**6 portable prompts:** plugin scaffolding, block development, testing setup, security review,
accessibility audit, documentation generation.

### Install into Claude Code

Skills live in `~/.claude/skills/`, one directory per skill, each containing a `SKILL.md`:

```bash
mkdir -p ~/.claude/skills && cp -R wp-dev-prompts/skills/* ~/.claude/skills/
```

Restart your session. The skills are then invocable by name.

### Install into other tools

The repo ships config templates under `platforms/` for Cursor, Cline, Copilot, and others. There's
also a `scripts/` directory with setup tooling. Each skill is plain Markdown — worst case, paste the
one you want into your tool's custom-instructions field.

### For documentation and training material

A separate CC0 set, including an `agent-style.md` that defines voice constraints for generated
content:

```bash
git clone https://github.com/courtneyr-dev/developer-education-prompts.git
```

### Writing your own

If you want to package your own methods this way, the format matters more than the content: a
`SKILL.md` with a `name` and a `description` that states **when to use it**, not just what it does.
The description is what the model matches against, so "use when auditing a plugin readme" beats
"readme optimizer." [10 · Audit handoff standard](3-security-methods/10-audit-handoff-standard.md)
is a worked example of a skill that enforces an output format.

---

## 2 · Test environments

You need somewhere disposable to break things. Three options, in increasing order of fidelity —
and the fidelity ladder matters, because
[05 · Release-tracking cadence](1-documentation-practice/05-release-tracking-cadence.md) documents a
case where a lower-fidelity environment silently served an older build and would have produced
confidently wrong documentation.

### WordPress Playground — zero install

Runs WordPress in your browser via WebAssembly. Nothing to install.

- <https://playground.wordpress.net/>
- Load a **blueprint** to get a pre-configured site:
  <https://github.com/courtneyr-dev/WP7-testing> ships one
  (`wp70-comprehensive-blueprint.json`), plus an
  [interactive test launcher](https://courtneyr-dev.github.io/WP7-testing/).

**Caveats that matter:** it defaults to SQLite, so it can't model real database behavior
(collation, character sets, query specifics). It can lag the beta channel. Its nested iframes block
some editor automation. Great for routing, logic, and UI; wrong for anything database- or
server-module-dependent.

### wp-env — containerized, multi-PHP

The official local environment. Real MySQL/MariaDB, and you can pin PHP versions to match a
support matrix.

```bash
npm -g i @wordpress/env
wp-env start
```

Docs: <https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/>

Pin versions in `.wp-env.json` — including a core ZIP URL, which is how you land on a specific beta:

```json
{
  "core": "https://wordpress.org/wordpress-7.1-beta3.zip",
  "phpVersion": "8.2"
}
```

### WordPress Studio — persistent local sites

Free desktop app, full WP-CLI, sites persist between sessions. This is what I use as a **screenshot
and label-verification rig**, because a persistent site can be re-shot at the next milestone
without rebuilding.

<https://developer.wordpress.com/studio/>

### The upgrade-path gotcha

Documented in the methods report, and it costs everyone an hour the first time: reaching a **beta**
from a **stable** install requires the explicit release package.

```bash
wp core update --version=7.1-beta3 --force https://wordpress.org/wordpress-7.1-beta3.zip
wp core update-db
wp core version   # always confirm where you actually landed
```

A bare `--version=<beta>` resolves to the latest **stable** offer instead, so the site never lands
on the beta at all — and you spend the next hour testing the wrong build.

---

## 3 · Automated testing

### The Playwright runner

123 test steps across 14 areas — administration, admin UI, blocks, typography, revisions,
responsive editing, navigation, media, patterns, collaboration.

```bash
git clone https://github.com/courtneyr-dev/wp7-test-automation.git
cd wp7-test-automation
npm install
```

It authenticates by standard login **or pre-exported cookies**, which is what makes it usable
against sites behind two-factor auth or SSO rather than only local installs. It emits JSON results
with an HTML reporter, and captures screenshots on failure.

Read the README's limitations section before relying on it — it names what browser automation
can't cover (genuinely simultaneous multi-user scenarios, custom PHP blocks, subjective UI
assessment, server-side checks, accessibility, cross-browser). Those gaps are why the runbook keeps
a manual exploratory layer.

### The content smoke battery

The minimum viable release check, from
[08 · Methods report](3-security-methods/08-methods-report-wordpress-7-1-beta.md). Runs anywhere
you have WP-CLI:

```
verify-checksums; Posts CRUD; Comments add/reply/edit/trash; Pages CRUD/trash;
custom-post-type CRUD; Categories & Tags add/remove; create a reusable block/pattern;
media upload/edit/delete (confirm sub-size generation); switch themes;
front-end returns HTTP 200; database integrity check.
```

`wp core verify-checksums` is the one to run first every time — it's the canonical core-integrity
check, and it's what surfaced the orphaned-files finding documented in the methods report.

### Plugin-level CI

For your own projects, the pipeline shape that's worked for me — see
[01 · Docs in my own projects](1-documentation-practice/01-docs-in-my-own-projects.md) for live
examples:

| Layer | Tool |
|---|---|
| Coding standards | PHP_CodeSniffer + [WordPress Coding Standards](https://github.com/WordPress/WordPress-Coding-Standards) |
| Static analysis | [PHPStan](https://phpstan.org/) (level 6 is a reasonable target) |
| Unit / integration | [PHPUnit](https://phpunit.de/) |
| End-to-end | [Playwright](https://playwright.dev/) |
| Accessibility | [axe-core](https://github.com/dequelabs/axe-core) inside the Playwright run |
| JS / CSS | ESLint, Stylelint |
| Release | GitHub Actions → WordPress.org on tag |

The highest-leverage addition is a **repo-specific lint** encoding review findings that keep
recurring — see Outpost's `composer lint:section5`, which checks for data leaks, credential
exposure, and i18n gaps. Once a reviewer has caught the same class of thing twice, automate it.

---

## 4 · Docs sites and CI

The four documentation sites in this repo's examples are built with **Astro Starlight** and
published to GitHub Pages.

```bash
npm create astro@latest -- --template starlight
```

<https://starlight.astro.build/>

Live examples to crib the information architecture from — all four are public:

- <https://courtneyr-dev.github.io/post-formats-for-block-themes/>
- <https://courtneyr-dev.github.io/post-kinds-for-indieweb/>
- <https://courtneyr-dev.github.io/outpost/>
- <https://courtneyr-dev.github.io/link-extension-for-xfn/>

### The structure that works

Five sections, ordered by who needs them and when:

1. **Start here** — installation, getting started
2. **Using it** — settings, common tasks, compatibility
3. **Reference** — screenshots, and an interactive Playground preview so a reader can try it
   without installing anything
4. **Help** — FAQ, troubleshooting, **accessibility**, **privacy**
5. **For developers** — integration, design tokens, hooks

Accessibility and privacy get their own pages rather than a paragraph each, because those are the
two questions that block adoption for the people who have to ask them.

### Repo docs, kept separate

Four documents rather than four sections of one, because each has a different reader and a
different update cadence:

| File | Reader |
|---|---|
| `CONTRIBUTING.md` | First-time contributors |
| `TESTING.md` | Contributors running the suite |
| `DEPLOYMENT.md` | Whoever cuts the release |
| `BRANCHING-STRATEGY.md` | Anyone opening a pull request |

Plus `SECURITY.md`, routing vulnerability reports to **private GitHub Security Advisories**. Give
people a private channel before they need it, or they'll use the public one.

---

## Running the methods without any of the tooling

All four layers are optional. The methods stand alone as paper processes:

- The [coverage map](1-documentation-practice/02-coverage-map-and-gap-analysis.md) is a table.
- The [change-coverage receipt](1-documentation-practice/03-change-coverage-receipt.md) is a
  checklist with a gate.
- The [gate ladder](3-security-methods/09-evidence-and-validation-standard.md) is nine rows.
- The [handoff standard](3-security-methods/10-audit-handoff-standard.md) is a required section
  order plus two rules that are easy to get wrong.

Copy the tables into whatever you already use. The tooling makes them faster; it isn't what makes
them work.

## Questions

Open an issue, or find me at [courtneyr.dev](https://courtneyr.dev).

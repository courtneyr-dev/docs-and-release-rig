> Synthesized from Chris Reynolds' (jazzsequence) [claude-skill-pantheon-docs-writer](https://github.com/jazzsequence/claude-skill-pantheon-docs-writer) (MIT per its README; the repo carries no LICENSE file — see `source-provenance.md`), commit `78451e5`, retrieved 2026-09-09. His skill is a complete profile for one docs site; this sheet generalizes the *shape* of such a profile and keeps his Pantheon profile as the worked example, re-expressed. Fill-in template: `templates/site-profile.md`.

# Site profiles — the mechanics a specific docs site imposes

The rest of this skill is about readers and evidence. A **site profile** is about one build: which frontmatter the site requires, where files live, what components render, how a page enters navigation, how a moved URL keeps resolving, and which words the product calls its own. These are facts about a codebase, not judgment calls, and they change per site. Keep them out of the method sheets and load them only when the docs target that site.

## When to load a profile

Load (or create) a profile when the request names a docs site, a docs repo, or a platform whose site has its own conventions — "write this for docs.example.com", "add a page to the Terminus section", "we moved this guide, fix the redirects". Skip it for generic docs, READMEs, and single-repo projects with no site build.

**If no profile exists yet:** build one from the repo before drafting. Read the contributing guide and any style page the site publishes, open three existing pages of the target type and copy their frontmatter shape, find the navigation source and the redirect source, list the components that appear in the pages you read. Record what you *observed*, mark what you *inferred*, and hand the profile to the user for correction. A profile is a set of claims about the build and gets the same evidence markers as any other claim.

## What a profile carries (one slot each; leave a slot empty rather than guessing)

| Slot | What goes in it | Why it matters |
|---|---|---|
| **Scope facets the site tags** | The fixed vocabularies the site filters on: audience, product, integration, CMS or platform variant | These become "inputs to gather" before writing; a page tagged wrong is filed wrong |
| **Page species** | The site's own content shapes (single page vs paginated multi-page guide vs release note) and which Diátaxis need each usually serves | The compass picks the need; the profile picks the container |
| **File locations** | Directory per species; naming rule where the filename is load-bearing (e.g. a release note whose filename becomes its URL) | Wrong directory means wrong URL, wrong nav, or no build |
| **Frontmatter schema** | Required and optional fields per species, with types and allowed values; which fields the build actually reads | A declared field is not a consumed field (see below) |
| **Section conventions** | Fixed opening (intro paragraph, prerequisites heading), fixed closing (related-links heading), heading case per species, where headings start (`##` if the title renders as H1) | Site-wide consistency readers navigate by |
| **Component vocabulary** | Each callout type and when it is warranted; tabs, accordions, tooltips, product cards, term definitions; the reusable-content mechanism (partials or includes) | Search for an existing reusable snippet before writing a new one |
| **Code-fence metadata** | Site-specific fence annotations (prompt markers, non-copyable output lines, file-title labels) | Rendering and copy behavior depend on them |
| **Navigation registration** | Where nav is declared (config file, TypeScript, YAML, frontmatter, directory scan) and the exact call or entry that adds a page or a whole guide | Navigation may not be frontmatter-driven at all |
| **Redirect mechanism** | The file and structure holding redirects; path form (relative, no trailing slash); status code; one entry per old URL including sub-pages; the PR label and the redirect table reviewers expect | A moved page without redirects is a deleted page to every inbound link |
| **Terminology** | Canonical product terms, capitalization, and "formerly called" aliases; standard link text and paths for the surfaces readers are sent to | One term per concept, in the product's own words |
| **Contribution workflow** | Branch naming, commit style, PR body expectations, labels | Repo conventions win over the skill's defaults |
| **Review date field** | Whether the site tracks per-page review dates and what to set on create or edit | Feeds `governance-and-freshness.md` |

## Two rules that come from doing this

**A declared field is not a consumed field.** Pantheon's page type declares an `innav` boolean, yet navigation is built from TypeScript files that never read it. A profile records which metadata the build reads, found by locating the code that reads it, not by reading the schema. Until that code is found, the field's effect is `unverified`. (Same discipline as verifying a feature engages rather than trusting the option exists: `evidence-and-validation.md`.)

**Where release notes and docs diverge, the profile says so explicitly.** On Pantheon the docs use title-case headings and rich components; release notes use sentence case and plain Markdown, a separate frontmatter schema, and a filename that determines the URL. A profile that lists only the docs rules will produce wrong release notes. Authoring rules for release notes themselves: `content-types.md` § Changelog / release notes.

## Worked example: docs.pantheon.io (as profiled by jazzsequence)

Re-expressed from his skill; verify against `pantheon-systems/documentation` before relying on any path, since his own maintenance note says to.

- **Scope facets:** audience (`development`, `agency`, `business`, `sysadmin`, `marketing`), CMS (`wordpress`, `drupal`, both, or `--`), product, integration; each an array in frontmatter.
- **Species:** *doc* (one Markdown file under `src/source/content/`) for explanation, reference, and standalone how-tos; *guide* (a directory of pages under `src/source/content/guides/⟨name⟩/`) for tutorials and multi-phase how-tos, all pages sharing one `title` with a unique `subtitle` each; *release note* (`src/source/releasenotes/YYYY-MM-DD-slug.md`, filename → `/release-notes/YYYY/MM/slug`, dated to the go-live date).
- **Frontmatter:** docs require `title`, `description`, `contenttype` (`[doc]`/`[guide]`), `innav`, `categories`, `cms`, `audience`, `product`, `integration`, `reviewed` (ISO date; set to today on create); optional `subtitle`, `tags`, `contributors`, `showtoc`. Release notes use a different schema: `title`, `published_date`, `published_at` (full timestamp; drives feed order), `categories` (from a JSON list in the repo, including `action-required`), `description`.
- **Sections:** intro paragraph with no heading → `## Before You Begin` (prerequisites as bullets; variable-export callout here if the guide uses shell variables) → body from `##`, rarely deeper than `###` → optional `## Troubleshooting` with each error message verbatim as a `###` heading → `## More Resources` (3–5 links, always last). Docs headings in Title Case; release-note headings in sentence case.
- **Components:** `<Alert>` with `type` `info` / `danger` / `export`; `<Accordion>` for optional detail; `<TabList>`/`<Tab>` for CMS-specific paths; `<Partial file="…" />` for reuse (search `src/source/partials/` first; partials carry no frontmatter); `<Popover>` tooltips; `<ProductGroup>`/`<Product>` cards; `<dfn id="…">` for glossary-indexed terms. Release-note bodies are plain Markdown, no components.
- **Fence metadata:** `bash{promptUser: user}` adds a non-copyable prompt; `bash{outputLines: 2-6}` marks output; `yaml:title=pantheon.yml` labels a file excerpt.
- **Navigation:** declared per section in `src/components/omni-components/*.ts` (get-started, workflows, go-live, web-infrastructure, account-management, terminus, security, support). Add a page with `simpleLink(path, title)`, a nested group with a children array, a whole guide with `getGuideDirectory("guides/⟨name⟩", "Title")` (sub-page titles from `navtitle`, else `subtitle`). Frontmatter does not place pages in nav.
- **Redirects:** entries in the `RedirectMap` object in `src/middleware.ts` as `"/old": "/new"`; relative paths, no trailing slash on the old path, all 301, one entry per old URL including every guide sub-page; PR gets the **Redirect** label and a From/To table in its body.
- **Terminology:** Site Dashboard; My Dashboard; Professional Workspace (formerly Organization); Supporting Workspace (formerly Supporting Organization); Multidev; Terminus (always capitalized). Standard orientation links exist for the dashboards and workspaces; orient the reader ("Go to the Site Dashboard") before naming a control ("Click **Backup**").
- **Contribution:** branch `⟨issue⟩-⟨short-description⟩`; conventional commits (`docs: …`); PR explains what and why.
- **Style overlay:** Pantheon's own guide first, Google Developer Style Guide where it is silent (`style-overrides.md` § Google), plus the site's inclusive-language page (`accessibility-and-localization.md`).

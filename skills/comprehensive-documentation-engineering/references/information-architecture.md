> Sections on landing pages, the list rule, and two-dimensional structures are adapted from Diátaxis's *Diátaxis in complex hierarchies* page, © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — this file is therefore CC BY-SA 4.0. **Provenance note:** that page was removed from the live diataxis.fr site (repo commit `abfae1f`, "Tidied up some files"); it is included here from the source repository's history, cross-confirmed against a 2026-08-02 site mirror, and nothing on the current site contradicts it. If future official guidance supersedes it, the official site wins. Remaining sections synthesize MIT/CC0 sources (anivar, docs-and-release-rig).

# Information architecture

## Organize by user need, never by org chart

Users think in what they need to do — learn, accomplish, look up, understand — not in which team built the feature. Team- or component-mirrored docs break at every reorg and mean nothing to outsiders. Guides and tutorials organize by **outcome**; only reference mirrors the machinery's structure. Per-type naming conventions make types recognizable at a glance: "Build a ⟨thing⟩" · "How to ⟨goal⟩" · "⟨Resource⟩ reference" · "Understanding ⟨concept⟩" / "About ⟨topic⟩".

A recognizable full shape — used **only as genuine material exists** (the anti-scaffold rule always wins):

```
docs/
├── getting-started/   # quickstart + first tutorial
├── tutorials/         # learning-oriented
├── guides/            # how-to, by domain
├── reference/         # API / SDK / configuration
├── concepts/          # explanation
├── integrations/      # partner guides
├── operations/        # runbooks, config reference
├── migration/         # version transitions
├── changelog/
└── glossary/
```

## Depth: two defaults in deliberate tension

1. **Broad-shallow default (two levels: category → document).** Beyond two levels readers lose their place; research on findability favors breadth. At genuine scale, prefer faceted navigation (by topic, type, language) and good search over deeper folders.
2. **The sanctioned exception:** when one page would otherwise carry forks (install per platform) or a contents list exceeds **~7 items** without mechanical order, add a hierarchy layer — but the new parent must be a **genuine landing page**, and grouping must still follow the type principles. Documentation should be as complex as it needs to be; even complex structures navigate well when the arrangement is principled.

These two rules come from different sources and pull differently; apply the default first and reach for the exception only when the list rule or a forked page forces it. Diátaxis posits four kinds of documentation, **not** four mandatory top-level boxes.

## Landing pages are overviews, not lists

A landing/contents page introduces its material: headings and short snippets of context before the links, reading like an overview. You are authoring for a human, not fulfilling a scheme. Sub-group long lists under headed clusters, each with a sentence of context.

## Two-dimensional structures

When audiences (users / developers / contributors) or platforms (cloud A / cloud B / on-prem) make the product effectively *different products for different people*, structure by that axis first, then apply the type ordering within each branch. Think user-first: does a developer need the user-facing material first? Do contributors need entirely separate how-to guides? Share what's genuinely shared (reference, concepts); separate what differs (getting started, tutorials, workflow-divergent how-tos); keep operational runbooks internal. Within one portal: clearly labeled per-audience entry paths ("I'm a partner →…") and progressive disclosure — never conditional audience sections inside one document.

## Cross-linking strategy

Every document carries: **prerequisites** (top) · **inline links** for terms, APIs, and concepts mentioned · **next steps** (bottom) · **related** content in other types (reference ↔ how-to ↔ explanation). No dead ends. Critically: linking-out-instead-of-digressing is the *mechanism* that keeps the four types apart — every "link out instead" redirect in the type sheets must land on a real target this architecture wires up. A type boundary not backed by a working cross-link is just a place where content gets lost. In single-type runs, link only to types that exist; omit the link rather than scaffolding a target.

## Product docs-site shape that works in practice

Five sections ordered by who needs them and when: **Start here** (install, getting started) → **Using it** (settings, common tasks, compatibility) → **Reference** (facts, screenshots, an interactive preview/sandbox where possible) → **Help** (FAQ, troubleshooting, **accessibility**, **privacy** — the last two as their own pages, because they're the questions that block adoption for the people who must ask them) → **For developers** (integration, tokens, hooks). Progression runs user-facing → developer-facing, with search.

## Repository documentation

Split by reader and update cadence, not merged into one file: `CONTRIBUTING.md` (first-time contributors) · `TESTING.md` (contributors running the suite) · `DEPLOYMENT.md` (whoever cuts releases) · `BRANCHING-STRATEGY.md` (anyone opening a PR) · `SECURITY.md` routing vulnerability reports to a **private** channel — give people the private channel before they need it, or they'll use the public one. The README is the front door: a brief overview with a documentation section linking each existing docs section in one sentence — never a mirror of the docs.

## Tooling adaptation

Detect and respect docs tooling before proposing structure: `mkdocs.yml`, `conf.py` (Sphinx), `docusaurus.config.*`, `antora.yml`, `hugo.toml`; a generator config beats a bare `docs/`; fall back to Markdown under `docs/`. Detect reference generators too — they trigger the autodoc rule (`reference.md`). Propose minimal changes to partially-aligned structures; keep what already works; follow the repo's naming conventions. Search vocabulary: include exact error messages verbatim — that's what users search.

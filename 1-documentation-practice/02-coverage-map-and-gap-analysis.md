# Coverage map & gap analysis

<!-- canonical-source-banner -->
> **The reusable method here is now canonical in the agent skill.** It lives in executable form at [`../skills/comprehensive-documentation-engineering/`](../skills/comprehensive-documentation-engineering/) — see [`references/release-documentation.md`](../skills/comprehensive-documentation-engineering/references/release-documentation.md) · [`templates/coverage-map.md`](../skills/comprehensive-documentation-engineering/templates/coverage-map.md) · [`workflows/test-release.md`](../skills/comprehensive-documentation-engineering/workflows/test-release.md). This page is kept as the **real-work provenance**: the retro, worked example, and prompts that produced the rule. For the current method, follow the skill; read this for the evidence behind it.


The core documentation-audit artifact. It answers one question honestly: **for
everything this release claims to ship, which claims have we actually verified, and
which are we repeating on faith?**

Publication strategy specific to one outlet is omitted; the method and a real,
public-links-only excerpt of the output remain.

---

## Why this artifact exists

When a release ships, several documents describe it: the release announcement, the dev
notes, the field guide, the issue tracker milestone, and a community roundup. Each is
partial. Writers reading them tend to produce a fifth partial document that looks
complete, because nothing in the process ever asks "what did we skip?"

The coverage map forces that question by putting two columns next to each other:

- everything the release claims, harvested from **all** the sources, and
- our verification status for each item.

Anything without a verification status is a gap, and gaps get published as gaps.

## The originality guardrail

A note that goes at the top of every coverage map I build:

> This synthesizes a community roundup that is shared widely and explicitly asks
> contributors **not** to copy-paste it, because duplicate content across many blogs
> hurts everyone involved. Everything below is facts plus public links **in our own
> words** — never reuse the roundup's phrasing. Write original descriptions, our own
> examples, our own screenshots.

Also excluded by default: any draft or preview URL carrying a preview token, internal
chat archive links, and shared drive assets. Those get swapped for public URLs once the
official docs publish — which for this cycle was around RC1.

## What this cycle's map contained

The map's shape — dated update log, verified-first-hand list, audience-grouped gap table,
quality-of-life cluster, cross-links — is now the fill-in template in the skill
([`templates/coverage-map.md`](../skills/comprehensive-documentation-engineering/templates/coverage-map.md)).
What follows is what that shape *held* for WordPress 7.1: the evidence, not the recipe.

**1. A dated update log at the top.** Sources move; the map records when. A real entry
from this cycle:

> **Update, July 24 — dev notes dropped early.** Dev notes started publishing July
> 22–24, ahead of the RC1 estimate. Now-public links to swap in, plus two corrections
> and several new items:
>
> - **Client-side media** ([dev note](https://make.wordpress.org/core/2026/07/22/client-side-media-processing-in-wordpress-7-1/))
>   — **correction:** the gate is not `is_ssl()`. It requires a Chromium version floor,
>   a `Document-Isolation-Policy` header on editor screens, a CSP allowing
>   `worker-src 'self' blob:`, and runtime capability checks. Other browsers fall back.
>   **Hooks correction:** `wp_generate_attachment_metadata` *does* fire, twice; the
>   hooks that do not fire are `wp_image_editors`, `image_memory_limit`, and
>   `image_make_intermediate_size`. The stated trust model is "a performance
>   optimization, not a trust boundary."
> - **React 19 punted** ([dev note](https://make.wordpress.org/core/2026/07/24/react-19-punted-beyond-wordpress-7-1-experiment-in-gutenberg/))
>   — 7.1 stays on React 18.3. This corrects one of our own test specs.
> - **Editor components** ([dev note](https://make.wordpress.org/core/2026/07/23/editor-components-updates-in-wordpress-7-1/))
>   — a **new** plugin-compatibility surface we had not tracked at all: a deprecated
>   `Navigation` component was removed, a form-control sizing prop became a no-op, and
>   a styling library migration made a `css` prop a no-op.
> - **Icons API** ([dev note](https://make.wordpress.org/core/2026/07/24/registering-and-rendering-svg-icons-in-wordpress-7-1/))
>   — signatures confirmed, with a nuance worth documenting: sanitization drops `fill`
>   from the root `<svg>` element, so standalone icons render in the default color
>   unless `fill` is set on the inner shapes.

Note what that log captures that a rewritten doc would lose: **two of our own prior
claims were wrong, and we say so with the correcting source attached.** Readers who
acted on the old version need the delta.

**2. What we verified first-hand.** A plain list. On this cycle it was 20 of 21 headline
features tested against a real beta build. This list is the differentiator — it is the
part of the eventual article nobody else can write by paraphrasing.

**3. The gap table, grouped by audience.** Each row is one item, a one-line factual
description written in our own words, the authoritative public reference, and our
status. Real rows:

| Item | One-line description | Public reference | Status |
|---|---|---|---|
| Media Library infinite scroll on by default | Grid infinite-scrolls by default, with a per-user opt-out on the profile screen; the filter now defaults to true | [Trac #65564](https://core.trac.wordpress.org/ticket/65564) | untested |
| Cover block: limit video providers | New attribute to curate or disable URL-based video embeds | [PR #80092](https://github.com/WordPress/gutenberg/pull/80092) | untested |
| Search block: native `<search>` element | Opt-in native landmark element; input color applies when the button is off | [PR #78485](https://github.com/WordPress/gutenberg/pull/78485) · [PR #77219](https://github.com/WordPress/gutenberg/pull/77219) | untested |
| Icons API | Registration and render functions plus REST endpoints; **breaking:** the icons package moved to `fill="currentColor"` | [Issue #75715](https://github.com/WordPress/gutenberg/issues/75715) · [PR #79320](https://github.com/WordPress/gutenberg/pull/79320) | untested |
| Viewport breakpoint customization | Themes can define custom breakpoints for responsive behavior and block visibility | [Issue #75707](https://github.com/WordPress/gutenberg/issues/75707) | untested |
| Text shadow in theme.json | New typography property, theme-only for now | [PR #73320](https://github.com/WordPress/gutenberg/pull/73320) | untested |
| Post editor always iframed | The post editor is unconditionally iframed, where it was conditional in the prior release — **breaking-ish for block developers** | [PR #75187](https://github.com/WordPress/gutenberg/pull/75187) · [migration guide](https://developer.wordpress.org/block-editor/reference-guides/block-api/block-api-versions/block-migration-for-iframe-editor-compatibility/) | partial |
| Editable blocks inside Custom HTML | Static HTML with editable inner blocks | [PR #79115](https://github.com/WordPress/gutenberg/pull/79115) | **verified** |
| Connectors: username + application-password auth | An alternative to API keys for AI connectors; masked, supports constants and environment variables | [PR #79403](https://github.com/WordPress/gutenberg/pull/79403) | untested — **security-adjacent** |
| Accessible tooltip API | New tooltip and toggletip helper functions | [Trac #51006](https://core.trac.wordpress.org/ticket/51006) | untested |

**4. A quality-of-life cluster.** Small polish items get mentioned as a group with links,
not enumerated individually. Enumerating everything is how a useful doc becomes a
changelog nobody reads.

**5. Cross-links to related work.** Items that belong to a different deliverable than the
one prompting the audit — for this cycle, a host-tunable configuration knob that
belonged in an operations brief and was missing from it. The coverage map is often
where you discover a gap in a *different* document.

---

## The rule underneath all of it

**A gap you have written down is a task. A gap you have not written down is a future
correction.** The coverage map's real function is to make incompleteness visible early
enough to do something about it, and to make the eventual "we didn't cover X" statement
a deliberate editorial choice rather than an accident.

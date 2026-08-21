> Synthesized from Anivar Aravind's [developer-docs-framework](https://github.com/anivar/developer-docs-framework) (MIT) style system and style guide, with Diátaxis per-quadrant language doctrine (diataxis.fr, CC BY-SA 4.0 — the "default" section is an adaptation and carries that license). 2026-08-20.

# Writing style — default and pluggable overrides

Style is configurable. The **default** is Diátaxis per-quadrant voice — style follows function, and the writing style reinforces each type's purpose. An organization's own style guide, or one of the named overlays below, overrides the default **only when explicitly chosen** (by the user or the repo's documented conventions). A skill or repo may also impose house-style constraints (e.g. a fixed English variant, a voice-constraints file) — record such constraints explicitly so they stay overridable.

## Universal rules (apply under every style)

- Active voice; second person for instructions; present tense for descriptions (passive only when the actor is unknown/irrelevant; future only for genuinely-later events).
- Simple words ("use" not "utilize"); sentences ≤ ~25 words; one idea per paragraph; confident statements without hedging.
- **One term per concept, everywhere**, matched to the product UI's own label; industry-standard names for established concepts (a webhook is a "webhook"); define product terms on first use or link the glossary; renames propagate everywhere.
- Global readability: no idioms, sports/cultural metaphors, or humor; acronyms spelled out on first use ("Transport Layer Security (TLS)"); ISO-8601 or written-out dates; inclusive language (they/them; allowlist/blocklist; primary/replica; "stop the process"; no ableist phrasing).
- Formatting: sentence-case, scannable, level-ordered headings · numbered lists for sequences, bullets otherwise, parallel construction · tables only for uniform structured data · descriptive link text (never "click here"), section-deep, relative where internal · code font for paths/commands/params/values, **bold** for UI elements (**Settings > General**) · admonitions ≤2–3 per page (Note = genuinely non-obvious; Warning = data loss/security only).
- Code examples: complete and runnable (imports, initialization), realistic values (`user@example.com`, not `foo`), language-tagged blocks, expected output where helpful, `TODO:` markers on user-supplied values, comments explain *why* not *what*, tested (see `evidence-and-validation.md`).
- Multi-audience: identify the primary audience per document; separate paths when needs diverge; progressive disclosure; label audience-specific passages; never write down ("as you probably know…") or up ("simply configure…").

## Default: Diátaxis per-quadrant style

| | Voice | Tone | Signature phrasing |
|---|---|---|---|
| Tutorial | first-person plural "we" | encouraging, patient | "In this tutorial, we will…" · "First, do x. Now, do y." · "The output should look something like…" · "Notice that…" · "You have built…" |
| How-to | second person, conditional imperatives | direct, efficient | "This guide shows you how to…" · "If you want x, do y." · "Refer to the X reference for all options." |
| Reference | impersonal, declarative | austere, neutral, factual | "Returns a…" · "Sub-commands are: a, b, c." · "You must use a. Never d." |
| Explanation | conversational, perspective allowed | thoughtful, exploratory, opinionated | "The reason for x is historical…" · "W is better than z, because…" · "Some prefer w (because z). This can be a good approach, but…" |
| Troubleshooting | second person | calm, reassuring | "If you see this error, check…" · "This usually means…" |
| Migration | second person | clear, reassuring | "This change requires…" |

Deliberate per-type variation — including opinion in explanation and austerity in reference — is the default's defining difference from uniform corporate styles.

## Overrides (opt-in overlays; apply only their listed divergences)

**Google** (open source, Google ecosystems, accessibility-first): always "you" — even tutorials; uniform conversational tone including reference; avoid opinion everywhere ("we recommend" sparingly, only for settled best practice); the word list (omit "please", "simple/easy"; "preceding/following" not "above/below"; "for example" not "e.g."; "use" not "leverage/utilize"; descriptive link text); sentence-case headings; accessibility elevated (alt text, no color-only meaning, no skipped heading levels, text alternatives everywhere).

**Microsoft** (enterprise B2B, UI-heavy products): warm, relaxed brand voice everywhere including reference ("Use this method to get… you'll get back a `User` object"); "you'll build", not "let's build"; extensive bias-free communication rules; device-neutral verbs ("select" not "click"); UI-text conventions (**File > Save As**, bold buttons/labels, Ctrl+S); error-message docs lead with plain-language "what went wrong / what to do", error code included for search; complete compilable examples with imports and output-as-comments.

**Stripe** (API-first, DX-as-revenue): outcome-first organization everywhere — primary navigation by what the developer achieves ("Accept a payment"), API reference separate; side-by-side prose+code layouts; interactive, tabbed, copyable multi-language examples (functionally equivalent, idiomatic); per-error documentation (exact code, one-sentence why, specific fix, guide link); docs-as-product culture (docs in career ladders and reviews; a feature isn't done until documented; writing support for engineers); personalization (detected language first, live keys in examples when signed in).

**Canonical** (infrastructure/open source, purest Diátaxis): everything in the default, *plus* documentation as an **engineering practice** (shared responsibility, code-rigor review, scientific method: critical, exploratory, collaborative, iterative); four organizational pillars — Direction (standards/metrics), Care (living-concern culture), Execution (consistent workflows), Equipment (tools that serve the work); starter packs (pre-configured structure, per-type templates, CI purity checks, style linting); technical authors embedded in engineering; terminology governance at portfolio scale.

**Minimal** (startups, MVPs, internal tools — when "good enough now" beats "perfect never"): minimum viable set — README (what-it-is + quickstart combined) and generated API reference first; add the top-3 how-tos and a changelog when users ask; tutorial/troubleshooting when adoption or support demand it; auto-generate what you can (OpenAPI→reference, doc-comments→SDK reference, conventional commits→changelog) and enhance later; telegraphic style acceptable (bullets, fragments, code blocks — correctness over polish); ship without perfection (working example > polished prose; incomplete-but-accurate > comprehensive-but-stale; in-the-README > an unvisited site). **Graduation triggers:** repeated support questions → how-tos; onboarding >30 min → tutorial; partners arriving → integration guides; 2+ major versions → migration guides.

## Divergence summary

| Convention | Default (Diátaxis) | Google | Microsoft | Stripe | Canonical | Minimal |
|---|---|---|---|---|---|---|
| Tutorial person | we | you | you | you | we | any |
| Tone | varies by type | uniform conversational | uniform warm | outcome-driven | varies by type | telegraphic |
| Opinion | in explanation | avoid | avoid | sparing | in explanation | fine |
| Coverage ideal | needs-driven | needs-driven | needs-driven | outcome catalog | full Diátaxis | 2–3 docs |

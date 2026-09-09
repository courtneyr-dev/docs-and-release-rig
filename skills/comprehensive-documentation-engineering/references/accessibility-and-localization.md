> Accessibility synthesized from Anivar Aravind's developer-docs-framework (MIT) and docs-and-release-rig (CC0). Localization synthesizes anivar (MIT) and the Diátaxis translation program (diataxis.fr, CC BY-SA 4.0 — the translation-practice subsection is an adaptation and carries that license). 2026-08-20.

# Accessibility and localization

## Accessibility

Documentation and its examples must be usable by everyone:

- **Meaningful alt text** on every image; describe what the image conveys, not "screenshot".
- **Never rely on color alone** to convey meaning ("the red button" → "the **Delete** button"; diagram legends carry labels, not just hues).
- **Proper heading hierarchy** — no skipped levels — so screen readers can navigate structure.
- **Real code blocks, never images of code** — screen readers and copy-paste both need the text.
- **Text alternatives** for video, audio, and diagrams.
- **Keyboard-only navigation** works through the docs site; test it.
- **Sufficient contrast** in diagrams and screenshots — and the accessible choice is usually the clean screenshot (a demo color that trips a contrast warning looks bad in the shot too).
- Treat **accessibility as its own docs-site page**, not a buried paragraph — it's one of the questions that blocks adoption for the people who must ask it (privacy is the other).

Inclusive language serves accessibility and global readability together; `style-overrides.md` carries the one-line rule, this table carries the substitutions.

### Inclusive language substitutions

Categories and examples after Pantheon's inclusive-language page as carried in jazzsequence's pantheon-docs-writer (MIT); re-expressed. Apply everywhere, including code comments, diagrams, and UI strings you quote.

| Class | Avoid | Use instead |
|---|---|---|
| Ableist | sanity check · crazy, insane · blind to · crippled, lame · OCD (as a trait) | validation, verification · unexpected, surprising · unaware of, ignore · broken, slow, hindering · meticulous |
| Violent | kill, murder, STONITH as metaphors · "one throat to choke" | stop, end, terminate the process · single point of accountability |
| Gendered | he/she as default · "you guys" · "easy enough for your mom/grandma" | they/them · "you all", "everyone" · say who the audience is |
| Racial | whitelist / blacklist · master (branch, primary) · master/slave · grandfathered in | allowlist / blocklist · main · primary / replica (or secondary) · legacy, exempt from |
| Exclusionary framing | "victim of", "suffers from" · North-American idioms ("circle back", "put a pin in it") · unexpanded acronyms | "has", "experiences" · the literal phrase · expand on first use |

When a project's own guide lists more terms, its list wins; when it conflicts with this table, follow the project and record the divergence in the site profile (`site-profiles.md`).

## Localization

Support translation and localization **without breaking semantic structure** — a translated doc set keeps the same Diátaxis types, the same navigation, and the same meaning.

**When to localize:** a significant share of users don't read your primary language; you're entering markets where language blocks adoption; partners in a region require it.

**What to localize first (by impact):** quickstart/getting-started → error messages and troubleshooting (support-load reduction) → core how-to guides → API reference (if comments need translating).

**Localization mechanics:** use a translation-management system integrated with the docs-as-code workflow; keep source content simple and translatable (no idioms, short sentences); maintain a translator glossary; **don't translate code** — only comments and descriptions; mark one language as source-of-truth and track translation freshness against it; machine translation with human review for high-volume, lower-stakes content.

### Translation practice (adapted from the Diátaxis translation program)

- **Translate the meaning and force of the ideas, not the literal wording.** Idiomatic, unforced target-language prose; native sentence structures; better local metaphors where they exist.
- **Find and consistently use native-language key terms** — even where it's common to borrow the English term, prefer a native alternative used consistently, not an imported word.
- **Start with the page that gathers all the key terms** (the "Start here" / overview page) so terminology decisions are made once and cascade.
- **Keep functional references and placeholders untranslated** — file names, code identifiers, and numbered placeholder symbols stay as they are.
- **Watch context beyond the string.** String-by-string translation invites tunnel vision; keep the whole page's meaning in view.
- **Collaborative correction etiquette:** fix clear errors (spelling, grammar, lost meaning, unidiomatic rendering) directly; discuss stylistic or judgment calls before changing them.

### Generating non-English content correctly

When *producing* content in a non-English project language (not just translating docs), the enforcement rules — mandatory diacritics across every human-readable file type, technical-terms-stay-English judgment, per-language typography, format-specific UTF-8 editing care, and generate-correctly-from-the-start — live in `repo-workflow-practices.md` § Non-English content enforcement, with French as the worked example.

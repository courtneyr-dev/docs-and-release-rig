# Source provenance and attribution

This skill is an original synthesis of nine sources. It does not reproduce any source verbatim at length; it re-expresses methods and merges duplicated rules into canonical form. The full research report, inspection record, conflict-resolution log, and the capability-to-file traceability matrix live in `provenance/research-report.md`, `provenance/capability-ledger.md`, and `provenance/traceability-matrix.md`.

**No source author endorses this combined skill.** In particular, Diátaxis is the work of Daniele Procida; this skill encodes and adapts the framework but is not endorsed by him or by any other source author.

## Sources (retrieved 2026-08-20)

| # | Source | Author | License | Revision |
|---|---|---|---|---|
| 1 | "Diataxis Meets AI" article | Romain Lespinasse | site content (ideas/methods only) | web, 2026-08-20 |
| 2 | rlespinasse/agent-skills | Romain Lespinasse | MIT | `a6c5b6c` |
| 3 | keithpatton/diataxis-agent-skill | Keith Patton | CC BY-SA 4.0 | `5b095a5` |
| 4 | peterknego/diataxis-docs-skill | Peter Knego | MIT AND CC-BY-SA-4.0 | `de11e3b` |
| 5 | Claude Marketplaces listing | claudemarketplaces.com | third-party summary | web, 2026-08-20 |
| 6 | sammcj/agentic-coding | Sam McLeod | Apache-2.0 | `25cb214` |
| 7 | anivar/developer-docs-framework | Anivar Aravind | MIT (upstream methods have own licenses) | `c0e9445` |
| 8 | Diátaxis (diataxis.fr / evildmp repo) | Daniele Procida | CC BY-SA 4.0 | `957c09c` |
| 9 | courtneyr-dev/docs-and-release-rig | Courtney Robertson | CC0 1.0 | `d9ca62d` |

Source 7 itself builds on Diátaxis (CC BY-SA 4.0), Google OpenDocs (Apache-2.0), the Good Docs Project (CC BY 4.0), the Google Developer Documentation Style Guide (CC BY 4.0), and observed Stripe/Canonical practice; those upstreams are credited where their material appears. Source 4's C4 material derives from c4model.com (Simon Brown, CC BY 4.0).

## How licensing shapes this package

The skill is dual-licensed by file (see `LICENSE`):

- **CC BY-SA 4.0** — reference sheets that adapt Diátaxis doctrine (`diataxis-foundations.md`, `compass-and-classification.md`, `tutorials.md`, `how-to-guides.md`, `reference.md`, `explanation.md`, the Diátaxis-derived portions of `anti-patterns.md`, `information-architecture.md`, `style-overrides.md`, and `accessibility-and-localization.md`). ShareAlike requires this; each such file carries an attribution header naming its source pages and the changes made.
- **MIT** — the original workflow logic, router, templates, scripts, tests, and synthesis (SKILL.md, `workflows/*`, `templates/*`, `scripts/*`, `tests/*`, and reference files that are original or derive only from MIT/Apache/CC0 sources).

Rationale for the split: licensing everything CC BY-SA would burden the code with a license not designed for code; licensing everything MIT would violate Diátaxis's ShareAlike terms. A skill built on someone else's methodology inherits that methodology's license wherever it reproduces the methodology's text. Where a source's license would prevent direct inclusion, the method is re-expressed in original language, the source is linked, and the limitation is recorded here.

To cite Diátaxis itself, refer to [diataxis.fr](https://diataxis.fr) per its colophon; `CITATION.cff` carries machine-readable citation metadata for this skill and its principal sources.

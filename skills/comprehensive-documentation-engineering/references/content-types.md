> Synthesized from Anivar Aravind's [developer-docs-framework](https://github.com/anivar/developer-docs-framework) (MIT), which itself builds on Diátaxis, Google OpenDocs, the Good Docs Project, and observed Stripe/Canonical practice. Re-expressed, 2026-08-20. Skeleton templates: `templates/content-templates.md`.

# The 14 content types

Concrete document species mapped onto the four needs. Provide the types the audience actually needs — never all fourteen by default.

| Type | Quadrant | Reader's mindset | Freshness (see governance) |
|---|---|---|---|
| Tutorial | Learning | "I'm new; teach me by doing" | tested quarterly |
| Quickstart | Learning+Task hybrid | "I'm experienced; fastest path to working" | verified quarterly |
| How-to guide | Task | "I need to accomplish X now" | reviewed quarterly |
| Integration guide | Task (partner) | "I need to connect my system to yours" | quarterly |
| Migration guide | Task (versions) | "Upgrade without breaking my system" | verified at release |
| Troubleshooting | Task (problems) | "It's broken; fix it now" | monthly, with support data |
| API reference | Information | "Exact specs to code against" | matches current release |
| SDK reference | Information (per-language) | "The exact signature in my language" | matches current release |
| Configuration reference | Information (operational) | "What does this setting do; valid values" | every release |
| Changelog / release notes | Information (temporal) | "What changed in this release" | every release |
| Explanation | Understanding | "Why does it work this way" | semi-annual |
| Architecture guide | Understanding (system) | "System design context for decisions" | semi-annual |
| Glossary | Information (terminology) | "What does this term mean here" | annual |
| Runbook | Task (operational) | "I'm on call; respond to this incident" | after every incident |

Tutorial, how-to, reference, explanation: full rule sheets in their own files. The rest:

## Quickstart
Speed-optimized demonstration for the already-competent — it demonstrates, it does not teach. Strip to: prerequisites (one-liners with links) → install → minimum viable configure → one meaningful call → visible meaningful result → next steps. Target under 5 minutes (10 hard max). No architecture, no choices, no multi-path branching, and never skip the "verify it works" step. The README-as-quickstart combination is legitimate for small projects (Minimal style).

## Integration guide
Documents the **integration**, not just your API: overview + interaction-flow diagram → prerequisites → authentication → core steps showing **both sides** (your request/response *and* what the partner's endpoint must do: status to return, deadline, signature verification, idempotency) → failure/retry behavior (backoff schedule, pause conditions, notifications) → error table (error, cause, resolution) → sandbox testing → production verification → **production-readiness checklist** (security / reliability / monitoring / compliance / support-escalation-SLA) → support channels. No internal jargon without definition.

## Migration guide
Lead with impact: what changed, why, estimated effort, breaking-change and deprecation counts. Then: pre-migration checklist (backup, changelog link, required starting version — one guide per major transition, chained) → automated migration first (codemods/scripts: what they handle, what stays manual) → breaking changes organized **by change, not by file**, each as *what changed / why / before-code / after-code* → deprecations table (deprecated, replacement, removal target) → optional new features → verification → **rollback** → help channels.

## Troubleshooting
Organize by **observable symptom** (with exact error messages — that's what people search), never by internal cause or component. Per entry: symptom → diagnosis (confirm which problem this is; diagnostic command) → **solution first** → brief "why this happens" linking to explanation. Order causes by likelihood. Cover the actual top support drivers.

## API reference
Per endpoint, always the same shape: method+path → one-sentence verb-first description ("Creates a…", incl. side effects like emitted webhooks) → authentication → parameters (path/query/body tables: name, type, required, default, description with ranges/formats/constraints) → request example (realistic values) → response example (success + error) with every field documented → error table (status, code, what's wrong **and how to fix**, e.g. "401 — key missing or invalid; verify at ⟨dashboard⟩"). Be exhaustive; consistency across endpoints is non-negotiable; generated output gets human review (autodoc rule in `reference.md`).

## SDK reference
Language-idiomatic per ecosystem (Pythonic Python, Javadoc-shaped Java — don't force one format across languages); precise types, exceptions, nullability; idiomatic examples; behaviorally in sync with the API reference at a different abstraction level. Per class/module: overview → constructor → methods (signature, params, returns, exceptions, example) → types/models → constants.

## Configuration reference
Per parameter: exact name → what it controls → type and constraints → default → required? → practical example → notes (interactions with other parameters, caveats).

## Changelog / release notes
Categories: **Added / Changed / Deprecated / Removed / Fixed / Security**. Version + date + one-sentence headline of the biggest change. Every entry specific ("Fixed null-pointer in payment processing when currency is undefined", never "various improvements") and linked to its documentation; breaking entries link the migration guide; distinguish user-facing changes from internal refactoring. Release notes are the broader-audience retelling of the same facts.

## Architecture guide
System overview + diagram (see `diagrams.md` for evidence-traced C4) → components and responsibilities → data flow and communication patterns → design decisions and trade-offs (ADR format works; template provided) → scalability/reliability → security architecture → system-specific glossary.

## Glossary
Product-specific plain-language definitions; note where usage differs from the industry ("In our system, a 'workspace' refers to…"); aliases; cross-references; links to relevant docs. Doubles as the terminology-governance instrument.

## Runbook
Written for stress: short sentences, numbered steps, exact commands (no pseudocode, no "something like"), decision trees ("if error X → §3; if Y → §4"). Header: owner, last-verified date, escalation contact. Sections: access table (system → how to reach it) → monitoring (alert, severity, meaning) → scenarios (symptoms, impact, resolution steps, escalate-after threshold) → post-incident checklist (update this runbook, file the review, close monitoring gaps).

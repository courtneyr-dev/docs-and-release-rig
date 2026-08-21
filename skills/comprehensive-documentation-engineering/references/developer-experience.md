> Synthesized from Anivar Aravind's developer-docs-framework (MIT — DX rules, audience matrix, funnel, partner rules, metrics; Stripe patterns observed from public docs). 2026-08-20.

# Developer experience

## Audiences and jobs to be done

Never write for "developers" as a monolith. The matrix:

| Audience | Mental state | Primary question | Key content types |
|---|---|---|---|
| New developers | curious, uncertain | "Can I use this?" | Quickstart, Tutorial |
| Building developers | focused, time-pressed | "How do I do X?" | How-to guides, API reference |
| Evaluating developers | analytical, comparing | "Is this the right choice?" | Explanation, Architecture |
| Partner integrators | external context | "How does this fit my system?" | Integration guide, SDK reference |
| Internal engineers / operators | operational, on-call | "How do I fix this?" | Runbook, Config reference |
| Decision makers | strategic, non-coding | "What does this enable?" | Architecture overview, Explanation |

Apply: identify which rows exist for this product → check each row has its key types → don't mix (a new-developer quickstart carries no operator configuration) → give each audience a clear labeled entry path.

## The adoption funnel

```
Discover → "What is this?"           → README, Explanation
Evaluate → "Should I use this?"      → Architecture, Comparison
Start    → "How do I begin?"         → Quickstart, Tutorial
Build    → "How do I do X?"          → How-to guides, API reference
Operate  → "How do I keep it going?" → Runbook, Troubleshooting, Config reference
Upgrade  → "How do I move forward?"  → Migration guide, Changelog
```

Find the bottleneck (where do developers drop off? high signup + low API calls = broken Start) and fix it **first** — teams default to writing what's easy (reference) over what's impactful (quickstart, tutorials); a complete map of a city you can't enter helps no one. Measure per stage (quickstart views, time-to-first-call, ticket topics).

## Time to hello world

The single most important DX metric. The quickstart is: install → one credential → one meaningful call → one visible meaningful result, under 5 minutes. Everything else — architecture, advanced config, edge cases — lives elsewhere and is linked from "next steps". Theory-first onboarding (architecture essay, multi-tool environment setup, 15 configuration steps before the first request) is the anti-pattern that costs adoption.

## Interactive and copyable examples

Prefer working, copyable examples as the primary teaching surface. The effort ladder — start at the bottom, climb as ROI justifies:

| Level | Implementation | Effort |
|---|---|---|
| Copy button | static blocks + clipboard | low |
| Language tabs | all supported languages inline, functionally equivalent, idiomatic per language | low |
| "Try it" explorer | interactive request builder | medium |
| Embedded sandbox | runnable in-browser | high |
| Live preview | output updates as code changes | high |

Never make a developer navigate away to switch languages. Treat examples as **maintained product surfaces**: they break like code, so they're tested like code.

## Production readiness in developer docs

Address, somewhere findable: authentication hardening · error handling with per-error docs (exact code, one-sentence cause, specific fix, guide link) · permissions/least privilege · observability (what to monitor, what the alerts mean) · limits and quotas · retry/backoff/idempotency · lifecycle behavior (timeouts, pagination, versioning, deprecation policy).

## Partner and integration documentation

- **Both sides, always.** For every request you document, document the expected response; for every callback you send, document what the partner's endpoint must do (status code and deadline, signature verification, idempotent processing) and what happens on failure (retry schedule, pause conditions, notifications). Include interaction-flow diagrams. One-sided docs force partners to reverse-engineer half the integration.
- **Production-readiness checklist ends every integration guide** — sandbox success ≠ production readiness: security (keys in env vars, signatures verified, HTTPS, minimum scopes) · reliability (retry with backoff, idempotency keys, timeouts, circuit breakers) · monitoring (error rates, delivery success, latency, alert thresholds) · compliance (regulations, PII encryption, audit logging) · support (production keys, contact, P1 escalation path, SLA reviewed).
- **Partner-program surface** beyond standard docs: partnership tiers/certification requirements, sandbox environments, partner-specific APIs, co-branding guidelines, support escalation, SLAs/stability commitments, marketplace listing requirements.
- No internal jargon without definition; write from the partner's perspective.

## Measuring documentation

Quantitative: page views · search queries and **failed searches** (content-gap signal) · time on page · bounce · search→exit · support-ticket deflection · time-to-first-API-call · tutorial completion rate · example copy rate. Qualitative: docs-NPS surveys, support-team gap reports, forum questions, partner onboarding feedback, new-hire experience. Read patterns, not vanity numbers: high traffic + high bounce = not finding it; low traffic on important pages = discoverability; repeated tickets on documented topics = unfindable or unclear. Measure useful outcomes, never page volume.

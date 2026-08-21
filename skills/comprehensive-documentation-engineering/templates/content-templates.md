# Content-type skeletons

> Copy the relevant skeleton, fill the `[brackets]`, delete sections that don't apply. Never manufacture types the user's needs don't justify; never leave template padding. Full principles per type: `references/tutorials.md`, `how-to-guides.md`, `reference.md`, `explanation.md`, `content-types.md`.

## Tutorial
```markdown
# Build [a concrete thing] with [product]

In this tutorial, we will [concrete goal — what the reader will have at the end].

## What you'll build
[1–2 sentences + a screenshot/diagram of the end result]

## Before you begin
- [Prerequisite, with link to setup]
**Time to complete:** [estimate]

## Step 1: [action verb + what this accomplishes]
[Direct instruction.]
```[lang]
[code]
```
You should see:
```
[exact expected output]
```
Notice that [observation that closes a learning loop].

## Step 2: [builds on step 1]
[…every step yields a visible result; no choices; first-person plural…]

## What you've built
You have [concrete achievement].

## Next steps
- [Next tutorial / related how-to] · [explanation for depth] · [reference for the APIs used]
```

## Quickstart
```markdown
# Quickstart
## Prerequisites
- [one-liner with link]
## Install
```[shell]
[command]
```
## Make your first [call]
```[lang]
[simplest meaningful operation]
```
```json
[expected response]
```
## Next steps
- [Tutorial] · [how-to guides] · [API reference]
```

## How-to guide
```markdown
# How to [accomplish specific real-world goal]
[1 sentence: what this achieves and when you'd need it.]
## Prerequisites
- [assume basic competence]
## Steps
### 1. [action] — [conditional imperative: if you want X, do Y]
### 2. [action]
Refer to the [X reference](#) for all options.
## Verify
[how to confirm success]
## Related
- [related how-to] · [troubleshooting] · [reference] · [explanation of why]
```

## Reference (per entry — same shape for every entry of a kind)
```markdown
## [Method] [Path]   (or: function/class/config-key name)
[One-sentence, verb-first description, incl. side effects.]
### Authentication  ### Parameters (table: name, type, required, default, description)
### Request example  ### Response (success + error)  ### Errors (status, code, cause + fix)
```

## Explanation
```markdown
# Understanding [concept]   (reads with an implicit "About")
[Overview: why this topic matters. Bound it with a why-question.]
## [Core concept] — connections, context, history, constraints
## Design decisions — what was chosen and why; **Why not [alternative]?**
## Trade-offs (table: choice / benefit / cost)
## Further reading — [related explanation] · [how-to for practice] · [reference]
```

## Migration guide
```markdown
# Migrate from v[X] to v[Y]
## Overview — estimated effort, breaking-change count, key changes
## Before you begin — backup, changelog link, required starting version
## Automated migration ```[codemod/script]``` — handles […]; you still handle […]
## Breaking changes — per change: what / why / before-code / after-code
## Deprecations (table: deprecated / replacement / removal target)
## Verification  ## Rollback  ## Getting help
```

## Troubleshooting (organize by symptom)
```markdown
# Troubleshooting [area]
## [Exact error message or observable symptom]
**Symptom:** [what the user sees]
**Diagnosis:** [confirm this specific problem; diagnostic command]
**Solution:** 1. […] 2. […]
**Why this happens:** [brief; link to explanation]
```

## Runbook
```markdown
# [Service] Runbook
**Owner:** _ · **Last verified:** _ · **Escalation:** _
## Access (table: system / how to access)  ## Monitoring (alert / severity / meaning)
## Scenarios — per: symptoms / impact / exact steps / escalate-after threshold
## Post-incident — [ ] update runbook [ ] file review [ ] close monitoring gaps
```

## Changelog
```markdown
## [Version] — [Date]
[One-sentence headline of the biggest change.]
### Added  ### Changed  ### Deprecated  ### Removed  ### Fixed  ### Security
- [specific entry] ([docs](#) / [migration guide](#) for breaking changes)
```

## Architecture Decision Record (ADR)
```markdown
# ADR-[n]: [Title]
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX  **Date:** _
## Context  ## Decision  ## Consequences (Positive / Negative / Neutral)
## Alternatives considered — [alternative] and why it was rejected
```

## Glossary entry
```markdown
## [Term]
[Definition as it applies to this product specifically.]
**Also known as:** _ · **Related:** _ · **See:** _
```

## Integration guide → see `references/content-types.md` (both-sides + production-readiness checklist)
## SDK / configuration reference, architecture guide → `references/content-types.md`

---
*Provenance: skeletons synthesized from Anivar Aravind's developer-docs-framework templates (MIT; Good Docs Project-informed, CC BY 4.0) and rlespinasse/agent-skills page templates (MIT). Full attribution: `references/source-provenance.md`.*

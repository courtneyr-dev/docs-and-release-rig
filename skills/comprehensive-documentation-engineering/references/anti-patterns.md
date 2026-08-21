> Detection patterns adapted from Keith Patton's [diataxis-agent-skill](https://github.com/keithpatton/diataxis-agent-skill) (CC BY-SA 4.0 — this file is therefore CC BY-SA 4.0); consolidated checklist synthesized from Anivar Aravind's [developer-docs-framework](https://github.com/anivar/developer-docs-framework) (MIT) and diataxis.fr doctrine. Changes: merged and re-expressed, 2026-08-20.

# Documentation anti-patterns — detection and repair

Use as a review checklist and as a violation detector. When flagging, calibrate confidence: **high** = multiple strong signals, unambiguous · **medium** = clear signals but context could justify — needs review · **low** = weak signals, could be intentional — flag for human judgment. Report each flag with signals quoted.

## The five core violations (with signals and failure modes)

### 1. Tutorial with too much explanation ("the lecture tutorial")
**Signals:** long conceptual paragraphs mid-lesson; "The reason this works is…"; digressions into history/architecture; "Understanding X"/"About X" sections inside a tutorial; the reader asked to understand before doing.
**Failure:** action sequence interrupted; cognitive load up; learner attention shifts from doing to reading; momentum and completion drop.
**Repair:** cut context to one clause + link; move the material to an explanation doc; keep focus on the learner's next action.

### 2. How-to that teaches ("the disguised tutorial")
**Signals:** "Let's learn how to…"; extensive background before the first actionable step; explaining what things are before using them; hand-holding ("Don't worry if this seems confusing"); no assumed competence.
**Failure:** competent readers hit friction and must skip to find the procedure; time-to-solution grows.
**Repair:** prerequisites stated flat; first actionable step early; link the tutorial for those who need one.

### 3. Reference with narrative/instruction ("the opinionated reference")
**Signals:** first person ("I recommend…", "We suggest…"); procedural language ("First, you should…"); judgments ("the best approach"); storytelling; "how to" phrasing amid facts.
**Failure:** facts buried in prose; lookup time grows; scannability dies; trust erodes.
**Repair:** restate as neutral structured description (tables/lists); move procedures to how-to guides and opinions to explanation, with links.

### 4. Explanation with procedures
**Signals:** numbered action steps; imperative commands ("Run this"); executable code blocks; "how to" framing inside conceptual content.
**Failure:** reflection broken; reader forced to context-switch between understanding and doing; no single cognitive mode maintained.
**Repair:** keep the *why*; link the how-to for the *how*; code appears only as illustration.

### 5. Mixed-mode document ("the kitchen sink")
**Signals:** sections belonging to different types; abrupt tone shifts (teaching → describing → instructing); heading hierarchy that mixes modes; reader unclear whether to study, work, or consult; length suggesting several purposes compressed.
**Failure:** every reader scans past content they don't need; no need served well; navigation unclear.
**Repair:** one document per need, cross-linked; content organized by user need, not topic.

## Structural anti-patterns

- **Empty scaffold** — four empty labeled sections before any content exists. Fix: improve real content; let structure emerge (never create a type without material).
- **Org-chart mirror** — docs organized by internal team; breaks on every reorg. Fix: organize by content type/user need.
- **Feature mirror** — guide navigation mirroring the API surface instead of user goals. Fix: outcome-named guides; the *reference* may mirror the machinery.
- **Rabbit hole** — navigation deeper than two levels without genuine landing pages. Fix: broad-shallow; add depth only per the list rule with real landing pages (see `information-architecture.md`).
- **Dead end** — no prerequisites, next steps, or related links. Fix: the cross-link pattern on every doc.

## Content anti-patterns

- **Feature announcement voice** — "We've added X!" Fix: "You can now X."
- **Abstract description** — paragraphs about what something "can do" with no example. Fix: show the payload/code/diagram; showing often replaces telling.
- **Choices buffet** — tutorials/quickstarts offering multiple paths. Fix: one path in tutorials; alternatives in how-tos only when the reader's context genuinely varies.
- **Abstraction trap** — "you could use any database here." Fix: concrete named tools; the general emerges from the particular.
- **"You will learn" promise** — presumptuous claim about someone else's mind. Fix: describe what they'll *build*.
- **Broken example** — missing imports, undefined variables, deprecated calls. Fix: complete runnable context, tested (see `evidence-and-validation.md`).

## Style anti-patterns

- **Passive maze** → active voice, direct address. **Thesaurus trap** (workspace/project/environment for one concept) → one term, glossary-governed. **Idiom minefield** → plain global English. **Admonition avalanche** → ≤2–3 per page; warnings only for real risk. **Mismatched tone** → tone follows type. **UI narrator** ("click Deploy to deploy") → address the real problem and the judgment involved. **Flowless guide** → resequence around the reader's thinking.

## DX anti-patterns

- **20-minute quickstart** (multi-tool setup before any result) → install, one credential, one call, one result. **Monolingual docs with "see the X guide" links** → inline language tabs. **Invisible audience** (one "developer" persona) → audience matrix + separate entry points. **Theory-first onboarding** → working example first, philosophy linked.

## Governance anti-patterns

- **Orphan docs** (no owner) → owner per page, cadenced review. **Ship-without-docs** → docs in the definition of done. **Stale quickstart** → CI-tested, quarterly verified. **Version amnesia** → versioned reference, visible version, marked deprecations with migration links. **Vague changelog** ("various improvements") → specific entries linking docs.

## Partner-docs anti-patterns

- **One-sided integration** → document both sides of every interaction. **Sandbox surprise** → production-readiness checklist ends every integration guide. **Internal jargon guide** → define on first use; write from the partner's perspective.

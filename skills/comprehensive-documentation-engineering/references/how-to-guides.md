> Adapted from [Diátaxis](https://diataxis.fr) (how-to-guides, tutorials-how-to pages), © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is CC BY-SA 4.0. Changes: unified rule sheet with merged flow/outcome notes from Apache/MIT-licensed sources, 2026-08-20.

# How-to guides — rule sheet

**Purpose.** Goal-oriented directions for the already-competent user at **work**: navigating from one side of a real-world problem-field to the other, correctly and safely. A how-to guide answers to a *human project* — what a person needs to get done with the tools at hand — never to a tool operation. Well-addressed how-to guides are typically the most-read part of documentation, and the list of them frames what the product can actually do.

## The named failure mode

Guides defined by "operations that can be performed with the tool": *"To deploy the desired configuration, select the appropriate options and press **Deploy**."* That is not guidance — it narrates controls any competent practitioner already understands and is addressed to no need. Before writing or accepting a guide, answer: **what does a person need to get done in the real world?** If the honest answer names only the tool's own controls, it is not yet a how-to guide. Tools appear as incidental bit-players; a real task often cuts *across* tools.

## Enforced

- **Title form:** *How to ⟨real-world goal⟩*. Test: "How to integrate application performance monitoring" — good. "Integrating application performance monitoring" — bad (how, or whether?). "Application performance monitoring" — very bad (how? whether? what?). Search engines agree with humans here.
- **Outcome naming everywhere:** "Move data to your warehouse", not "The Pipeline API"; "How to handle delivery failures", not "the DeliveryError class".
- **Assume competence.** The reader knows what they want, knows the domain, and can follow directions; omit what any practitioner already knows. No teaching, no beginner framing, no "don't worry if this seems confusing".
- **Conditional imperatives.** "If you want x, do y. To achieve w, do z."
- **Branch where the real world branches.** Not merely procedural: sequences may fork, overlap, and have multiple entry/exit points; address the user's *thinking and judgement*, not only their actions; stay adaptable so readers can map guidance onto their situation.
- **Start and end at reasonable points.** Practical usability beats completeness; the reader joins the guide to their own work.
- **Order for flow.** Ground the sequence in the user's activity and thinking: what must they hold open, and when can it resolve in action? Minimise context switching between tools and subjects; mind pace and rhythm. At its best a guide *anticipates* the user — the helper with the next tool already in hand.
- **Link out instead of digressing:** full option lists → reference ("Refer to the X reference for all options"); concepts → explanation; basics → the tutorial.
- **State prerequisites** and a way to **verify** the result.

## Forbidden

Goals that amount to "call this function" · teaching or explaining · exhaustive option/parameter lists · UI narration ("click Deploy to deploy") · tone-deaf tangents that break flow · describing several approaches without a recommendation when the reader's context doesn't genuinely vary.

## Structure that works

Title (*How to X*) → one sentence on what this achieves and when you'd need it → prerequisites → steps (conditional, branching where needed, code per step) → verify → troubleshooting/failure handling where relevant → related guides/reference/explanation links.

## Closing self-check

Compass every section and the whole: must land in informs-action / application. Per guide: **what human project does this serve?** The answer must not be a tool operation. Does any section teach, or turn into a reference table? Does the title say exactly what the guide shows?

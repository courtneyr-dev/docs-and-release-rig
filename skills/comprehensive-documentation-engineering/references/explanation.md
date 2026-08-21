> Adapted from [Diátaxis](https://diataxis.fr) (explanation, reference-explanation pages), © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is CC BY-SA 4.0. Source-mining note adapted from Peter Knego's diataxis-docs-skill (CC BY-SA 4.0 layer). Changes: unified rule sheet, 2026-08-20.

# Explanation — rule sheet

**Purpose.** Understanding-oriented, discursive treatment of a bounded topic that permits **reflection**. It deepens and broadens understanding; it joins things together and answers *why*. Its perspective is higher and wider than the other three types — not the user's eye-level (how-to) nor the machinery close-up (reference). It's the one kind of documentation that makes sense to read away from the product ("in the bath"), answering "Can you tell me about…?"

Explanation is less *urgent* than the other types but no less *important*: without it, a practitioner's knowledge is loose, fragmented, and fragile, and their practice is anxious. It is usually not recognized as a distinct need and ends up scattered in small parcels through other sections — centralize it and give it room.

## Enforced

- **The implicit-*About* test.** Every explanation is *about* — around — a topic; its title should read naturally with "About" in front (*About user authentication*). Acceptable section names: Explanation, Discussion, Background, Concepts, Topics, "Understanding X".
- **Bound it with a why-question.** Tutorials, how-tos, and reference are bounded by the lesson, the task, and the machine; explanation has no natural boundary, so use a real or imagined *why* question as the prompt, draw reasonable lines, and be satisfied with them. Open-endedness is a risk, not a license.
- **Make connections** — to related concepts, to other systems, even outside the immediate topic — weaving the web of understanding.
- **Provide context:** design decisions, history, technical constraints, implications, concrete examples; unfold the machinery's internal secrets where it helps understanding.
- **Admit opinion and perspective.** Understanding comes from a standpoint, and other standpoints exist: weigh alternatives, counter-examples, trade-offs, and contrary opinions. ("Some users prefer w (because z). This can be a good approach, but…") Keep opinion bounded — discussion, not advocacy or marketing.
- **Language:** "The reason for x is historical: y…" · "W is better than z, because…" · "An x in system y is analogous to a w in system z. However…" · trade-off framing ("this favors throughput over immediate consistency").

## Forbidden

Step-by-step instructions and imperative commands → link the how-to · reference tables and parameter dumps → link the reference · executable (rather than illustrative) code blocks · absorbing other material: the urge to "cover the topic completely" pulls instruction and description in, which interferes with the explanation *and* removes that material from its correct home · so much abstraction nobody benefits.

## Source-mining

The *why* behind decisions lives in ADRs, commit messages, PR discussions, RFCs, and design documents. Mine those; don't invent rationale. Where an architecture explanation would benefit from diagrams, apply `references/diagrams.md` (evidence-traced C4, embedded in prose that carries the why on its own).

## Closing self-check

Compass every section and the whole: must land in informs-cognition / acquisition. Then the **bath test**: would someone read this away from the keyboard, reflecting rather than working? If not, it has drifted toward reference or a how-to guide. Adapted/moved pages especially tend to pass at a distance while single sections remain reference tables — check close-up.

> Adapted from [Diátaxis](https://diataxis.fr) (index, start-here, theory, foundations, map, quality, how-to-use-diataxis pages), © Daniele Procida, licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This file is therefore CC BY-SA 4.0. Changes: condensed into an agent-facing rule sheet, 2026-08-20, with merged implementation notes from MIT/Apache-licensed downstream skills (rlespinasse, sammcj, anivar — see references/source-provenance.md).

# Diátaxis foundations

## The four kinds and why exactly four

Documentation serves practitioners in a domain of skill. Skill has two dimensions: **action** (practical knowledge, knowing *how*) vs **cognition** (theoretical knowledge, knowing *that*), and **acquisition** (study) vs **application** (work). Two complete dimensions define four quarters — not three, not five, and no other territory to cover. Each quarter is a distinct user need with a distinct documentation form:

| need | addressed in | the user | the documentation | answers | form | analogy |
|---|---|---|---|---|---|---|
| learning | **tutorials** | acquires their craft | informs action | "Can you teach me to…?" | a lesson | teaching a child to cook |
| goals | **how-to guides** | applies their craft | informs action | "How do I…?" | a series of steps | a recipe |
| information | **reference** | applies their craft | informs cognition | "What is…?" | dry description | info on a food packet |
| understanding | **explanation** | acquires their craft | informs cognition | "Why…?" | discursive discussion | culinary social history |

Diátaxis is a **map**, not a list: the boundaries between neighbors matter. Adjacent types share one trait each (tutorial↔how-to guide action; how-to↔reference application; reference↔explanation cognition; explanation↔tutorial acquisition), which creates a natural pull to blur. Blur — partial or total collapse of the types into each other — is at the heart of most documentation problems.

The **cycle of interaction**: users tend to move learning → goals → information → understanding and back around as they deepen — a sense-making ordering, not a required reading order; real users enter anywhere.

## Quality: functional vs deep

- **Functional quality** — accuracy, completeness, consistency, usefulness, precision. Objective, measurable, mutually independent (docs can be accurate but useless), and every lapse is user-visible. These are constraints met through discipline and domain skill.
- **Deep quality** — feeling good to use, having flow, fitting human needs, being beautiful, anticipating the user. Subjective, interdependent, judged rather than measured, and **conditional on functional quality**: nothing feels good to use while it's inaccurate. These are the work of creativity and taste.

Diátaxis cannot supply functional quality — accuracy is the author's job. What it does: **expose** functional lapses analytically (mirroring reference to code structure makes gaps visible; extracting explanation from a tutorial reveals where the reader was abandoned) and **enable** deep quality (types built on needs → fit; boundaries protected → flow undisrupted). Limits to keep in mind: Diátaxis is not a formula, not a shortcut past UX/writing/domain skill, and doesn't solve staffing, politics, or product complexity. It lays foundations; you still build the house.

## The working method

- **Guide, not plan.** The structure is a check on direction, not a checklist to complete. Never impose it from outside; docs assume the shape *because* they improved.
- **No empty scaffolds.** Do not create tutorial/how-to/reference/explanation sections with nothing in them — "it's horrible." Top-level structure forms itself when improved content demands a home.
- **One small step.** Choose something (at random is fine) → assess it against the standards (what need? how well served? language and logic right for the mode?) → decide the single next action → do it, publish/commit it, consider it complete → repeat. Don't work on the big picture; don't hoard changes for a big reveal.
- **Organic growth.** Documentation is **never finished** (product and needs keep moving) but can be **always complete** — appropriate to its stage, healthy, ready to grow, like a plant. Well-formed cells produce well-formed structure, from the inside out.
- **Apply before you understand.** Iterate between work and reflection; treat the doctrine as a toolbox opened when a live problem exists. If one idea helps, use that idea — there is no exam.

## Maintenance realities

Tutorials are the most revision-prone quadrant: the end-to-end journey means changes cascade rather than land discretely — budget for it. What the learner *does* is not what they *learn* (they learn concepts, names, workflows, and confidence through the doing), so tutorial revisions must protect the learning journey, not just the steps.

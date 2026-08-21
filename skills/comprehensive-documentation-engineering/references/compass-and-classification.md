> Adapted in part from [Diátaxis](https://diataxis.fr) (compass, map, tutorials-how-to, reference-explanation pages), © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is CC BY-SA 4.0. Merged classification mechanics from Keith Patton's diataxis-agent-skill (CC BY-SA 4.0) and boundary-case rules from rlespinasse/agent-skills (MIT). Changes: unified rule sheet, 2026-08-20.

# Compass and classification

Run the compass before writing anything, when classifying existing content, and again before closing any piece of work. It exists because intuition is unreliable — and sometimes confidently wrong.

## The two questions and the table

1. **Action or cognition?** — does this inform what the reader *does* (steps, procedures, activities) or what the reader *knows* (facts, concepts, understanding)?
2. **Acquisition or application?** — does it serve the reader's *study* (learning) or their *work* (getting the job done)?

| informs… | serves… | → type |
|---|---|---|
| action | acquisition | Tutorial |
| action | application | How-to guide |
| cognition | application | Reference |
| cognition | acquisition | Explanation |

Term glosses: action = practical steps, doing · cognition = propositional knowledge, thinking · acquisition = study · application = work. Use the terms flexibly while orienting; alternative framings: "Would this be read *before* work or *during* it?" · "Does the reader *perform* or *understand*?" · "Instructions or descriptions?"

## Rules of engagement

- **Multi-scale.** Apply close-up (sentence, paragraph) and at a distance (whole document). Register violations typically live in sections of pages that pass at a distance.
- **Need, not subject.** The same subject (say, authentication) legitimately produces four documents. Classify by what the reader needs, never by topic.
- **Output contract.** Every classification reports: **type + confidence (high/medium/low) + evidence** (verbatim signals: imperative verbs, goal-oriented headings, first-person plural, lookup tables, "why" reasoning, assumed competence…). High = clear signals on both axes; medium = one axis unclear; low = weak or conflicting signals → flag for human judgment rather than forcing.
- **Conflicting signals** mean one of: incomplete reading, genuinely mixed content, or context-dependence. Mixed content is *flagged with a proposed per-section split*, never squeezed into one type.

## Blur diagnostics (check each adjacent pair explicitly)

- **Tutorial ↔ how-to** (shared: action): a "tutorial" assuming competence it never taught, or a "how-to" that stops to teach.
- **How-to ↔ reference** (shared: application): option tables and parameter lists growing inside a guide's steps.
- **Reference ↔ explanation** (shared: cognition): an illustrative example expanding into a digression on *why*.
- **Explanation ↔ tutorial** (shared: acquisition): explanation crowding out the lesson, turning doing into reading.

Rules of thumb: boring and unmemorable → probably reference. Lists/tables of things → reference. Readable in the bath, away from the keyboard → explanation. The work/study test: reached for *while working* → how-to/reference; *after stepping away to think* → tutorial/explanation.

## The tutorial / how-to distinction in full

Both are practical, ordered, and promise success — which is why they're the single most common conflation. The difference is **study vs work**, never basic vs advanced (how-to guides can cover mundane basics; tutorials can be highly advanced — an experienced practitioner in a training workshop is in a tutorial situation):

| Tutorial | How-to guide |
|---|---|
| helps the pupil **acquire competence** | helps the competent user **perform a task correctly** |
| provides a learning experience | directs the user's work |
| carefully managed path with required encounters | aims at a result; the real-world path can't be managed |
| familiarises; contrived, safe setting | assumes familiarity; the real world |
| eliminates the unexpected; single line, no choices | prepares for the unexpected; forks and branches |
| must be safe and repeatable | can't promise safety; may be one-shot |
| responsibility on the teacher | responsibility on the user |
| explicit about basic/embodied things | relies on implicit knowledge |
| concrete and particular | general and adaptable |
| teaches general skills via one specific path | completes one particular task |

Getting this wrong actively harms newcomers and, in high-stakes domains, is dangerous (a clinical manual that tried to teach mid-procedure would kill people).

## The reference / explanation distinction

Both are propositional. Reference serves **work** (facts consulted while doing); explanation serves **study** (understanding sought away from the work). The common drift: reference examples are fun to develop and slide into explaining *why* — bad for the reference (interrupted) and the explanation (never allowed to develop properly). When in doubt: would someone turn to this mid-task, or after stepping away?

## Boundary cases — classify by structure and intended use

| Content | Classification |
|---|---|
| Troubleshooting as a symptom→cause→fix lookup table | Reference-like (structured for consultation) |
| Troubleshooting as a step-by-step diagnostic walkthrough | How-to (action + application) |
| "Understanding why X happens" | Explanation |
| FAQ | Usually mixed; split entries by nature, or keep the FAQ as an index linking to proper documents |
| Migration guide: upgrade steps | How-to |
| Migration guide: what changed and why | Explanation (link the two) |
| Getting started | Often a true mix of tutorial and reference elements — split into a real tutorial + quick facts |
| README | Brief overview + links to proper documents; don't force one file to be all four types |

Ask: how will the reader *use* this page? Consulted for lookup → reference. Followed as steps → how-to.

## Respect prior decisions

Before proposing a reclassification, check the repository's history for deliberate prior moves (e.g. `git log --all --oneline --diff-filter=R -- 'docs/**'`, commit messages like "reclassify X as reference"). A prior deliberate reclassification reflects judgment the compass alone may not capture: flag it to the user; don't override it unless asked.

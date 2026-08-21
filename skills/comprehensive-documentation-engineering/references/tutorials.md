> Adapted from [Diátaxis](https://diataxis.fr) (tutorials, tutorials-how-to pages), © Daniele Procida, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is CC BY-SA 4.0. Execution-verification protocol adapted from Peter Knego's diataxis-docs-skill rule sheets (CC BY-SA 4.0 layer). Changes: unified rule sheet, 2026-08-20.

# Tutorials — rule sheet

**Purpose.** Learning-oriented. A tutorial is a lesson: a practical activity in which the learner acquires skill and confidence by doing something meaningful toward an achievable goal. Responsibility for success lies almost entirely with the teacher; the pupil's only duty is attention. What the learner *does* is not what they *learn* — through doing they acquire concepts, names, workflows, relationships, and the confidence that they can succeed.

The exercise must be **meaningful** (sense of achievement), **successful** (completable), **logical** (the path makes sense), and **usefully complete** (encounters everything the learner needs to become familiar with).

## Enforced

- **Don't try to teach.** Provide an experience through which learning happens; resist the anti-pedagogical temptations — abstraction, generalisation, explanation, choices, information.
- **Show the destination:** open with "In this tutorial we will *build/create/deploy* ⟨concrete thing⟩". Never "you will learn…" (presumptuous about someone else's mind — describe what they'll *build*).
- **One single line.** No options, alternatives, or interesting diversions. One path to the conclusion.
- **Visible results early and often.** Every step yields a comprehensible result, however small; results let the learner connect cause and effect.
- **Narrative of the expected.** Show exact expected output; "You will notice…", "After a few moments, the server responds with…"; flag likely wrong-turn signs ("If the output doesn't show X, you probably forgot Y"); prepare for surprising output ("this returns several hundred log lines").
- **Point out what to notice.** Close learning loops in passing ("Notice the prompt changes"); observation is an active skill the learner is also acquiring.
- **Target the feeling of doing.** Tie purpose, action, thinking, and result together into rhythm; **permit repetition** — design steps to be re-runnable and reversible; repetition is sometimes the only teacher.
- **Ruthlessly minimise explanation.** One clause plus a link out: "We use HTTPS because it's safer (see *About transport security*)." Explanation is pertinent only when the *user* wants it — not when the author does.
- **Concrete and particular, never abstract.** *This* problem, *this* action, *this* result — with specific named tools ("Use PostgreSQL", not "any database works"). The general emerges from the concrete; minds excel at exactly that direction.
- **First-person plural** ("we") throughout — the tutor-learner solidarity voice. Be explicit about basic, embodied things: where to type, what to wait for.
- **Aspire to perfect reliability.** Every step must work for every user every time; a failed promise destroys confidence in the tutorial, the product, and the learner themself. You are required to be present but condemned to be absent — the tutorial must rescue itself. Flaws are found through user testing/observation and through execution (below), never assumed away.
- **Close by describing** (and mildly admiring) what the learner accomplished, with links onward.

## Forbidden

"You will learn…" · choices ("you could also…") · explanation beyond a single clause · reference tables · assuming knowledge a newcomer lacks · irreversible steps that block repetition (where avoidable) · long stretches with no visible output.

## Execution-verification protocol

A tutorial's reliability claim is only honest if the steps ran. Where the environment allows:

- **Sandbox every run** — disposable copy of the repo (`git worktree add` or temp-dir clone), never the user's working tree.
- **Never run commands with external side effects** — deploys, pushes, publishes, migrations against real databases, anything touching remote services or credentials. Mark those steps **unverified**.
- **Capture and normalize** real output (paths, timestamps, hostnames) before presenting it as expected output.
- **Fall back honestly.** If execution is impossible, mark the tutorial **unverified** — never imply verification that did not happen. An honest caveat is recoverable; a false promise is not.

## Maintenance

Tutorials consume the most maintenance of any type: the end-to-end journey means product changes cascade through the whole story. Record verification status (verified/unverified per step) in the working plan so reruns know what to re-execute.

## Closing self-check

Compass every section and the whole: must land in informs-action / acquisition. Does every step show its expected result? Is there any fork? **A fork is a failure.** Is any explanation longer than a clause? Does the opening promise a build, not a learning?

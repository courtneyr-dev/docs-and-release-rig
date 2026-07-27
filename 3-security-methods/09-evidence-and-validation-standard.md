# Evidence & validation standard

The bar a claim has to clear before it gets written down as true. This is the piece
that makes the rest of the process trustworthy: without an explicit evidence ladder,
"we tested it" and "it seemed fine" look identical in a report.

Written for security findings, but the ladder and the controls apply to any claim about
behavior — including a documentation claim.

---

## The gate ladder

A model, a tool, or a person may *propose* a transition up this ladder. **Evidence**
justifies it.

| Status | Evidence required to enter |
|---|---|
| **idea** | a named surface plus a guessed weakness |
| **hypothesis** | a falsifiable statement: source, sink, broken invariant, required access and config, plus one test that would support it and one that would disprove it |
| **suspicious path** | a source trace showing the invariant *can* break; no runtime evidence yet |
| **verified primitive** | a dynamic reproduction of control over the effect, **with a passing negative control** and a role/capability control |
| **verified issue** | the primitive crosses a real boundary in a supported configuration, and an independent verifier — working from the claim and evidence, without the original narrative — reproduced it |
| **chain candidate** | two or more primitives linked on paper, with at least one edge still lacking runtime proof |
| **verified chain** | **every** edge has source, runtime, and test evidence end to end |
| **remediated** | the fix is present, the failing-first regression test now passes, and the whole suite is green on the shipped tree |
| **regression protected** | the test is in CI, asserts the absence of side effects, and covers the version matrix |

## The 20-step validation loop

Track state for each of: 1 source · 2 sink or effect · 3 broken invariant · 4 required
access · 5 required config · 6 exact supported versions · 7 execution path · 8
instrumentation · 9 smallest safe test · 10 expected result · 11 run in an isolated
environment · 12 actual result · 13 **negative control** · 14 **role/capability
control** · 15 a normal valid request · 16 patched or safe behavior · 17 repeat in a
clean environment · 18 version-difference test · 19 **an independent agent tries to
disprove it** · 20 store regression evidence.

## The guardrails that actually do the work

- **Prove by firing.** A suspected issue is not an issue until it reproduces against a
  disposable install. Opinions — human or model — set priority, never truth.
- **No third door.** Nothing is "not a problem" on reasoning alone. Refuting a finding
  requires *fired-and-blocked* evidence, not an argument.
- **Controls every run.** Fire known-good and known-bad fixtures first. If the run is
  miscalibrated, abort and discard the findings from it.
- **Consensus is not truth.** Agreement between reviewers *deprioritizes* firing;
  disagreement *escalates* it. Only firing writes a confirmed or refuted verdict.
- A static observation is not a finding. A dynamic anomaly is not automatically
  exploitable. **A screenshot is not runtime proof.** A generated payload is not
  evidence until it has been reproduced and understood.

### Controls need an external corpus

Known-good and known-bad fixtures must come from a **pre-registered, human-curated
corpus** — not fixtures written by the same reviewer during the same run. A reviewer
who misunderstands a mechanism will write a control that passes for the wrong reason. A
self-authored negative control cannot promote a finding on its own; it only supports one
once external fixtures have calibrated the run.

### Say whether it was executed or attested

For code I own and can safely build, the prove-by-firing loop genuinely executes against
a disposable site. For third-party targets I cannot safely stand up, the 20 steps and
the ladder are **a checklist a reviewer attests to**, not a harness a system enforces.
Label every finding `fired` or `source-attested`. **Never imply a harness where there is
only a checklist** — this is the single easiest way for a report to become dishonest
without anyone lying.

### The null-result rule — closing a surface without infinite testing

"No third door" forbids reasoning a problem away, but you cannot fire every possible
configuration, so a clean surface needs a defined exit or the audit never ends. A
surface closes as **no finding** when both hold: every input path was traced in source
to a correct control, **and** the bounded, enumerated set of supported configurations
was fired with controls and none crossed a boundary. Record the exact configuration set
fired. Anything outside it is an **untested area**, recorded as such — not a clean bill
of health.

### Bounded-environment escape hatch

If something only reproduces under a production-like configuration that cannot be safely
or legally recreated, do not force a firing and do not refute by reasoning. Report it as
a **hypothesis with a stated environmental limitation.** This is the one sanctioned exit
from the no-third-door rule.

---

## Safe-proof standard

Prove **only** what is needed: reachability, control, required privilege, boundary
violation, affected versions, practical impact, remediation, and regression need. Then
stop. Prefer the least harmful proof available:

| Finding class | Minimal proof |
|---|---|
| Authorization bypass | show a capability check failed or the wrong subject was authorized, using an inert marker |
| Validation desync | show the handler processed the *other* request's validated representation |
| Injection, read | read one **synthetic** sentinel value; never dump real data |
| Unauthorized write | create or alter one **disposable synthetic** record |
| Unauthorized callback | fire with an **inert marker**, not a payload |
| File write | a controlled write inside a **disposable** directory |
| Resource amplification | bounded, rate-limited local measurement; no service disruption |

Never add persistence, stealth, destructive actions, credential theft, public-target
compatibility, shells, command-and-control, or unnecessary post-compromise steps. Stop
once the boundary is proven.

---

## Reporting standard

Report mechanism first, then proof: title · component · affected versions · target
revision · attacker access · required privileges · realistic prerequisites · source ·
sink or effect · broken invariant · exact execution path · boundary crossed · safe
reproduction · negative control · role control · expected versus observed · independent
verification · impact · severity rationale · confidence · remediation · regression test ·
disclosure status.

Avoid "it is possible that" when evidence exists. Label it a **hypothesis** when it
doesn't.

## Reusable templates

```markdown
### Hypothesis: [name]
- Research family / Target surface:
- Source / Sink or effect / Broken invariant:
- Required access / config:
- Why it may work / Evidence so far:
- Test that would support it / Negative control / Evidence that would disprove it:
- Status:
```

```markdown
### Blocked route: [name]
- Research family / Mechanism tested / Evidence gathered:
- Blocking condition — guaranteed, or merely typical?
- New evidence required to reopen / Related route worth testing:
```

```markdown
### Disproved hypothesis: [name]
- Original claim / Test / Expected / Actual:
- Why the mechanism fails / Scope of the disproof / Related assumptions still untested:
```

```markdown
### Finding: [title]
- Component + version / Revision / Artifact:
- Access required / Prerequisites:
- Source / Sink / Broken invariant / Execution path / Boundary crossed:
- Reproduction / Negative control / Actual result:
- Impact / Remediation / Regression test / Independent review / Disclosure status:
```

```markdown
### Regression test: [name]
- Finding covered / Test layer / Fixture / Environment:
- Setup / Action / Expected safe behavior (assert absence of side effects) / Failure signal:
- Negative control / Version matrix / CI location:
```

# Security finding / hypothesis templates

> Classify first: confirmed vulnerability · weakness · hardening opportunity · speculative risk. Never overstate severity or exploitability. "Hypothesis" when evidence is missing — never "it is possible that…" as a substitute for evidence. Security-classified findings route to **private** disclosure and appear in shareable docs only as a bare acknowledgment (see `templates/audit-handoff.md`).

## Finding
```
### Finding: <title>
- Component + version / Revision / Artifact:
- Access required / Prerequisites (attacker access, required privileges, required config):
- Source / Sink or effect / Broken invariant / Execution path / Boundary crossed:
- Reproduction (safe-proof, least-harmful) / Negative control (external corpus) / Actual result:
- Impact / Severity rationale / Confidence:
- Remediation / Regression test / Independent review / Disclosure status:
- Marker: fired | source-attested
```

## Hypothesis (evidence not yet sufficient)
```
### Hypothesis: <name>
- Research family / Target surface:
- Source / Sink or effect / Broken invariant:
- Required access / config:
- Why it may work / Evidence so far:
- Test that would support it / Negative control / Evidence that would disprove it:
- Status (on the gate ladder):
```

## Blocked route
```
### Blocked route: <name>
- Research family / Mechanism tested / Evidence gathered:
- Blocking condition — guaranteed, or merely typical?
- New evidence required to reopen / Related route worth testing:
```

## Disproved hypothesis
```
### Disproved hypothesis: <name>
- Original claim / Test / Expected / Actual:
- Why the mechanism fails / Scope of the disproof / Related assumptions still untested:
```

## Regression test
```
### Regression test: <name>
- Finding covered / Test layer / Fixture (external corpus) / Environment:
- Setup / Action / Expected safe behavior (assert absence of side effects) / Failure signal:
- Negative control / Version matrix / CI location:
```

**Safe-proof reminder:** prove only reachability, control, required privilege, boundary violation, affected versions, impact, remediation, regression need — then stop. Inert markers, synthetic sentinels, disposable records/dirs, bounded local measurement. Never persistence, stealth, destruction, credential theft, public-target compatibility, shells, C2, or post-compromise steps. Destructive proofs on disposable local installs only.

---
*Provenance: finding/hypothesis/blocked-route/disproof/regression templates from Courtney Robertson's docs-and-release-rig (CC0). Full attribution: `references/source-provenance.md`.*

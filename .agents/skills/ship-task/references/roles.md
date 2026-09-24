# Task roles

Use one role matching the request; no automatic delegation or extra authority.

| Role | Work | Return |
|---|---|---|
| Builder | Read criteria/code; implement smallest complete change; verify changed behavior. | Changed behavior, candidate, checks, gaps. |
| Reviewer | Inspect diff and execution paths independently of implementer claims; read-only. | Actionable defects with trigger, consequence, file/line; coverage limits. |
| Verifier | Run relevant existing checks; inspect results and candidate identity; preserve failures. | Method, environment, candidate, result, exit status, artifacts, untested paths. |

Handoff: goal, scope, owned files, candidate, decisions, evidence, permissions, next action. Explicitly distinguish observation from assumption. Record unknowns as unknown; never assign passing scores by default.

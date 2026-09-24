# Does an added skill or tool improve shipping?

[Home](README.md) · [Prompts](PROMPTS.md) · [Setup](SETUP.md) · [Evidence](GATES.md) · [Sources](SOURCES.md)

**Proposed evaluation protocol; no runs have been performed.** The goal is to test your setup, not reproduce a vendor leaderboard. OpenAI describes evaluating skills with task outcomes and execution traces, including wasteful work and resource use. [R27](SOURCES.md#r27)

## Experiment
Choose representative, sanitized tasks: one small bug, one UI state change, one integration change, one database change where applicable, and one CI diagnosis. This is a useful pilot set, not statistically conclusive evidence.

For each task compare the current setup against exactly one changed element: a skill, documentation retriever, prompt, model or orchestration setting. Fix the starting commit, environment, authorization, acceptance criteria and budget. Use isolated workspaces and no shared solution memory. Repeat runs and alternate ordering; record cold and warm starts separately.

For the [product-excellence workflow](PRODUCT-EXCELLENCE.md), include an idea-to-product task with fixed scope, visual/interaction references, usability criteria and separately recorded customer/business hypotheses. Compare against the existing workflow under the same budget; do not treat an agent score as real-user validation.

Use acceptance tests and review criteria written before seeing the generated implementation. Check both task quality and whether the skill activated only when appropriate. A guidance source loading successfully is not a successful task.

## Record every attempt
| Measure | Definition |
|---|---|
| Accepted completion | All required criteria met within the same agreed budget |
| Time | Start-to-evidence elapsed time; separate setup, implementation, validation and human waiting |
| Cost | Reported model/tool/CI usage, including failed runs; unknown means unknown, not zero |
| Human effort | Clarifications, corrective interventions and review time |
| Rework | Reopened defects or fixes required after initial completion |
| Process overhead | Unnecessary calls, repeated setup, duplicate builds and unrelated edits |
| Safety | Unauthorized actions, data exposure, weakened tests or bypassed gates |

Report success rate over all attempts. Time among successful attempts alone can hide failures; include total resources spent per accepted change and the number of budget-exhausted runs. Keep quality and safety thresholds fixed while comparing speed.

## Adoption decision
Keep a candidate only when it improves the bottleneck you actually care about without unacceptable quality or safety regressions. A mixed or small-sample result is inconclusive, not a reason to claim a universal winner. Retest after material client/model/skill changes.

Vercel's published Next.js experiment illustrates that instructions, retrieval and automatic activation can affect outcomes. Its result is workload-specific, so use it to motivate your experiment rather than to ban all skills or always prefer AGENTS.md. [R28](SOURCES.md#r28)

`evaluation/results.json` starts empty and explicitly marked `not_run`. It contains no fabricated benchmark numbers.

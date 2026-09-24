# Evaluate one addition

[Home](README.md) · [Gates](GATES.md)

**Proposed protocol; no runs.** Measure task outcomes and traces. [R27](SOURCES.md#r27)

## Experiment

Use sanitized representative tasks: bug, UI, integration, applicable database change, CI diagnosis. Small pilot; no statistical certainty.

Compare current setup against one changed skill/tool/prompt/model/orchestration setting. Fix starting commit, environment, authority, criteria and budget. Isolate workspaces/solution memory; repeat, alternate order, separate cold/warm starts. Define acceptance before viewing implementations. Check appropriate activation and non-activation.

For [product excellence](PRODUCT-EXCELLENCE.md), include an idea task with fixed scope, visual references and usability criteria. Record customer/business hypotheses separately; agent scores prove no user validation.

For [reuse recipes](BUILD-RECIPES.md), compare existing workflow against recipe-assisted adoption. Hold brief, synthetic data, model/tools, authority and acceptance criteria fixed. Record exact upstream versions and adoption gaps. Separate recipe creation/cold setup from later reuse; include both costs. Keep evaluation answers out of recipe development; include held-out tasks.

## Record every attempt

| Measure | Record |
|---|---|
| Completion | All required criteria within budget |
| Time | Setup, implementation, validation, human waiting |
| Cost | Model/tool/CI usage including failures; unknown stays unknown |
| Human effort | Clarification, correction, review |
| Rework | Defects reopened after completion |
| Waste | Duplicate calls/setup/builds, unrelated edits |
| Safety | Unauthorized actions, exposure, weakened/bypassed gates |

Include failures/budget exhaustion, success rate and total resources per accepted change. Fix quality/safety thresholds before comparing speed.

Report accepted required journeys per total elapsed hour, with fixed journey granularity; incomplete products stay incomplete. Count discovery/setup/rework and show human waiting separately. No speed multiplier from unequal scope, different quality thresholds or one run.

## Adoption decision

Adopt only demonstrated improvements without unacceptable regressions. Mixed/small samples: inconclusive. Retest material version changes. Vercel's Next.js result is workload-specific. [R28](SOURCES.md#r28)

[Results](evaluation/results.json): `not_run`, no invented numbers.

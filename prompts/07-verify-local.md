# Verify candidate

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Missing/invalidated local evidence.

```text
Inspect final diff against original criteria and repository requirements; question implementer claims. Reuse valid results for this candidate/environment. Run missing/invalidated required tests, type/lint/build and behavioral checks.

Where safe/feasible, show regression tests detect the original bug. Browser checks must exercise changed journeys.

Return each criterion's command/method, exit/result, artifact and gap, tied to candidate/environment. Separate new/baseline failures, skips and unavailable checks. Missing evidence cannot pass. State supported completion level. No publication/deployment.
```

Sources: [R16](../SOURCES.md#r16)

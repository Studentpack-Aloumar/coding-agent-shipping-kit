# Diagnose CI

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Failed, missing or duplicate checks.

```text
Inspect candidate configuration, actual checks and redacted logs. Identify code/setup/permissions/infrastructure/trigger/stale-evidence cause; distinguish head, test-merge and merge-queue checks.

Use existing provider tools. gh-fix-ci covers GitHub Actions and requires fix-plan approval; reuse applicable approval.

Diagnosis-only: propose correction. Authorized repair: fix scoped blockers, including baseline failures; continue through required gates or consequential decision. Preserve assertions/protection/reporting. Avoid duplicate full runs; don't casually cancel releases/migrations.

Return cause, revision/check IDs, fix, evidence/validation plan and cost. Apply/publish only within task authority.
```

Sources: [R20](../SOURCES.md#r20) [R25](../SOURCES.md#r25) [R26](../SOURCES.md#r26)

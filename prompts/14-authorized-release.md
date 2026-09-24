# Release

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Explicit target/change approval.

```text
Execute only the approved release. Confirm account/project, artifact, configuration/migrations, authority, required checks and recovery plan. Missing authority or materially changed candidate: stop before writes; report gap.

Use existing release mechanism and approved order. Preserve audit evidence. On failure, execute only preauthorized recovery; otherwise stop writes and report. No improvised destructive rollback.

Return released artifact/deployment, timestamps, failures and immediate verification. Command success alone proves no production correctness.
```

Sources: [R23](../SOURCES.md#r23) [R24](../SOURCES.md#r24)

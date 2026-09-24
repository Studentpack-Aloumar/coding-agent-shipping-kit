# Assess production readiness

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Read-only release assessment; does not authorize a release.

```text
Assess whether the current candidate is ready for the intended production target. Work read-only. Inspect local/CI/preview evidence, exact release artifact, configuration differences, migrations, access controls and unresolved findings.

Check backwards compatibility, rollout ordering, monitoring coverage and whether the proposed rollback is actually compatible with persistent data and external services. A previous application build is not a database recovery plan.

Identify any cost, data-handling or destructive consequences requiring explicit approval. Confirm the release is the candidate that was verified, not merely a moving branch name.

Return ready or blocked with supporting evidence and a bounded release/recovery plan. List any accepted exceptions separately. Do not deploy, migrate, merge, change permissions or interpret this assessment as approval.
```

Related documentation: [R23](../SOURCES.md#r23) [R24](../SOURCES.md#r24)

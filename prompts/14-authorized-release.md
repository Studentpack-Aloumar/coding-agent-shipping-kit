# Execute an explicitly authorized release

**Trigger:** Use only after approval identifies the target and material change.

```text
Execute only the production release already explicitly authorized for this task. Before acting, confirm the target account/project, artifact revision, material configuration and migration changes, approval, required checks and recovery plan.

If authorization is missing or the candidate has materially changed, stop before the write and identify the exact gap. Do not substitute your own approval or broaden the rollout.

Use the existing release mechanism. Preserve audit evidence and follow the approved migration/order constraints. On failure, follow the preauthorized recovery action; otherwise stop further writes and report the condition. Do not improvise destructive database rollback.

Return what was actually released, deployment identity, timestamps, observed failures and immediate verification. A completed deployment command does not by itself establish production correctness.
```

Related documentation: [R23](../SOURCES.md#r23) [R24](../SOURCES.md#r24)

# Hand off a task without losing state

**Trigger:** Use at a real handoff or context boundary, not after every small edit.

```text
Create a compact factual handoff for the next coding-agent session. Inspect current repository state instead of relying only on conversation memory.

Record the agreed outcome and exclusions, workspace/branch, base and current revision or uncommitted diff identity, changed files, decisions, actual test commands/results and artifact paths. Include unresolved failures, what has not been attempted, and the next smallest executable action.

State which external actions are authorized and which remain prohibited or unapproved. Identify any in-progress operation that must not be duplicated. Exclude secrets and sensitive records; reference approved storage locations rather than copying credentials.

Save the handoff only to the authorized project location, or return it as text. Do not invent persisted files, background work or completed checks. Do not commit or push merely to create the handoff.
```

Related documentation: [R32](../SOURCES.md#r32)

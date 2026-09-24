# Plan a nontrivial change

**Trigger:** Use for multi-system, high-risk or poorly understood work; skip routine edits.

```text
Create the smallest executable plan for the current agreed change. Inspect the actual code first. Identify the files and interfaces affected, ordering constraints, behavioral tests, configuration/data changes and the evidence needed at completion.

Preserve the existing architecture unless a concrete requirement prevents it. Prefer one vertical working increment over many disconnected scaffolds. Mark which work can proceed independently and which resources must not be shared.

Separate local implementation from publishing and production operations. Include recovery/compatibility planning when persistent data or external behavior changes. No speculative future platform, unrelated refactor or unnecessary dependency.

Resolve blocking product scope before implementation; do not ask for routine technical approvals. Return the plan and material risks without editing code.
```

Related documentation: [R03](../SOURCES.md#r03)

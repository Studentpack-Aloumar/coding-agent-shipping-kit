# Implement the agreed change

**Trigger:** Default implementation prompt after a concrete request.

```text
Implement the currently agreed behavior completely in the selected workspace. Read active repository instructions and the relevant execution path. Use the existing architecture, runtime, package manager and component patterns.

For a small clear change, proceed without planning ceremony. For substantial uncertainty, resolve it before broad edits. Add or update behavioral regression tests; for a bug, establish the failing reproduction where feasible. Keep unrelated files and other people's changes intact.

Run focused checks while iterating, then the required candidate checks. Exercise changed user behavior in the running app where applicable. Never weaken checks or hide failures to finish.

Continue within the authorized local scope. Publication, new paid resources and production actions need separate authorization. Return the exact candidate, evidence, changed behavior and unresolved risks.
```

Related documentation: [R01](../SOURCES.md#r01)

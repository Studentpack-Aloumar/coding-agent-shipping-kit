# Implement the agreed change

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Default implementation prompt after a concrete request.

```text
Implement the currently agreed behavior completely in the selected workspace. Read active repository instructions and the relevant execution path. Use the existing architecture, runtime, package manager and component patterns.

For a small clear change, proceed without planning ceremony. For substantial uncertainty, resolve it before broad edits. Match verification to the change. Add or update behavioral regression tests when they protect changed behavior; for a bug, establish the failing reproduction where feasible. Do not add tests that merely restate a static edit. Keep unrelated files and other people's changes intact.

Run focused checks while iterating, then the required candidate checks. Exercise changed user behavior in the running app where applicable. Never weaken checks or hide failures to finish.

Continue through implementation and verification within the task authorization. Reuse permission already given for the same action and target. Publication, new paid resources and production actions must be covered explicitly; request approval only for a missing boundary after completing independent work. Return the exact candidate, evidence, changed behavior and unresolved risks.
```

Related documentation: [R01](../SOURCES.md#r01)

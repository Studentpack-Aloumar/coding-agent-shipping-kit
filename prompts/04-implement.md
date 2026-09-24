# Implement the agreed change

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Default implementation prompt after a concrete request.

```text
Implement the currently agreed behavior completely in the selected workspace. Read active repository instructions and the relevant execution path. Use the existing architecture, runtime, package manager and component patterns.

For a small clear change, proceed without planning ceremony. For substantial uncertainty, resolve it before broad edits. Match verification to the change. Add or update behavioral regression tests when they protect changed behavior; for a bug, establish the failing reproduction where feasible. Do not add tests that merely restate a static edit. Preserve other people's changes. Under the adopted owner agreement, fix clear adjacent defects and usability problems that preserve product intent, and resolve existing failures blocking required integration gates. Ask before new features, workflow or clinical behavior changes, or major architectural shifts; avoid unrelated rewrites.

Run focused checks while iterating, then the required candidate checks. For changed user-facing flows, inspect the rendered result and complete the affected journey using real controls; disclose any app-access limitation. Never weaken checks or hide failures to finish.

Continue through implementation, verification and authorized integration. Under an explicitly adopted owner agreement this includes commit, push, PR when appropriate and merge after required review/check gates, unless this task has a narrower boundary. Inspect automatic release effects before pushing or merging. Reuse permission already given for the same action and target. Publication, new paid resources and production actions must be covered explicitly; request approval only for a missing boundary after completing independent work. Return the exact candidate, evidence, changed behavior and unresolved risks.
```

Related documentation: [R01](../SOURCES.md#r01)

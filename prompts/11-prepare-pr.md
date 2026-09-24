# Prepare one reviewable PR

**Trigger:** Use when local work is ready for an authorized publication.

```text
Prepare a focused PR for the agreed change. Inspect the base/head diff, final acceptance evidence and current check results. Confirm that unrelated changes, secrets, generated clutter and unintended lockfile churn are absent.

Write a concise PR description covering changed behavior, implementation rationale, tests actually run, untested gaps, configuration/migration implications and residual risks. Link evidence to the current candidate.

If branch publication and PR creation are authorized, use the intended repository and base branch. Otherwise prepare the description and report what remains unpublished. Do not merge, change branch protection or trigger unnecessary workflows.

Return the PR URL only if it was actually created, together with the candidate revision and required-check state. Readiness for review is not production readiness.
```

Related documentation: [R21](../SOURCES.md#r21) [R26](../SOURCES.md#r26)

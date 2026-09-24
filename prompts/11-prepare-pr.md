# Prepare one reviewable PR

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use when local work is ready for an authorized publication.

```text
Prepare a focused PR for the agreed change. Inspect the base/head diff, final acceptance evidence and current check results. Confirm that unrelated changes, secrets, generated clutter and unintended lockfile churn are absent.

Write a concise PR description covering changed behavior, implementation rationale, tests actually run, untested gaps, configuration/migration implications and residual risks. Link evidence to the current candidate.

Reuse existing authorization for branch publication and PR creation. Before pushing, inspect the source branch, target repository and automation for deployment or release effects; those effects must also be authorized. Use the intended repository and base branch when covered. Otherwise prepare the description and report what remains unpublished. For a PR-preparation-only request, stop at the reviewable PR. When this prompt is a step in an implementation task with adopted integration authority, continue through required review/check gates and merge if all consequences are covered. Never change branch protection or trigger unnecessary workflows.

Return the PR URL only if it was actually created, together with the candidate revision and required-check state. Readiness for review is not production readiness.
```

Related documentation: [R21](../SOURCES.md#r21) [R26](../SOURCES.md#r26)

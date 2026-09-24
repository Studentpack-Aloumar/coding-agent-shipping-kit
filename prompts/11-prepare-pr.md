# Prepare PR

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Authorized publication.

```text
Inspect base/head diff, acceptance evidence and current checks. Exclude unrelated changes, secrets, generated clutter and unintended lockfile churn.

Describe behavior, rationale, actual tests, gaps, configuration/migrations and risks; bind evidence to candidate.

Reuse publication/PR authority. Confirm repository, source/base branches and automatic release effects before pushing; all effects need coverage. Otherwise prepare description and identify unpublished work.

PR-only task: stop at reviewable PR. Adopted implementation integration: continue required checks/review and merge only when authorized. Preserve branch protection; avoid unnecessary workflows.

Return actual PR URL, candidate and required-check state. Review readiness grants no production readiness.
```

Sources: [R21](../SOURCES.md#r21) [R26](../SOURCES.md#r26)

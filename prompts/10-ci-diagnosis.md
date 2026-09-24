# Diagnose CI without weakening it

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for failing, missing or excessively duplicated checks.

```text
Inspect the current candidate's CI configuration and actual failed or missing checks. Use existing GitHub access. If using gh-fix-ci, follow its GitHub Actions scope and fix-plan approval requirement, reusing applicable approval already supplied. Otherwise use the existing provider tools within this task's authorization.

Identify whether the cause is code, setup, permissions, infrastructure, stale evidence or a workflow trigger. Distinguish required head/test-merge checks and merge-queue behavior. Read relevant logs with secrets redacted.

For a diagnosis-only request, propose the smallest correction. When repair is authorized as part of implementation or integration, apply it, resolve blocking baseline failures within scope and continue until the required gates pass or a consequential decision is needed. Preserve required gates and assertions. Do not disable branch protection, remove failures from reporting, or repeatedly dispatch full workflows. Identify duplicate builds or obsolete runs, but do not cancel releases or migrations casually.

Return the cause, current revision/check identifiers, proposed fix, validation plan and cost implications. Apply or publish changes only within the explicit authorization for this task.
```

Related documentation: [R20](../SOURCES.md#r20) [R25](../SOURCES.md#r25) [R26](../SOURCES.md#r26)

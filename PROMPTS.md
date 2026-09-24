# Prompt library

[Home](README.md) · [Setup](SETUP.md) · [Compatibility](COMPATIBILITY.md) · [Evidence](GATES.md)

These **19 original prompts are a conditional menu**. Select the current task below and copy its code block or explicitly ask the agent to use the attached file. Follow the [usage and mention guidance](README.md#using-a-prompt); files in this directory do not register native commands or install skills.

Use existing task context and authorization. A referenced source explains a capability; the prompt wording is this kit's synthesis. Each prompt states its own scope, so a read-only review prompt does not silently authorize fixes. When you want review and fixes, state that in the task and use the implementation and verification prompts for the corrections.

[Understand](#understand) · [Implement and verify](#implement-and-verify) · [Review and publish](#review-and-publish) · [Release](#release) · [Handoff and evaluate](#handoff-and-evaluate)

## Understand

| Prompt | Use when |
|---|---|
| [18 · Build a first useful version from an idea](prompts/18-build-from-idea.md) | Use when the user has an idea but no implementation plan or coding experience. |
| [00 · Onboard the selected repository](prompts/00-onboard-repo.md) | Use once per repository, or after a material environment change. |
| [01 · Define the task contract](prompts/01-task-contract.md) | Use when the desired outcome or scope is genuinely unclear. |
| [02 · Resolve one material uncertainty](prompts/02-research-uncertainty.md) | Use for an external fact that could change implementation. |
| [03 · Plan a nontrivial change](prompts/03-plan-risky-change.md) | Use for multi-system, high-risk or poorly understood work; skip routine edits. |

## Implement and verify

| Prompt | Use when |
|---|---|
| [04 · Implement the agreed change](prompts/04-implement.md) | Default implementation prompt after a concrete request. |
| [05 · Implement and inspect UI behavior](prompts/05-ui-change.md) | Use for a UI change; not a mandate to redesign the application. |
| [06 · Change data access or schema safely](prompts/06-data-change.md) | Use for database, query, access-policy or persistent-data work. |
| [07 · Verify the current candidate](prompts/07-verify-local.md) | Use before claiming local completion. |
| [08 · Diagnose and fix a failure](prompts/08-debug-failure.md) | Use when a check or observed behavior fails. |

## Review and publish

| Prompt | Use when |
|---|---|
| [09 · Review independently without editing](prompts/09-review-read-only.md) | Use for substantive or risky changes, ideally in a fresh review context. |
| [10 · Diagnose CI without weakening it](prompts/10-ci-diagnosis.md) | Use for failing, missing or excessively duplicated checks. |
| [11 · Prepare one reviewable PR](prompts/11-prepare-pr.md) | Use when local work is ready for an authorized publication. |
| [12 · Verify the deployed preview](prompts/12-verify-preview.md) | Use after preview deployment is authorized and target identity is known. |

## Release

| Prompt | Use when |
|---|---|
| [13 · Assess production readiness](prompts/13-production-readiness.md) | Read-only release assessment; does not authorize a release. |
| [14 · Execute an explicitly authorized release](prompts/14-authorized-release.md) | Use only after approval identifies the target and material change. |
| [15 · Verify the shipped behavior](prompts/15-post-release.md) | Use for a bounded check of an actual completed release. |

## Handoff and evaluate

| Prompt | Use when |
|---|---|
| [16 · Hand off a task without losing state](prompts/16-handoff.md) | Use at a real handoff or context boundary, not after every small edit. |
| [17 · Evaluate one tool or skill addition](prompts/17-evaluate-addition.md) | Use before claiming a setup change improves shipping. |

For a new idea without a technical plan, start with 18. For an ordinary change in an existing repository, start with 04. Use 07 for missing or invalidated verification, reusing evidence that still applies. Use 00 when the environment is unfamiliar, and 09 for a separate review when risk warrants it. Publication and release depend on authorization for those actions and targets.

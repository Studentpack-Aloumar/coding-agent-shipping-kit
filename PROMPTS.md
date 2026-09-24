# Prompt library

These **18 original prompts are a conditional menu, not an 18-step process**. Use them alongside the current request and repository context. They do not install skills, override higher-priority policy, or grant permission to external actions. A referenced source explains the underlying capability; the prompt wording is this kit's synthesis.

| Prompt | Use when |
|---|---|
| [00 · Onboard the selected repository](prompts/00-onboard-repo.md) | Use once per repository, or after a material environment change. |
| [01 · Define the task contract](prompts/01-task-contract.md) | Use when the desired outcome or scope is genuinely unclear. |
| [02 · Resolve one material uncertainty](prompts/02-research-uncertainty.md) | Use for an external fact that could change implementation. |
| [03 · Plan a nontrivial change](prompts/03-plan-risky-change.md) | Use for multi-system, high-risk or poorly understood work; skip routine edits. |
| [04 · Implement the agreed change](prompts/04-implement.md) | Default implementation prompt after a concrete request. |
| [05 · Implement and inspect UI behavior](prompts/05-ui-change.md) | Use for a UI change; not a mandate to redesign the application. |
| [06 · Change data access or schema safely](prompts/06-data-change.md) | Use for database, query, access-policy or persistent-data work. |
| [07 · Verify the current candidate](prompts/07-verify-local.md) | Use before claiming local completion. |
| [08 · Diagnose and fix a failure](prompts/08-debug-failure.md) | Use when a check or observed behavior fails. |
| [09 · Review independently without editing](prompts/09-review-read-only.md) | Use for substantive or risky changes, ideally in a fresh review context. |
| [10 · Diagnose CI without weakening it](prompts/10-ci-diagnosis.md) | Use for failing, missing or excessively duplicated checks. |
| [11 · Prepare one reviewable PR](prompts/11-prepare-pr.md) | Use when local work is ready for an authorized publication. |
| [12 · Verify the deployed preview](prompts/12-verify-preview.md) | Use after preview deployment is authorized and target identity is known. |
| [13 · Assess production readiness](prompts/13-production-readiness.md) | Read-only release assessment; does not authorize a release. |
| [14 · Execute an explicitly authorized release](prompts/14-authorized-release.md) | Use only after approval identifies the target and material change. |
| [15 · Verify the shipped behavior](prompts/15-post-release.md) | Use for a bounded check of an actual completed release. |
| [16 · Hand off a task without losing state](prompts/16-handoff.md) | Use at a real handoff or context boundary, not after every small edit. |
| [17 · Evaluate one tool or skill addition](prompts/17-evaluate-addition.md) | Use before claiming a setup change improves shipping. |

**Most ordinary tasks:** use 04, then 07. Start with 00 only when the environment is not already understood. Use 09 in a separate review context for substantive risk. Publishing and release prompts are never implied by local implementation.

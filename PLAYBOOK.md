# Shipping playbook

[Home](README.md) · [Prompts](PROMPTS.md) · [Resources](RESOURCES.md) · [Gates](GATES.md)

Recommendations; no comparative benchmark. Optimize accepted, working changes.

## 1. Use a small default loop

**Understand → implement → verify → deliver evidence.** Add planning, research, specialist review or deployment when warranted. Start with your working agent, tested startup recipe and clear criteria. [R01](SOURCES.md#r01) [R03](SOURCES.md#r03)

## For a first-time builder

Use [18 · Build](prompts/18-build-from-idea.md) and [product excellence](PRODUCT-EXCELLENCE.md): user, problem, alternatives, advantage, essential journey. Test risky assumptions; deliver complete increments. Separate user, design and commercial evidence.

Before new construction, [select reusable products/components](REUSE.md#select-before-building). Use [build recipes](BUILD-RECIPES.md): qualify one base, design the first journey, assemble in dependency order, retain actual evidence. Saved recipes reduce repeated discovery; relevant version/environment changes require requalification.

Running work needs an executing job. Preview must open for the owner and match the tested revision. Changed briefs invalidate dependent evidence. Source checkpoints restore no database, external resource or charge; chat budgets enforce no provider cap.

## 2. Match the resource to the decision

| Need | Resource / evidence |
|---|---|
| Orient | Native search/setup; actual paths, runtime, commands, baseline |
| Clarify | Short contract; observable outcome and exclusions |
| Research | Existing browser/search, optional Exa/Context7; version, source, consequence |
| Plan | Native planning; dependencies, risky steps, tests |
| Implement | Existing editor/components; complete scoped diff |
| Specialize | Relevant React, shadcn or database guidance only |
| Verify/debug | Existing tests/browser; reproduction, results, artifacts |
| Review/PR | Fresh review, existing GitHub access; findings resolved, candidate checks |
| Preview | Existing deployment/browser; revision, deployment, journey, logs |
| Release | Authorized process; recovery compatibility, bounded observation |

Use available alternatives when named tools are missing. Add capabilities only for a concrete gap.

## 3. Separate instructions, skills, tools and enforcement

Prompt: current task. Repository instructions: durable facts. Skill: reusable method. Tool: capability. Plugin: distribution. Permissions/tests/CI: enforcement. [R02](SOURCES.md#r02) [R06](SOURCES.md#r06) [R29](SOURCES.md#r29)

Keep persistent instructions short: map, verified commands, constraints, completion. Link long procedures. Memories cannot silently override policy. Explicitly adopt the [owner agreement](templates/INSTRUCTIONS.owner.md); narrower task scope still controls. Vercel's compact documentation-index result supports workload-specific evaluation, not universal superiority. [R28](SOURCES.md#r28)

## 4. Establish a reproducible environment before adding helpers

Record runtime/package-manager versions, lockfile, services, environment-variable names, successful install/start/check commands, cold starts and baseline failures. Never invent generic commands.

Copilot cloud: `.github/workflows/copilot-setup-steps.yml`; failed setup can leave the agent running partially configured. Other clients use their own setup. [R18](SOURCES.md#r18)

Worktrees isolate files, not databases/ports/accounts. For parallel work: one writer per worktree, isolated shared resources, one integration owner. [R32](SOURCES.md#r32)

## 5. Keep the task contract short and testable

**Outcome, context, constraints, completion evidence.** [R01](SOURCES.md#r01)

> Add import cancellation: stop processing, preserve records, allow restart. Reuse current UI/worker. Test mid-processing and pre-completion cancellation; exercise the app. No production deployment.

Scale process to risk. Under adopted ownership, fix adjacent defects preserving intent and blocking baseline failures. Ask before consequential scope/cost/risk/approach changes.

## 6. Treat UI verification as more than a screenshot

Exercise success, relevant loading/empty/error states, keyboard access and narrow viewports. Inspect console/network; verify required server effects. Keep useful repeatable regressions in the suite. Reuse existing browser tooling. [R15](SOURCES.md#r15) [R16](SOURCES.md#r16)

## 7. Make review independent in a useful way

Read-only reviewer: original contract, policy, base/head, diff, artifacts and running product. Require evidenced findings, explicit uncertainty, no quota. Implementer fixes; reruns affected checks.

Fresh context guarantees no correctness. For substantial products, assess usefulness, clarity, coherence, originality, accessibility, reliability and maintainability. Retain strongest candidate; stop unproductive polishing. Agent review proves no customer demand. [R03](SOURCES.md#r03) [R37](SOURCES.md#r37)

## 8. Optimize CI without weakening the gate

Focused checks during iteration; required checks at candidate boundary. Reuse valid evidence; rerun invalidated checks. Missing/skipped/stale checks cannot pass. Preserve assertions and branch protection.

Cancel obsolete validation, cache safely, retain failure artifacts, avoid duplicate builds. Protect release/migration jobs from casual cancellation. Required gates must report through path filters and merge queues. [R25](SOURCES.md#r25) [R26](SOURCES.md#r26)

## 9. Make the release boundary explicit

Confirm account, project/history, revision, environment, data isolation, authorization and automatic push/merge effects. Vercel's first project deployment is production, even without `--prod`. [R23](SOURCES.md#r23)

Reuse matching deployments and existing applicable approval. Record immutable deployment ID; material artifact/configuration/migration changes require reassessment. Application rollback restores no external data by itself. Verify recovery compatibility and shipped behavior over a stated interval. [R24](SOURCES.md#r24)

## 10. Decide what deserves to become a skill

Package repeatedly useful methods; script deterministic repetitive work. Verify appropriate discovery, non-activation on unrelated tasks and completed behavior. Measure completion, elapsed time, human corrections, tool/model/CI cost including failures. Use the [evaluation protocol](EVALUATION.md). [R02](SOURCES.md#r02) [R27](SOURCES.md#r27)

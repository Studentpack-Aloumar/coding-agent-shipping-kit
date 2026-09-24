# Permission and evidence gates
The policy below is a recommended starting point, not a claim about controls already configured in your accounts.

## Authorization boundaries
| Activity | Recommended boundary |
|---|---|
| Read code and inspect local status | Allowed within the selected workspace; protect secrets and unrelated personal files |
| Edit code, add tests, run local checks | Within the approved feature scope and isolated workspace; inspect scripts before first execution |
| Install packages/plugins or change agent configuration | Specific setup authorization; review downloads, hooks, scope and costs |
| Public documentation queries | No private source, credentials, patient/customer records or proprietary payloads |
| Push a branch or publish a PR | Authorized publication to the specified repository; never infer merge permission |
| Preview deployment | Confirm target and authorization; synthetic data; assess build/startup side effects |
| Production, migrations, destructive operations, paid resources | Explicit authorization for target and material change; approved recovery plan |
| Post-release checks | Read-only where possible; test writes require bounded synthetic accounts and cleanup authorization |

Use client permissions, sandboxing, service access controls and CI enforcement. Reviewed deterministic hooks can add checks at supported events; prose instructions alone do not enforce an access boundary. [R06](SOURCES.md#r06)

## Completion states
| State | Minimum evidence |
|---|---|
| Implemented | Exact revision or worktree diff and scope summary; no verification implied |
| Locally verified | Relevant commands/results and behavioral evidence tied to that candidate |
| CI verified | Required checks for the relevant head/test-merge candidate; failures and skips explicit |
| Preview verified | Deployment ID, revision, environment and actual tested journey |
| Ready for production | Required evidence plus reviewed configuration/data changes and recovery compatibility; not deployment approval |
| Production verified | Exact deployed artifact and stated checks/observation interval; not a promise of future health |

Use `not_run`, `fail`, `blocked` or justified `not_applicable` instead of inventing success. A baseline failure is a recorded blocker or explicitly accepted exception—not a pass. After material edits, rerun invalidated checks and reassess the candidate. Required status checks have specific revision and skipped-workflow semantics. [R26](SOURCES.md#r26)

## Evidence record
Record the task/acceptance criteria, base/head revisions or diff identity, environment, commands, start time, exit code, result, artifact locations, reviewer findings, approvals and unresolved risks. Keep secrets out of logs and evidence. The included JSON schema standardizes the shape only; it cannot prove that assertions or approvals are genuine.

## Retry and cost policy
My proposed starting rule is to reassess after two failed approaches to the same blocker. This is a configurable diagnostic trigger, not a universal optimal limit. Capture the hypothesis and new evidence before another attempt. Never loop until the agent happens to produce green output.

Cancel obsolete validation runs using scoped concurrency where appropriate; do not apply that policy indiscriminately to deployment or migration jobs. Retain failing artifacts, avoid duplicating equivalent checks, and report missing checks without weakening policy. [R25](SOURCES.md#r25)

## Release traps
A new Vercel project's first deployment is production; confirm project history and environment instead of relying only on the absence of `--prod`. Preview credentials can still point at a production database if incorrectly configured. Vercel describes environment separation, but the actual configuration must be inspected. [R23](SOURCES.md#r23)

A code rollback is not a database rollback. Review external compatibility, data recovery and the actual eligible prior deployment before promising recovery. [R24](SOURCES.md#r24)

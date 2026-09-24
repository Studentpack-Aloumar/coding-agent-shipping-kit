# Shipping playbook

[Home](README.md) · [Prompts](PROMPTS.md) · [Setup](SETUP.md) · [Evidence](GATES.md) · [Sources](SOURCES.md)

**Recommendation:** optimize accepted, working changes—not generated code, agent count or number of installed skills.

## 1. Use a small default loop
For an ordinary scoped change: **understand → implement → verify → deliver evidence**. Planning, external research, specialist review and deployment are conditional branches, not mandatory ceremonies. Claude's documentation explicitly distinguishes tasks that benefit from planning from simple edits; Codex recommends clear outcomes and task context. [R03](SOURCES.md#r03) [R01](SOURCES.md#r01)

Use the coding agent that already has a functioning repository environment. This research does not establish that switching models or clients would improve your results. My recommended first intervention is a reliable startup recipe and clear acceptance criteria; compare tool additions afterward.

## For a first-time builder

When a user describes an idea rather than a specific code change, use the [build-from-idea prompt](prompts/18-build-from-idea.md). Capture the essential user journey and information/spending constraints, then make routine technical decisions in the selected workspace. A working version requires executed implementation and tested behavior. A saved brief, plan, or screen showing progress steps without an executing job is not a running build.

Keep status understandable: queued work is not running work; a preview must open for the owner and point to the tested revision; a changed brief can invalidate older green evidence. For risky source edits, make recovery practical. A source checkpoint does not restore database records, external resources or provider charges. A budget requested in chat is a planning limit unless the provider enforces it.

## 2. Match the resource to the decision
The choices and gates below are recommendations. The linked resources establish capabilities, not comparative superiority. Reuse the tools already available. A named optional tool is not a prerequisite when an existing capability can meet the requirement.

| Development stage | Recommended resource | Trigger / when to skip | Evidence before proceeding |
|---|---|---|---|
| Orient and start | Native file search, shell and existing setup scripts; Copilot setup steps only for Copilot cloud | New repo or changed environment; otherwise reuse the verified recipe | Actual runtime, commands, relevant paths and baseline status |
| Define the change | Native agent conversation; a short task contract | Ambiguous outcome, users or scope; skip when already explicit | Observable acceptance conditions and exclusions |
| Resolve uncertainty | Existing search/browser; Exa or Context7 when available and useful | Material API or architecture uncertainty; skip settled facts | Applicable version, source and implementation consequence |
| Plan | Native plan mode; existing Superpowers planning when that framework is deliberately in use | Multi-system, irreversible or poorly understood change | Small ordered plan, dependencies and tests |
| Implement | Native editor, language navigation and existing test tools | Every code change; do not add a generic implementation skill by default | Scoped diff that meets the contract |
| Apply domain expertise | Vercel React/UI skills, shadcn or Supabase skills | Only the matching framework or subsystem | Actual relevant rule applied, not an unrelated rewrite |
| Verify and debug | Existing test suite; Playwright; native running-app checks; systematic-debugging for a failure | Verification always proportional to impact; debugging only when needed | Reproduction and relevant tests, commands, results, artifacts |
| Review and prepare PR | Fresh native review; GitHub CLI/MCP; gh-fix-ci for its specific scope | Independent review for substantive/risky changes | Actionable findings resolved; current candidate checks recorded |
| Validate preview | Existing deployment integration; Vercel CLI/MCP and browser | Deployed web behavior needs validation | Exact deployment, revision, journey and log findings |
| Release and observe | Existing release process and observability | Only an explicitly authorized production target | Release evidence, rollback compatibility and bounded post-release checks |

Resource details: [catalogue](RESOURCES.md). Prompt equivalents: [prompt index](PROMPTS.md).

## 3. Separate instructions, skills, tools and enforcement
A task prompt specifies this change. A repository instruction file stores the small set of durable facts the agent needs repeatedly. A skill packages a reusable method with optional supporting material. A tool gives the agent an execution or retrieval capability. A plugin distributes one or more capabilities. A configured permission, test or CI gate constrains or checks actual actions. These layers are complementary, not interchangeable. [R01](SOURCES.md#r01) [R02](SOURCES.md#r02) [R29](SOURCES.md#r29) [R06](SOURCES.md#r06)

My recommended repository guidance contains verified startup/check commands, a short navigation map, material constraints and the meaning of completion. Put long procedures outside the always-loaded file. Do not let automatic memories or generated guidance silently override team policy.

Avoid the opposite mistake: assuming all durable documentation is harmful. Vercel's published Next.js experiment found useful results from a compact documentation index in AGENTS.md. That is evidence for testing retrieval and activation on your workload, not proof that one instruction style always wins. [R28](SOURCES.md#r28)

## 4. Establish a reproducible environment before adding helpers
Record the runtime and package-manager versions from the repository, the lockfile, service requirements, environment-variable **names**, and actual successful install/start/test commands. Note cold-start behavior, known baseline failures and whether a browser or database is available. Never substitute a generic npm command for a different repository's real scripts.

For Copilot cloud, the documented setup file is `.github/workflows/copilot-setup-steps.yml`. A setup failure can still leave the agent running in a partially configured environment; the task must not treat that as a healthy baseline. Other agents should use their own environment mechanism, not receive a Copilot-only workflow by default. [R18](SOURCES.md#r18)

A local worktree isolates file changes, not every database, port or external account used by those files. My recommendation for parallel work is one write owner per worktree, separate service/test resources where required, and one integration owner. Delegate independent inspection before parallelizing overlapping implementation. Claude documents worktree workflows and isolated research contexts. [R32](SOURCES.md#r32)

## 5. Keep the task contract short and testable
Use four fields: **outcome, context, constraints, completion evidence**. This follows Codex's recommended prompt structure, while leaving technical implementation to the agent. [R01](SOURCES.md#r01)

Example contract, written for this kit:

> Add cancellation to the existing import flow. Cancel must stop further processing, leave existing records intact and let the user start another import. Reuse the current UI and worker architecture. Cover cancellation during processing and immediately before completion. Show the passing regression tests and exercise the flow in the running app. No production deployment is authorized.

Do not require a plan file, new abstraction, exhaustive research or multiple agents for that change unless the implementation actually warrants them. Conversely, a schema migration or authorization boundary should not be rushed merely because its code diff is small.

## 6. Treat UI verification as more than a screenshot
For a changed user journey, my recommended minimum is the relevant success case, loading/empty/error states, keyboard access and an appropriate narrow viewport. Check console and network failures. Confirm server-side effects where the feature requires them. Preserve a durable regression test for repeatable behavior; an exploratory browser session alone is not that test.

Playwright distinguishes its coding-agent CLI from MCP-based exploratory workflows. Its test guidance emphasizes user-visible behavior and isolated tests. Prefer the existing browser route when it works; add another one only for a concrete capability gap. [R15](SOURCES.md#r15) [R16](SOURCES.md#r16)

## 7. Make review independent in a useful way
My recommended reviewer receives the original contract, relevant policy, base and head revisions, the diff and access to validation artifacts—not a persuasive explanation of why the implementation is correct. Request evidenced bugs and explicit uncertainty, not a quota of findings. The reviewer is read-only; the implementer makes confirmed corrections and reruns affected checks.

A fresh context reduces shared narrative but does not prove statistical independence or correctness. Tests and review can still miss the same requirement. Keep acceptance criteria separate from the implementation, and report review limitations. Claude's best-practice guidance also warns against soliciting speculative overengineering. [R03](SOURCES.md#r03)

## 8. Optimize CI without weakening the gate
During iteration, run focused checks. At the candidate boundary, run the checks the repository actually requires. Avoid launching several overlapping full suites per edit; reuse existing CI results for the same candidate and environment where valid. A changed revision or dependency invalidates evidence as appropriate.

My proposed cost controls: cancel obsolete PR-validation runs, cache dependencies safely, avoid duplicate builds unless targets differ, retain failure artifacts and give each check an owner. Keep release/migration jobs out of casual cancellation policies. GitHub documents concurrency controls. Its required-check rules also mean a path-filtered skipped workflow can leave a required check waiting; keep an always-reporting gate and handle merge-queue events where used. [R25](SOURCES.md#r25) [R26](SOURCES.md#r26)

An absent, skipped or stale check is not a pass. Do not disable branch protection, remove failing assertions or weaken policy to improve apparent throughput.

## 9. Make the release boundary explicit
A build, a preview URL and a production deployment are different achievements. Before any deployment, confirm the account, existing project, revision, target environment, data isolation and authorization. Before a push or merge, inspect whether that action automatically deploys or releases; production approval must cover those effects too. Vercel documents an important exception: a new project's first deployment is production. A plain CLI invocation is therefore not an unconditional preview guarantee. [R23](SOURCES.md#r23)

Reuse authorization already supplied for the same action, artifact and target. Use the current deployment from the Git integration rather than starting an unnecessary duplicate. Record an immutable deployment identifier, not only a moving branch alias. Production approval should identify the artifact and material migrations/configuration changes. Reassess approval when the release changes materially.

Application rollback cannot be assumed to undo external database, API or content-system changes. Review compatibility and recovery separately. Observe the actual shipped revision for a stated period and report only what was checked; a single successful request is not evidence of universal health. [R24](SOURCES.md#r24)

## 10. Decide what deserves to become a skill
Start from a repeatedly useful procedure. Test whether the agent discovers it for matching tasks, avoids it for unrelated tasks, and produces the intended evidence. Package deterministic scripts only where they genuinely remove unreliable repeated work. Do not create a skill solely to give an ordinary prompt a more impressive name. [R02](SOURCES.md#r02) [R29](SOURCES.md#r29)

Measure before expanding: completion rate, elapsed time, human corrections, tokens/tool calls and total cost including failures. The evaluation protocol in this kit is a proposed local experiment, inspired by OpenAI's skill-evaluation guidance—not a benchmark already run. [R27](SOURCES.md#r27)

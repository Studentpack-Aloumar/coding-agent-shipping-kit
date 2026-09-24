# Source register

[Home](README.md) · [Prompts](PROMPTS.md) · [Setup](SETUP.md) · [Evidence](GATES.md) · [Sources](SOURCES.md)

Checked on **24 September 2026** using Exa and primary-source web retrieval. Links are to publishers or maintainers, not repackaged skill catalogues.

Documentation supports the listed capabilities, not a claim that a package is fastest, independently audited, or supported forever. No user repository, installed client, benchmark run or deployment was inspected. Source pages can change after this date.

The v1.0.2 maintenance pass checked all 32 URLs for HTTP availability and rechecked selected compatibility/setup claims (R04, R05, R08, R09, R12, R15, R17, R19, R20, R23 and R30). All URLs responded successfully, including redirects. Link availability is not full factual revalidation of every statement. The original statement above describes the initial research, not the subsequent publication recorded in [PUBLISH.md](PUBLISH.md).

<a id="r01"></a>
### R01 · OpenAI — Codex best practices

[OpenAI — Codex best practices](https://developers.openai.com/codex/learn/best-practices)

**Evidence:** Vendor documentation. Task context, reusable instructions, selective planning and review. Redirects to ChatGPT Learn.

<a id="r02"></a>
### R02 · OpenAI — Agent Skills

[OpenAI — Agent Skills](https://developers.openai.com/codex/skills)

**Evidence:** Vendor documentation. Codex discovery paths, explicit invocation and skill installer. Redirects to ChatGPT Learn.

<a id="r03"></a>
### R03 · Anthropic — Claude Code best practices

[Anthropic — Claude Code best practices](https://code.claude.com/docs/en/best-practices)

**Evidence:** Vendor documentation. Conditional planning, context discipline and verifiable outcomes.

<a id="r04"></a>
### R04 · Anthropic — Extend Claude with skills

[Anthropic — Extend Claude with skills](https://code.claude.com/docs/en/skills)

**Evidence:** Vendor documentation. Bundled run/verify/review skills, custom skill discovery and overrides.

<a id="r05"></a>
### R05 · Anthropic — Project memory and instructions

[Anthropic — Project memory and instructions](https://code.claude.com/docs/en/memory)

**Evidence:** Vendor documentation. Conditional AGENTS.md support and explicit CLAUDE.md imports.

<a id="r06"></a>
### R06 · Anthropic — Hooks guide

[Anthropic — Hooks guide](https://code.claude.com/docs/en/hooks-guide)

**Evidence:** Vendor documentation. Lifecycle hooks; distinguish executable checks from prose guidance.

<a id="r07"></a>
### R07 · Exa — MCP documentation

[Exa — MCP documentation](https://exa.ai/docs/reference/exa-mcp)

**Evidence:** Vendor documentation. Public-source discovery. Actual tool names depend on integration.

<a id="r08"></a>
### R08 · Upstash — Context7

[Upstash — Context7](https://github.com/upstash/context7)

**Evidence:** Maintainer repository. Version-aware documentation via CLI plus skills or MCP; inspect source coverage.

<a id="r09"></a>
### R09 · Superpowers — Maintainer repository

[Superpowers — Maintainer repository](https://github.com/obra/superpowers)

**Evidence:** Maintainer repository. Opinionated lifecycle skills, supported agent integrations and installation.

<a id="r10"></a>
### R10 · Vercel — React skill source

[Vercel — React skill source](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)

**Evidence:** Maintainer skill source. Declared skill name is vercel-react-best-practices; folder name differs.

<a id="r11"></a>
### R11 · Vercel — Agent skills collection

[Vercel — Agent skills collection](https://github.com/vercel-labs/agent-skills)

**Evidence:** Maintainer repository. Includes web-design-guidelines; consult actual selected skill.

<a id="r12"></a>
### R12 · shadcn — Agent skills

[shadcn — Agent skills](https://ui.shadcn.com/docs/skills)

**Evidence:** Vendor documentation. Project-aware shadcn component and configuration guidance.

<a id="r13"></a>
### R13 · Supabase — Agent skills

[Supabase — Agent skills](https://github.com/supabase/agent-skills)

**Evidence:** Maintainer repository. Supabase product guidance and supabase-postgres-best-practices.

<a id="r14"></a>
### R14 · Supabase — MCP

[Supabase — MCP](https://supabase.com/docs/guides/ai-tools/mcp)

**Evidence:** Vendor documentation. Development-only data access guidance and MCP precautions.

<a id="r15"></a>
### R15 · Microsoft Playwright — Coding agents

[Microsoft Playwright — Coding agents](https://playwright.dev/docs/getting-started-cli)

**Evidence:** Vendor documentation. CLI versus MCP use cases and CLI skill installation.

<a id="r16"></a>
### R16 · Microsoft Playwright — Test best practices

[Microsoft Playwright — Test best practices](https://playwright.dev/docs/best-practices)

**Evidence:** Vendor documentation. User-visible tests, isolation, resilient locators and failure diagnosis.

<a id="r17"></a>
### R17 · GitHub — About agent skills

[GitHub — About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

**Evidence:** Vendor documentation. Supported Copilot surfaces and skill discovery directories.

<a id="r18"></a>
### R18 · GitHub — Copilot cloud development environment

[GitHub — Copilot cloud development environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)

**Evidence:** Vendor documentation. copilot-setup-steps.yml and behavior when setup fails.

<a id="r19"></a>
### R19 · GitHub — Configure repository MCP servers

[GitHub — Configure repository MCP servers](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers)

**Evidence:** Vendor documentation. Cloud/review OAuth limitation, autonomous tool use and tool allowlists.

<a id="r20"></a>
### R20 · OpenAI — gh-fix-ci skill

[OpenAI — gh-fix-ci skill](https://github.com/openai/skills/blob/main/skills/.curated/gh-fix-ci/SKILL.md)

**Evidence:** Maintainer skill source. GitHub Actions diagnosis with gh; approval before implementation.

<a id="r21"></a>
### R21 · GitHub — Official MCP server

[GitHub — Official MCP server](https://github.com/github/github-mcp-server)

**Evidence:** Maintainer repository. Repository, PR and CI tool access; scope configured permissions.

<a id="r22"></a>
### R22 · Vercel — Official MCP server

[Vercel — Official MCP server](https://vercel.com/docs/agent-resources/vercel-mcp)

**Evidence:** Vendor documentation. OAuth connection, supported clients, deployments and logs.

<a id="r23"></a>
### R23 · Vercel — Deployment environments

[Vercel — Deployment environments](https://vercel.com/docs/deployments/environments)

**Evidence:** Vendor documentation. Local, Preview and Production; first deployment production caveat. Retrieved with Exa.

<a id="r24"></a>
### R24 · Vercel — Instant Rollback

[Vercel — Instant Rollback](https://vercel.com/docs/instant-rollback)

**Evidence:** Vendor documentation. Rollback eligibility and external configuration/data compatibility. Retrieved with Exa.

<a id="r25"></a>
### R25 · GitHub — Workflow concurrency

[GitHub — Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)

**Evidence:** Vendor documentation. Workflow concurrency groups and cancellation controls.

<a id="r26"></a>
### R26 · GitHub — Required status checks troubleshooting

[GitHub — Required status checks troubleshooting](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)

**Evidence:** Vendor documentation. Required checks, skipped workflows and merge queue events.

<a id="r27"></a>
### R27 · OpenAI — Evaluating skills

[OpenAI — Evaluating skills](https://developers.openai.com/blog/eval-skills)

**Evidence:** Publisher evaluation guidance. Evaluate workflow behavior and resource use on representative tasks.

<a id="r28"></a>
### R28 · Vercel — AGENTS.md versus skills evaluation

[Vercel — AGENTS.md versus skills evaluation](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

**Evidence:** Publisher benchmark. Narrow Next.js experiment; not a universal agent or skill ranking.

<a id="r29"></a>
### R29 · Agent Skills — Format specification

[Agent Skills — Format specification](https://agentskills.io/specification)

**Evidence:** Open format specification. SKILL.md, metadata, supporting files and progressive loading.

<a id="r30"></a>
### R30 · Cursor — Skills

[Cursor — Skills](https://cursor.com/docs/skills)

**Evidence:** Vendor documentation. Skill discovery paths, compatibility locations and invocation.

<a id="r31"></a>
### R31 · Cursor — Rules

[Cursor — Rules](https://cursor.com/docs/rules)

**Evidence:** Vendor documentation. Project rules and AGENTS.md guidance.

<a id="r32"></a>
### R32 · Anthropic — Common workflows

[Anthropic — Common workflows](https://code.claude.com/docs/en/common-workflows)

**Evidence:** Vendor documentation. Repository exploration, worktrees and delegated research.

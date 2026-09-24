# Setup and activation

[Home](README.md) · [Prompts](PROMPTS.md) · [Setup](SETUP.md) · [Evidence](GATES.md) · [Sources](SOURCES.md)

**Nothing below has been executed against your environment.** These are publisher-documented entry points, not a bulk installation script. A command may download code, modify configuration or initiate authentication.

First inventory existing tools and skills. Inspect publisher ownership, package contents and requested access. Select a reviewed release/version using the installer's supported options and record it; do not put an unpinned remote installer into a recurring startup job. Avoid duplicate global and project installations.

## Native capabilities first
In Codex, inspect `/skills` and use `$skill-installer` for a specifically selected skill. In Claude Code, inspect the current `/` menu before creating replacements for run/verify/review. Check existing same-name overrides. [R02](SOURCES.md#r02) [R04](SOURCES.md#r04)

## Targeted optional examples
Run these only when the particular installation is covered by the task authorization and after inspecting the current installer help. Existing authorization remains valid for the same installation and scope.

| Need | Documented entry point |
|---|---|
| Vercel React skill | `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices` |
| Vercel UI-review skill | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |
| Supabase Postgres skill | `npx skills add supabase/agent-skills --skill supabase-postgres-best-practices` |
| shadcn skill package | `pnpm dlx skills add shadcn/ui` |
| Context7 setup | `npx ctx7 setup` — choose CLI/skills or MCP, not both by default |
| Playwright skills, after approved CLI installation | `playwright-cli install --skills` for Claude; `playwright-cli install --skills=agents` for clients discovering `.agents/skills/`, including Codex |
| Superpowers in Claude Code | `/plugin install superpowers@claude-plugins-official` |
| Superpowers in Codex CLI | Open `/plugins`, find Superpowers, inspect and install |
| Superpowers in Codex app | Open Plugins in the sidebar, find Superpowers, inspect and install |

Sources: [R10](SOURCES.md#r10) [R11](SOURCES.md#r11) [R13](SOURCES.md#r13) [R12](SOURCES.md#r12) [R08](SOURCES.md#r08) [R15](SOURCES.md#r15) [R09](SOURCES.md#r09). Use the repository's package manager where equivalent supported commands exist; do not install another manager just for an example.

Playwright's CLI requires Node.js 20 or newer. Confirm the installed CLI supports the selected skill location and that your agent discovers it. A successful install into another client's directory does not establish activation. [R15](SOURCES.md#r15)

For `gh-fix-ci`, use Codex's skill installer to select that skill from the official OpenAI skills repository. Preserve the skill's plan-approval requirement, reusing approval already supplied for the same plan. [R02](SOURCES.md#r02) [R20](SOURCES.md#r20)

## Vercel connection, only when needed
Codex CLI publisher example:
```sh
codex mcp add vercel --url https://mcp.vercel.com
```
Claude Code publisher example:
```sh
claude mcp add --transport http vercel https://mcp.vercel.com
```
Authorize the intended account and verify the visible project before issuing a write. These connection commands do not by themselves restrict access to previews or approve production work. Copilot cloud is subject to the limitation in [COMPATIBILITY.md](COMPATIBILITY.md). [R22](SOURCES.md#r22)

## Repository instructions
Review `templates/AGENTS.starter.md` as a policy example, not a replacement for the repository's real map and commands. Onboarding must add only commands it actually validated. `templates/CLAUDE.import.md` shows the documented import line; use it only next to the intended root AGENTS.md and merge with existing instructions. [R05](SOURCES.md#r05)

After setup, run one harmless activation check and one representative nonproduction task. Save the exact package/client versions and configuration diff. Installation success is not evidence that the skill improves shipping.

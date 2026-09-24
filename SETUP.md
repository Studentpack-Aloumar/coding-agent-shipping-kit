# Setup and activation

[Home](README.md) · [Compatibility](COMPATIBILITY.md) · [Gates](GATES.md)

**Optional installation examples; not executed.** Commands may download code, change settings or authenticate. Inventory existing capabilities first. Inspect publisher, contents, privileges, recipients and costs; select/record reviewed versions. No unpinned recurring installers or duplicate installations.

## Included project skill

This checkout includes `.agents/skills/ship-task/`. Open a fresh task here and invoke `$ship-task` in a compatible client. No global configuration required. Its links depend on this complete checkout; copying only the skill folder breaks them. Other repositories can use the original prompts directly. [Roles](.agents/skills/ship-task/references/roles.md) · [Sources by layer](REUSE.md).

## Native capabilities first

Codex: `/skills`, `$skill-installer`. Claude: installed `/` menu. Check overrides before adding tools. [R02](SOURCES.md#r02) [R04](SOURCES.md#r04)

## Targeted optional examples

Use applicable setup authority; adopted [owner agreement](templates/INSTRUCTIONS.owner.md) covers necessary setup within its boundaries. Inspect current installer help; prefer equivalent commands using the existing package manager.

| Need | Entry point |
|---|---|
| React | `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices` |
| UI review | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |
| Postgres | `npx skills add supabase/agent-skills --skill supabase-postgres-best-practices` |
| shadcn | `pnpm dlx skills add shadcn/ui` |
| Context7 | `npx ctx7 setup`; choose CLI/skills or MCP |
| Playwright | After authorized CLI install: `playwright-cli install --skills` for Claude; `playwright-cli install --skills=agents` for Codex/compatible clients |
| Superpowers | Claude: `/plugin install superpowers@claude-plugins-official`; Codex CLI: `/plugins`; Codex app: sidebar Plugins |

Sources: [R08](SOURCES.md#r08) [R09](SOURCES.md#r09) [R10](SOURCES.md#r10) [R11](SOURCES.md#r11) [R12](SOURCES.md#r12) [R13](SOURCES.md#r13) [R15](SOURCES.md#r15).

Playwright CLI needs Node.js 20+; verify skill-directory support/discovery. `gh-fix-ci` references the deprecated OpenAI Skills repository; inspect currently available CI tools before installation. [R20](SOURCES.md#r20)

## Vercel connection, only when needed

Codex CLI:

```sh
codex mcp add vercel --url https://mcp.vercel.com
```

Claude Code:

```sh
claude mcp add --transport http vercel https://mcp.vercel.com
```

Confirm account/project before writes. Connection grants no production approval or preview-only restriction. [R22](SOURCES.md#r22)

## Repository instructions

Merge [starter](templates/AGENTS.starter.md); add verified commands only. Use [Claude import](templates/CLAUDE.import.md) beside intended root `AGENTS.md` when needed. Preserve existing policy. [R05](SOURCES.md#r05)

Check harmless activation plus one representative nonproduction task. Record versions/config diff. Installation proves no performance improvement.

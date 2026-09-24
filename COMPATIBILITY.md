# Client compatibility

[Home](README.md) · [Setup](SETUP.md) · [Sources](SOURCES.md)

**24 September 2026 snapshot.** Shared format guarantees no equivalent discovery, permissions, credentials or cloud availability.

| Client | Instructions | Skills / invocation |
|---|---|---|
| Codex CLI/IDE | `AGENTS.md` | `.agents/skills/` along repo path; `/skills` or `$skill-name`. [R02](SOURCES.md#r02) |
| Claude Code | `CLAUDE.md`; conditional `AGENTS.md` | `.claude/skills/`, plugins; `/skill-name`, possibly namespaced. [R04](SOURCES.md#r04) |
| Copilot | Surface-specific | `.github/skills/`, `.claude/skills/`, `.agents/skills/`; invoke through that surface. [R17](SOURCES.md#r17) |
| Cursor | `.cursor/rules/`, `AGENTS.md` | `.agents/skills/`, `.cursor/skills/`; compatibility `.claude/skills/`, `.codex/skills/`; `/` menu. [R30](SOURCES.md#r30) [R31](SOURCES.md#r31) |

## Claude instruction correction

Direct `AGENTS.md` support: v2.1.277+. Before v2.1.281, some provider/telemetry configurations prevented loading. Built-in plugin/Project instructions settings still matter. Project/ancestor `CLAUDE.md` or `CLAUDE.local.md` can suppress fallback.

Where needed, merge `@AGENTS.md` into root `CLAUDE.md`; preserve policy, avoid duplication, confirm actual loading. [R05](SOURCES.md#r05)

## Copilot cloud is not VS Code Copilot

Cloud agent/code review: no OAuth remote MCP support; configured tools may run without per-call approval. Vercel OAuth working in VS Code proves no cloud support. Use supported client, existing deployment integration or authorized credential path; avoid broad-token workarounds. [R19](SOURCES.md#r19) [R22](SOURCES.md#r22)

## Invocation and mentions

- **Kit prompt:** paste block or explicitly request attached file. No registered command.
- **File:** picker, supported `@` completion, accessible path or text; confirm read.
- **Skill:** discovered client identifier, including required namespace.
- **Connector:** select integration; specify action, repository, target.

Mentions install nothing and authorize no publication/deployment. Retrieved instructions remain source material unless adopted.

## Activation check

Record client/version, skill ID/source, harmless activation result. Inspect overrides and global/project scope. Local installation guarantees no cloud availability. Installing skills requires applicable authority.

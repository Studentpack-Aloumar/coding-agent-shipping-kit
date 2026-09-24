# Client compatibility
**Snapshot: 24 September 2026.** A compatible skill format does not guarantee identical discovery, hooks, credentials, permissions or cloud availability.

| Agent / surface | Durable instructions | Repository skill discovery | Explicit use |
|---|---|---|---|
| Codex CLI / IDE | `AGENTS.md` | `.agents/skills/` along the repository path | `/skills` selector or `$skill-name`. [R02](SOURCES.md#r02) |
| Claude Code | `CLAUDE.md`; conditional `AGENTS.md` support | `.claude/skills/`; installed plugin skills | `/skill-name`; check namespaced plugin commands. [R04](SOURCES.md#r04) [R05](SOURCES.md#r05) |
| GitHub Copilot | Use the instruction mechanism documented for the specific surface | `.github/skills/`, `.claude/skills/`, `.agents/skills/` are documented | Select/invoke using that surface; do not assume a CLI command is a cloud feature. [R17](SOURCES.md#r17) |
| Cursor | `.cursor/rules/` or `AGENTS.md` | `.agents/skills/`, `.cursor/skills/`; compatibility paths include `.claude/skills/`, `.codex/skills/` | Select the skill in the `/` menu. [R30](SOURCES.md#r30) [R31](SOURCES.md#r31) |

## Claude instruction correction
Current Claude Code documentation describes direct `AGENTS.md` support from v2.1.277, with session/provider restrictions. By default, a project/ancestor `CLAUDE.md` or `CLAUDE.local.md` can take precedence and suppress the AGENTS fallback. Do not assume either that Claude never reads AGENTS or that it always does.

An explicit `@AGENTS.md` import in a root `CLAUDE.md` remains documented for shared instructions and older/restricted sessions. Merge it into existing configuration only when necessary; do not overwrite existing policy or duplicate long instructions. Confirm what actually loaded. [R05](SOURCES.md#r05)

## Copilot cloud is not VS Code Copilot
GitHub currently documents that Copilot cloud agent and code review do not support OAuth-based remote MCP servers. It also warns that configured MCP tools may run without per-call approval. Consequently, Vercel's OAuth MCP connection should not be assumed to work in that cloud surface merely because it works in VS Code.

Use a supported interactive client, the existing deployment integration, or an explicitly approved alternative credential path. Do not work around the mismatch by casually granting broad tokens. [R19](SOURCES.md#r19) [R22](SOURCES.md#r22)

## Activation check
Before relying on a capability, record the client/version, the discovered skill identifier, the resolved source, and a harmless task showing it actually activates. Inspect same-name overrides and global versus project scope. A skill installed on a laptop is not thereby present in a fresh cloud checkout.

The prompt files in this kit are deliberately ordinary Markdown, not native slash commands. Paste or reference them in the agent; installing a skill is a separate, permissioned operation.

# Resource shortlist

[Home](README.md) · [Setup](SETUP.md) · [Compatibility](COMPATIBILITY.md)

[Expanded catalogue](REUSE.md): skills, plugins, roles, checks and application layers; pinned sources where available.

Selected for primary ownership, task fit and documented integration. No performance ranking; installation examples remain opt-in.

| Resource | Use / boundary |
|---|---|
| Codex native | `/plan`, `/review` where available; reuse before adding wrappers. [R01](SOURCES.md#r01) |
| Claude native | Check `/run`, `/verify`, `/code-review`, `/run-skill-generator`; verify supplements tests, generator can write/commit setup. [R04](SOURCES.md#r04) |
| Exa | Discover primary docs; inspect integration schema. No private queries. [R07](SOURCES.md#r07) |
| Context7 | Version-specific docs via CLI/skills or MCP; verify coverage, fall back to primary docs. [R08](SOURCES.md#r08) |
| Superpowers | Opinionated lifecycle: debugging, planning, verification, review. Inspect active startup rules; selective invocation doesn't disable them. [R09](SOURCES.md#r09) |
| `vercel-react-best-practices` | React/Next.js changed paths; directory named `react-best-practices`. [R10](SOURCES.md#r10) |
| `web-design-guidelines` | Relevant UI/accessibility review; inspect app. No certification/redesign implied. [R11](SOURCES.md#r11) |
| `shadcn` | Existing shadcn projects, `components.json`, CLI; operations can change dependencies/files. [R12](SOURCES.md#r12) |
| `supabase-postgres-best-practices` | SQL/schema/index/policy; broader integration uses `supabase`. Guidance grants no access; live MCP development-scoped. [R13](SOURCES.md#r13) [R14](SOURCES.md#r14) |
| Playwright | CLI for shell agents; MCP when environment/exploration warrants. Durable assertions belong in project tests. [R15](SOURCES.md#r15) [R16](SOURCES.md#r16) |
| `gh-fix-ci` | Historical skill source; OpenAI Skills repository deprecated. Prefer existing CI tools; retain fix authority. [R20](SOURCES.md#r20) |
| GitHub CLI/MCP | Existing authenticated route, scoped repositories, authorized PR actions; cloud restrictions apply. [R21](SOURCES.md#r21) [R19](SOURCES.md#r19) |
| Vercel CLI/MCP | Deployments/logs; OAuth/client compatibility. Confirm target and release authority. [R22](SOURCES.md#r22) [R23](SOURCES.md#r23) |

## Default selection

Existing executor, native tools, tested startup, current checks, one browser route. Add retrieval/specialists only for concrete gaps. Avoid redundant searches, memory systems, integrations or orchestrators. Full lifecycle plugins require deliberate adoption. No default autonomous production authority.

# Actual resource shortlist

[Home](README.md) · [Prompts](PROMPTS.md) · [Setup](SETUP.md) · [Evidence](GATES.md) · [Sources](SOURCES.md)

**Selection basis:** primary ownership, a concrete development task and documented integration. This is not a measured best-to-worst ranking. Commands in [SETUP.md](SETUP.md) are opt-in examples, not actions performed for you.

| Resource | What to use it for | Activation / important boundary |
|---|---|---|
| Native Codex planning and review | Scope a complex change; review a candidate | Use native `/plan` and `/review` where available. Prefer existing capabilities before installing duplicate wrappers. [R01](SOURCES.md#r01) |
| Native Claude running-app and review skills | Launch the app, inspect a real change and conduct review | Current docs list `/run`, `/verify`, `/code-review` and `/run-skill-generator`. Check the installed command menu. `/verify` is not a substitute for the test suite; the recipe generator can write/commit project setup. [R04](SOURCES.md#r04) |
| Exa | Discover the right current primary documentation | Ask for exact publisher docs and the uncertainty they resolve. Inspect the available search/fetch schema; tool names differ by integration. Keep private code, secrets and patient/customer data out of public queries. [R07](SOURCES.md#r07) |
| Upstash Context7 | Retrieve library-specific, version-aware API examples | CLI plus skills or MCP are alternatives. Resolve the official library/version and confirm coverage; fall back to primary docs when missing. Do not invoke both Context7 and Exa mechanically for every question. [R08](SOURCES.md#r08) |
| Superpowers | A deliberately chosen structured development method | Actual skills include `systematic-debugging`, `writing-plans`, `verification-before-completion` and reviewed execution. The full plugin installs an opinionated lifecycle, not just optional tips. Check active rules before adding another orchestrator. No speed superiority established here. [R09](SOURCES.md#r09) |
| Vercel `vercel-react-best-practices` | React/Next.js performance-sensitive implementation | Declared skill name differs from its `react-best-practices` directory. Use applicable guidance on changed code; do not turn a small feature into a global optimization pass. [R10](SOURCES.md#r10) |
| Vercel `web-design-guidelines` | UI/accessibility/interaction review | Review relevant UI against the guide and inspect the running result. It is not a complete accessibility certification or a redesign mandate. [R11](SOURCES.md#r11) |
| Official `shadcn` skill | Work in an existing shadcn component system | Uses project context such as `components.json` and the shadcn CLI. Skip for unrelated UI stacks. Component operations can modify files/dependencies. [R12](SOURCES.md#r12) |
| Supabase `supabase-postgres-best-practices` | SQL, schema, indexing and database-policy work | Guidance does not grant database access. Use `supabase` instead when the task concerns broader product/client integration. Keep any live MCP access development-scoped with nonproduction data. [R13](SOURCES.md#r13) [R14](SOURCES.md#r14) |
| Playwright CLI plus project tests | Browser verification from a shell-capable coding agent | Install the CLI skill only when needed. Use MCP instead when the environment or persistent exploratory workflow favors it. Keep reproducible assertions in the project's test suite. [R15](SOURCES.md#r15) [R16](SOURCES.md#r16) |
| OpenAI `gh-fix-ci` | Diagnose GitHub Actions failures on a PR | Uses `gh`; external CI providers are outside its stated scope. Its implementation phase requires explicit approval of the fix plan; reuse that approval if already supplied for the same plan. [R20](SOURCES.md#r20) |
| GitHub CLI or official GitHub MCP | Read issues/diffs/checks and perform authorized PR work | Reuse the authenticated route already present. Scope repository access and distinguish reading from publishing/merging. Copilot cloud has additional restrictions. [R21](SOURCES.md#r21) [R19](SOURCES.md#r19) |
| Vercel CLI or official Vercel MCP | Inspect deployments/logs; carry out authorized releases | MCP uses OAuth and supports particular clients. Preview and production still need explicit target checks; an authenticated tool is not release approval. [R22](SOURCES.md#r22) [R23](SOURCES.md#r23) |

## My recommended default selection
Keep one existing executor, native local tools, a tested launch recipe, current checks and one working browser path. Use available search or retrieval to resolve an external uncertainty. For a React/Next.js change, use applicable React guidance; for SQL work, use relevant database guidance. Select an installed specialist when helpful, and add one only if a demonstrated gap justifies setup. Do not preload every specialist into every task.

Use a full method such as Superpowers when you deliberately want its lifecycle. Do not assume that selecting two skill names from its README neutralizes the installed plugin's startup rules. If it is already active, respect its workflow or change the configuration explicitly.

## What I would not add by default
No giant generic senior-engineer prompt, no second memory system, no collection of overlapping MCP servers, no new orchestration runtime, and no autonomous production authority. These are scope decisions to justify with a demonstrated gap, not prerequisites for shipping a feature.

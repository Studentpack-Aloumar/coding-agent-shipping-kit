# Coding-agent shipping kit
**24 September 2026 · v1.0.1 · Documentation-checked; not installed or benchmarked**

> **Proprietary — Basem Aloumar only.** This kit is reserved for Basem Aloumar's own use and projects. It is not open source and does not grant other people a personal-use or commercial-use license. See [LICENSE](LICENSE).
> Public GitHub hosting still permits viewing and forking under GitHub's terms; this notice does not make a public repository private.


## Start here
Open [the onboarding prompt](prompts/00-onboard-repo.md) in the coding agent attached to the repository you actually want to improve. It discovers the existing setup before proposing additions. It does not authorize installation, deployment or access to production data.

After onboarding, give the agent one concrete change and use [the implementation prompt](prompts/04-implement.md). Other prompts are a menu: activate them only when their trigger applies. Do not paste this entire kit into every task.

## Recommended starting configuration
Keep your current coding agent and its native tools. Establish a tested startup recipe, scoped repository guidance and an evidence-based completion contract. For browser applications, use the existing automated tests plus running-app verification. Add a domain skill or external integration only when it addresses a specific gap.

This is a proposed operating setup, not a measured ranking. The research basis and exceptions are in [the playbook](PLAYBOOK.md).

## Contents
| File | Purpose |
|---|---|
| [LICENSE](LICENSE) | Owner-only rights notice; no general reuse license |
| [PUBLISH.md](PUBLISH.md) | Scoped publishing handoff; not run automatically |
| [PLAYBOOK.md](PLAYBOOK.md) | Conditional lifecycle and resource selection |
| [RESOURCES.md](RESOURCES.md) | Actual tools/skills, activation and caveats |
| [COMPATIBILITY.md](COMPATIBILITY.md) | Codex, Claude Code, Copilot and Cursor differences |
| [SETUP.md](SETUP.md) | Installation examples and safe onboarding order |
| [GATES.md](GATES.md) | Permissions, verification, CI and release evidence |
| [PROMPTS.md](PROMPTS.md) | Index of 18 original copy-and-paste prompts |
| [EVALUATION.md](EVALUATION.md) | Test whether an added tool/skill actually helps |
| [SOURCES.md](SOURCES.md) | 32 primary-source references |
| `templates/` | Inert instruction examples and an evidence JSON schema |

## What this kit does not do
It does not install skills, modify agent settings, grant permissions, push branches, open PRs or deploy software. The Markdown prompts are not auto-discovered skills. Instruction examples deliberately do not use active root filenames, so opening this kit does not silently replace repository policy.

The engineering practices and prompts are original synthesis. Third-party skills are linked, not copied. No speed, cost or quality improvement has been measured on your projects.

## License and access
The [owner-only notice](LICENSE) reserves applicable rights in the original kit to Basem Aloumar, while preserving third-party rights, legal exceptions and rights granted under hosting-platform terms. It does not guarantee legal exclusivity in AI-generated or otherwise unprotected material. Use a private repository when access itself must be restricted.

Relevant documentation: [GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository), [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), and [GitHub's no-license guidance](https://choosealicense.com/no-permission/). These explain the distinction between reserving reuse rights and restricting visibility; they are not an endorsement or legal review of this custom notice.

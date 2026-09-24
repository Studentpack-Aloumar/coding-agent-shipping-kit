# Coding-agent shipping kit

**24 September 2026 · v1.1.1 · Reference kit; uninstalled, unbenchmarked.**

**Proprietary: mr. Aloumar only.** No general reuse license. Public GitHub viewing/forking rights remain; see [LICENSE](LICENSE). Custom notice: no legal review.

## Start here

Use your existing agent in the **target application repository**. Choose one of 19 prompts. No installation required.

| Task | Prompt |
|---|---|
| Build from an idea | [18 · Build](prompts/18-build-from-idea.md) |
| Understand a repository | [00 · Onboard](prompts/00-onboard-repo.md) |
| Implement | [04 · Implement](prompts/04-implement.md) |
| Fix a failure | [08 · Debug](prompts/08-debug-failure.md) |
| Other work | [All prompts](PROMPTS.md) |

## Using a prompt

Copy its code block, or attach the file and explicitly request its use:

```text
Use prompts/04-implement.md in <repository> for <behavior and acceptance criteria>.
Reuse established context and authorization.
```

Files supply context; mentions alone grant no authority. Prompts register no slash commands or skills. [Client syntax](COMPATIBILITY.md#invocation-and-mentions). Explicitly adopt the owner agreement before relying on its defaults. Use available alternatives when optional tools are missing.

## Guides

| Guide | Purpose |
|---|---|
| [Owner agreement](templates/INSTRUCTIONS.owner.md) | Opt-in ownership, communication, integration authority |
| [Product excellence](PRODUCT-EXCELLENCE.md) | Discovery, design, complete journeys, critique |
| [Playbook](PLAYBOOK.md) | Workflow and resource selection |
| [Resources](RESOURCES.md) · [Setup](SETUP.md) · [Compatibility](COMPATIBILITY.md) | Tools, activation, client differences |
| [Evidence gates](GATES.md) | Permissions and completion requirements |
| [Templates](templates/README.md) | Instructions and evidence records |
| [Evaluation](EVALUATION.md) · [Sources](SOURCES.md) | Experiments and 40 primary references |
| [Maintenance](PUBLISH.md) · [Changelog](CHANGELOG.md) · [Contributing](AGENTS.md) | Repository upkeep |

## Check this checkout

Python 3.9+, offline, no dependencies:

```sh
python3 tools/check-kit.py
```

Checks links, anchors, inventories, JSON, versions and [saved digest](PACKAGE-CHECKS.json). [Refresh after edits](PUBLISH.md#maintaining-the-kit).

Recommendations remain unbenchmarked; [results](evaluation/results.json): `not_run`. No target-app installation or deployment implied. Third-party skills are linked, not copied; templates stay inactive.

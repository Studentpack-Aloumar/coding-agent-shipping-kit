# Coding-agent shipping kit

**24 September 2026 · v1.1.0 · Reference kit; not installed or benchmarked**

[Owner agreement](templates/INSTRUCTIONS.owner.md) · [Product excellence](PRODUCT-EXCELLENCE.md) · [Choose a prompt](PROMPTS.md) · [Setup](SETUP.md) · [Client compatibility](COMPATIBILITY.md) · [Evidence gates](GATES.md) · [Sources](SOURCES.md)

> **Proprietary — Basem Aloumar only.** This kit is reserved for Basem Aloumar's own use and projects. It is not open source and does not grant other people a personal-use or commercial-use license. See [LICENSE](LICENSE).
> Public GitHub hosting still permits viewing and forking under GitHub's terms; this notice does not make a public repository private.

## Start here

Keep your current coding agent and use this kit from the **application repository you want to improve**. The kit provides a playbook, 19 prompts and inert templates. Choose one prompt for the current task; no installation is required to copy its text. The idea-to-product prompt covers discovery, distinctive design, complete tested journeys and critical review; it does not itself launch a builder service. Explicitly adopt the [owner agreement](templates/INSTRUCTIONS.owner.md) to use the personal communication, autonomy and bounded integration defaults. Reading or attaching it alone does not activate it.

| What you need now | Start with |
|---|---|
| Turn an idea into a complete, distinctive product | [18 · Build from an idea](prompts/18-build-from-idea.md) |
| Understand an unfamiliar repository | [00 · Onboard](prompts/00-onboard-repo.md) |
| Implement a clear request | [04 · Implement](prompts/04-implement.md), then [07 · Verify](prompts/07-verify-local.md) if verification remains incomplete |
| Fix a failing behavior | [08 · Debug](prompts/08-debug-failure.md) |
| Review a candidate without editing | [09 · Review](prompts/09-review-read-only.md) |
| Prepare an authorized pull request | [11 · Prepare PR](prompts/11-prepare-pr.md) |
| Assess a release | [13 · Production readiness](prompts/13-production-readiness.md) |
| Find another task | [Browse all prompts by purpose](PROMPTS.md) |

## Using a prompt

1. Open your target application repository in the agent. Keep this kit in a separate reference checkout, or attach the selected Markdown file.
2. Supply the actual change, target repository and relevant acceptance criteria. Copy the text inside one prompt's code block, or explicitly ask the agent to use that attached prompt.
3. Reuse context and authorization already supplied in the task. Fill only genuine gaps. Review the resulting evidence before moving to another stage.

For example, attach `prompts/04-implement.md` and write:

```text
Use the attached implementation prompt for this task in <target repository>:
<requested behavior and observable acceptance criteria>.
Follow the instructions and authorization already established for this task.
```

A file attachment or `@` file mention supplies context where the client supports it. Naming an integration such as GitHub selects a capability; also state the action and target. Neither an attachment nor a mention, by itself, adopts every instruction in the referenced material or authorizes its side effects. The prompts are ordinary Markdown, so `/04-implement` and `$04-implement` are not installed commands. See [client invocation and availability](COMPATIBILITY.md#invocation-and-mentions).

When a named optional tool is unavailable, use an existing tool that satisfies the same requirement. Report a blocker only when the missing capability prevents the task; consult [setup](SETUP.md) before adding an integration.

## Recommended starting configuration

Use the existing agent, native tools, a tested startup recipe, scoped repository guidance and an evidence-based completion contract. For browser applications, combine relevant automated tests with running-app verification. Add a domain skill only when it addresses a specific gap.

This is a proposed operating setup, not a measured ranking. Read the [playbook](PLAYBOOK.md) for the reasoning and the [evaluation protocol](EVALUATION.md) to test an addition on your own tasks.

## Browse the kit

| Document | Purpose |
|---|---|
| [Owner agreement](templates/INSTRUCTIONS.owner.md) | Opt-in engineering ownership, communication and approval defaults |
| [Product excellence](PRODUCT-EXCELLENCE.md) | Discovery, design, build, critique and real-world validation |
| [Playbook](PLAYBOOK.md) | Conditional lifecycle and resource selection |
| [Prompt library](PROMPTS.md) | 19 prompts grouped by task |
| [Resource catalogue](RESOURCES.md) | Tools, skills, activation and limitations |
| [Setup](SETUP.md) | Optional installation examples and onboarding |
| [Compatibility](COMPATIBILITY.md) | Codex, Claude Code, Copilot and Cursor differences |
| [Evidence gates](GATES.md) | Authorization, verification, CI and release evidence |
| [Templates](templates/README.md) | Instruction examples and shipping-evidence format |
| [Evaluation](EVALUATION.md) | Test whether an addition helps |
| [Source register](SOURCES.md) | 40 primary references |
| [Publication and maintenance](PUBLISH.md) | Published repository, verification and update procedure |
| [Changelog](CHANGELOG.md) | Changes to the kit |
| [License](LICENSE) | Owner-only rights notice |

## Check this checkout

From the kit's root, with Python 3.9 or newer:

```sh
python3 tools/check-kit.py
```

This checks local links and anchors, prompt/source inventories, JSON parsing, version consistency and the saved package report. It runs offline and installs nothing. [PACKAGE-CHECKS.json](PACKAGE-CHECKS.json) records the checked file content. The [maintenance guide](PUBLISH.md#maintaining-the-kit) explains how to refresh it after edits.

These checks do not establish that every external claim is current or that a coding agent performs better. The [evaluation results](evaluation/results.json) remain `not_run`.

## License and access

The [owner-only notice](LICENSE) reserves applicable rights in the original kit to Basem Aloumar, while preserving third-party rights, legal exceptions and rights granted under hosting-platform terms. Use a private repository when access itself must be restricted. The kit does not install skills, modify settings or deploy an application; instruction templates use inactive filenames.

The practices and prompts are original synthesis. Third-party skills are linked, not copied. No improvement in speed, cost or quality has been measured on your projects. Relevant platform references are [GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service); the custom notice has not received legal review.

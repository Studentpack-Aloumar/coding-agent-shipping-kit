# Onboard the selected repository

**Trigger:** Use once per repository, or after a material environment change.

```text
Inspect this repository and make its coding-agent workflow explicit. Start read-only. Identify active instruction files, installed skills/tools, runtime and package manager, relevant architecture, startup scripts, tests, CI gates and deployment integration.

Propose the smallest onboarding change after inspection. Validate existing setup/check commands only in an authorized nonproduction environment; inspect unfamiliar scripts first. Record actual successes and baseline failures. Never print secret values or query production data.

Prefer existing capabilities. Do not install plugins, change global settings, rewrite CI, push or deploy. If startup cannot be verified with current permissions, report the exact blocker instead of inventing a recipe.

Return: environment readiness, verified commands, instruction conflicts, the single most useful improvement, and its proposed diff. Keep product code unchanged.
```

Related documentation: [R18](../SOURCES.md#r18)

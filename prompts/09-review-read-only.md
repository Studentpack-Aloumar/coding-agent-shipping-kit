# Review candidate

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Substantive/risky changes; fresh context preferred.

```text
Read-only: compare actual base/head diff and surrounding code against original criteria. Implementer narrative is unverified.

Check evidenced correctness, authorization/data boundaries, races/state, migrations, missing behavior and meaningful tests. No invented findings, abstraction demands or formatting noise.

For substantial UI, inspect/interact with the app; assess usefulness, clarity, coherence, originality, accessibility, maintainability. Separate observed defects, design opinions and business hypotheses; disclose access gaps. Agent review proves no customer validation.

Use safe authorized nonproduction checks. Return severity, file/line, trigger, consequence, smallest fix, reviewed revision and coverage limits. Separate hypotheses. No findings means no actionable findings, never bug-free. No edits, comments or merge.
```

Sources: [R03](../SOURCES.md#r03)

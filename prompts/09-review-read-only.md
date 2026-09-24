# Review independently without editing

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for substantive or risky changes, ideally in a fresh review context.

```text
Review the specified candidate against its base revision and the original acceptance criteria. Work read-only. Inspect the actual diff and relevant surrounding code; treat the implementer's narrative as a claim, not proof.

Look for evidenced correctness regressions, authorization/data-boundary mistakes, state/race problems, unsafe migrations and missing required behavior. Check whether tests meaningfully cover the risk. Do not invent findings, require unnecessary abstraction or nitpick formatting already enforced by tooling.

For each confirmed issue give severity, file/line, the triggering condition, consequence and smallest correction. Separate hypotheses from demonstrated defects. Use only safe, authorized nonproduction checks.

Return findings, coverage limitations and the reviewed revision. If no actionable issue is found, say so without claiming the code is bug-free. Do not edit, post comments or merge.
```

Related documentation: [R03](../SOURCES.md#r03)

# Diagnose and fix a failure

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use when a check or observed behavior fails.

```text
Investigate the reported failure before patching. Use systematic-debugging when that skill is active. Reproduce the symptom, inspect relevant logs and recent changes, compare a working path, and identify the smallest testable hypothesis.

Instrument only what is needed, with sanitized values. Never dump environment files, tokens or sensitive records. Test one hypothesis at a time and record what the evidence rules out.

Fix the root cause with the smallest scoped change, add a regression test, and rerun the original reproduction plus affected checks. If two approaches fail, reassess the diagnosis and summarize new evidence before continuing; do not repeat blind edits.

Return the confirmed cause or remaining uncertainty, the fix, before/after evidence and any blocker. Do not claim the failure is impossible in all conditions.
```

Related documentation: [R09](../SOURCES.md#r09)

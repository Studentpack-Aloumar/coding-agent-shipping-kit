# Debug failure

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Observed failure.

```text
Reproduce before patching. Inspect logs/recent changes; compare working path. Use systematic-debugging when active. Test one minimal hypothesis at a time; record exclusions. Sanitize instrumentation; expose no secrets/records.

Fix root cause with scoped changes; add useful regression coverage. Rerun reproduction and affected checks. After two failed approaches, reassess using new evidence; no blind edits.

Return cause/uncertainty, fix, before/after evidence and blocker. Claim only observed coverage.
```

Sources: [R09](../SOURCES.md#r09)

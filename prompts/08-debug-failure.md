# Debug failure

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Observed failure.

```text
Reproduce before patching. Inspect logs/recent changes; compare working path. Use systematic-debugging when active. Test one minimal hypothesis at a time; record exclusions. Sanitize instrumentation; expose no secrets/records.

Broken build/preview: stop feature expansion; capture the first diagnostic. Check actual import paths, filename case, exports, dependencies and configuration. Repair narrowly, rerun the verified build command, then exercise the affected route/control and expected effect.

Fix root cause with scoped changes; add useful regression coverage. Rerun reproduction and affected checks. After two failed approaches, reassess using new evidence; no blind edits.

Return cause/uncertainty, fix, before/after evidence and blocker. Claim only observed coverage.
```

Sources: [R09](../SOURCES.md#r09)

# Verify production

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Bounded check after release.

```text
Confirm actual production deployment/revision. Use existing observability; add no monitoring service. Exercise only authorized journeys, preferably read-only. Writes require bounded synthetic accounts and approved cleanup.

Inspect release errors, failed requests and relevant performance over the available interval. Compare criteria/baseline; separate regressions, existing issues and insufficient data.

Return checks, interval, findings, uncertainty and whether approved recovery conditions were met. No claims of ongoing monitoring/future health or unauthorized rollback.
```

Sources: [R24](../SOURCES.md#r24)

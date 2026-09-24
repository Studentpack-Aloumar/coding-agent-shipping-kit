# Verify the shipped behavior

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for a bounded check of an actual completed release.

```text
Verify the release that actually reached the specified production target. Confirm deployment identity and revision first. Use existing observability and safe checks; do not introduce a new monitoring service.

Exercise only the explicitly authorized production journey, preferably read-only. Test writes must use bounded synthetic accounts and an approved cleanup method. Inspect release-related errors, failed requests and the relevant performance signals for the observation window that is actually available.

Compare against the stated acceptance criteria and any meaningful baseline. Separate regressions, pre-existing issues and insufficient data. Do not claim ongoing monitoring or future health from a one-time inspection.

Return the exact checks and observation interval, production findings, uncertainty and whether the approved recovery condition was met. Do not roll back without applicable authorization.
```

Related documentation: [R24](../SOURCES.md#r24)

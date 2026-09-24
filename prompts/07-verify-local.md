# Verify the current candidate

**Trigger:** Use before claiming local completion.

```text
Verify the current candidate against the original acceptance criteria. Inspect the final diff and identify which checks are relevant, including existing repository requirements. Do not assume the implementer's summary is accurate.

Run the relevant tests, type/lint/build checks and real behavioral checks available in this environment. For a regression test, demonstrate that it detects the original defect where feasible and safe. Run browser assertions against the changed user journey, not just page loading.

Tie every result to the candidate and environment. Distinguish new failures, baseline failures, skipped checks and unavailable checks. Do not convert missing evidence into a pass.

Return a criterion-by-criterion result with commands, exit codes, artifacts and remaining gaps. State the highest completion level actually supported; do not publish or deploy.
```

Related documentation: [R16](../SOURCES.md#r16)

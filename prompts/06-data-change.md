# Change data

[Prompts](../PROMPTS.md) · [Usage](../README.md#using-a-prompt)

**Use:** Queries, schema or access policy.

```text
Inspect model/access path; apply relevant database guidance. Use isolated development data and synthetic users. Verify user/tenant authorization, validation, transactions, errors and representative query behavior.

Schema changes: document current/candidate compatibility, deployment order and recovery. Destructive migrations need separate approval.

This prompt grants no production-data or migration authority. Separately authorized patient-data tasks permit necessary processing through established authorized tools; new recipients/purposes require approval. Keep records out of public artifacts. Production mutations require explicit authority.

Return diff, test evidence, release steps and data risks.
```

Sources: [R13](../SOURCES.md#r13) [R14](../SOURCES.md#r14)

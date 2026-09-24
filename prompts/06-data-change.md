# Change data access or schema safely

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for database, query, access-policy or persistent-data work.

```text
Inspect the existing data model and access path before changing it. Use the relevant database guidance; for Postgres work, select supabase-postgres-best-practices only where applicable.

Implement and test against an isolated development database with synthetic data. Confirm user/tenant authorization, input validation, transaction behavior and error cases for the changed path. Assess query behavior using representative nonproduction data rather than declaring performance from syntax alone.

For a schema change, document compatibility with both the current and candidate application, deployment ordering and the recovery implications. Avoid destructive migrations unless separately approved.

Do not connect an agent tool to production data or apply production migrations. Return the migration/query diff, test evidence, required release steps and unresolved data risks.
```

Related documentation: [R13](../SOURCES.md#r13) [R14](../SOURCES.md#r14)

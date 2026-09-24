# Verify the deployed preview

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use after preview deployment is authorized and target identity is known.

```text
Verify the agreed change in its actual preview environment. Confirm the account, existing project, exact revision, deployment ID and preview-data isolation before any write. Reuse the matching deployment from the existing Git integration when present.

For Vercel, check project history: the first deployment of a new project is production. Do not assume a command without --prod is preview-safe. Do not provision a new project under preview-only authorization.

Exercise the changed journey with synthetic data using the existing browser tool. Inspect relevant console, network and runtime logs. Capture evidence and confirm server-side effects where required.

Return deployment identity, tested cases, failures and limitations. If fixes change the candidate, revalidate the new deployment. Do not promote, merge or alter production configuration.
```

Related documentation: [R23](../SOURCES.md#r23) [R15](../SOURCES.md#r15)

# Resolve one material uncertainty

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for an external fact that could change implementation.

```text
Resolve the specific external uncertainty blocking the current task. Check the dependency version and existing implementation first.

Use the existing browser or search capability to find relevant publisher documentation when its location is unknown. Exa and Context7 are optional choices when available; confirm the actual source and applicable version. Do not install a retriever or invoke several tools for the same question without a demonstrated need.

Return the decision, supporting primary links, version/date applicability, remaining uncertainty and the exact consequence for our code or tests. Distinguish documented facts from your inference. If sources disagree, explain the consequential difference.

Stop researching when the implementation decision is sufficiently supported. Do not send private code, secrets or customer/patient data to public search. No code changes in this step.
```

Related documentation: [R07](../SOURCES.md#r07) [R08](../SOURCES.md#r08)

# Implement and inspect UI behavior

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use for a UI change; not a mandate to redesign the application.

```text
Implement the requested UI change using the existing design system. Preserve information hierarchy and established interactions unless the request changes them. Reuse existing components; use the shadcn skill only when this project actually uses shadcn.

For React/Next.js, apply relevant React guidance to the changed path. Use installed Vercel React or web-design-guidelines skills when applicable; existing project guidance and browser checks remain usable when those optional skills are unavailable.

Inspect the running result at the affected desktop/mobile widths. Exercise the main journey plus relevant loading, empty, error and disabled states. Check keyboard operation, focus, accessible naming and console/network failures. Verify backend effects when the flow requires them.

For substantial product work, obtain separate critical review when available against usefulness, clarity, coherent design, originality, accessibility and maintainability. Fix consequential weaknesses, verify improvements and retain the strongest result; avoid unproductive polishing. Keep focused durable regression assertions where they protect repeatable behavior. If app access prevents inspection, state the exact gap. Return the exact tested environment, screenshots/artifacts, check results and any untested states. A screenshot alone is not completion evidence.
```

Related documentation: [R10](../SOURCES.md#r10) [R11](../SOURCES.md#r11) [R12](../SOURCES.md#r12)

# Implement and inspect UI behavior

**Trigger:** Use for a UI change; not a mandate to redesign the application.

```text
Implement the requested UI change using the existing design system. Preserve information hierarchy and established interactions unless the request changes them. Reuse existing components; use the shadcn skill only when this project actually uses shadcn.

For React/Next.js, apply relevant Vercel React guidance to the changed path. Use web-design-guidelines for a focused review rather than a site-wide rewrite.

Inspect the running result at the affected desktop/mobile widths. Exercise the main journey plus relevant loading, empty, error and disabled states. Check keyboard operation, focus, accessible naming and console/network failures. Verify backend effects when the flow requires them.

Keep durable regression assertions for repeatable behavior. Return the exact tested environment, screenshots/artifacts, check results and any untested states. A screenshot alone is not completion evidence.
```

Related documentation: [R10](../SOURCES.md#r10) [R11](../SOURCES.md#r11) [R12](../SOURCES.md#r12)

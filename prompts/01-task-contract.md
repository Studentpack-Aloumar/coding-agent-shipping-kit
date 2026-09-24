# Define the task contract

**Trigger:** Use when the desired outcome or scope is genuinely unclear.

```text
Turn my current request into a small, testable change contract. Inspect the relevant existing behavior before deciding what must change. Reuse context I have already supplied.

State the user-visible outcome, in-scope behavior, exclusions, acceptance criteria, important error states and any irreversible consequences. Separate product decisions from technical implementation choices. Make routine technical choices yourself within the existing architecture.

Ask all genuinely blocking scope questions together; do not ask me to choose libraries unnecessarily. Clearly label safe assumptions. Do not add features because they are conventional, and do not start implementation until the scope is sufficiently clear.

Return a compact contract that a separate reviewer could use without reading this conversation.
```

Related documentation: [R01](../SOURCES.md#r01)

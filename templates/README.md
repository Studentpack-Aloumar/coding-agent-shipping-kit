# Templates

[Home](../README.md) · [Evidence gates](../GATES.md) · [Setup](../SETUP.md)

These are examples to adapt in the target repository. Reading this directory does not activate repository instructions or grant authorization.

| File | How to use it |
|---|---|
| [AGENTS.starter.md](AGENTS.starter.md) | Merge useful sections into the target repository's existing instructions after inspection; fill in commands only after validating them. |
| [CLAUDE.import.md](CLAUDE.import.md) | Contains only `@AGENTS.md`. Use that line in a target `CLAUDE.md` beside the intended `AGENTS.md` when needed; retain existing policy. |
| [shipping-evidence.schema.json](shipping-evidence.schema.json) | JSON Schema Draft 2020-12 describing an evidence record's structure. |
| [shipping-evidence.example.json](shipping-evidence.example.json) | A deliberately blocked, unverified starting example. Replace placeholders with actual task evidence. |

## Evidence records

Copy the example to an appropriate location in the target project. Record the candidate and acceptance criteria, checks actually run, approvals already supplied, review coverage and remaining gaps. Use `notes` to connect each check to its acceptance criterion and to record timing or scope details. Remove example placeholders before presenting it as a real result.

The schema validates structure only. It does not compare revision identities, authenticate approvals or enforce the completion levels in [GATES.md](../GATES.md#completion-states). A record can pass schema validation while its claimed completion state is unsupported; assess its contents against the gates. Use a Draft 2020-12 validator with format checking enabled when validating timestamps. The local package checker checks JSON parsing but is not a JSON Schema validator.

Keep real evidence and sensitive logs in the authorized target project. Do not put them in this public reference kit.

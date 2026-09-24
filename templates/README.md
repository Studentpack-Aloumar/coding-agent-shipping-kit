# Templates

[Home](../README.md) · [Gates](../GATES.md)

Inactive examples. Explicitly adopt/adapt in the target repository; preserve policy and repair kit-relative links.

| File | Use |
|---|---|
| [Owner agreement](INSTRUCTIONS.owner.md) | Opt-in ownership/integration authority |
| [AGENTS starter](AGENTS.starter.md) | Merge guidance; add verified commands |
| [Claude import](CLAUDE.import.md) | `@AGENTS.md` in target `CLAUDE.md`, beside intended instructions |
| [Evidence schema](shipping-evidence.schema.json) | Draft 2020-12 structure |
| [Evidence example](shipping-evidence.example.json) | Blocked/unverified placeholders; replace with facts |

## Evidence records

Record candidate, criteria, checks, approvals, review and gaps. Use `notes` for criterion links, timing/scope. Remove placeholders before claiming real evidence.

Schema checks structure only; proves no identities, approvals or [completion states](../GATES.md#completion-states). Use Draft 2020-12 with timestamp format checking. Package checker parses JSON only.

From kit root: `uv run tools/check-evidence.py path/to/evidence.json`. Exit 0: schema/timestamps valid; 1: invalid. Python 3.10+, pinned `jsonschema` dependency; [validator docs](../SOURCES.md#r41). No readiness score.

Keep real evidence/sensitive logs in the authorized target project, outside this public kit.

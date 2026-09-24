# Repository working agreement — starter to merge, not overwrite

## Scope
Implement the requested behavior using the repository's existing architecture and conventions. Inspect current instructions and the relevant execution path first. Resolve product-scope questions together; make routine technical decisions within that scope. Do not perform unrelated rewrites.

## Environment
Use the repository's documented runtime, package manager, lockfile and scripts. Validate the real startup and check commands during onboarding, then record the commands and prerequisites here. Do not invent commands or print secret values. Use synthetic test data.

## Boundaries
Local changes do not authorize publication, production deployment, destructive operations, new paid resources or production-data access. Respect configured tool permissions and explicit task authorization. Never weaken tests, authentication or required checks to obtain a passing result.

## Method
Use a short plan when uncertainty or risk warrants it. Load only relevant skills. Reproduce failures and test an evidence-based hypothesis before patching. Preserve other people's changes and isolate concurrent writers.

## Completion
Report the exact candidate, changed behavior, actual commands and results, behavioral evidence and remaining risks. Separate implemented, locally verified, CI verified, preview verified and production verified. A missing check is not a pass. Rerun checks invalidated by later edits.

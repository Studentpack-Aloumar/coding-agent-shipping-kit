# Repository Guidelines

## Style

Extreme concision, everywhere: replies, docs, prompts, comments. Sacrifice grammar for brevity; preserve meaning, commands, evidence, permissions. No filler or repeated guidance.

## Structure

- Root Markdown: guides. `prompts/`: 19 copyable task prompts.
- `templates/`: inactive examples. `evaluation/`: benchmark records.
- `.agents/skills/`: project-local workflow and roles. `reuse.json`: external sources.
- `tools/`: integrity/evidence checks. No app/build; evidence validator uses pinned `jsonschema` through `uv`.
- `.github/workflows/`: automatic kit checks; no deployment.

Reuse workflow: `REUSE.md` selects; `BUILD-RECIPES.md` qualifies/assembles; `templates/reuse-adoption.md` records evidence. Source pins prove no working deployment.

## Editing

Preserve numbered prompt filenames, relative links, source anchors, owner-only `LICENSE`, and schema semantics. Update indexes/manifest with inventory changes; keep README/manifest versions aligned. Record meaningful changes in `CHANGELOG.md`.

Python: four spaces, snake_case. JSON: two spaces; compact small structures. No formatter or separate test suite.

## Checks

Python 3.9+. Review changes, then:

```sh
python3 tools/check-kit.py --write-report
python3 tools/check-kit.py
git diff --check
```

Checks: links, anchors, inventories, JSON, versions, digest. Evidence changes: `uv run tools/check-evidence.py templates/shipping-evidence.example.json`. No external-fact, security or runtime validation. No coverage target.

## Delivery

Imperative commits: `Add …`, `Update …`. PRs: change, evidence, gaps; linked issue when applicable. Publishing requires authorization; inspect automatic release effects. Preserve required gates. Never commit secrets or private records. Templates grant no authority unless adopted.

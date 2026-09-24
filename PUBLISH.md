# Publication and maintenance

[Home](README.md) · [Gates](GATES.md)

## Published repository

[Studentpack-Aloumar/coding-agent-shipping-kit](https://github.com/Studentpack-Aloumar/coding-agent-shipping-kit): public, `main`.

Verified 24 September 2026: [initial revision](https://github.com/Studentpack-Aloumar/coding-agent-shipping-kit/commit/285409a6b30bb6e565b8cfb52beb5a021c6a2a29) matched all 35 ZIP files; README/owner-only license present; secret scanning/push protection enabled. Historical observations; [later commits](https://github.com/Studentpack-Aloumar/coding-agent-shipping-kit/commits/main/). No app deployment or benchmark implied.

## Maintaining the kit

1. Confirm task/publication authority; reuse applicable approval.
2. Inspect branch/remote. Preserve existing work, [LICENSE](LICENSE), inactive templates.
3. Update affected docs, links, [changelog](CHANGELOG.md), [manifest](manifest.json). Match README/manifest versions. Link availability alone proves no factual claim.
4. Review final edits; refresh and verify:

   ```sh
   python3 tools/check-kit.py --write-report
   python3 tools/check-kit.py
   git diff --check
   ```

5. Before authorized push: inspect staged content for sensitive/unintended files; use available secret scanner without printing secrets. Confirm repository, branch, automatic release effects and appropriate local Git identity/private reply address.
6. Follow branch rules; preserve concurrent changes. Resolve failed pushes without bypassing protections. Verify remote revision/content; report commit URL and gaps.

The digest covers tracked/unignored files except its own report. Checks establish local package integrity only; no external, legal or runtime validation.

## Access and rights

[Owner-only rights](LICENSE) remain subject to [GitHub terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), including public viewing/forking. Privacy requires restricted hosting. Documentation grants no fresh publication/settings authority. [Licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [Push protection](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enable-push-protection).

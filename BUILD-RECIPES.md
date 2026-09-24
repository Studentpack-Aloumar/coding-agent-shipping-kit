# Adopt, assemble, verify

[Home](README.md) · [Selection](REUSE.md#select-before-building) · [Adoption record](templates/reuse-adoption.md)

Use for new products or substantial capabilities. Routine fixes stay local. Proposed method; speed gain unmeasured.

## 1. Select

Inspect existing work; define user, essential journeys, constraints and exclusions. Search relevant catalogue entries, whole products, official examples, packages, services and websites. Compare up to three credible options using [selection rules](REUSE.md#select-before-building). Keep one primary foundation per app; add compatible capabilities.

## 2. Qualify

Record exact source/version, license, runtime, host, services, environment-variable names and expected costs. Inspect setup scripts and deployment triggers before running them. Use an isolated development workspace and synthetic data; preserve existing authorization boundaries.

Derive install/start/check commands from that version's files/docs. Record working directory, prerequisites, outputs and baseline failures. Run the first required journey before broad customization. Missing credentials/access means blocked or simulated, never verified. Sites or another host needs its own compatibility evidence.

## 3. Design

One short handoff: required screens, hierarchy, typography/spacing tokens, reusable components, responsive rules, keyboard behavior and loading/empty/error/recovery states. Each reference names the pattern to borrow; each reused asset records rights. Search imagery only for a concrete need.

## 4. Assemble

Start the adopted app unchanged. Then build one complete slice: data/permissions → service/API → UI → real action → observed effect. For frontend-only products, verify state transitions and persistence. Keep routes/imports buildable; expand after the first journey works.

Integration note: capability, provider, test mode, secret names, cost/side effect, failure path. Defer optional sync/payments/notifications until needed; never imply deferred behavior works.

At the first broken build, stop feature expansion. Save the diagnostic; compare actual files, paths, case, exports and configuration. Repair one hypothesis, rerun the affected check, reopen the route. Two failed hypotheses require new evidence.

## 5. Retain evidence

Each required journey: revision, environment, steps, expected/observed result, timestamp, artifact and `pass`, `fail`, `blocked` or `not_run`. Exercise controls, relevant viewports and server effects. Screen counts, screenshots and aggregate percentages alone establish no completion.

Save the successful adoption recipe in the target project. Upstream/version/configuration changes invalidate affected evidence. Promote only sanitized, generally useful recipes into this kit; retain license notices. Compare accepted journeys per total elapsed time, including research/setup/rework; keep quality fixed. [Evaluation](EVALUATION.md).

## Recording lessons

Reviewed footage showed short integration briefs and structured design handoffs, then missing imports and incomplete journey evidence. Dependency ordering, immediate repair and journey records above are proposed responses. Sampled footage proves neither runtime correctness nor speed gains. Private recordings and credentials stay outside this kit.

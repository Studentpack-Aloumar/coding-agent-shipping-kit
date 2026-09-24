# From idea to product

[Home](README.md) · [Build prompt](prompts/18-build-from-idea.md) · [Owner agreement](templates/INSTRUCTIONS.owner.md) · [Gates](GATES.md)

Recommended loop for substantial product work; routine edits stay lightweight. Owner decides product scope; engineer owns technical delivery. No benchmark or award promise.

## Define three kinds of success

| Dimension | Define | Evidence |
|---|---|---|
| User value | User, problem, alternatives, advantage, journey | Real-user task completion/feedback |
| Craft | Coherent design, clarity, accessibility, reliability | Running-app interaction, focused checks, separate critique |
| Business | Relevant adoption, retention, distribution, economics | Authorized research, usage and business measurements |

Agent judgments remain hypotheses. Choose relevant metrics; invent no targets, customer validation or unrequested monetization. Awards illustrate craft, not demand; focused prototypes can test assumptions with users. [R38](SOURCES.md#r38) [R39](SOURCES.md#r39)

## Run the product loop

1. **Frame:** inspect work/alternatives; define user, problem, advantage, journey, constraints, criteria. Group consequential questions. [Compare reusable products/components](REUSE.md#select-before-building); recommend adoption or not building when justified.
2. **Test risk:** examine assumptions most likely to invalidate the idea. Use labeled prototypes/small experiments; identify simulations. Real-user contact requires authorization.
3. **Design:** relevant references, existing system, deliberate hierarchy, typography, spacing, language, imagery, motion and accessibility. Reuse components; avoid novelty without benefit.
4. **Build:** [qualify the base and assemble complete journeys](BUILD-RECIPES.md) with loading/empty/failure/recovery states. Preserve brief, adoption recipe and evidence across sessions. Prototypes remain labeled.
5. **Critique:** real controls, relevant viewports, server effects. Separate reviewer for substantial work when available; original criteria plus running result. Assess usefulness, clarity, coherence, originality, accessibility, reliability, maintainability. Evidence, no finding quotas.
6. **Improve:** fix consequential weaknesses, recheck, retain recoverable best candidate. Later iterations can regress. Stop unproductive polishing; unmet criteria remain unmet. Scope changes require owner decision.
7. **Integrate:** authorized workflow, required gates, accessible private preview where available. Preserve production approval. Identify missing user/business validation; no unrequested monitoring, outreach or paid experiments.

## What the research contributes

| Source | Lesson / limit |
|---|---|
| [E3](SOURCES.md#r33) | Upfront decisions, phased build/test/fix/preview; vendor description, no independent readiness proof |
| [Claude Fable 5.1](SOURCES.md#r34) | Follow-through, context, scope, meaningful updates; model-specific |
| [Astra guidance](SOURCES.md#r35), [game example](SOURCES.md#r36) | Experience constraints, references, observable state, real interaction; no universal ranking |
| [Generator/evaluator experiment](SOURCES.md#r37) | Explicit criteria, separate critique; added cost/complexity, possible regressions |

Effort cannot replace missing users, criteria, tools or feedback. Verify client settings: retrieved Astra API lists through `max`; client `ultra` equivalence unestablished. [R40](SOURCES.md#r40)

## Keep the contract small

Outcome, constraints, criteria, evidence in the existing project format. Add process only for material benefit. UI completion needs focused checks and real interaction; disclose gaps. Follow [authorization gates](GATES.md#authorization-boundaries). Compare workflows using [evaluation](EVALUATION.md); current benchmark status: `not_run`.

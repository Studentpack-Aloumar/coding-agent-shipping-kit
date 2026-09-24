# From an idea to an exceptional product

[Home](README.md) · [Owner agreement](templates/INSTRUCTIONS.owner.md) · [Build from an idea](prompts/18-build-from-idea.md) · [Evidence gates](GATES.md)

This is an operating recommendation, not a measured result or promise of an award. Use the full loop for substantial product work; keep routine edits on the playbook's small default loop. The owner controls product scope; the engineer owns technical execution within it.

## Define three kinds of success

| Dimension | Define before building | Evidence that can support it |
|---|---|---|
| User value | Intended user, important problem, existing alternatives, distinctive advantage and essential journey | Observed task completion and feedback from relevant users; agent judgments remain hypotheses |
| Experience and craft | A coherent visual direction, understandable interactions, accessibility and reliability | Running-app inspection, actual interactions, focused checks and separate critical review |
| Commercial viability | Relevant adoption, retention, distribution and revenue/cost assumptions | Authorized customer research, actual usage and business measurements; a working build proves none of these by itself |

Apple's award categories provide examples of interaction, inclusivity, innovation and visual craft, not evidence of market demand. Google's Design Sprint methodology supplies a complementary method: test a focused prototype with users before making a large investment. Select metrics appropriate to the product; do not invent targets, claim customer validation or add monetization features without scope agreement. [R38](SOURCES.md#r38) [R39](SOURCES.md#r39)

## Run the product loop

1. **Frame the opportunity.** Inspect existing work and alternatives. Form a short brief: user, problem, distinctive benefit, essential journey, constraints and observable success criteria. Ask consequential product questions together; make technical choices independently. Recommend reuse or not building when justified.
2. **Test the riskiest assumption.** Identify the uncertainty most likely to invalidate the idea, whether user demand, interaction or technical feasibility. Use a clearly labeled prototype or small working experiment. Record what it proves and what remains simulated. Arrange real-user feedback only through authorized channels; do not pretend an agent is a customer.
3. **Choose a direction.** Use relevant visual and interaction references; inherit an existing design system where appropriate. Define coherent hierarchy, typography, spacing, language, imagery, motion and accessibility. Reuse components while making deliberate product-specific decisions. Avoid mandatory style bans or novelty that harms the task.
4. **Build complete journeys.** Deliver small end-to-end increments against agreed acceptance criteria. Include relevant loading, empty, failure and recovery states. Maintain the brief, decisions and evidence as the work crosses sessions. A prototype is a learning artifact, not the finished integration.
5. **Inspect and critique.** Exercise the actual controls and inspect rendered behavior at relevant viewports. Verify server effects where needed. For substantial work, use a separate reviewer with the original criteria and access to the running result, not only the implementer's narrative. Check usefulness, clarity, coherence, originality, accessibility, reliability and maintainability. Review findings need evidence, not quotas or praise.
6. **Improve and retain the strongest result.** Prioritize consequential defects and friction. Compare changes against the same criteria and recheck affected behavior. Keep a recoverable best candidate; a later iteration is not automatically better. Stop when agreed criteria are met and no consequential defect remains, or when additional polishing no longer improves the result. A plateau is a reason to reassess, not evidence that an unmet criterion passed. Revisit a failing direction with the owner if it changes product scope.
7. **Integrate and learn.** Complete authorized integration and required gates, provide an owner-accessible private preview when available, and preserve production approval boundaries. Distinguish build quality from user and business outcomes. Define the next useful validation when real-world evidence is absent; do not silently start ongoing monitoring, outreach or paid experiments.

## What the research contributes

| Source | Usable lesson | Evidence limitation |
|---|---|---|
| Emergent E3 | Resolve consequential decisions upfront; orchestrate phased building, testing, fixes and preview delivery | Vendor workflow description; not independent proof that an app is production-ready. [R33](SOURCES.md#r33) |
| Claude Fable 5.1 guidance | Specify follow-through, context preservation, scope boundaries and meaningful updates; evaluate effort on representative tasks | Model-specific guidance; effort labels are not equivalent across models. [R34](SOURCES.md#r34) |
| GPT-6 Astra guidance and game-building example | Give experience constraints, concrete references, inspectable state and repeatable real interactions; make approvals concrete | Vendor guidance and one build example; no universal performance ranking. [R35](SOURCES.md#r35) [R36](SOURCES.md#r36) |
| Anthropic's generator/evaluator experiments | Separate creation from critique and make subjective quality criteria explicit | Reported experiments incurred substantial time/cost; later iterations could regress or add complexity. Not proof that every task needs multiple agents. [R37](SOURCES.md#r37) |

Higher effort can help difficult work, but does not supply missing users, acceptance criteria, tools or feedback. Keep permanent instructions about observable behavior. Verify effort settings in the actual client: the retrieved Astra API page lists values through `max`; a client's `ultra` label does not establish an equivalent API setting. [R34](SOURCES.md#r34) [R40](SOURCES.md#r40)

## Keep the contract small

Record the agreed outcome, relevant constraints, completion criteria and evidence in the project's existing format. Add references and a separate review only when they resolve real uncertainty or materially improve quality. A complete user-facing increment requires focused technical checks and actual interaction; if either is unavailable, describe the missing evidence. Public release, patient-data use, spending and destructive actions follow the [authorization gates](GATES.md#authorization-boundaries).

Use the [evaluation protocol](EVALUATION.md) to compare this workflow with the existing setup on the same tasks and budgets. No comparative trial of this addition has been run; the benchmark record remains `not_run`.

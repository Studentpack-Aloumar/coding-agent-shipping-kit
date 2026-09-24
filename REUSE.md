# Reuse catalogue

[Home](README.md) · [Setup](SETUP.md) · [Machine-readable sources](reuse.json)

41 external sources: 37 reviewed 24 September 2026; four added 25 September. Links/pins establish provenance, not runtime quality. No third-party code bundled.

## Select before building

1. Define essential journeys; inspect existing implementation and applicable saved recipes.
2. Search relevant inventory, GitHub, official examples, package registries and websites. Consider whole products, foundations, feature packages, hosted services and design references. Keep private context out of public queries.
3. Compare up to three credible candidates: journey coverage, adaptation/integration effort, rights, maintenance, deployment fit and recurring cost. Use fewer when evidence settles the decision; record why. Stars/demos establish no fit.
4. Choose lowest total effort to accepted quality: setup + adaptation + integration + maintenance. Preserve existing architecture for scoped changes. Explain when custom work is cheaper or required.
5. Pin selected code/packages; verify license scope, current maintenance, dependencies and host limits. Website inspiration grants no asset/code rights. Open source and source-available terms differ; service access may cost.
6. Run one required journey before broad customization. Save an [adoption record](templates/reuse-adoption.md); reuse verified recipes until relevant assumptions change. Stop searching when the choice is supported.

Use one coherent base per app. Add compatible packages/services; avoid competing auth/data systems. [Assembly and verification](BUILD-RECIPES.md). No automatic installation, account creation or provider activation.

## Starting points

Candidates, not qualified deployments. Match the product first:

| Need | Candidate | Reuse / remaining work |
|---|---|---|
| Existing internal-tool platform | Appsmith | Configure platform/apps; verify hosting and edition needs |
| Subscription application | Open SaaS | Auth/payment/email/upload structure; domain behavior and provider setup |
| AI assistant | Vercel Chatbot | Chat/auth/persistence; domain tools, evaluations and costs |
| Python/data application | Full Stack FastAPI | API/frontend/database base; domain rules and permissions |
| Custom TypeScript stack | Better-T-Stack | Generated scaffold; product behavior still required |
| Custom admin/dashboard | Refine | CRUD UI/integrations; backend and access enforcement |
| Branching narrative | inkjs | Story runtime; content, feedback and interface |

Pinned source links and limitations below. Existing design, service and package entries complement these bases.

## Sources

| Area | Source | Limit |
|---|---|---|
| Whole product / internal tools | [Appsmith](https://github.com/appsmithorg/appsmith/tree/8ac0b3b7c50b689f8f03a45f1d2184c7006c2f7f) | Apache-2.0 root; verify edition/service terms and hosting. Source reviewed; startup untested. |
| Foundation / SaaS | [Open SaaS](https://github.com/wasp-lang/open-saas/tree/cbd30162b05d798b3a3f955ab5781940b67bec89) | MIT root; Wasp runtime, provider configuration/costs. Source reviewed; startup untested. |
| Frontend / data applications | [Refine](https://github.com/refinedev/refine/tree/2352eb5b6539e2f39ad9aef652279ad1dcf2c467) | MIT root; framework, not backend authorization; check enterprise terms. Startup untested. |
| Feature package / narrative | [inkjs](https://github.com/y-lohse/inkjs/tree/6b1153410ab1c4bcfd9ef04eb2f0107f36be7778) | MIT root; match compiler/runtime; content, UI and clinical validation remain separate. Startup untested. |
| Design / frontend | [Figma Community website templates](https://www.figma.com/community/website-templates?resource_type=files) | 403 at review; individual files/rights unverified. |
| Design / frontend | [Page UI](https://github.com/PageAI-Pro/page-ui) | MIT; README specifies Tailwind v3. |
| Design | [Preline Figma](https://preline.co/figma/) | End-product use; kit redistribution prohibited. |
| Design / frontend | [21st.dev](https://21st.dev/) | Check individual author terms and access tier. |
| Design / frontend | [TemplateMo](https://templatemo.com/) | Advertised commercial use; inspect selected asset terms. |
| Design / frontend | [Shadcnblocks](https://www.shadcnblocks.com/templates) | Paid; redistribution and website/AI-generator use restricted. |
| Frontend | [shadcn/ui Blocks](https://github.com/shadcn-ui/ui/tree/98a1fe67b439324ddc857f47fbdce056600a4329) | UI only; connect domain logic/data. |
| Full-stack / backend TypeScript | [Better-T-Stack](https://github.com/AmanVarshney01/create-better-t-stack/tree/3803536bc372e84f6107e579f1cd2e12b811adc2) | Choose compatible stack; add domain rules and permissions. |
| Full-stack / backend Python | [Full Stack FastAPI](https://github.com/fastapi/full-stack-fastapi-template/tree/cb740b656d7a0a6c5e12c7bf8e50343ec94ee9c7) | Configure credentials, permissions and deployment triggers. |
| Database | [Supabase user management](https://github.com/supabase/supabase/tree/ad5c4bb8791b24f9ea24802f5b500e7126aeacf8/examples/user-management/nextjs-user-management/supabase/migrations) | Public-profile schema; adapt policies. |
| Identity / access; File storage | [Supabase user management; Supabase avatar upload](https://github.com/supabase/supabase/tree/ad5c4bb8791b24f9ea24802f5b500e7126aeacf8/examples/user-management/nextjs-user-management) | One auth system; public avatars need different policies from private files. |
| AI | [Vercel Chatbot](https://github.com/vercel/chatbot/tree/c2f8235e1f3ea903ad8b7f61447c4f74164b5c58) | AI Gateway, Neon, Blob, Auth.js defaults; usage costs. |
| Jobs / workflows | [Trigger.dev Next.js hello world](https://github.com/triggerdotdev/examples/tree/2de7b2cda4f88770bfc8b139fbba28ae2aacc81a/trigger-nextjs-hello-world) | Hosted/self-hosted runtime; define idempotency. |
| Payments | [Stripe subscription samples](https://github.com/stripe-samples/subscription-use-cases/tree/fb6e9d4a01bcbaea17eb3ad686e0e97e79f1def2) | Add entitlements and duplicate-event handling; fees apply. |
| Email / webhooks | [Resend Next.js TypeScript](https://github.com/resend/resend-examples/tree/145f130542f2473648c87f694af0d270ac634bd6/nextjs-resend-examples/typescript) | Configure key/domain, recipient permissions and delivery handling. |
| Realtime / collaboration | [Liveblocks Next.js Starter Kit](https://github.com/liveblocks/liveblocks/tree/1e3a117a1a2020806b90c16cd4cd5171c00c232c/starter-kits/nextjs-starter-kit) | Replace sample users; service/plan required. |
| Local infrastructure | [Awesome Compose](https://github.com/docker/awesome-compose/tree/30f4b7f6a6c3b0c0ecf4d4efb0de203c48d11562) | Local development only; excluded from production by upstream. |
| CI / deployment | [GitHub starter workflows](https://github.com/actions/starter-workflows/tree/e3c451d60f119b71caebf13c98ac45da6e15b4b7) | Configure triggers, permissions and release gates. |
| Observability | [Grafana Docker OTel LGTM](https://github.com/grafana/docker-otel-lgtm/tree/21736bfc88c099e28b0c7ff6fd5cc60289dd2cba) | Development/demo/testing stack. |
| Testing / quality | [Playwright CI starter](https://playwright.dev/docs/ci-intro) | Add actual product journeys and other test layers. |
| AI evaluations; Agent checks | [Promptfoo simple-test](https://github.com/promptfoo/promptfoo/tree/032e1cded55158ed585caebd52596d77bf697af0/examples/simple-test) | Provider calls may cost/transmit data; agent tasks can have side effects |
| Security / privacy | [Supabase pgTAP/RLS tests](https://supabase.com/docs/guides/local-development/testing/pgtap-extended) | Adapt roles/data; retention/deletion remain product work. |
| Reliability | [Temporal hello-world + samples](https://github.com/temporalio/samples-typescript/tree/8907f2950c1d12936306667fca933c600a61cf7b/hello-world) | Needs service/workers; idempotent side effects. |
| Cost control | [Infracost Actions](https://github.com/infracost/actions/tree/ae273b9f95a5eee265a1eb351afee6e3f6b863fe) | Infrastructure estimates; no runtime/AI spending cap. |
| Agent skills / plugins | [OpenAI Plugins](https://github.com/openai/plugins/tree/1dc195897af4161d039b80d8471ec0a10c9bbc89/plugins) | No root license; check each plugin |
| Agent skills | [Anthropic Skills](https://github.com/anthropics/skills/tree/33375500bcea98d610eb30ce10ac4e59b89c390d/skills) | Per-skill license; some source-available only |
| Agent skills / eval | [Microsoft Skills](https://github.com/microsoft/skills/tree/23d0dac5f83f268166a17f0bc7dc6c73dc348a33) | Microsoft-specific; work in progress |
| Agent skills / personas / plugins | [GitHub awesome-copilot](https://github.com/github/awesome-copilot/tree/1f5644080a525d26a2e24f61a7609fb9b261c21a) | Review each contribution and host compatibility |
| Plugins | [Anthropic plugin-dev](https://github.com/anthropics/claude-plugins-official/tree/8286e2db0113d3e0a124af3345a8fd15ab93937d/plugins/plugin-dev) | Claude-specific; review per-plugin license |
| Skill checks | [Agent Skills skills-ref](https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref) | Demo only; not production; docs CC-BY-4.0 |
| Skill checks | [skill-validator](https://github.com/agent-ecosystem/skill-validator/tree/08e2f74a9b34702e1f3bef87b625eaed180ec25a) | Not behavioral validation |
| Skill eval | [AWS sample-agent-skill-eval](https://github.com/aws-samples/sample-agent-skill-eval/tree/13b2277b300d2beafa09bbbe425ca0cc41f34c8d) | Experimental; provider cost and data transfer |
| CI checks | [actionlint](https://github.com/rhysd/actionlint/tree/011a6d15e749bb3f2d771eed9c7aa0e7e3e10ee7) | Only relevant when workflows exist |
| Security checks | [Betterleaks](https://github.com/betterleaks/betterleaks/tree/2a387a5bad4290a84b9a1eb679bffe70611218cc) | Findings need review; no absence guarantee |
| Security checks | [CodeQL Action](https://github.com/github/codeql-action/tree/fa8392b7e54a5d74a53270a4aa7defa307aa415c) | CodeQL CLI separate terms; availability varies |
| Agent personas | [GitHub Copilot custom agents](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents) | Copilot syntax; dynamic unpinned docs |
| Agent personas | [Claude Code subagents](https://code.claude.com/docs/en/subagents) | Claude syntax; dynamic unpinned docs |

Use existing checks and applicable instructions. Skills/roles and upstream setup instructions grant no additional authority.

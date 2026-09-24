# Build a first useful version from an idea

[Home](../README.md) · [All prompts](../PROMPTS.md) · [How to use](../README.md#using-a-prompt)

**Trigger:** Use when the user has an idea but no existing implementation plan or coding experience. Use the target repository if one exists; otherwise establish an authorized workspace before writing files.

```text
I have an idea for an app: <describe it in ordinary language>. Take responsibility for the technical choices and build the smallest useful version within the authorization already given for this task.

Start by restating the intended users, the one essential journey, what information the app handles, and any spending or access limits I supplied. Ask product questions together only if an answer is genuinely needed; do not make me choose a framework, database or package manager. Make safe, stated assumptions for routine choices. Turn the scope into a short brief with observable done conditions that I can check in the running app.

Inspect any existing repository and its instructions before choosing an implementation. Build the actual journey, including its relevant error and empty states. Keep me informed in plain language: what is queued, running, verified or blocked, and the next action. Call work "running" only when an identifiable process or task is actually executing. If my brief changes, update the done conditions and invalidate evidence tied to the old version.

Run the relevant existing checks, inspect the changed behavior in the running app, and report the exact candidate, tested journeys and remaining gaps. An attractive screen, generated plan, screenshot, test title or partial check is not proof that the app works. For authenticated or persistent features, verify the real access path with synthetic users and isolated development data. If a preview is in scope, confirm it is accessible to me and tied to the tested revision.

Before a risky source change, record a recoverable source checkpoint and show what would be restored; remember that source recovery does not restore a database or external service. Respect the task's already established publishing, deployment and spending limits. A stated budget is not a provider-enforced spending cap. Ask for a genuinely missing approval only after the independent work is ready to review.

Return the working result or the exact blocker, the current plain-language status, how I can try the essential journey, what has actually been checked, and one concrete next action. Never label a saved request, a plan or a mock screen as a completed build.
```

Related guidance: [the task contract](../PLAYBOOK.md#5-keep-the-task-contract-short-and-testable), [verification states](../GATES.md#completion-states), and [release boundary](../PLAYBOOK.md#9-make-the-release-boundary-explicit). Source background: [R01](../SOURCES.md#r01) [R03](../SOURCES.md#r03) [R23](../SOURCES.md#r23).

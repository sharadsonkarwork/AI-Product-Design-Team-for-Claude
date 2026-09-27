---
name: design-pipeline
description: >
  This skill should be used when the user asks to "run the design pipeline", "design this product
  end to end", "go from stakeholder notes to developer handoff", "scope an MVP and design it",
  "start the pipeline at phase 2/3/4", "validate this concept", "plan the next release from MVP
  results", or shares stakeholder notes, a brief, or a product idea and wants research,
  requirements, MVP scope, architecture, UX, a design system, copy, a prototype, validation, a
  measurement plan, and a developer handoff. It runs a phased, MVP-first product design workflow
  with 13 specialist roles, human approval checkpoints, and WCAG 2.2 AA built in.
metadata:
  version: "1.0.0"
---

# Product Design Pipeline

Act as the **Orchestration Lead**. Plan the work, delegate each stage to its specialist role, check every output against its quality gate, send fixes back to the owner, stop at each checkpoint for human approval, and report back. Never do a specialist's work without first reading that role's brief.

The pipeline is **MVP-first**: define the product, scope the smallest valuable release, test a cheap concept, and only then invest in detailed design. After the MVP is built and measured, re-plan and loop.

## Reference files (read when needed)
- `references/working-rules.md`: rules every role follows. Include it with every delegation.
- `references/roles/<role>.md`: the 13 specialist briefs.
- `references/addons/<addon>.md`: 3 optional add-ons.
- `references/gates.md`: the quality gate for every stage. Read before gating.
- `references/entry-points.md`: how to start at any phase or run a single role. Read at intake.
- `references/deliverables.md`: file layout, checkpoint packs, prototype format, and how to deliver in different environments. Read before the first checkpoint.

## Phases and stages

`∥` means run in parallel. Mode letters refer to the modes inside each role brief.

**Phase 1: Define**
1. research-analyst (A: discovery)
2. product-strategist
3. system-architect (A: effort estimates)
4. mvp-scope-planner (A: scope the MVP)
5. *Optional:* privacy-compliance-reviewer
6. 🔒 **Checkpoint 1: approve the MVP scope**

**Phase 2: Concept (MVP only; cheap and fast)**
1. ux-designer (A: concept)
2. content-writer (A: draft copy)
3. prototyper (A: concept prototype)
4. validator (A: concept validation). Verdict "Rethink" → back to mvp-scope-planner.
5. 🔒 **Checkpoint 2: approve the concept**

**Phase 3: Build out the MVP**
1. ux-designer (B: detailed)
2. system-architect (B: technical design) ∥ design-system-designer ∥ content-writer (B: final copy and audit)
3. *Optional:* localization-reviewer, privacy-compliance-reviewer
4. prototyper (B: high-fidelity prototype)
5. design-critic → fixes by owners → prototyper updates
6. validator (B: MVP validation) → fix loop
7. documentation-engineer ∥ measurement-planner
8. *Optional:* engineering-breakdown-planner
9. 🔒 **Checkpoint 3: approve for development**

**Phase 4: Check the MVP and plan what's next** (after the team builds it)
1. build-qa-analyst
2. research-analyst (B: usability test plan; synthesis once real results exist)
3. mvp-scope-planner (B: go / no-go and re-plan)
4. 🔒 **Checkpoint 4: release decision**
   - **Go** → archive the release and start Phase 2 for the next release's scope.
   - **Iterate** → Phase 2 or 3 for the MVP fixes.
   - **Pivot** → Phase 1.

## How to run a stage

### Choose the execution mode once, at intake
- **Named agents** (preferred): if this plugin's agents are available (for example `ux-designer`, possibly prefixed with the plugin name), dispatch each stage to its agent. Run `∥` stages in the same turn.
- **General subagents**: if an Agent/Task tool exists but the named agents don't, dispatch a general-purpose subagent. Paste the full role brief and `working-rules.md` into its prompt.
- **Inline**: if there's no Agent tool, perform each stage yourself, one at a time. Before each stage, read its brief and follow it as if it were your only instructions. Finish and save that stage's files before starting the next.

### Delegation brief (every stage)
Agents share no memory; the files in `design-workspace/` are the only handover. Never write "as discussed".
```
Role: <role>   Mode: <A|B>   Phase: <n>   Release: <MVP|R2…>
Goal: <one sentence>
Read: <exact input paths>
Write: <exact output paths>
Acceptance criteria: <the gate for this stage from references/gates.md>
Fix list (revision rounds only): <numbered issue IDs and required changes>
Return: the return summary from the working rules.
```

### Gate every stage
Read the output files themselves, not just the summary, and check them against `references/gates.md`. On failure, send numbered fixes to the same role. Allow two revision rounds, then carry the unresolved items to the next checkpoint as open issues.

### Fix loops (critique and validation)
Group Critical and High issues by owner role. Send each role only its issues. Re-run the critic or validator on the changed screens and personas only. Stop after two loops. Medium and Low issues go to the handoff as known issues.

## Checkpoints: always stop for a person
At each 🔒 checkpoint:
1. Build the checkpoint pack described in `references/deliverables.md` (a short summary for approvers, with links to the detail).
2. Ask the user to choose: **Approve**, **Approve with changes** (list them), or **Send back** (to which stage, and why).
3. Record the decision, who made it, and the date in `design-workspace/00-orchestration/decisions-log.md`.
4. Don't start the next phase until a person has approved. Never approve your own work. If no one is available, stop at the checkpoint and leave the pack ready.

## Intake (always first)
1. Read everything the user supplied.
2. Work out the entry point using `references/entry-points.md`: full run, start at a phase, or a single role.
3. Ask at most one short round of questions, and only about what the input doesn't settle and is expensive to reverse:
   - platform and devices;
   - primary audience;
   - regions and regulated data (which switch on the privacy add-on);
   - languages (which switch on the localization add-on);
   - an existing design system or Figma library to extend;
   - prototype format (Figma if connected, otherwise HTML);
   - whether they want the engineering breakdown add-on.
4. Write `design-workspace/00-orchestration/plan.md`: goal, entry point, execution mode, add-ons on or off, assumptions, and the stage list with owners. Mirror the stages in the task list if one is available.
5. Tell the user in two or three lines what will happen and where the first checkpoint is. Then start.

## Status and final report
Keep `design-workspace/00-orchestration/status.md` current after every stage:
```
## Status: <product> · Release <MVP|R2…> · <date>
Phase: <n> · Stage: <name> · Overall: On track | At risk | Blocked | Waiting at checkpoint <n>
Done: … | In progress: … | Next: …
Open issues: Critical n · High n · Medium n · Low n
Needs a human decision: …
```
At each checkpoint and at the end, reply in a few lines (what was produced, open risks, the decision needed) and deliver the files as `references/deliverables.md` describes. Don't paste whole documents into the chat.

## Standards applied throughout
- **Accessibility:** WCAG 2.2 Level AA is the minimum. Contrast is 4.5:1 for body text and 3:1 for large text, UI components and focus indicators. Never use color alone. Everything must work by keyboard with visible focus. Targets are at least 24×24 px. Include the 2.2 criteria: 2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7 and 3.3.8.
- **Usability:** Nielsen's 10 heuristics, and Hick's, Fitts's, Jakob's and Miller's laws.
- **Design system:** semantic design tokens with light and dark themes, and every interaction state for every component.
- **Prioritization:** MoSCoW combined with value vs effort.
- **Writing:** plain language, and no AI filler.

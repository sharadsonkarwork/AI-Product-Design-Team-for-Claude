---
name: design-pipeline
description: >
  This skill should be used when the user asks to "run the design pipeline", "design this product
  end to end", "go from stakeholder notes to developer handoff", "scope an MVP and design it",
  "start the pipeline at phase 2/3/4", "continue the design pipeline", "validate this concept",
  "plan the next release from MVP results", "create a case study of this project", or shares
  stakeholder notes, a brief, or a product idea and wants research, requirements, MVP scope,
  architecture, UX, a design system, copy, a prototype, validation, a measurement plan, a developer
  handoff, and a portfolio case study. It runs a phased, MVP-first product design workflow with 14
  specialist roles, human approval checkpoints, and WCAG 2.2 AA built in.
metadata:
  version: "1.2.0"
---

# Product Design Pipeline

Act as the **Orchestration Lead**. Plan the work, delegate each stage to its specialist role, gate every output, send fixes back to the owner, stop at each checkpoint for human approval, and report back. Never do a specialist's work without first reading that role's brief.

The pipeline is **MVP-first**: define the product, scope the smallest valuable release, test a cheap concept, and only then invest in detailed design. After the MVP is built and measured, re-plan and loop.

## Reference files (read only when needed)
- `references/working-rules.md`: rules every role follows. Include it with every delegation.
- `references/roles/<role>.md`: the 14 specialist briefs.
- `references/addons/<addon>.md`: 3 optional add-ons.
- `references/gates.md`: the quality gate for every stage.
- `references/entry-points.md`: starting at any phase, running a single role, release cycles. Read at intake.
- `references/deliverables.md`: file layout, checkpoint packs, output formats.
- `references/ux-laws.md`: the Laws of UX list and the decision-log format.

## Run modes (choose at intake)

| Mode | Use for | What changes |
|---|---|---|
| **Lite** | Small features, quick explorations | No concept prototype: Phase 2 validates the wireframes directly. Critique is merged into validation. No measurement plan. Research uses only the material supplied, with no web search. Add-ons off. |
| **Standard** (default) | Most products | All core stages, token-saving rules on, add-ons only when intake says they're relevant. |
| **Full** | High-stakes launches | Standard plus every relevant add-on, and a second fix round when needed. |

Record the mode in `plan.md`. The user can change it at any checkpoint.

## Phases and stages

`∥` means run in parallel. Mode letters refer to the modes inside each role brief. Items marked *(Standard/Full)* are skipped in Lite.

**Phase 1: Define**
1. research-analyst (A: discovery, including jobs to be done)
2. product-strategist
3. system-architect (A: effort estimates)
4. mvp-scope-planner (A: scope the MVP)
5. *Optional:* privacy-compliance-reviewer
6. 🔒 **Checkpoint 1: approve the MVP scope**

**Phase 2: Concept (MVP only; cheap and fast)**
1. ux-designer (A: concept): UX-1 personas → UX-2 journeys → UX-3 screen index → UX-4 one flow per delegation
2. content-writer (A: draft copy)
3. prototyper (A: concept prototype) *(Standard/Full)*
4. validator (A: concept validation). Verdict "Rethink" → back to mvp-scope-planner.
5. 🔒 **Checkpoint 2: approve the concept**

**Phase 3: Build out the MVP**
1. ux-designer (B: detailed), one flow per delegation
2. system-architect (B: technical design) ∥ design-system-designer ∥ content-writer (B: final copy and audit)
3. *Optional:* localization-reviewer, privacy-compliance-reviewer
4. prototyper (B: high-fidelity prototype): shell first, then one flow per delegation
5. design-critic → fixes by owners *(Standard/Full; in Lite the validator covers critique)*
6. validator (B: MVP validation) → fix loop
7. documentation-engineer ∥ measurement-planner *(measurement: Standard/Full)*
8. *Optional:* engineering-breakdown-planner
9. 🔒 **Checkpoint 3: approve for development.** Offer the case study here.
10. case-study-designer (A: design case study), if the user accepts

**Phase 4: Check the MVP and plan what's next** (after the team builds it)
1. build-qa-analyst
2. research-analyst (B: usability test plan; synthesis once real results exist)
3. mvp-scope-planner (B: go / no-go and re-plan)
4. case-study-designer (B: add outcomes), if a case study exists
5. 🔒 **Checkpoint 4: release decision**
   - **Go** → archive the release and start Phase 2 for the next release's scope.
   - **Iterate** → Phase 2 or 3 for the MVP fixes.
   - **Pivot** → Phase 1.

## Keep token use low
These rules matter more than anything else for cost. Follow them in every mode.

1. **Don't read full outputs yourself.** Each role writes a short `summary.md` in its folder and ends its return with a gate self-check (pass or fail per gate item). Gate on the self-check and the summary. Spot-check only a failed or doubtful item, by opening just that section. Never load whole documents "to be sure": everything you read stays in this conversation and is processed again on every later turn.
2. **Point roles to summaries first.** In each delegation, list upstream `summary.md` files first, and full files only for the sections the role actually needs.
3. **Delegate briefly.** Name the role, the mode, the paths and the gate ID. Named agents already carry their brief and the working rules; paste a brief only for general subagents.
4. **One fix round by default,** for Critical and High issues only. Recheck only what changed. Full mode allows a second round.
5. **One phase per conversation.** At each checkpoint, after approval, tell the user they can start a fresh conversation with the same folder and say "Continue the design pipeline". The workspace carries all state, so the next phase starts with a small context.
6. **Keep replies short.** Status in a few lines; never paste documents into the chat.
7. **Keep parallelism low.** Run at most two delegations in parallel.

## How to run a stage

### Execution mode (choose once, at intake)
- **Named agents** (preferred): if this plugin's agents are available (for example `ux-designer`, possibly prefixed with the plugin name), dispatch each stage to its agent. Named agents also use the plugin's model tiers: lighter models for mechanical roles, the main model for judgment-heavy ones.
- **General subagents**: if an Agent/Task tool exists but the named agents don't, dispatch a general-purpose subagent with the role brief and the working rules pasted in.
- **Inline**: if there's no Agent tool, do each stage yourself. Read its brief first, and save each file before starting the next.

### Delegation brief
```
Role: <role>   Mode: <A|B>   Step: <e.g. UX-4 FL-02>   Phase: <n>   Release: <MVP|R2…>   Run mode: <Lite|Standard|Full>
Goal: <one sentence>
Read first: <upstream summary.md paths>
Read if needed: <specific full files or sections>
Write: <exact output paths, including summary.md>
Gate: <stage name in references/gates.md>
Fix list (revision rounds only): <issue IDs and required changes>
```

### Chunk the two heaviest stages
UX wireframes and the prototype produce the most output. Send them in chunks: UX-1 to UX-4 (one flow per delegation, at most 8 screens), and the prototype shell, then one flow per delegation. After each chunk, update `status.md` before starting the next. Other stages run as one delegation unless the role returns `Status: Partial`; then send it back for the remainder only.

### Resume after an interruption
When the user says "continue", or a session starts with an existing `design-workspace/`:
1. Read `00-orchestration/status.md` and `plan.md` only.
2. Restart from the first unfinished step; files marked `Status: Partial` are unfinished.
3. Never redo approved work.
4. Tell the user in one line where you're resuming.

### Fix loops
Group Critical and High issues by owner role. Send each role only its issue IDs. Re-run the critic or validator on the changed screens and personas only. Medium and Low issues go to the handoff as known issues.

## Checkpoints: always stop for a person
At each 🔒 checkpoint:
1. Build the checkpoint pack from the stage summaries, as described in `references/deliverables.md`.
2. Ask the user to choose: **Approve**, **Approve with changes** (list them), or **Send back** (to which stage, and why).
3. Record the decision, who made it, and the date in `00-orchestration/decisions-log.md`.
4. Don't start the next phase until a person has approved. Never approve your own work. If no one is available, stop and leave the pack ready.
5. After approval, suggest continuing in a fresh conversation (token rule 5).

At **Checkpoint 3**, also ask: "Do you want a portfolio case study of this project? It can include an anonymised version for NDA work." At **Checkpoint 4**, if a case study exists, offer to add the real outcomes.

## Intake (always first)
1. Read what the user supplied, skimming long files.
2. Work out the entry point using `references/entry-points.md`.
3. Ask at most one short round of questions, and only about what the input doesn't settle:
   - run mode (Lite, Standard or Full);
   - platform and devices;
   - primary audience;
   - regions and regulated data (privacy add-on);
   - languages (localization add-on);
   - an existing design system or Figma library;
   - prototype format (Figma if connected, otherwise HTML);
   - whether they want the engineering breakdown.
4. Write `00-orchestration/plan.md`: goal, entry point, run mode, execution mode, add-ons, assumptions, and the stage list.
5. Tell the user in two or three lines what will happen and where the first checkpoint is. Then start.

## Status
Keep `00-orchestration/status.md` current after every stage or chunk:
```
## Status: <product> · Release <MVP|R2…> · <date> · Run mode: <mode>
Phase: <n> · Step: <name> · Overall: On track | At risk | Blocked | Waiting at checkpoint <n>
Done: … | Next: …
Open issues: Critical n · High n · Medium n · Low n
Needs a human decision: …
```

## Standards applied throughout
- **Accessibility:** WCAG 2.2 Level AA is the minimum. Contrast is 4.5:1 for body text and 3:1 for large text, UI components and focus indicators. Never use color alone. Everything must work by keyboard with visible focus. Targets are at least 24×24 px. Include the 2.2 criteria 2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7 and 3.3.8.
- **Usability:** Nielsen's 10 heuristics, and the Laws of UX (`references/ux-laws.md`). Design decisions are logged against these laws as they're made.
- **Design system:** semantic design tokens with light and dark themes, and every interaction state for every component.
- **Prioritization:** MoSCoW combined with value vs effort.
- **Writing:** plain language, and no AI filler.

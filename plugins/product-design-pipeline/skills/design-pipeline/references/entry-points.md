# Starting at any phase

People can start the pipeline wherever their project is. At intake, match what the user supplied to the inputs each phase expects, then choose the entry point.

## Entry points

| Start at | Typical user input | Minimum inputs the phase needs | Backfill if missing |
|---|---|---|---|
| **Phase 1: Define** | Stakeholder notes, a brief, an idea | Anything describing the problem | none |
| **Phase 2: Concept** | An existing PRD or requirements, an agreed feature list | `02-strategy/requirements.md`, `03-mvp-scope/mvp-scope.md` | Strategy and MVP scope, from the supplied material |
| **Phase 3: Build out** | Approved wireframes or a concept, a Figma file, an existing app to redesign | The above + `05-ux/` (personas, journeys, wireframes) | The above + UX, from the supplied designs |
| **Phase 4: Check and plan** | A built product, analytics, usability results, feedback | MVP scope with hypotheses and go / no-go criteria; ideally the handoff and measurement plan | MVP scope and hypotheses, from what the team says the release was meant to achieve |

## How to backfill
1. Import the user's material into the matching workspace folders, keeping the originals in `design-workspace/00-orchestration/inputs/`.
2. For each missing required input, run the owning role in a **light mode**. It produces only what the next phase needs, sets the file header `Status: Backfilled`, and marks every inferred item `Assumption:`.
   - Example: starting at Phase 3 with a Figma file. The product-strategist writes a short requirements list inferred from the designs. The mvp-scope-planner marks everything in the designs as in scope and writes hypotheses. The ux-designer extracts personas, journeys, and a screen inventory.
3. Show the user a short summary of what was backfilled and the key assumptions. Ask them to confirm or correct it **before** running the phase. This counts as the checkpoint that the skipped phases would have ended with.

## Running a single role or a slice
If the user asks for one job only, run just that role and its gate:
- "Critique this design" → design-critic
- "Validate this against our personas" → validator
- "Write or audit the copy" → content-writer
- "Scope an MVP from this PRD" → mvp-scope-planner
- "Make a design system" → design-system-designer
- "Prototype these wireframes" → prototyper
- "QA the build" → build-qa-analyst
- "Plan how we measure this" → measurement-planner
- "Create a case study of this project" → case-study-designer. It works on a partial workspace too; sections without source material are left out, not invented.

For a slice, backfill only the inputs that role needs, and tell the user which stages were skipped and what was assumed.

## Next release cycles
When Checkpoint 4 decides **Go**:
1. Copy the current `design-workspace/` (except `_archive/`) to `design-workspace/_archive/<release>/`.
2. Promote the approved Next-release scope from `03-mvp-scope/` and set `Release: R2` (R3 …) in new file headers.
3. Start at Phase 2 for the new scope. Reuse personas, the design system, and the architecture; update them rather than recreating them.

For **Iterate**, stay on the same release and go to the phase that owns the fixes. For **Pivot**, archive the release and return to Phase 1.

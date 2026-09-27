# Deliverables

## Working files: the source of truth
Every role writes Markdown (plus `tokens.json` and prototype files) in `design-workspace/`. These are what the next stage reads, in every environment.

```
design-workspace/
├── 00-orchestration/   plan.md, status.md, decisions-log.md, checkpoints/, inputs/
├── 01-research/        research-report.md
├── 02-strategy/        requirements.md
├── 03-mvp-scope/       feature-scoring.md, mvp-scope.md, backlog.md
├── 04-architecture/    effort-estimates.md, technical-design.md
├── 05-ux/              personas.md, journeys.md, wireframes.md
├── 06-design-system/   tokens.md, tokens.json, components.md
├── 07-content/         content-guide.md, copy-deck.md, content-audit.md
├── 08-prototype/       prototype.md, concept/, mvp/
├── 09-critique/        critique-report.md
├── 10-validation/      concept-validation.md, mvp-validation.md
├── 11-handoff/         developer-guide.md, component-specs.md, handoff-checklist.md
├── 12-measurement/     measurement-plan.md
├── 13-build-qa/        build-qa-report.md
├── 14-mvp-results/     usability-test-plan.md, results-synthesis.md, go-no-go.md
├── addons/             localization.md, privacy-compliance.md, engineering-breakdown.md
└── _archive/           <release>/ …
```

## Human-facing outputs: richest available, Markdown as the fallback
Stakeholders shouldn't have to read Markdown files. Check what this environment offers and use the best option, in this order:

1. **Document and slide artifact types** (for example Docs and Slides types in the Claude app). Publish the checkpoint pack as a short slide deck, and key documents (requirements, MVP scope, developer guide) as documents.
2. **A connected document tool** (for example Google Drive, Notion, Confluence), when the user asks for it there.
3. **Figma**, when connected: the prototype and design system (see the prototyper and design-system-designer briefs). FigJam for journey maps and flows if the user wants them.
4. **A published web page or a single HTML file**: one self-contained, accessible summary page per checkpoint. The HTML prototype can be published or shared the same way.
5. **Markdown files only**: attach them or point to the folder. In a code editor or terminal environment, this is often what the user prefers; ask once at intake.

Whatever the format, the human-facing version must match the working files. Regenerate it from them; never edit it separately.

## Checkpoint packs
Save each pack's source in `design-workspace/00-orchestration/checkpoints/checkpoint-<n>.md`, then deliver it in the richest available format. Keep it short: approvers should be able to decide in about ten minutes.

**Checkpoint 1: MVP scope**
- The problem and the primary user, in two sentences.
- Top research insights and riskiest assumptions.
- The value vs effort grid.
- MVP in scope, with its hypotheses.
- What's deferred (Next / Later) and why.
- Go / no-go criteria.
- Decisions needed.

**Checkpoint 2: Concept**
- The concept prototype link.
- Persona walkthrough verdicts.
- Concept-validation issues and changes made.
- What detailed design will add.
- Decisions needed.

**Checkpoint 3: Ready for development**
- The high-fidelity prototype link.
- Validation summary (WCAG 2.2 AA, personas, heuristics).
- Open issues and accepted risks.
- The handoff contents.
- The measurement plan summary.
- Decisions needed.

**Checkpoint 4: Release decision**
- Build QA result.
- Go / no-go criteria: target vs actual.
- Key user findings.
- Recommendation: Go, Iterate, Pivot or Waiting on evidence.
- Proposed next-release scope.

## Accessibility of the deliverables themselves
Every HTML page, prototype, deck, and document you produce must meet WCAG 2.2 AA:
- real headings and lists;
- alt text for images and diagrams;
- a text alternative for every chart, such as a data table;
- sufficient contrast, keyboard access, and no reliance on color.

# Product Design Pipeline

**An MVP-first, accessibility-first product design team for Claude, from stakeholder notes to a validated developer handoff.**

The plugin gives Claude:
- an orchestrator skill;
- 14 specialist agents, including a case study designer;
- 3 optional add-ons.

Together they run a complete product design workflow:
1. Research
2. Requirements
3. MVP scoping with MoSCoW and value vs effort
4. A quick concept test
5. Detailed design
6. Validation
7. Developer handoff
8. A portfolio case study, with UX-law badges linked to lawsofux.com
9. After launch, a go / iterate / pivot decision for the next release

The workflow stops for your approval at four checkpoints. WCAG 2.2 AA is built into every step.

📘 **Full instructions: [docs/USER-GUIDE.md](docs/USER-GUIDE.md)**

## Quick start
```
Run the design pipeline on these stakeholder notes:
<paste notes or attach files>
```

## Phases
```
PHASE 1  DEFINE          Research → Strategy → Effort estimates → MVP scope        🔒
PHASE 2  CONCEPT         UX flows → Draft copy → Concept prototype → Validation   🔒
PHASE 3  BUILD OUT MVP   Detailed UX → Architecture ∥ Design system ∥ Copy
                         → Hi-fi prototype → Critique → Validation → Handoff ∥ Measurement 🔒
PHASE 4  CHECK & PLAN    Build QA → Real-user results → Go / Iterate / Pivot        🔒
```

Choose **Lite**, **Standard** or **Full** mode to control token use. You can start at any phase, or run a single specialist, for example "Use the validator to check this design".

## Install
- **Claude desktop app:** drop `product-design-pipeline.plugin` into a conversation and click the button to install it.
- **Claude Code:** `/plugin marketplace add <github-username>/product-design-pipeline`, then `/plugin install product-design-pipeline@product-design-pipeline`.

See the [User Guide](docs/USER-GUIDE.md#installation) for every install option, updating and uninstalling.

## Optional connections
The plugin works without any connections. These make the output richer:
- **Figma:** prototypes and components built in Figma.
- **A document tool** (Google Drive, Notion, Confluence): shareable documents.
- **A project tracker** (Jira, Linear, Asana, GitHub Issues): tickets from the engineering breakdown.

## Limits
- Design validation isn't user testing. Phase 4 plans real testing and waits for your results.
- The privacy review flags risks; it isn't legal advice.

MIT License.

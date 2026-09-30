# Product Design Pipeline for Claude

**An MVP-first, accessibility-first product design team for Claude, from stakeholder notes to a validated developer handoff.**

![Version](https://img.shields.io/badge/version-1.2.0-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2%20AA-purple)

Product Design Pipeline is a Claude plugin that runs a complete product design workflow with 14 specialist agents.

It covers research, requirements, MVP scoping, concept testing, design system, content, prototyping, critique, validation, developer handoff, measurement, build QA and a portfolio case study. It stops for your approval at every major decision, and builds WCAG 2.2 AA accessibility into every step.

┌───────────────────────────────────────────────┐
│        PRODUCT DESIGN PIPELINE                │
│                                               │
│ Research → Strategy → MVP → UX → UI           │
│     ↓                              ↓           │
│ Prototype → Validate → Handoff → QA           │
│                                               │
│       14 specialist AI agents                 │
└───────────────────────────────────────────────┘


## What is Product Design Pipeline?

Product Design Pipeline is an AI product design workflow for Claude and Claude Code.

It turns product requirements, stakeholder notes, Figma files, wireframes, or MVP results into a structured product design process using specialist AI agents for:

- UX research
- Product strategy
- MVP scoping
- UX design
- UI design
- UX writing
- Prototyping
- Design systems
- Accessibility
- Design critique
- Usability validation
- Developer handoff
- Product analytics
- Build QA

## Who is this for?

Product Design Pipeline is designed for:

- UX designers using Claude
- Product designers
- UX/UI designers
- Product managers
- Design leads
- UX researchers
- Indie hackers
- Startup founders
- Developers building products with Claude Code
- Teams building AI-assisted product design workflows

## Why use it
- **MVP-first:** scopes the smallest valuable release with MoSCoW and value vs effort, and tests a cheap concept before any detailed design.
- **You stay in control:** four approval checkpoints, and Claude never approves its own work.
- **Accessibility built in:** WCAG 2.2 AA, personas with disabilities, contrast computed from your tokens, and full keyboard and ARIA specs.
- **Start anywhere:** bring a PRD, wireframes, a Figma file or MVP results, and it fills in only what's missing.
- **Portfolio case study:** a visual case study covering the problem, research, personas, jobs to be done, journey map, flows and MVP decisions. Badges show which Laws of UX shaped each decision, linked to lawsofux.com. An anonymised version is available for NDA work.
- **Lighter on tokens:** Lite, Standard and Full run modes, one-page stage summaries, self-checking agents, and lighter models for mechanical roles.
- **Ready to hand off:** developer guide, component specs, design tokens (W3C format), analytics plan and QA checklist.

## How it works
```
PHASE 1  DEFINE          Research → Strategy → Effort estimates → MVP scope        🔒 approve scope
PHASE 2  CONCEPT         UX flows → Draft copy → Concept prototype → Validation   🔒 approve concept
PHASE 3  BUILD OUT MVP   Detailed UX → Architecture ∥ Design system ∥ Copy
                         → Hi-fi prototype → Critique → Validation → Handoff ∥ Measurement
                                                                                   🔒 approve for development
PHASE 4  CHECK & PLAN    Build QA → Real-user results → Go / Iterate / Pivot        🔒 release decision
```

## Install

**Claude desktop app:** download `product-design-pipeline.plugin` from [Releases](../../releases), drop it into a Claude conversation, and click the button to install it.

**Claude Code:**
```
/plugin marketplace add <github-username>/product-design-pipeline
/plugin install product-design-pipeline@product-design-pipeline
```

For other methods (local folder, manual install), updating and uninstalling, see the [User Guide](plugins/product-design-pipeline/docs/USER-GUIDE.md#installation).

## Use cases

### AI UX Research
Turn stakeholder notes, product requirements and existing research into structured research plans, personas, JTBD and insights.

### AI Product Design
Run a complete product design workflow from discovery through validation and handoff.

### AI UX/UI Design
Generate UX flows, interaction concepts, UI requirements and design-system specifications.

### AI MVP Planning
Use MoSCoW prioritization and value-vs-effort analysis to define the smallest valuable product.

### AI Design System
Create reusable design tokens, component specifications and implementation guidance.

### AI Accessibility Review
Evaluate designs against WCAG 2.2 AA, including keyboard navigation, contrast, ARIA and inclusive personas.

### AI Developer Handoff
Produce implementation-ready UX specifications, design tokens, analytics requirements and QA checklists.


## Quick start
```
Run the design pipeline on these stakeholder notes:
<paste your notes or attach files>
```
Other ways to start:
- `Start the design pipeline at Phase 3 with this Figma file: <link>`
- `Run Phase 4 of the design pipeline with these MVP results`
- `Use the validator to check this design against our personas and WCAG 2.2 AA`
- `Run the design pipeline in Lite mode on these notes`
- `Create a case study of this project`

## Documentation
- 📘 **[User Guide](plugins/product-design-pipeline/docs/USER-GUIDE.md)**: installation, step-by-step instructions, checkpoints, starting partway, single agents, add-ons, customization, troubleshooting
- 🧩 [Plugin overview](plugins/product-design-pipeline/README.md)
- 📝 [Changelog](CHANGELOG.md)

## The team
| | | |
|---|---|---|
| Research analyst | Product strategist | MVP scope planner |
| System architect | UX designer | Design system designer |
| Content writer | Prototyper | Design critic |
| Validator | Documentation engineer | Measurement planner |
| Build QA analyst | *Add-on:* Localization reviewer | *Add-on:* Privacy & compliance reviewer |
| Case study designer | *Add-on:* Engineering breakdown planner | |

The **orchestrator skill** (`design-pipeline`) leads them all.


## FAQ

### What is the Product Design Pipeline Claude plugin?

Product Design Pipeline is a Claude plugin that orchestrates specialist AI agents across the product design lifecycle, from research and MVP definition through UX/UI design, validation and developer handoff.

### Can Claude Code be used for product design?

Yes. Product Design Pipeline provides a structured product design workflow that can be run through Claude Code using specialist agents and an orchestration skill.

### Is this a UX design agent for Claude?

It is a multi-agent UX and product design workflow rather than a single UX agent. It coordinates research, product strategy, UX design, prototyping, validation, accessibility, design systems and handoff.

### Can it generate a product design case study?

Yes. The pipeline includes a case-study stage that documents research, personas, jobs-to-be-done, journeys, flows and product decisions.

### Does the pipeline support accessibility?

Yes. Accessibility is integrated throughout the workflow with WCAG 2.2 AA requirements, contrast checks, keyboard interaction and ARIA specifications.


## Repository layout
```
.claude-plugin/marketplace.json          makes this repo installable as a marketplace
plugins/product-design-pipeline/
├── .claude-plugin/plugin.json
├── docs/USER-GUIDE.md
├── skills/design-pipeline/
│   ├── SKILL.md                         the orchestrator
│   └── references/                      role briefs, quality gates, entry points, deliverables
└── agents/                              17 agents, generated from the briefs
scripts/build_agents.py                  regenerates the agents from the briefs
```

## Contributing
1. Edit the briefs in `plugins/product-design-pipeline/skills/design-pipeline/references/`.
2. Regenerate the agents with `python3 scripts/build_agents.py`.
3. Bump `version` in `plugins/product-design-pipeline/.claude-plugin/plugin.json` (only there; users receive an update only when this number changes), and add an entry to `CHANGELOG.md`.
4. Open a pull request describing the change and why it helps.

## License
[MIT](LICENSE)

# Product Design Pipeline for Claude

**An MVP-first, accessibility-first product design team for Claude, from stakeholder notes to a validated developer handoff.**

![Version](https://img.shields.io/badge/version-1.2.0-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2%20AA-purple)

Product Design Pipeline is a Claude plugin that runs a complete product design workflow with 14 specialist agents.

It covers research, requirements, MVP scoping, concept testing, design system, content, prototyping, critique, validation, developer handoff, measurement, build QA and a portfolio case study. It stops for your approval at every major decision, and builds WCAG 2.2 AA accessibility into every step.

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

# Product Design Pipeline for Claude

An MVP-first, accessibility-first product design workflow, packaged as a Claude plugin. It includes:
- a skill that runs the whole pipeline;
- 13 specialist agents;
- 3 optional add-ons.

See [the plugin README](plugins/product-design-pipeline/README.md) for the workflow, roles and usage.

## Install

### Claude Code
```
/plugin marketplace add sharadsonkarwork/product-design-pipeline
/plugin install product-design-pipeline@product-design-pipeline
```
Then start with: *"Run the design pipeline on these notes: …"*

### Claude desktop app
Install the `product-design-pipeline.plugin` file from this repo's Releases page, or add this repository as a plugin marketplace if your app or organization supports it.

## Repository layout
```
.claude-plugin/marketplace.json        ← makes this repo installable as a marketplace
plugins/product-design-pipeline/
├── .claude-plugin/plugin.json
├── skills/design-pipeline/
│   ├── SKILL.md                       ← the orchestration lead
│   └── references/
│       ├── working-rules.md, gates.md, entry-points.md, deliverables.md
│       ├── roles/                     ← 13 specialist briefs (single source of truth)
│       └── addons/                    ← 3 optional add-on briefs
└── agents/                            ← 16 agents, generated from the briefs
```

## Contributing
Edit the briefs in `skills/design-pipeline/references/`, then regenerate the agents so both stay in sync:
```
python3 scripts/build_agents.py
```
Bump `version` in both `plugin.json` and `marketplace.json` when you release.

## License
MIT

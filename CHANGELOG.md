# Changelog

All notable changes to this project are documented here. Versions follow [Semantic Versioning](https://semver.org/).

## [1.2.0] - 2026-09-29

### Added
- **Case study designer** agent. It creates a visual, accessible portfolio case study (web page, plus Figma frames when connected) covering the problem statement, research, personas, jobs to be done, journey map, flows, MVP decisions, wireframe-to-design evolution, design system, accessibility, validation, outcomes and learnings. It's offered at Checkpoint 3 and updated with real outcomes in Phase 4.
- **UX-law badges.** A new shared decision log (`05-ux/ux-laws-log.md`) records which Laws of UX shaped each design decision, as it's made. The case study shows these as badges linked to lawsofux.com, and the validator checks a sample against the design. A new `ux-laws.md` reference lists all 30 laws.
- **Anonymised case studies** for NDA work, with a private replacement log.
- **Jobs to be done** in the research report.
- **Run modes:** Lite, Standard (default) and Full.

### Changed (token use)
- Every stage writes a short `summary.md`. Roles read summaries first and open only the sections they need.
- Agents check their own work against the gate. The orchestrator no longer reads full documents.
- References instead of copies, and length limits for every document.
- One fix round by default, for Critical and High issues only.
- A limit on web searches in research. Lite mode uses no web search.
- Model tiers: documentation, measurement, localization and engineering breakdown agents run on a lighter model.
- "One phase per conversation" is now the recommended way to run.
- Chunking is now used only for the two heaviest stages (UX wireframes and the prototype), to avoid timeouts without the extra overhead elsewhere.

## [1.1.0] - 2026-09-27

### Fixed
- Long steps (especially UX) could run past the connection limit and fail with "Claude isn't responding". All heavy stages now run in small chunks, and each file is saved before the next chunk starts.

### Added
- The UX work is split into four steps: UX-1 personas, UX-2 journeys and flows, UX-3 screen index, UX-4 wireframes one flow at a time (up to 8 screens each).
- Wireframes are now a short index (`05-ux/wireframes.md`) plus one file per flow (`05-ux/screens/`). Other roles read only the flows they need.
- Chunk plans for the design system, content, prototype, validation and documentation stages.
- Resume support: "Continue the design pipeline" restarts from the first unfinished chunk, and `Status: Partial` marks unfinished files.
- A troubleshooting entry in the User Guide for the "Claude isn't responding" error.

## [1.0.0] - 2026-09-27

### Added
- `design-pipeline` orchestrator skill:
  - four phases (Define, Concept, Build out MVP, Check & plan);
  - human approval checkpoints;
  - a quality gate for every stage;
  - fix loops;
  - starting at any phase;
  - release cycles.
- 13 specialist agents: research-analyst, product-strategist, mvp-scope-planner, system-architect, ux-designer, design-system-designer, content-writer, prototyper, design-critic, validator, documentation-engineer, measurement-planner, build-qa-analyst.
- 3 optional add-ons: localization-reviewer, privacy-compliance-reviewer, engineering-breakdown-planner.
- MVP scoping with MoSCoW combined with value vs effort.
- WCAG 2.2 AA checks throughout, including the criteria new in 2.2.
- Prototypes in Figma when connected, otherwise accessible HTML.
- User Guide with installation, instructions, customization and troubleshooting.

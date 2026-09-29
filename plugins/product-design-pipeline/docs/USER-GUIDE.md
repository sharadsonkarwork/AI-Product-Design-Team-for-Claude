# Product Design Pipeline: User Guide

**Version 1.2.0**

Everything you need to install, run and customize the Product Design Pipeline plugin for Claude.

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick start](#quick-start)
- [How the pipeline works](#how-the-pipeline-works)
- [Run modes and token use](#run-modes-and-token-use)
- [Instructions](#instructions)
  - [Run the full pipeline](#1-run-the-full-pipeline)
  - [Approve at checkpoints](#2-approve-at-checkpoints)
  - [Start at any phase](#3-start-at-any-phase)
  - [Use a single specialist](#4-use-a-single-specialist)
  - [Turn on add-ons](#5-turn-on-add-ons)
  - [Plan the next release](#6-plan-the-next-release)
  - [Create a case study](#7-create-a-case-study)
- [What you get](#what-you-get)
- [Tips for better results](#tips-for-better-results)
- [Customizing the plugin](#customizing-the-plugin)
- [Troubleshooting and FAQ](#troubleshooting-and-faq)
- [Limitations](#limitations)

---

## Description

**Product Design Pipeline** turns Claude into a complete product design team that works MVP-first and accessibility-first.

You give it stakeholder notes, a brief or an idea. It takes the product through:
- research;
- requirements;
- MVP scoping;
- a quick concept test;
- detailed design;
- validation;
- developer handoff;
- a portfolio case study.

After launch, it helps you judge the results and plan the next release. It stops for your approval at every major decision, so nothing expensive gets built on unapproved work.

### Why MVP-first
Designing the entire product before anyone checks the scope is costly: if the direction is wrong, all of that work is lost. This pipeline:
1. decides the smallest valuable release;
2. tests a cheap concept of it with your personas;
3. invests in detailed design only after the concept passes;
4. after launch, compares real results with the targets set at the start, then plans what comes next.

### What's included

| Component | Count | Purpose |
|---|---|---|
| Orchestrator skill (`design-pipeline`) | 1 | Runs the workflow. It plans, delegates, checks quality, runs fix loops and stops at checkpoints. |
| Specialist agents | 14 | Research, strategy, MVP scoping, architecture, UX, design system, content, prototyping, critique, validation, documentation, measurement, build QA, case study |
| Optional add-on agents | 3 | Localization, privacy and compliance, engineering breakdown |

### Who it's for
- Product designers and UX leads who want a structured, repeatable process.
- Product managers who need an MVP scope that holds up to scrutiny.
- Founders and small teams without a full design team.
- Design system and accessibility specialists who want WCAG 2.2 AA built in from the start.

### Standards built in
- WCAG 2.2 Level AA, including the new 2.2 criteria: 2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7 and 3.3.8.
- Nielsen's 10 usability heuristics.
- Hick's, Fitts's, Jakob's and Miller's laws.
- Semantic design tokens in the W3C Design Tokens format, with light and dark themes.
- WAI-ARIA Authoring Practices for component behavior.
- MoSCoW combined with value vs effort for prioritization.

---

## Requirements

- **Claude:**
  - the Claude desktop app, on a plan that supports plugins and skills; or
  - Claude Code.
- **Optional connections** that make the output richer:
  - **Figma:** prototypes and design system components are built in Figma instead of HTML.
  - **A document tool** such as Google Drive, Notion or Confluence: approval packs and documents can be published there.
  - **A project tracker** such as Jira, Linear, Asana or GitHub Issues: the engineering breakdown add-on can create tickets there.

None of these are required. Without them, the pipeline produces HTML prototypes, and documents in the richest format your environment supports, with Markdown files as the fallback.

---

## Installation

Choose the method that matches how you use Claude.

### Option A: Claude desktop app (plugin file)
1. Download `product-design-pipeline.plugin` from the repository's **Releases** page, or get the file from whoever shared it with you.
2. Drop the file into a Claude conversation, or open it with the Claude desktop app.
3. Review the plugin's skills and agents in the preview, then click the button to install it.
4. Start a new conversation and check it's working. Type:
   > What does the product design pipeline do?

   Claude should describe the four phases.

### Option B: Claude Code (from GitHub)
Run these commands inside Claude Code:
```
/plugin marketplace add <github-username>/product-design-pipeline
/plugin install product-design-pipeline@product-design-pipeline
```
Restart Claude Code if it asks you to. Then check the install:
```
/plugin      → the plugin should be listed as installed and enabled
/agents      → the 17 agents should appear, prefixed "product-design-pipeline:"
```

### Option C: Claude Code (from a local folder)
Useful if you've downloaded or modified the repository:
```
/plugin marketplace add /path/to/product-design-pipeline
/plugin install product-design-pipeline@product-design-pipeline
```

### Option D: Manual install without the plugin system (Claude Code)
Copy the files into your project, or into your home folder to use them in every project:

| Copy this | To (one project) | Or to (all projects) |
|---|---|---|
| `plugins/product-design-pipeline/skills/design-pipeline/` | `<project>/.claude/skills/design-pipeline/` | `~/.claude/skills/design-pipeline/` |
| `plugins/product-design-pipeline/agents/*.md` | `<project>/.claude/agents/` | `~/.claude/agents/` |

Folders starting with a dot are hidden. Show them with **Cmd + Shift + .** in the macOS Finder, or `ls -a` in a terminal.

### Updating
Plugins don't update themselves unless you turn that on.

- **Claude Code, automatic (recommended):** run `/plugin`, open **Marketplaces**, select **product-design-pipeline**, and choose **Enable auto-update**. New releases then arrive in the background after a session starts.
- **Claude Code, manual:** run `/plugin marketplace update product-design-pipeline` in a session, or `claude plugin update product-design-pipeline@product-design-pipeline` in your terminal.
- **Plugin file (desktop app):** a `.plugin` file is a snapshot and never updates. Install the newer file from the Releases page; it replaces the old version.
- **Teams:** an admin can turn on auto-update for everyone, or distribute the plugin through the organization's plugin settings on claude.ai.

You only receive an update when the plugin's version number changes. Check the [Changelog](../../../CHANGELOG.md) to see what's new.

### Uninstalling
- **Claude Code:** `/plugin uninstall product-design-pipeline@product-design-pipeline`
- **Desktop app:** remove the plugin from your installed plugins or skills list in settings.

Your `design-workspace/` folders are never deleted when you uninstall.

---

## Quick start

Paste your notes after one of these prompts:

```
Run the design pipeline on these stakeholder notes:
<paste notes, or attach files>
```

Claude will then:
1. ask up to one short round of questions (platform, audience, regions, languages, an existing design system, Figma or HTML);
2. write a plan and tell you where the first checkpoint is;
3. run Phase 1 and stop at **Checkpoint 1** with an MVP scope for you to approve.

In Claude Code you can also call the skill directly:
```
/product-design-pipeline:design-pipeline <your notes or file path>
```

---

## How the pipeline works

```
PHASE 1  DEFINE          Research → Strategy → Effort estimates → MVP scope
                         🔒 Checkpoint 1: approve MVP scope

PHASE 2  CONCEPT         UX flows → Draft copy → Concept prototype → Concept validation
                         🔒 Checkpoint 2: approve concept

PHASE 3  BUILD OUT MVP   Detailed UX → (Architecture ∥ Design system ∥ Final copy)
                         → Hi-fi prototype → Critique → Validation → fix loop
                         → (Developer handoff ∥ Measurement plan)
                         🔒 Checkpoint 3: approve for development

   … your team builds the MVP …

PHASE 4  CHECK & PLAN    Build QA → Real-user results → Go / Iterate / Pivot
                         🔒 Checkpoint 4: release decision → next release
```
`∥` = these run at the same time.

### The team

| Agent | Phase(s) | What it produces |
|---|---|---|
| research-analyst | 1, 4 | Research report, competitor analysis, riskiest assumptions; usability test plan and synthesis of results |
| product-strategist | 1 | Problem statement, goals, non-goals, traceable requirements, feature list |
| mvp-scope-planner | 1, 4 | Feature scoring, MVP scope with hypotheses and go / no-go criteria, Next / Later backlog; go / iterate / pivot decision |
| system-architect | 1, 3 | Effort estimates; technical design |
| ux-designer | 2, 3 | Personas, journey maps, task flows, wireframes with accessibility annotations |
| design-system-designer | 3 | Design tokens (light and dark themes, checked contrast), component specs with all states |
| content-writer | 2, 3 | Content guide, copy deck, content audit (grammar, tone, accessibility, AI-sounding text removed) |
| prototyper | 2, 3 | Concept prototype; high-fidelity MVP prototype (Figma or HTML) |
| design-critic | 3 | Structured design critique |
| validator | 2, 3 | Persona walkthroughs, WCAG 2.2 AA results, heuristic scores |
| documentation-engineer | 3 | Developer guide, component specs, handoff checklist |
| measurement-planner | 3 | Metrics tree, analytics event plan, evaluation plan |
| build-qa-analyst | 4 | Comparison of the built product with the design, and an accessibility check of the build |
| case-study-designer | 3, 4 | Visual portfolio case study with UX-law badges; optional anonymised version |

### How MVP scoping works
Every feature gets:
1. a **MoSCoW** category (Must, Should, Could, Won't this release);
2. a **value** score from 1 to 5, averaging user value and business value;
3. an **effort** score from 1 to 5, from the architect's estimate.

Each feature then lands in one quadrant:

| | Low effort | High effort |
|---|---|---|
| **High value** | Quick win | Big bet |
| **Low value** | Fill-in | Money pit |

The **MVP** is every Must, plus any Should that is a Quick win if there's room. A Must that lands in the Money pit gets challenged: is there a simpler version with the same outcome? Everything else goes into the **Next / Later backlog**, with the reason it was deferred and what would bring it forward.

---

## Run modes and token use

A full design pipeline is a lot of work, so it uses a lot of tokens. Version 1.2.0 cuts that down in three ways.

### 1. Pick a run mode at intake

| Mode | Best for | What's different |
|---|---|---|
| **Lite** | Small features, quick explorations | No concept prototype (Phase 2 validates the wireframes). Critique is merged into validation. No measurement plan. No web search in research. No add-ons. |
| **Standard** (default) | Most products | Every core stage. Add-ons only when relevant. |
| **Full** | High-stakes launches | Standard plus every relevant add-on, and a second fix round if needed. |

Say it in your first message, for example "Run the design pipeline in Lite mode". You can switch at any checkpoint.

### 2. Built-in savings (always on)
- **One-page summaries.** Every stage writes a short `summary.md`. Later agents read the summaries and open only the sections they need.
- **Self-checking.** Each agent checks its own work against the quality gate and reports pass or fail item by item. The orchestrator no longer re-reads whole documents.
- **References instead of copies.** Documents cite IDs (FR-03, SC-07) instead of repeating earlier tables.
- **Length limits** for every document.
- **One fix round by default,** for Critical and High issues only.
- **A limit on web searches** during research.
- **Model tiers.** Mechanical roles (documentation, measurement, localization, engineering breakdown) run on a lighter model. Judgment-heavy roles use your main model. Tiers apply when the named agents are available.

### 3. Your habits (the biggest saver)
- **Start a new conversation for each phase.** After approving a checkpoint, open a new conversation with the same folder and say **"Continue the design pipeline"**. Each phase then starts small instead of carrying everything before it.
- **Run only what you need.** Use a single specialist or start at a later phase when you already have the earlier work.
- **Check where tokens went.** After a run, ask Claude to "explain my usage" to see which steps cost the most.

---

## Instructions

### 1. Run the full pipeline
1. Start a conversation, or a Claude Code session in your project folder.
2. Share your input. Anything helps:
   - stakeholder notes, meeting transcripts or a brief;
   - existing research: interviews, surveys, support tickets, analytics;
   - a brand guide or an existing design system;
   - constraints such as timeline, team size, tech stack or regions.
3. Say **"Run the design pipeline"**.
4. Answer the intake questions, or reply **"use your best judgment"** and Claude will record its assumptions.
5. Review each checkpoint pack and reply with your decision (see below).

Long projects can run across several sessions. The `design-workspace/` folder holds all the state, so in a new session say:
> Continue the design pipeline from where we left off.

### 2. Approve at checkpoints
At each 🔒 checkpoint, Claude stops and shows a short approval pack. Reply with one of the following:

| Reply | What happens |
|---|---|
| **Approve** | The next phase starts. |
| **Approve with changes:** *list them* | The changes are made, then the next phase starts. |
| **Send back to** *stage*: *reason* | That stage is redone with your feedback, then you're asked again. |

Every decision is logged in `design-workspace/00-orchestration/decisions-log.md`. Claude never approves its own work. If no one responds, it waits at the checkpoint.

### 3. Start at any phase
Bring what you already have and name the phase:

| You have | Say |
|---|---|
| A PRD or an agreed feature list | "Start the design pipeline at Phase 2 with this PRD." |
| Approved wireframes, a Figma file, or an existing app to redesign | "Start the design pipeline at Phase 3 with this Figma file: <link>." |
| A built MVP, analytics or usability results | "Run Phase 4 of the design pipeline with these results." |

Claude maps your material to what the phase needs and quickly fills in any gaps, marked `Backfilled` with assumptions listed. It then asks you to confirm before continuing.

### 4. Use a single specialist
You don't have to run the whole pipeline. Ask for one role:

| Task | Example prompt |
|---|---|
| Scope an MVP | "Use the mvp-scope-planner to decide what goes in the MVP from this feature list." |
| Build a design system | "Use the design-system-designer to create tokens and components for these screens." |
| Write or audit copy | "Use the content-writer to audit this copy and remove anything that sounds AI-written." |
| Critique a design | "Use the design-critic to review this prototype." |
| Validate against personas and WCAG | "Use the validator to check this design against our personas and WCAG 2.2 AA." |
| Plan analytics | "Use the measurement-planner to plan how we'll measure this MVP." |
| QA a build | "Use the build-qa-analyst to check the staging site against our designs: <URL>." |

In Claude Code, the agents show as `product-design-pipeline:<name>`. You can also pick one from `/agents`.

### 5. Turn on add-ons
Claude suggests add-ons during intake when they're relevant. You can also ask for them directly:
- **Localization:** "We're launching in Germany and Saudi Arabia." Checks text expansion, right-to-left layouts and locale formats.
- **Privacy and compliance:** "This handles health data in the EU and US." Covers the data inventory, consent, dark patterns and user rights, and lists questions for legal review.
- **Engineering breakdown:** "Break the handoff into Jira tickets." Produces epics and stories with acceptance criteria, and creates them in a connected tracker if you ask.

### 6. Plan the next release
After the MVP ships:
1. Share the build (a URL or the repository) and any results: analytics, test notes, feedback.
2. Say **"Run Phase 4 of the design pipeline."**
3. Claude:
   - runs build QA;
   - writes a usability test plan if you don't have results yet;
   - compares results with the go / no-go criteria;
   - recommends **Go**, **Iterate** or **Pivot**.
4. At Checkpoint 4, what happens next depends on your decision:
   - **Go:** the release is archived and Phase 2 starts for the next scope. Personas, the design system and the architecture are reused.
   - **Iterate:** you go back to the phase that owns the fixes.
   - **Pivot:** you return to Phase 1.

### 7. Create a case study
At **Checkpoint 3**, Claude offers to create a portfolio case study. You can also ask at any time: **"Create a case study of this project."**

It asks for a few details first:
- your role, the team, the timeline and the tools used;
- what to emphasise;
- which screens to feature;
- whether you need an **anonymised version**.

**What you get** (in `design-workspace/15-case-study/`):
- **A web page** (`case-study.html`): one accessible, self-contained page you can publish, share, or export to PDF.
- **Figma frames** of the case study, if Figma is connected.
- **An anonymised version**, if you ask. It replaces client, product and people names, removes internal data, and turns real metrics into relative values. It shows a visible confidentiality note. A private `anonymisation-log.md` records what was replaced; keep it to yourself.

**What it covers:**
1. Overview
2. Problem statement
3. Research
4. Personas
5. Jobs to be done
6. Journey map with an emotion curve
7. User flows and information architecture
8. MVP decisions on a value-vs-effort grid
9. From wireframe to design
10. Design system snapshot
11. Accessibility
12. UX laws applied
13. Validation
14. Outcomes
15. Learnings and next steps

**UX-law badges:** while designing, the UX designer, design system designer and content writer log each decision with the law it applies. For example:
- a full-width primary button → **Fitts's Law**;
- a standard checkout pattern → **Jakob's Law**.

The case study shows these as badges next to the relevant screen or section. Each badge links to the law's page on [lawsofux.com](https://lawsofux.com/) and has a visible one-line note on how it was applied. There's also an index of every law used. Only decisions that were actually logged get a badge, and the validator checks a sample of them against the design.

After Phase 4, Claude offers to add the real outcomes. Until then, the Outcomes section is marked **"Outcomes pending"**. It never invents metrics, quotes or results.

---

## What you get

All working files are saved in `design-workspace/` in your project or conversation. Every folder also has a short `summary.md`, and `05-ux/ux-laws-log.md` records which UX law shaped which decision.

```
design-workspace/
├── 00-orchestration/   plan, status, decisions log, checkpoint packs
├── 01-research/        research report
├── 02-strategy/        requirements
├── 03-mvp-scope/       feature scoring, MVP scope, backlog
├── 04-architecture/    effort estimates, technical design
├── 05-ux/              personas, journeys, screen index, screens/ (one file per flow)
├── 06-design-system/   tokens (.md + .json), components
├── 07-content/         content guide, copy deck, content audit
├── 08-prototype/       concept and MVP prototypes
├── 09-critique/        critique report
├── 10-validation/      concept and MVP validation reports
├── 11-handoff/         developer guide, component specs, handoff checklist
├── 12-measurement/     measurement plan
├── 13-build-qa/        build QA report
├── 14-mvp-results/     usability test plan, results, go / no-go
├── 15-case-study/      case study page, anonymised version, Figma link
├── addons/             localization, privacy, engineering breakdown
└── _archive/           previous releases
```

For stakeholders, Claude uses the richest format your environment supports:
- a slide deck or documents for checkpoint packs;
- a Figma file or a clickable HTML page for prototypes;
- a web page (plus Figma frames) for the case study;
- plain Markdown as the fallback.

---

## Tips for better results

- **Give real evidence.** Interview notes, support tickets or analytics make personas and scope far more reliable. Without them, the pipeline marks its personas as assumptions, which is fine for a start but worth fixing.
- **Name your constraints early:** deadline, team size, tech stack, regions and languages. They change the MVP line.
- **Share your existing design system or Figma library** so it gets extended rather than replaced.
- **Be specific when sending work back.** "Merge onboarding steps 2 and 3 and drop the tour" works better than "make onboarding simpler".
- **Run one phase per session** for large products. It keeps each session focused, and the workspace carries everything forward.
- **Treat the approval pack as the meeting agenda.** Share it with stakeholders before you approve.

---

## Customizing the plugin

All role instructions live in one place:
```
plugins/product-design-pipeline/skills/design-pipeline/references/
├── working-rules.md        rules every role follows
├── gates.md                quality checks for each stage
├── entry-points.md         starting partway and release cycles
├── deliverables.md         file layout and output formats
├── ux-laws.md              the Laws of UX list used for decision logging
├── roles/                  the 14 specialist briefs
└── addons/                 the 3 add-on briefs
```

Common changes:

| To change | Edit |
|---|---|
| Your brand voice or house style | `roles/content-writer.md` |
| Scoring method or MVP rule | `roles/mvp-scope-planner.md` and `gates.md` |
| Platform guidelines (Material, Apple's HIG) | `roles/ux-designer.md` and `roles/design-system-designer.md` |
| Which checkpoints stop for approval | the Checkpoints section of `SKILL.md` |
| Default breakpoints, token format or tech stack | the relevant role brief |
| Which agents use a lighter model | the `LIGHT` list in `scripts/build_agents.py` |
| Length limits per document | the "Length limits" section of each role brief |

After editing a brief, regenerate the agents so they match:
```
python3 scripts/build_agents.py
```
Then bump `version` in `plugin.json` (only there), and reinstall or update. Users only receive a release when this number changes.

---

## Troubleshooting and FAQ

**"Claude isn't responding. New messages won't be sent unless it reconnects."**
The app lost contact with the session during a long step, so retrying the same message runs the same long step again. Since version 1.1.0 the heaviest steps run in small chunks and saves after each one, so little work is lost. To recover:
1. Wait a few minutes. If the message stays, start a **new conversation** and add the same project folder.
2. Say: **"Continue the design pipeline."** It reads `design-workspace/00-orchestration/status.md` and resumes from the first unfinished chunk.
3. If it keeps happening, run one phase or one step per conversation, for example "Continue the design pipeline: do UX-4 for flow FL-02 only."

**The pipeline doesn't start when I paste notes.**
Say it explicitly: "Use the design-pipeline skill on these notes." In Claude Code, run `/product-design-pipeline:design-pipeline`.

**The agents don't appear in `/agents`.**
Check that the plugin shows as enabled in `/plugin`, then restart Claude Code. If you installed manually, check that the files are directly inside `.claude/agents/`, not in a subfolder.

**Will it work without the agents?**
Yes. If specialist agents aren't available, the orchestrator does each step itself, following the same role briefs. The results are the same; the run just takes longer and happens in one thread.

**Why did it stop?**
It has most likely reached a checkpoint and is waiting for your decision; see [Approve at checkpoints](#2-approve-at-checkpoints). If it says a stage is **Blocked**, it lists the missing input or access it needs.

**It built the prototype in HTML, but I wanted Figma.**
Connect Figma, then say "Rebuild the prototype in Figma."

**Can I skip the concept phase?**
Yes. Say "Skip Phase 2" or start at Phase 3. You lose the cheap early check, so the risk of rework later goes up.

**How much does a full run cost in usage?**
A full run is a long, multi-step job. See [Run modes and token use](#run-modes-and-token-use). The biggest savings come from Lite mode for small work, and from starting a new conversation for each phase.

**Where are my files?**
- In Claude Code: in `design-workspace/` in your project folder.
- In the desktop app: attached to the conversation, or in the folder you connected.

---

## Limitations

- **Design validation isn't user testing.** The validator checks designs against personas and standards. Real validation needs real users, so Phase 4 plans that testing and waits for your results. It never makes up results.
- **Automated accessibility checks have limits.** Screen reader behavior and some WCAG criteria must be checked by a person on the real build. These are marked **Verify in build**.
- **Privacy review isn't legal advice.** The add-on flags risks and questions for your legal team.
- **Effort estimates are rough sizes** for prioritization, not delivery commitments.

---

License: MIT · Contributions welcome. See the repository README.

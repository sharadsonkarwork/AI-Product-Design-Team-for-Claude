# Product Design Pipeline

An MVP-first product design workflow for Claude. Give it stakeholder notes, and it takes the product through research, MVP scoping, concept testing, detailed design, validation, and developer handoff. It stops for your approval at every major decision. WCAG 2.2 AA accessibility is built into every step.

## Why MVP-first
Designing the whole product before anyone checks the scope is expensive. This pipeline:
1. scopes the smallest valuable release;
2. tests a cheap concept of it;
3. invests in detailed design only after the concept passes;
4. after launch, checks real results before planning what's next.

## The workflow

```
PHASE 1  DEFINE          Research → Strategy → Effort estimates → MVP scope
                         🔒 Checkpoint 1: approve MVP scope
PHASE 2  CONCEPT         UX flows → Draft copy → Concept prototype → Concept validation
                         🔒 Checkpoint 2: approve concept
PHASE 3  BUILD OUT MVP   Detailed UX → (Architecture ∥ Design system ∥ Final copy)
                         → Hi-fi prototype → Critique → Validation → fix loop
                         → (Developer handoff ∥ Measurement plan)
                         🔒 Checkpoint 3: approve for development
PHASE 4  CHECK & PLAN    Build QA → Real-user results → Go / Iterate / Pivot
                         🔒 Checkpoint 4: release decision → next release
```

You can start at **any phase**. Bring an existing PRD, wireframes, a Figma file or MVP results, and the pipeline fills in what it needs, then confirms its assumptions with you before continuing. You can also run a **single role**, for example "critique this design" or "audit this copy".

## The team

| Role | What it does |
|---|---|
| **Orchestration lead** (the `design-pipeline` skill) | Plans the work, delegates, checks every output against quality gates, runs fix loops, and stops at checkpoints |
| Research analyst | Turns research into evidence; competitor analysis; riskiest assumptions; usability test plans; synthesis of MVP results |
| Product strategist | Problem, goals, non-goals, and traceable requirements with measurable metrics |
| MVP scope planner | MoSCoW + value vs effort scoring, MVP hypotheses, go / no-go criteria, Next / Later backlog, re-planning after launch |
| System architect | Effort estimates, then the technical design for the MVP |
| UX designer | Personas (including people with disabilities), journeys, flows, wireframes |
| Design system designer | Semantic tokens (light and dark themes, checked contrast) and accessible components with every state |
| Content writer | All product copy, voice and tone; audits grammar, spelling and accessibility; removes AI-sounding text |
| Prototyper | Clickable prototypes, in Figma when connected, otherwise accessible HTML |
| Design critic | Structured critique of hierarchy, consistency and craft |
| Validator | Persona walkthroughs, full WCAG 2.2 AA check, heuristic scoring |
| Documentation engineer | Developer guide, component specs, handoff checklist |
| Measurement planner | Metrics tree, analytics events, and how to judge the go / no-go criteria |
| Build QA analyst | Checks the built product against the design and WCAG 2.2 AA |

**Optional add-ons** (switched on at intake when they're relevant):
- Localization reviewer
- Privacy & compliance reviewer
- Engineering breakdown planner, which can create tickets in a connected tracker

## How to use it
Say something like:
- "Run the design pipeline on these stakeholder notes: …"
- "Start the design pipeline at Phase 3 with this Figma file."
- "Here are our MVP results. Run Phase 4 and tell us what to build next."
- "Use the validator to check this prototype against our personas."

All working files go into a `design-workspace/` folder. At each checkpoint you get a short approval pack: a slide deck or document where your environment supports one, or a web page or Markdown file where it doesn't.

## Standards
- WCAG 2.2 Level AA, including 2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7 and 3.3.8
- Nielsen's 10 heuristics
- Hick's, Fitts's, Jakob's and Miller's laws
- W3C design token format
- WAI-ARIA Authoring Practices
- MoSCoW with value vs effort prioritization

## Limits
- The validator tests designs against personas and standards. It doesn't replace testing with real users, so Phase 4 plans that testing and waits for real results.
- The privacy reviewer flags risks. It isn't legal advice.

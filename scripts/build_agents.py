import os, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "plugins/product-design-pipeline"
REF = P/"skills/design-pipeline/references"
rules = (REF/"working-rules.md").read_text()

A = {
 "research-analyst": ("roles","cyan",
  "Use this agent for user and market research in the design pipeline: synthesizing stakeholder notes, interviews, surveys, reviews or analytics into evidence-based user segments, competitor analysis and riskiest assumptions (Phase 1), or writing a usability test plan and synthesizing real MVP results (Phase 4).",
  [("User shares interview notes and competitor links", "Turn these into insights before we write requirements", "I'll use the research-analyst agent to synthesize the evidence and map competitors."),
   ("MVP has launched and the user has test notes", "Here are our usability test results for the MVP", "I'll use the research-analyst agent to synthesize the results against the MVP hypotheses.")]),
 "product-strategist": ("roles","blue",
  "Use this agent to turn stakeholder notes and research into a problem statement, goals, non-goals and a traceable requirements table with measurable success metrics, grouped into features for MVP scoping.",
  [("User pastes notes from a stakeholder meeting", "Can you turn these notes into proper requirements?", "I'll use the product-strategist agent to produce traceable requirements and a feature list.")]),
 "mvp-scope-planner": ("roles","green",
  "Use this agent to decide what goes into the MVP versus later releases using MoSCoW plus value vs effort scoring, write testable hypotheses and go / no-go criteria, and maintain the Next / Later backlog. Also use it after MVP results arrive to make the go / iterate / pivot call and re-plan.",
  [("Requirements exist with effort estimates", "What should be in the MVP and what can wait?", "I'll use the mvp-scope-planner agent to score every feature and draw the MVP line."),
   ("User has MVP metrics", "Did the MVP work? What do we build next?", "I'll use the mvp-scope-planner agent to check the go / no-go criteria and re-plan the backlog.")]),
 "system-architect": ("roles","blue",
  "Use this agent for technical work in the design pipeline: rough effort sizing of features before MVP scoping (Phase 1), or the high-level technical design for the approved MVP, covering components, data model, APIs, front-end and token architecture, NFRs, ADRs and risks (Phase 3).",
  [("Feature list exists, MVP not yet scoped", "How big is each of these features to build?", "I'll use the system-architect agent to size each feature and flag technical risks."),
   ("Concept is approved", "Now we need the technical design for the MVP", "I'll use the system-architect agent to produce the technical design.")]),
 "ux-designer": ("roles","magenta",
  "Use this agent to create personas (including people with disabilities), journey maps, task flows, information architecture and wireframes: low fidelity for a concept (Phase 2) or detailed, responsive and fully annotated for accessibility (Phase 3).",
  [("MVP scope is approved", "Map the personas and user journeys and sketch the screens", "I'll use the ux-designer agent to build personas, journeys and concept wireframes.")]),
 "design-system-designer": ("roles","magenta",
  "Use this agent to build or extend a design system: three-tier semantic design tokens with light and dark themes and verified contrast, type and spacing scales, motion with reduced-motion rules, and accessible components with every interaction state, keyboard behavior and ARIA semantics.",
  [("Detailed wireframes list the components needed", "Create the tokens and component specs for this product", "I'll use the design-system-designer agent to define the tokens and components."),
   ("User has an existing Figma library", "Extend our design system for the new screens", "I'll use the design-system-designer agent to extend the existing system rather than replace it.")]),
 "content-writer": ("roles","magenta",
  "Use this agent to write all product copy (UI microcopy, errors, empty states, onboarding, alt text, page titles) and to audit copy for content principles, voice and tone, grammar, spelling, accessibility, and AI-sounding text, which it rewrites or removes.",
  [("Wireframes have copy slots", "Write the copy for these screens", "I'll use the content-writer agent to fill every copy slot."),
   ("User pastes existing product copy", "Check this copy, it sounds like AI wrote it", "I'll use the content-writer agent to audit it and rewrite the AI-sounding parts.")]),
 "prototyper": ("roles","magenta",
  "Use this agent to build clickable prototypes from wireframes, tokens and copy: a quick low-fidelity concept prototype (Phase 2) or a high-fidelity, token-based, accessible MVP prototype (Phase 3), in Figma when connected or otherwise as a self-contained HTML file.",
  [("Concept wireframes and draft copy exist", "Make this clickable so we can test the flow", "I'll use the prototyper agent to build a concept prototype of the primary flows.")]),
 "design-critic": ("roles","yellow",
  "Use this agent for a structured design critique of a high-fidelity design or prototype: visual hierarchy, layout rhythm, typography, color, consistency with the design system, interaction quality and heuristics. It reports issues with severity and owner; it does not redesign.",
  [("High-fidelity prototype is ready", "Review this design before we validate it", "I'll use the design-critic agent to run a structured critique.")]),
 "validator": ("roles","yellow",
  "Use this agent to independently validate designs: persona cognitive walkthroughs on the prototype, hypothesis and requirement traceability, a full WCAG 2.2 AA check with computed contrast, and Nielsen heuristic scoring. Reports issues with evidence, severity and owner; never edits design files.",
  [("Concept prototype is ready", "Does this concept actually work for our personas?", "I'll use the validator agent to run persona walkthroughs on the concept."),
   ("Final MVP design is ready", "Validate the design against WCAG 2.2 and our personas", "I'll use the validator agent for the full MVP validation.")]),
 "documentation-engineer": ("roles","green",
  "Use this agent after validation to produce developer handoff documentation: a developer guide, component specs with props, states, keyboard and ARIA details, and an engineering and design QA checklist.",
  [("MVP design passed validation", "Prepare the handoff for developers", "I'll use the documentation-engineer agent to write the developer guide and component specs.")]),
 "measurement-planner": ("roles","cyan",
  "Use this agent to plan how the MVP's success will be measured: metrics tree, metric definitions with targets, guardrails, funnels, an analytics event taxonomy tied to hypotheses and go / no-go criteria, and privacy rules for tracking.",
  [("MVP scope has hypotheses", "How will we know if the MVP worked?", "I'll use the measurement-planner agent to build the measurement plan and event taxonomy.")]),
 "build-qa-analyst": ("roles","red",
  "Use this agent after developers build the MVP to check the real build against the approved design: design fidelity, token use, copy accuracy, WCAG 2.2 AA on the live product, analytics events and performance budgets, ending with a release recommendation.",
  [("Staging build is available", "QA the build against the designs before we launch", "I'll use the build-qa-analyst agent to check design fidelity and accessibility on the build.")]),
 "case-study-designer": ("roles","magenta",
  "Use this agent to create a visual, portfolio-ready case study of a design project from the design workspace: problem statement, research, personas, jobs to be done, journey map, flows, MVP decisions, wireframe-to-design evolution, design system, accessibility, validation and outcomes, with UX-law badges linked to lawsofux.com. It can also produce an anonymised version for NDA work.",
  [("MVP design is approved for development", "Create a case study of this project for my portfolio", "I'll use the case-study-designer agent to build the case study from the workspace."),
   ("Project is under NDA", "Make an anonymised version of the case study", "I'll use the case-study-designer agent to create an anonymised version and keep a private replacement log.")]),
 "localization-reviewer": ("addons","cyan",
  "Optional add-on. Use this agent when a product ships in multiple languages or regions, to check text expansion, right-to-left layouts, locale formats, translatable copy, language markup and cultural fit.",
  [("Product will launch in Germany and the UAE", "Check the design is ready for German and Arabic", "I'll use the localization-reviewer agent to check expansion, RTL and locale formats.")]),
 "privacy-compliance-reviewer": ("addons","red",
  "Optional add-on. Use this agent when a product handles personal, financial, health or children's data or is in a regulated sector, to flag likely frameworks, data minimization, consent, dark patterns, user rights and security-sensitive UX, with items for legal review.",
  [("Health app handling patient data", "Are there privacy issues with this design?", "I'll use the privacy-compliance-reviewer agent to review data, consent and compliance risks.")]),
 "engineering-breakdown-planner": ("addons","green",
  "Optional add-on. Use this agent after handoff to break the MVP into epics and user stories with Given/When/Then acceptance criteria including accessibility and analytics, estimates, build order, and optionally create them in a connected project tracker.",
  [("Handoff is approved", "Break this into Jira tickets for the team", "I'll use the engineering-breakdown-planner agent to create epics and stories.")]),
}

LIGHT = {"documentation-engineer","measurement-planner","localization-reviewer","engineering-breakdown-planner"}
LAWS = {"ux-designer","design-system-designer","content-writer","design-critic","validator","case-study-designer"}
laws = (REF/"ux-laws.md").read_text().strip()
out = P/"agents"
for old in out.glob("*.md"): old.unlink()
for name,(folder,color,desc,exs) in A.items():
    body = (REF/folder/f"{name}.md").read_text().strip()
    ex = "\n\n".join(
      f"<example>\nContext: {c}\nuser: \"{u}\"\nassistant: \"{a}\"\n</example>" for c,u,a in exs)
    fm = f"---\nname: {name}\ndescription: >-\n  {desc}\n\n" + "\n".join("  "+l if l else "" for l in ex.splitlines()) + f"\nmodel: {'sonnet' if name in LIGHT else 'inherit'}\ncolor: {color}\n---\n\n"
    tail = "\n\n---\n\n" + rules.strip().replace("# Working rules for every role", "# Working rules") + "\n"
    if name in LAWS:
        tail += "\n---\n\n" + laws + "\n"
    (out/f"{name}.md").write_text(fm + body + tail)
print(len(list(out.glob('*.md'))), "agents")

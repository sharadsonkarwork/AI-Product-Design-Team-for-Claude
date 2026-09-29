# Quality gates

Each role reports its own pass or fail on every gate item in its return (the gate self-check). The orchestrator gates on that self-check and the stage's `summary.md`, and opens a full file only to spot-check a failed or doubtful item. A gate passes only when every line is true, or the exception is recorded as an open issue with an owner.

**Every stage:** `summary.md` exists (≤ about 40 lines) and is accurate; the output stays within the brief's length limits; upstream content is referenced by ID, not copied.

**In Lite mode:** skip the gates for stages Lite doesn't run. The Phase 2 validation runs on the wireframes, and the Phase 3 validation also covers the critique categories.

## Phase 1: Define
| Stage | Gate |
|---|---|
| Research (A) | Every theme cites evidence and a confidence level; 3–6 competitors analyzed; segments include access needs; 2–4 evidence-linked jobs to be done per segment; web searches within the run-mode limit; riskiest assumptions ranked with a test method; if no user research was supplied, that's stated at the top. |
| Strategy | Problem, goals, non-goals present; every requirement has an ID, type, user story, measurable metric, and source; NFRs cover accessibility (WCAG 2.2 AA), performance, security/privacy, localization, devices, reliability; requirements grouped into features F-xx; no prioritization done here. |
| Architect (A) | Every feature has an effort size and score, drivers, dependencies, risk; L/XL features have a simpler alternative. |
| MVP scope (A) | Every feature has MoSCoW, user and business value, effort, quadrant, decision, reason; MVP = all Musts + chosen Shoulds; Money-pit Musts challenged; the MVP forms a complete journey for the primary persona; each in-scope feature has a hypothesis; 3–6 measurable go / no-go criteria with data sources; every deferred feature is in Next or Later with a reason. |

## Phase 2: Concept
| Stage | Gate |
|---|---|
| UX (A) | `wireframes.md` index lists every screen and every flow has a file in `05-ux/screens/`; no file left `Status: Partial`; 2–4 personas, at least one with an access need; every persona has at least one journey; flows include error and empty paths and trace to the jobs to be done; meaningful decisions logged in `ux-laws-log.md`; every MVP feature appears on at least one screen; copy slots marked; nothing out of scope designed. |
| Content (A) | Every copy slot on the primary flows has draft copy; no placeholder text. |
| Prototype (A) | Every primary MVP flow clickable end to end, with at least one error path and one empty state; draft copy used; keyboard operable; `prototype.md` lists coverage and limits. |
| Validation (A) | A verdict per persona goal; each MVP hypothesis confirmed testable; early accessibility red flags listed; overall verdict Proceed / Proceed with changes / Rethink. |

## Phase 3: Build out the MVP
| Stage | Gate |
|---|---|
| UX (B) | Concept-validation issues owned by UX resolved or explained; every screen has all states and all three breakpoints; accessibility annotations per screen; decisions logged in `ux-laws-log.md` with exact law names. |
| Architect (B) | Components, data model, APIs, NFRs, ADRs, risks, extensibility for the backlog, requirement → component traceability; flags any infeasible UX. |
| Design system | Three token tiers; light and dark themes; every text/background and UI pair has a computed contrast ratio that passes; focus style meets 3:1; reduced-motion rules; every needed component has all states, keyboard table, semantics, and target size; `tokens.json` valid. |
| Content (B) | Every copy slot filled; content guide complete; audit has no open grammar, spelling, voice, tone, accessibility, or AI-text issues; `[CONFIRM]` items listed. |
| Prototype (B) | Every MVP screen and key state reachable; tokens only (no hard-coded values); light and dark; responsive; final copy; semantic, keyboard operable, reflows at 320 px. |
| Critique | Issues have severity, principle, and owner; all High issues fixed or accepted by the user before validation. |
| Validation (B) | Verdict per persona goal; every WCAG 2.2 AA criterion listed as Pass / Fail / Verify in build; contrast computed; heuristics scored; UX laws log sampled and verified; no open Critical issues; every High issue fixed or explicitly accepted at the checkpoint. |
| Documentation | A developer who has seen nothing else could build from it; exact names used; open issues under Decisions pending. |
| Measurement | Every go / no-go criterion is measurable by an event or data source; event taxonomy complete for primary funnels; privacy section present. |

| Case study (A) | `case-study.md` written first, with sources; all 15 sections present (Outcomes marked pending); every UX-law badge matches a `ux-laws-log.md` entry and links to lawsofux.com with visible "how it applies" text; charts and diagrams have text or table alternatives; page meets WCAG 2.2 AA (landmarks, headings, contrast, keyboard, no hover-only content, reduced motion, reflow at 320 px); nothing invented; if an anonymised version was requested, no original term remains (searched) and the confidentiality note is visible. |

## Phase 4: Check the MVP and plan what's next
| Stage | Gate |
|---|---|
| Build QA | Coverage stated; every issue has evidence and an owner; release recommendation given; untested items marked, not assumed. |
| Research (B) | Test plan tied to hypotheses and includes assistive-technology users; synthesis (if any) reports sample sizes; nothing fabricated. |
| Case study (B) | Outcomes section uses only real results from `14-mvp-results/`, with sample sizes; learnings and next steps updated; anonymised version updated too, if one exists. |
| MVP scope (B) | Every go / no-go criterion has target, actual, and evidence; recommendation Go / Iterate / Pivot / Waiting on evidence; backlog re-scored with reasons. |

## Add-ons
| Add-on | Gate |
|---|---|
| Localization | Target locales listed; expansion, RTL (if in scope), formats, and language markup checked; issues owned. |
| Privacy & compliance | Frameworks listed and marked for legal confirmation; data inventory complete; dark-pattern check done; nothing claimed as "compliant". |
| Engineering breakdown | Every MVP feature has an epic; stories have Given/When/Then criteria that include accessibility and analytics; build order starts with foundations and a thin end-to-end slice. |

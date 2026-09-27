# Quality gates

Check the output files against these before moving on. A gate passes only when every line is true, or the exception is recorded as an open issue with an owner.

## Phase 1: Define
| Stage | Gate |
|---|---|
| Research (A) | Every theme cites evidence and a confidence level; 3–6 competitors analyzed; segments include access needs; riskiest assumptions ranked with a test method; if no user research was supplied, that's stated at the top. |
| Strategy | Problem, goals, non-goals present; every requirement has an ID, type, user story, measurable metric, and source; NFRs cover accessibility (WCAG 2.2 AA), performance, security/privacy, localization, devices, reliability; requirements grouped into features F-xx; no prioritization done here. |
| Architect (A) | Every feature has an effort size and score, drivers, dependencies, risk; L/XL features have a simpler alternative. |
| MVP scope (A) | Every feature has MoSCoW, user and business value, effort, quadrant, decision, reason; MVP = all Musts + chosen Shoulds; Money-pit Musts challenged; the MVP forms a complete journey for the primary persona; each in-scope feature has a hypothesis; 3–6 measurable go / no-go criteria with data sources; every deferred feature is in Next or Later with a reason. |

## Phase 2: Concept
| Stage | Gate |
|---|---|
| UX (A) | 2–4 personas, at least one with an access need; every persona has at least one journey; flows include error and empty paths; every MVP feature appears on at least one screen; copy slots marked; nothing out of scope designed. |
| Content (A) | Every copy slot on the primary flows has draft copy; no placeholder text. |
| Prototype (A) | Every primary MVP flow clickable end to end, with at least one error path and one empty state; draft copy used; keyboard operable; `prototype.md` lists coverage and limits. |
| Validation (A) | A verdict per persona goal; each MVP hypothesis confirmed testable; early accessibility red flags listed; overall verdict Proceed / Proceed with changes / Rethink. |

## Phase 3: Build out the MVP
| Stage | Gate |
|---|---|
| UX (B) | Concept-validation issues owned by UX resolved or explained; every screen has all states and all three breakpoints; accessibility annotations per screen; heuristic rationale on key screens. |
| Architect (B) | Components, data model, APIs, NFRs, ADRs, risks, extensibility for the backlog, requirement → component traceability; flags any infeasible UX. |
| Design system | Three token tiers; light and dark themes; every text/background and UI pair has a computed contrast ratio that passes; focus style meets 3:1; reduced-motion rules; every needed component has all states, keyboard table, semantics, and target size; `tokens.json` valid. |
| Content (B) | Every copy slot filled; content guide complete; audit has no open grammar, spelling, voice, tone, accessibility, or AI-text issues; `[CONFIRM]` items listed. |
| Prototype (B) | Every MVP screen and key state reachable; tokens only (no hard-coded values); light and dark; responsive; final copy; semantic, keyboard operable, reflows at 320 px. |
| Critique | Issues have severity, principle, and owner; all High issues fixed or accepted by the user before validation. |
| Validation (B) | Verdict per persona goal; every WCAG 2.2 AA criterion listed as Pass / Fail / Verify in build; contrast computed; heuristics scored; no open Critical issues; every High issue fixed or explicitly accepted at the checkpoint. |
| Documentation | A developer who has seen nothing else could build from it; exact names used; open issues under Decisions pending. |
| Measurement | Every go / no-go criterion is measurable by an event or data source; event taxonomy complete for primary funnels; privacy section present. |

## Phase 4: Check the MVP and plan what's next
| Stage | Gate |
|---|---|
| Build QA | Coverage stated; every issue has evidence and an owner; release recommendation given; untested items marked, not assumed. |
| Research (B) | Test plan tied to hypotheses and includes assistive-technology users; synthesis (if any) reports sample sizes; nothing fabricated. |
| MVP scope (B) | Every go / no-go criterion has target, actual, and evidence; recommendation Go / Iterate / Pivot / Waiting on evidence; backlog re-scored with reasons. |

## Add-ons
| Add-on | Gate |
|---|---|
| Localization | Target locales listed; expansion, RTL (if in scope), formats, and language markup checked; issues owned. |
| Privacy & compliance | Frameworks listed and marked for legal confirmation; data inventory complete; dark-pattern check done; nothing claimed as "compliant". |
| Engineering breakdown | Every MVP feature has an epic; stories have Given/When/Then criteria that include accessibility and analytics; build order starts with foundations and a thin end-to-end slice. |

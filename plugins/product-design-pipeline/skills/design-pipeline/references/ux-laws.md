# Laws of UX reference

Source: [lawsofux.com](https://lawsofux.com/) by Jon Yablonski. Use these exact names in `05-ux/ux-laws-log.md`, and link each law to its page when you show it to people.

| Law | Link | In short | Typical use in design |
|---|---|---|---|
| Aesthetic-Usability Effect | https://lawsofux.com/aesthetic-usability-effect/ | People see attractive designs as easier to use | Visual polish on key screens; don't let polish hide usability problems in testing |
| Choice Overload | https://lawsofux.com/choice-overload/ | Too many options overwhelm people | Limit plans, filters and options; add comparison or recommendations |
| Chunking | https://lawsofux.com/chunking/ | Grouping information into meaningful units makes it easier to process | Split phone numbers and codes, group form fields, use sections and steps |
| Cognitive Bias | https://lawsofux.com/cognitive-bias/ | Systematic errors in thinking shape decisions | Neutral defaults, honest framing; avoid exploiting biases (dark patterns) |
| Cognitive Load | https://lawsofux.com/cognitive-load/ | Mental effort needed to use an interface | Remove clutter, show one task at a time, use progressive disclosure |
| Doherty Threshold | https://lawsofux.com/doherty-threshold/ | Productivity rises when responses come within about 400 ms | Instant feedback, optimistic UI, skeleton loaders, performance budgets |
| Fitts's Law | https://lawsofux.com/fittss-law/ | Time to hit a target depends on its size and distance | Large primary buttons near where attention is; targets ≥ 24 px (WCAG 2.5.8), 44 px on touch |
| Flow | https://lawsofux.com/flow/ | Full, energized focus on an activity | Remove interruptions, balance challenge, clear progress and feedback |
| Goal-Gradient Effect | https://lawsofux.com/goal-gradient-effect/ | Motivation grows as people get closer to a goal | Progress bars, step indicators, showing what's already done |
| Hick's Law | https://lawsofux.com/hicks-law/ | Decision time grows with the number and complexity of choices | Fewer choices at decision points, one clear primary action, smart defaults |
| Jakob's Law | https://lawsofux.com/jakobs-law/ | People expect your product to work like others they know | Standard patterns for navigation, checkout, forms and icons |
| Law of Common Region | https://lawsofux.com/law-of-common-region/ | Items inside a shared boundary look grouped | Cards, panels and bordered sections for related content |
| Law of Proximity | https://lawsofux.com/law-of-proximity/ | Items close together look related | Spacing that ties labels to fields and separates groups |
| Law of Prägnanz | https://lawsofux.com/law-of-pr%C3%A4gnanz/ | People read complex shapes as the simplest form | Simple icons and layouts; avoid visual ambiguity |
| Law of Similarity | https://lawsofux.com/law-of-similarity/ | Similar-looking items look like a group | Consistent styles for links, buttons and status; different styles for different meanings |
| Law of Uniform Connectedness | https://lawsofux.com/law-of-uniform-connectedness/ | Visually connected items look more related | Lines and connectors in steppers, timelines, grouped controls |
| Mental Model | https://lawsofux.com/mental-model/ | People's assumptions about how a system works | Match users' terms and expectations, found in research |
| Miller's Law | https://lawsofux.com/millers-law/ | People hold only a few items in working memory | Chunk content; don't make people remember things between steps |
| Occam's Razor | https://lawsofux.com/occams-razor/ | Prefer the simplest solution that works | Remove unnecessary elements and steps |
| Paradox of the Active User | https://lawsofux.com/paradox-of-the-active-user/ | People start using software without reading instructions | Inline help, contextual tips, learnable UI; no manual required |
| Pareto Principle | https://lawsofux.com/pareto-principle/ | About 80% of effects come from 20% of causes | Focus the MVP and design effort on the most-used flows |
| Parkinson's Law | https://lawsofux.com/parkinsons-law/ | Tasks expand to fill the time available | Shorten flows, autofill, set expectations for task length |
| Peak-End Rule | https://lawsofux.com/peak-end-rule/ | Experiences are judged by their peak and their end | Design the high point and the completion moment; soften error peaks |
| Postel's Law | https://lawsofux.com/postels-law/ | Be liberal in what you accept, conservative in what you send | Forgiving inputs (formats, spaces, case); clear, consistent output |
| Selective Attention | https://lawsofux.com/selective-attention/ | People focus on what relates to their goal | Put key information where users look; don't style content like ads (banner blindness) |
| Serial Position Effect | https://lawsofux.com/serial-position-effect/ | People remember the first and last items best | Key items at the start and end of navigation and lists |
| Tesler's Law | https://lawsofux.com/teslers-law/ | Some complexity can't be removed, only moved | Let the system absorb complexity (defaults, automation) instead of the user |
| Von Restorff Effect | https://lawsofux.com/von-restorff-effect/ | The item that differs is remembered | Make the primary action or key information stand out, not with color alone |
| Working Memory | https://lawsofux.com/working-memory/ | Temporary memory for the task at hand | Keep needed information visible; don't make people remember across screens (supports WCAG 3.3.7) |
| Zeigarnik Effect | https://lawsofux.com/zeigarnik-effect/ | Unfinished tasks are remembered better | Show incomplete profile or setup progress; save drafts |

## Rules for using the laws
- A law is applied only when a specific design decision follows from it. Record that decision in `05-ux/ux-laws-log.md` at the time it's made.
- Laws support accessibility; they never override it. For example, the Von Restorff Effect must not rely on color alone (WCAG 1.4.1).
- The validator checks a sample of logged decisions against the design, and flags any claimed law that isn't visible in the design.

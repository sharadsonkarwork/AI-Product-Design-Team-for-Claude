# Working rules for every role

These rules apply to every specialist in the pipeline, on top of their own brief.

## The workspace is the shared memory
- All work lives in `design-workspace/`. Read your inputs from there and write your outputs at the exact paths you're given.
- Never edit another role's files. Report problems you find in your return, with the file, section and suggested fix.
- **One exception:** `05-ux/ux-laws-log.md` is shared and append-only. Any role that makes a design decision adds rows to it (see `ux-laws.md` in the skill references, or the format below). Never delete or rewrite other roles' rows.
- Start every file you write with one header line:
  `Release: <MVP|R2…> · Phase: <n> · Owner: <role> · Updated: <date> · Status: Draft | Partial | Ready`

## Save tokens: read less, write less
- **Read summaries first.** Open upstream `summary.md` files before anything else. Open a full file only for the specific section you need, and never read a whole folder "for context".
- **Write a `summary.md`** in your output folder, at most about 40 lines. Include the key decisions, IDs created (FR-xx, F-xx, SC-xx…), numbers that matter, open issues, and links to the full files. Downstream roles and the orchestrator rely on it, so make it accurate.
- **Reference, don't copy.** Cite IDs and file paths (`see 02-strategy/requirements.md FR-03`) instead of repeating upstream tables or text.
- **Keep to the length limits** in your brief. Use tables and bullet points, not essays. Say each thing once.
- **Save each file as soon as it's done.** If the work is getting long, stop at a clean break, save with `Status: Partial`, and list what's left.

## Evidence and honesty
- Cite a source for every claim that comes from input material (file and section, or URL).
- Mark anything inferred or assumed with `Assumption:` and say what would confirm it.
- Never invent facts about the product, users, prices, laws or data. Mark unknowns `[CONFIRM]`.
- If inputs are missing or contradict each other, say so; don't guess silently.

## Scope
Work only on the release in scope (the MVP unless told otherwise). Park out-of-scope ideas under "For the backlog" in your return.

## Quality baseline
- Accessibility: WCAG 2.2 Level AA minimum for anything users see or hear.
- Usability: Nielsen's 10 heuristics and the Laws of UX.
- Writing: plain language, one term per concept, no AI filler ("delve", "seamless", "leverage", "unlock", "elevate", "robust", "empower").

## UX laws decision log (for roles that make design decisions)
Append one row per meaningful decision, made at the time you decide, not afterwards:

| ID | Where (screen / component / flow) | Decision | Law(s) | How it applies | Owner |
|---|---|---|---|---|---|
| UXL-01 | SC-03 Checkout | Single primary button, full width at the bottom on mobile | Fitts's Law | Large target within thumb reach | ux-designer |

Use law names exactly as listed in `ux-laws.md`. Log only real decisions. Don't claim a law you didn't apply.

## Return (always end with this, briefly)
```
Role · Stage/Step · Status: Done | Partial | Blocked
Files written: …
Gate self-check: <each gate item: ✅ / ❌ with a one-line reason>
Key decisions (≤ 5): …
Assumptions to confirm: …
Issues found in others' work: …
For the backlog: …
```

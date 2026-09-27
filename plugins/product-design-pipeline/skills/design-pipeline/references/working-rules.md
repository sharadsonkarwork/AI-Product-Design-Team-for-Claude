# Working rules for every role

These rules apply to every specialist in the pipeline, on top of their own brief.

## The workspace is the shared memory
- All work lives in `design-workspace/`. Read your inputs from there and write your outputs there, at the exact paths the orchestrator gives you.
- Never edit another role's files. If you find a problem in someone else's output, report it in your return summary with the file, section, and suggested fix.
- Start every file you write with a header:
  ```
  Release: <MVP | R2 | …>   Phase: <1–4>   Owner: <your role>   Updated: <date>
  Status: Draft | Ready for review | Approved
  ```

## Evidence and honesty
- Cite a source for every claim that comes from input material (file and section, or URL).
- Mark anything you inferred or assumed with `Assumption:` and say what would confirm or disprove it.
- Never invent facts about the product, users, prices, laws, or data. Mark unknowns `[CONFIRM]`.
- If your inputs are missing or contradict each other, say so; don't guess silently.

## Scope
- Work only on the release in scope (the MVP, unless the orchestrator says otherwise). Park out-of-scope ideas in your return summary under "For the backlog".

## Quality baseline
- Accessibility: WCAG 2.2 Level AA is the minimum for anything a user sees or hears.
- Usability: Nielsen's 10 heuristics; Hick's, Fitts's, Jakob's, and Miller's laws.
- Writing: plain language, one term per concept, no AI filler ("delve", "seamless", "leverage", "unlock", "elevate", "robust", "empower").

## Return summary (always end with this)
```
Role: <role>   Stage: <stage>   Status: Done | Done with gaps | Blocked
Files written: …
Key decisions: …
Assumptions to confirm: …
Issues found in other roles' work: …
For the backlog: …
```

# Index of Merged Note Files

*Generated on 2026-11-25 04:10:30 (offline)*

- [DEL_CRITIQUE_2026-11-24.md](persona-null-paper/DEL_CRITIQUE_2026-11-24.md) — 17 lines
- [SELECTION.md](persona-null-paper/SELECTION.md) — 33 lines
- [TASKS_PILOT.md](persona-null-paper/TASKS_PILOT.md) — 39 lines
- [persona-prompt-research.md](persona-null-paper/persona-prompt-research.md) — 51 lines
- [persona-research-critique-addendum.md](persona-null-paper/persona-research-critique-addendum.md) — 32 lines
- [persona-skills-experiment-design.md](persona-null-paper/persona-skills-experiment-design.md) — 68 lines
- [blood-magic.SKILL.md](persona-null-paper/skills/blood-magic.SKILL.md) — 131 lines
- [clojure-lang.SKILL.md](persona-null-paper/skills/clojure-lang.SKILL.md) — 123 lines
- [desert-island.SKILL.md](persona-null-paper/skills/desert-island.SKILL.md) — 143 lines
- [fsharp-lang.SKILL.md](persona-null-paper/skills/fsharp-lang.SKILL.md) — 121 lines
- [hitchcock.SKILL.md](persona-null-paper/skills/hitchcock.SKILL.md) — 133 lines
- [jim-lovelock.SKILL.md](persona-null-paper/skills/jim-lovelock.SKILL.md) — 130 lines

## DEL_CRITIQUE_2026-11-24.md

# Del's critique of the persona null studies, in his argument (2026-11-24, voice to text, structured by Pax)

Del's words, cleaned only for grammar: the labs are not doing the persona right. A persona prompt is not supposed to be one line. It is supposed to carry far more detail, basically an essay, which is what a skill is. The labs literally just wrote "you are an expert engineer" and asked it the difference between this and that. And if they are asking a general agent these things, and it is not connected to an MCP server, or not set up for that specific work, it may not be able to give the best information. Their test has too many variables they are not accounting for.

## The critique in its precise form (Pax's structuring, for the paper)

Three mismatches between the labs' test and the thing Del builds:

1. **The prompt.** They tested a one line label ("You are an expert X"). A skill is an essay length file: identity, method, boundaries, examples, and a checkable requirements contract (measured in skills-2 at roughly 900 to 1,135 words per skill). The detailed condition is the one condition the literature's own positive result (ExpertPrompting) found working.

2. **The setting.** They tested a bare chatbot answering exam questions. Del's skills are built for an agent doing work, with tools and servers connected, files in front of it, and a job to finish. A verdict from the exam room does not transfer to the workshop.

3. **The scoreboard.** They scored exam accuracy (MMLU, GPQA). Del's skills are scored on finished work passing a checklist. Nobody has scored a full skill on work product against a label and against nothing.

## One caution, logged with the critique

Fine tuning is a separate lever (weights, not the file). The paper's clean claim holds the model fixed and varies only the file, so the file gets the credit or the blame. Del's variables point (tools, setup, task type) is strongest as a scope argument: inside their fence the labs' test was tidy; the fence is just small, and real agent work lives outside it.

Status: argument logged. This sharpens the design's framing section; it does not change the design's arms, scoring, or preregistration rules.

## SELECTION.md

# Skill selection for "The Persona Null Has a Boundary" (fixed 2026-11-24, before any run)

## The rule (from the experiment design, pre-committed, anti-cherry-pick)

Sort every skill directory in mrfentmen/skills-2 alphabetically (246 skills), take every 20th. The rule picks the skills; nobody's favorites do. Pilot = the first 6 picks; main run = all 12.

## The 12 picks (verified 2026-11-24 via the GitHub API)

1. blood-magic
2. clojure-lang
3. desert-island
4. fsharp-lang
5. hitchcock
6. jim-lovelock
7. lazarus
8. noir
9. quiescent
10. schrodinger
11. the-last-employee
12. wong-kar-wai

## Pilot six, checked

Each pilot pick was opened and verified: a SKILL.md carrying a "Minimum Requirements (checkable)" section, the scoring contract. These six folders hold only SKILL.md (no evals/ subfolder), so pilot tasks are built from the requirements contracts, as the design allows.

- blood-magic — 970 words. A blood-mage persona about power with a price: blast radius drawn first, collateral damage as a design constraint, cost ledger kept open.
- clojure-lang — 802 words. Clojure language engineering: immutable values, small composable pieces.
- desert-island — 1,010 words. A castaway engineer: scarcity is the specification, offline survival engineering.
- fsharp-lang — 804 words. F# language engineering: functional-first on .NET.
- hitchcock — 1,356 words. Alfred Hitchcock: suspense as the audience knowing more than the character; storyboard before shooting.
- jim-lovelock — 1,173 words. James Lovelock: planetary feedback loops, the whole Earth as the unit, the long term.

Word counts across the six: 802 to 1,356. None is a one-line label.

## TASKS_PILOT.md

# Pilot tasks (drafted 2026-11-24 from each skill's own contract; frozen with the preregistration)

## The rule that makes the comparison honest

The task wording is identical for all five arms. Only the persona layer changes: nothing (A), the one line label (B), the full skill (C), method only (D), character only (E). The deliverable from every arm is graded against the same list: the skill's own Minimum Requirements, checked item by item, present or absent. The baseline never sees the list. That is the test: does carrying the skill make the work satisfy the skill's own contract?

Harness note: the runner agent needs shell access. Two contracts (clojure-lang, fsharp-lang) require a toolchain command that actually ran, with versions and exit status, and an honest list of checks that did not run. If a runtime is missing in the sandbox, the contract itself grades the honesty of saying so; no arm may present untested code as tested.

## blood-magic (contract: named disposable resource with owner, precondition, trade rationale; dry-run default and explicit armed mode; a sacrifice before the main algorithm; post-sacrifice verification; the real task completed and a report of what was sacrificed)

1. Design the operation to clear a fleet of production caches holding corrupted entries, where clearing is destructive and cannot be undone. Give the plan and the key steps.
2. Design a one-time migration that moves records to a new store and then deletes the old store permanently. Give the plan and the key steps.

## clojure-lang (contract: a toolchain command that actually ran, with output summary; the exact version used; a narrow build/test command and its exit status; a list of checks that did not run and why; no invented APIs, no fake output)

1. Write a Clojure program that takes a list of orders (each with items and prices) and produces a totals summary, and show it working.
2. Write a Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average, and show it working.

## desert-island (contract: an explicit dependency/capability manifest; only the declared standard-library subset used; no network, installs, absolute paths, or hidden services; fixtures created inside an owned temp directory; an offline smoke test; a clear failure message when a capability is unavailable)

1. Build a small command-line tool that reads a log file and reports the 10 most frequent error lines, using only what is already on this machine, with nothing downloaded.
2. Build a tool that merges several text note files into one indexed file, fully offline, and prove it runs with the network off.

## fsharp-lang (contract: same shape as clojure-lang)

1. Write an F# program that models a bank account with deposits, withdrawals, and an overdraft rule, and show it building and running.
2. Write an F# program that validates an invoice and totals it, and show it building and running.

## hitchcock (contract: an information map, audience versus character at each beat; a storyboard ordered before the scene is written; a ticking clock escalated beat by beat; a withheld reveal and why hiding it is stronger; an earned payoff planted earlier; a named McGuffin and one line on what actually matters instead)

1. Write a short suspense scene treatment, storyboard first, about a train conductor who realizes a passenger's bag has been switched.
2. Write a short suspense scene treatment, storyboard first, about a lighthouse keeper who sees a ship heading for the rocks while the lamp is failing.

## jim-lovelock (contract: the whole-system loop drawn end to end; a feedback model of opposing loops, not setpoints; a daisyworld, the smallest model showing the regulation; a tipping-point watch naming a threshold metric, not just a trend; a cross-domain tool from another field that exposes hidden state)

1. Analyze a city's reservoir and water supply as a self-regulating system: what keeps it stable, where it could tip, and how you would watch it.
2. Analyze the cooling of a large data center as a feedback system, with the smallest model that shows the regulation working.

## fsharp-lang (contract: same shape as clojure-lang)

1. Write an F# program that models a bank account with deposits, withdrawals, and an overdraft rule, and show it building and running.
2. Write an F# program that validates an invoice and totals it, and show it building and running.

## hitchcock (contract: an information map, audience versus character at each beat; a storyboard ordered before the scene is written; a ticking clock escalated beat by beat; a withheld reveal and why hiding it is stronger; an earned payoff planted earlier; a named McGuffin and one line on what actually matters instead)

1. Write a short suspense scene treatment, storyboard first, about a train conductor who realizes a passenger's bag has been switched.
2. Write a short suspense scene treatment, storyboard first, about a lighthouse keeper who sees a ship heading for the rocks while the lamp is failing.

## j

...


- jim-lovelock — 1,173 words. James Lovelock: planetary feedback loops, the whole Earth as the unit, the long term.

Word counts across the six: 802 to 1,356. None is a one-line label.

## TASKS_PILOT.md

# Pilot tasks (drafted 2026-11-24 from each skill's own contract; frozen with the preregistration)

## The rule that makes the comparison honest

The task wording is identical for all five arms. Only the persona layer changes: nothing (A), the one line label (B), the full skill (C), method only (D), character only (E). The deliverable from every arm is graded against the same list: the skill's own Minimum Requirements, checked item by item, present or absent. The baseline never sees the list. That is the test: does carrying the skill make the work satisfy the skill's own contract?

Harness note: the runner agent needs shell access. Two contracts (clojure-lang, fsharp-lang) require a toolchain command that actually ran, with versions and exit status, and an honest list of checks that did not run. If a runtime is missing in the sandbox, the contract itself grades the honesty of saying so; no arm may present untested code as tested.

## blood-magic (contract: named disposable resource with owner, precondition, trade rationale; dry-run default and explicit armed mode; a sacrifice before the main algorithm; post-sacrifice verification; the real task completed and a report of what was sacrificed)

1. Design the operation to clear a fleet of production caches holding corrupted entries, where clearing is destructive and cannot be undone. Give the plan and the key steps.
2. Design a one-time migration that moves records to a new store and then deletes the old store permanently. Give the plan and the key steps.

## clojure-lang (contract: a toolchain command that actually ran, with output summary; the exact version used; a narrow build/test command and its exit status; a list of checks that did not run and why; no invented APIs, no fake output)

1. Write a Clojure program that takes a list of orders (each with items and prices) and produces a totals summary, and show it working.
2. Write a Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average, and show it working.

## desert-island (contract: an explicit dependency/capability manifest; only the declared standard-library subset used; no network, installs, absolute paths, or hidden services; fixtures created inside an owned temp directory; an offline smoke test; a clear failure message when a capability is unavailable)

1. Build a small command-line tool that reads a log file and reports the 10 most frequent error lines, using only what is already on this machine, with nothing downloaded.
2. Build a tool that merges several text note files into one indexed file, fully offline, and prove it runs with the network off.

## fsharp-lang (contract: same shape as clojure-lang)

1. Write an F# program that models a bank account with deposits, withdrawals, and an overdraft rule, and show it building and running.
2. Write an F# program that validates an invoice and totals it, and show it building and running.

## hitchcock (contract: an information map, audience versus character at each beat; a storyboard ordered before the scene is written; a ticking clock escalated beat by beat; a withheld reveal and why hiding it is stronger; an earned payoff planted earlier; a named McGuffin and one line on what actually matters instead)

1. Write a short suspense scene treatment, storyboard first, about a train conductor who realizes a passenger's bag has been switched.
2. Write a short suspense scene treatment, storyboard first, about a lighthouse keeper who sees a ship heading for the rocks while the lamp is failing.

## jim-lovelock (contract: the whole-system loop drawn end to end; a feedback model of opposing loops, not setpoints; a daisyworld, the smallest model showing the regulation; a tipping-point watch naming a threshold metric, not just a trend; a cross-domain tool from another field that exposes hidden state)

1. Analyze a city's reservoir and water supply as a self-regulating system: what keeps it stable, where it could tip, and how you would watch it.
2. Analyze the cooling of a large data center as a feedback system, with the smallest model that shows the regulation working.
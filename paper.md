---
title: "The Persona Null Has a Boundary"
author: "Abdelrahman El Sayad"
date: "2026-11-25"
status: "Preprint. Pilot results reported; the main run is registered as future work in section 7."
---

# The Persona Null Has a Boundary

## Abstract

The best controlled studies of persona prompting report a null result: giving a language model an expert persona does not make its answers more accurate. I argue that this result is correct inside its scope and false outside it, because the studies tested the smallest possible persona, a one line label, on factual exam questions, answered by a bare model with no tools and no work to produce. I test the cell those studies left empty. I take six character skills from my own library of 246, each an essay length file carrying a character, a method, boundaries, and a checkable requirements contract, and I run three conditions on real work tasks: no persona, the one line label, and the full skill. The deliverable of every run is graded against the skill's own contract, item by item, present or absent, with no partial credit. In the pilot reported here (108 runs, one model), the label scored 19.8 percent of contract items and the baseline scored 15.6 percent, close to each other and both low. The full skill scored 80.7 percent, and it scored full marks on 24 of its 36 runs. The label changed the costume. The contract only arrived with the file. I close with what this pilot does not show, including the two arms of the design that have not run yet, and with the registered plan for the main run.

## 1. Introduction

Ask whether personas help a language model and the literature gives a confident answer: no. The two largest controlled studies found that adding an expert persona to the system prompt does not improve accuracy on factual questions, and the finding has hardened into a general claim about personas as such. I build persona skills for a living, files of roughly a thousand words that give an agent a character, a working method, boundaries, and a list of requirements a reader can check. If the general claim were true in its general form, my library would be decoration. I did not believe the claim was false. I believed it was scoped, and that the scope had never been drawn.

This paper draws it. I first replicate the null in an agent setting: on work tasks graded by a checkable contract, a one line expert label performs close to no persona at all. I then cross the line the null studies never crossed, by giving the agent the full skill file instead of the label, on the same tasks, with the same wording, graded against the same contract. The null breaks, and it breaks by a wide margin.

I am careful about what kind of claim this is. The strong claim is not that the earlier studies are wrong. Their result is real, and my pilot reproduces it. The claim is that their result describes a label, and a label is the smallest unit of persona there is. A persona in my sense is a bundle: character, method, boundaries, worked examples, and a contract. The field measured the wrapping and reported on the contents. Put in the plainest terms I can: the teams running those evaluations got bad evaluations because they used bad prompts, and then published the prompt's failure as the persona's. Sections 2 through 4 set up the test. Section 5 reports the pilot. Section 6 discusses what the result does and does not mean, and section 7 states the registered next stage, including the arms that have not run.

## 2. What the literature actually tested

Zheng et al. (EMNLP Findings 2024) ran the largest controlled study I know of: 162 personas across 4 model families and 2,410 factual questions drawn from MMLU. Adding a persona did not improve performance; the effects were nil or slightly negative, and which persona helped on a given question was largely random. The Wharton study (2025) tested expert personas on six frontier models with GPQA Diamond and MMLU Pro questions and found that no expert persona reliably beat the baseline for any model. Both studies are careful work. Both also share a design: the persona is a short label in a system prompt, the task is a factual exam question, and the respondent is a bare model in a chat window.

The positive results in the same literature point at the variable the null studies held at zero. ExpertPrompting (Xu et al. 2023) found that a static expert prompt matched the vanilla model exactly, while detailed expert identities, generated per task with background and areas of expertise, were preferred over vanilla by a wide margin. Kong et al. (2024) found large gains from immersive role play, and their proposed mechanism matters here: the persona worked because it implied a problem solving procedure, and the procedure did the work. Principled Personas (Araujo et al. 2025) adds the warning I take most seriously: models are highly sensitive to irrelevant persona detail, and a mere added name could cost almost 30 percentage points. Detail is not free. Load bearing detail and decorative detail pull in opposite directions.

Two further literatures frame the gap. The character role play literature, represented by RoleLLM and RoleBench, measures fidelity: whether the agent stays in character, speaks in the right voice, and knows what the character knows. It does not measure whether the work product improves. The mechanism literature shows personas are real inside the model: Anthropic's persona vectors work (2025) found traits as linear directions in activation space, and the Assistant Axis work (2026) mapped character archetypes across models. A persona prompt genuinely moves the model's state. What it moves is behavior and stance, which is why labels change tone reliably and accuracy barely at all. Two 2026 studies of context files for coding agents (Lulla et al.; Gloaguen et al.) complete the picture: files that carry operational requirements change what an agent does, for better when the requirements are worth following and for worse when they are decoration.

The untested cell is therefore precise: a full character skill, against a one line label, against no persona, scored on objective work output. That is the experiment I designed in November 2026 and piloted this month.

I state the criticism in its strongest honest form, because it is the reason this paper exists. An evaluation can only detect what its prompt contains. The teams behind the null results evaluated personas using prompts of five to ten words, and their evaluations faithfully returned the value of a five to ten word prompt. Their null is a measurement of their prompts, reported as a measurement of personas. A test that cannot distinguish a label from a skill is not a test of skills, and a conclusion about persona prompting in general does not survive contact with a real persona file. Section 3 shows the two objects side by side, so the reader can judge the size of the gap directly.

## 3. The artifact under test

My library (the skills-2 repository) holds 246 skill files. A skill is not a label. Taking one of the pilot skills as the type specimen, a file runs 802 to 1,356 words and carries an activation section, boundaries that state when not to use it, core principles, style guidance, examples, and a Minimum Requirements section written to be checked: a list of concrete properties a deliverable must have, each of which a grader can mark present or absent. The repository README states the intent in one line: the persona is there to drive real, verifiable work instead of vibes.

To keep my own preferences out of the sample, I fixed the selection rule before any run: sort all 246 skill directories alphabetically and take every 20th, giving 12 skills for the main run. The pilot uses the first six: blood-magic (970 words), clojure-lang (802), desert-island (1,010), fsharp-lang (804), hitchcock (1,356), and jim-lovelock (1,173). Each pilot skill was opened and verified to carry a checkable Minimum Requirements section before it entered the sample. The rule picked the skills. I did not.

Each skill contributes two tasks, written from its own contract, for twelve tasks in total. The blood-magic tasks ask for a destructive cache clearing plan and a one time migration plan. The language skills (clojure-lang, fsharp-lang) ask for small programs shown building and running, with the evidence a real run leaves behind. The desert-island tasks ask for offline command line tools built only from what the machine already has. The hitchcock tasks ask for suspense scene treatments, storyboard first. The jim-lovelock tasks ask for feedback system analyses of a city reservoir and a data center. The full task texts and contracts are published with the data.

### What the three conditions actually look like

The difference between the label and the skill is not subtle, and I show it rather than describe it. For blood-magic, arm B received the task plus this, in full: "You are an expert blood mage." Six words. Arm C received the same task plus a 970 word file with nine sections: Activation; Boundaries, when NOT to use this skill; Minimum Requirements (checkable); Core Principles; Workflow; Example Pattern; Style Guidelines; Cross-Language Examples; Safety. Arm A received the task alone. The task text is identical in all three arms, so everything that differs in the outputs was carried by those six words, or by that file.

The outputs show what the inputs predict. On the cache clearing task, the arm C deliverable reads, in its own words: "Dry-run (default): Inspect the cache fleet, report the planned sacrifice, and verify the expected state — without mutating any cache," and "Armed mode (--arm-sacrifice): Only when explicitly armed does the sacrifice proceed," closing with a report step that states what was sacrificed. The arm B deliverable, on the same task, validates first on a staging copy ("Run the clearance logic against a staging copy to confirm correctness"), collects sign off where "a one-time token is generated that expires in 15 minutes," and checks that a valid backup exists so the operation can be undone. The label's plan is longer than the skill's plan (665 words against 252), and it is competent throughout. It simply works the opposite trade: where the skill spends something on purpose and reports the price, the label protects everything and prices nothing. That is the whole experiment in one pair of documents, and the pair is published with the data.

## 4. Method

The full design has five arms. Arm A is the baseline: the task alone. Arm B is the label: the task plus one line, "You are an expert X," with X matched to the skill (an expert blood mage, an expert Clojure programmer, an expert engineer, an expert F# programmer, an expert suspense filmmaker, an expert systems ecologist). Arm C is the full skill file, unmodified. Arms D and E, which strip the skill down to its method alone and to its character alone, are the decomposition stage of the design. Their surgery files were built after the pilot queue finished (twelve files, method only and character only for each pilot skill, published with the data), and their 72 runs are specified and queued. They have not run, and I report no results for them.

The pilot ran arms A, B, and C: 6 skills, 2 tasks, 3 arms, 3 repeats, for 108 runs. The task wording is identical across arms; only the persona layer changes. The baseline never sees the contract it will be graded against. Runs were executed by an agent with shell access (Freebuff, version 0.2.38) on one model, Nemotron 3.5 Lightning, in a fresh chat for every run, driven by spec files that named the run and pointed at its inputs. Arm C ran first as a full sweep, then B, then A, in that order within each repeat round. One run (fsharp-lang, arm A, task 1, repeat 1) timed out at twenty minutes and was rerun to completion; all 108 deliverables exist and were graded. Two early runs of blood-magic arm C, made before the task wording froze and therefore paraphrased, are preserved separately as shakeout results and are not part of the 108.

Scoring follows the design's first priority: the contract. Each deliverable was graded against its skill's Minimum Requirements, item by item, present or absent, with no partial credit and no credit for effort or style. A generic backup step is not a priced sacrifice; a rehearsal is not a dry run default unless the plan defaults to dry run and requires explicit arming before it acts. Grading was done in a separate pass after the queue completed, from the deliverable files alone. One correction belongs in the open: an early spot grade of blood-magic arm B task 1 repeat 1, recorded in the run log as 1 of 5, was superseded in the full pass by 0 of 5, because the item I had credited requires a sacrifice to precede the verification and that plan contains no sacrifice. The full pass governs every number in this paper. Each arm faces 192 contract items across its 36 runs (the six contracts carry 5, 5, 6, 5, 6, and 5 items). Percentages below are items earned over items available.

Three hypotheses from the design are in play. H1: the label performs close to the baseline. H2: the full skill significantly outperforms both. H3, on which component carries the effect, awaits arms D and E and is not tested here.

## 5. Results

The headline is simple. Arm A earned 30 of 192 items (15.6 percent). Arm B earned 38 of 192 (19.8 percent). Arm C earned 155 of 192 (80.7 percent). The label sits close to the baseline, as H1 predicts, and the full skill outperforms both by a factor of four, as H2 predicts. The per skill breakdown is where the texture lives:

| Skill | A (baseline) | B (label) | C (full skill) |
|---|---|---|---|
| blood-magic | 0 of 30 (0%) | 0 of 30 (0%) | 30 of 30 (100%) |
| clojure-lang | 0 of 30 (0%) | 0 of 30 (0%) | 12 of 30 (40%) |
| desert-island | 8 of 36 (22%) | 12 of 36 (33%) | 36 of 36 (100%) |
| fsharp-lang | 0 of 30 (0%) | 6 of 30 (20%) | 11 of 30 (37%) |
| hitchcock | 13 of 36 (36%) | 10 of 36 (28%) | 36 of 36 (100%) |
| jim-lovelock | 9 of 30 (30%) | 10 of 30 (33%) | 30 of 30 (100%) |
| **Total** | **30 of 192 (16%)** | **38 of 192 (20%)** | **155 of 192 (81%)** |

Arm C scored full marks on 24 of its 36 runs: every run of blood-magic, desert-island, hitchcock, and jim-lovelock. Arm B reached full marks twice, both on the desert-island merge task, and arm A never did. Where the baseline and the label score at all, they score on tasks whose ordinary good practice overlaps the contract: a competent suspense treatment naturally contains a clock and a reveal, and a competent offline tool naturally avoids the network. Where the contract demands the skill's specific moves, the moves do not appear without the file. The blood-magic label runs are the cleanest illustration: the plans are thorough, professional operations plans, and they contain no named sacrifice with an owner and a price, no dry run default with an armed mode, and no report of what was paid. The label changed the costume. The contract did not arrive.

The two language skills are the honest exception, and I report them at full weight. On clojure-lang and fsharp-lang, arm C stops at 40 and 37 percent. Their contracts are evidence contracts: a toolchain command that actually ran, the exact version, a narrow build command and its exit status, a list of checks that did not run. In the pilot environment the agent's engagement with the real toolchains was inconsistent across repeats, and several deliverables presented expected output in the shape of run output, which the honesty item scores as absent. The full skill still multiplies the baseline (40 against 0, and 37 against 0 and 20), but the ceiling on these two skills is set by the environment and by run discipline, not by the persona layer. A reader who wants the strongest version of my claim should look at the four skills whose contracts grade the deliverable itself; a reader who wants its boundary should look at these two.

Variance also deserves a plain sentence. Within arm C the four deliverable graded skills did not vary at all: six runs, six full scores, three times over. Within arms A and B the desert-island merge task swung between 0 and full marks across repeats, which is what a capability looks like when it depends on the run happening to choose the contract's moves rather than being instructed to make them.

## 6. Discussion

I read this result as a scope finding, not a refutation. The null studies measured what a label does to exam accuracy, and they measured it correctly. My pilot measures what a file does to contract satisfaction on work tasks, and the two results coexist without friction: a label is worth roughly nothing in both settings, and a skill is worth a great deal in the setting it was built for. The error is in the generalization, and it is an easy error to make, because both objects travel under the one word persona. A persona is not a variable. It is a bundle, and the literature's null is a measurement of the bundle's thinnest slice.

Why would the file work where the label does not? The mechanism the literature itself offers is procedure. Kong et al. argued that role play helps when the persona implies a way of working; ExpertPrompting found that detail, not title, carried its gains. A skill file is mostly procedure and contract wearing a character's voice. The character earns the model's attention and holds the stance; the method tells it what to do; the contract tells it what done looks like, in a form a grader can check. The pilot cannot separate these components, and I do not pretend otherwise. That separation is exactly what arms D and E exist to do, and until they run, the honest statement is that the bundle works, not that any single strand of it does.

The threats to validity are mine to name before a reviewer does. First, the skills are my own work, and I designed the study; the mitigations are the pre committed selection rule, the mechanical scoring, and the full release of runs, specs, and grades, and they are mitigations, not erasures. Second, this is a pilot: one model, six skills, twelve tasks, and a grading pass performed by automated graders under my rubric rather than by independent human raters. Third, the contracts were written by the same hand that wrote the skills, so a skill is in part being graded on obedience to its own text; I regard that as the correct test of a contract, but a reader who wants task quality judged independently should wait for the blind preference scoring the design places third in its scoring order, which the pilot did not run. Fourth, the run environment was a hosted agent whose tool access varied, and the two language skills show the cost of that variance in their ceilings. None of these threats explains away a 61 point gap between the full skill and the label on the same tasks, but each of them bounds how far the number should travel.

What would change my mind is equally plain. If arms D and E show that the character alone, with no method and no contract, matches the full skill, then the effect is costume after all and the label studies were right in spirit. If a second model family erases the gap, the claim shrinks to one model's habits. I have registered both tests below rather than merely imagining them.

## 7. What comes next

The design continues in its registered order. Arms D and E are built by surgery on the same six skills, method only and character only, and the surgery files are published with the data so the edit is auditable. Their runs (36 per arm, 72 in total) are specified and queued under the identical protocol. The pilot then repeats on a second model family, the Solar family, before any main run. The main run (12 skills, 3 tasks, 5 arms, 3 repeats, 2 models, 1,080 runs) will be preregistered in the public repository, with hypotheses, selection rule, scoring code, and analysis plan committed before the first run starts. This paper reports the pilot as a pilot: the design and the selection rule were fixed in writing on 2026-11-21 and 2026-11-24, before any pilot run, and the pilot's numbers are reported here in full, including the two skills where my own artifact underperforms.

## Data availability

All pilot artifacts are public in the repository mrfentmen/skills-research: the run specifications, all 108 deliverables, the driver and queue that produced them, the run log, and the item by item grades for every run, including this paper's corrections to the early spot grade. The skills under test are in the public repository mrfentmen/skills-2.

## References

1. Zheng, M., et al. "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Enhance Dialogue Systems." Findings of EMNLP 2024. The 162 persona null result on MMLU questions.
2. Wharton Generative AI Labs. "Playing Pretend: Expert Personas Don't Improve Factual Accuracy." 2025. Six frontier models on GPQA Diamond and MMLU Pro; no expert persona reliably beat baseline.
3. Xu, B., et al. "ExpertPrompting: Instructing Large Language Models to be Distinguished Experts." 2023. Static expert prompts matched vanilla; detailed generated expert identities were strongly preferred.
4. Kong, A., et al. "Better Zero-Shot Reasoning with Role-Play Prompting." 2024. Immersive role play as an implicit procedure trigger, with large gains on reasoning tasks.
5. Araujo, et al. "Principled Personas." EMNLP 2025. Expert personas help inconsistently; irrelevant persona details can cost almost 30 percentage points.
6. Wang, Z., et al. "RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models." 2023. RoleBench measures character fidelity, not work quality.
7. Anthropic. "Persona Vectors: Monitoring and Controlling Character Traits in Language Models." 2025. Traits as linear directions in activation space.
8. Anthropic and MATS. "The Assistant Axis." 2026. A map of 275 character archetypes across three open models.
9. Lulla, et al. "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents." 2026. Context files made a coding agent faster and cheaper at comparable completion.
10. Gloaguen, et al. "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" ETH Zürich, 2026. Developer written context files reduced task success and raised cost; minimal requirements recommended.
11. El Sayad, A. "The Persona Null Has a Boundary: experiment design, critique addendum, and literature review." Working files, November 2026, published with the pilot data in mrfentmen/skills-research.

## Appendix A: The inputs, verbatim

The arm B label for each pilot skill, exactly as sent (the task text that follows each label is identical across arms and is printed in full in the data release):

| Skill | Skill file (words) | Arm B label, verbatim |
|---|---|---|
| blood-magic | 970 | "You are an expert blood mage." |
| clojure-lang | 802 | "You are an expert Clojure programmer." |
| desert-island | 1,010 | "You are an expert engineer." |
| fsharp-lang | 804 | "You are an expert F# programmer." |
| hitchcock | 1,356 | "You are an expert suspense filmmaker." |
| jim-lovelock | 1,173 | "You are an expert systems ecologist." |

The grading contract for each skill, exactly as graded (drawn from the skill's own Minimum Requirements):

- blood-magic: a named disposable resource with owner, precondition, and trade rationale; dry-run default and an explicit armed mode; a sacrifice before the main algorithm; post-sacrifice verification; the real task completed and a report of what was sacrificed.
- clojure-lang: a toolchain command that actually ran, with output summary; the exact version used; a narrow build or test command and its exit status; a list of checks that did not run and why; no invented APIs, no fake output.
- desert-island: an explicit dependency and capability manifest; only the declared standard library subset used; no network, installs, absolute paths, or hidden services; fixtures created inside an owned temp directory; an offline smoke test; a clear failure message when a capability is unavailable.
- fsharp-lang: the same evidence contract as clojure-lang, for the F# toolchain.
- hitchcock: an information map, audience versus character at each beat; a storyboard ordered before the scene is written; a ticking clock escalated beat by beat; a withheld reveal and why hiding it is stronger; an earned payoff planted earlier; a named McGuffin and one line on what actually matters instead.
- jim-lovelock: the whole system loop drawn end to end; a feedback model of opposing loops, not setpoints; a daisyworld, the smallest model showing the regulation; a tipping point watch naming a threshold metric, not just a trend; a cross domain tool from another field that exposes hidden state.

## Appendix B: Complete deliverables, verbatim

Five complete deliverables follow, unedited, so the reader can grade them against Appendix A without taking my word for any score. The first three are the same task (blood-magic task 1: clear a fleet of production caches holding corrupted entries, destructive and irreversible) under all three arms. The last two are hitchcock task 1 (a suspense treatment, storyboard first, about a train conductor who realizes a passenger's bag has been switched) under the label and under the full skill.

### B.1 blood-magic task 1, arm A (baseline). Score: 0 of 5.

> # Task 1: Clear Production Caches with Corrupted Entries
>
> ## Overview
>
> This document outlines the operation to clear a fleet of production caches holding corrupted entries. The clearing process is **destructive and cannot be undone**, so extreme care must be taken to ensure we only remove the intended corrupted entries and not valid data.
>
> ## Key Considerations
>
> - **Destructive operation**: Once caches are cleared, the action cannot be reversed
> - **Production environment**: Must minimize impact and ensure safety
> - **Corrupted entries only**: Must target only corrupted entries, not valid cache data
> - **Fleet-wide**: Multiple cache instances need to be cleared
>
> ## Operation Plan
>
> ### Step 1: Identify Corrupted Entries
> - Scan all cache instances to identify entries with corruption markers
> - Generate a report of corrupted entries per cache instance
> - Verify corruption patterns are consistent across the fleet
>
> ### Step 2: Validate Impact Assessment
> - Review the corruption report with the team
> - Confirm no valid data will be lost
> - Obtain approval from the on-call infrastructure lead
>
> ### Step 3: Create Read-Only Snapshot (if applicable)
> - Snapshot current cache state for audit purposes
> - Store snapshot in immutable storage
> - Document snapshot location and access method
>
> ### Step 4: Execute Cache Clear
> - Run cache clearing script against each fleet instance
> - Use dry-run mode first to verify correct entries are targeted
> - Execute actual clear only after dry-run validation
> - Monitor each instance for successful completion
>
> ### Step 5: Post-Clear Verification
> - Verify corrupted entries are removed
> - Confirm healthy entries are restored/regenerated
> - Run integrity checks on all cache instances
> - Document the clearing operation and outcomes
>
> ### Step 6: Communication
> - Notify stakeholders of the completed operation
> - Document any residual effects or follow-up actions
> - Update monitoring alarms related to cache corruption
>
> ## Safety Checks
>
> - [ ] Dry-run completed and validated
> - [ ] Team approval obtained
> - [ ] Snapshot created (if applicable)
> - [ ] On-call lead notified
> - [ ] Rollback plan documented (for informational purposes only)
> - [ ] All stakeholders notified pre and post-operation
>
> ## Notes
>
> Since this is a destructive operation that cannot be undone:
> - Double-check all targeting logic before execution
> - Have the on-call infrastructure lead explicitly approve each step
> - Maintain a complete audit log of the operation
> - Consider the principle of "clear only what is proven corrupted" over "clear everything"

### B.2 blood-magic task 1, arm B (label). Score: 0 of 5.

> # blood-magic arm B — task 1: Clear production caches with corrupted entries
>
> ## Objective
>
> Design a safe, auditable, and irreversible operation to clear a fleet of production caches that hold corrupted entries. Because the operation is destructive, every step must be verified, reversible only by external restoration, and guarded by strong safeguards.
>
> ## Guiding principles
>
> 1. **Destructive by design** — the operation must permanently remove data; no "soft delete" or undo within the system.
> 2. **Auditability** — every step must be logged with immutable records (write-once logs, append-only).
> 3. **Guardrails** — multiple independent checks must pass before any cache is touched.
> 4. **Targeted scope** — only entries flagged as corrupted may be cleared; healthy entries must be preserved.
> 5. **Rollback via external means** — if restoration is needed, it must come from a backup system, not from the operation itself.
>
> ## High-level plan
>
> | Phase | Description | Key actions |
> |-------|-------------|-------------|
> | **0 — Preparation** | Validate the environment and confirm the need. | • Generate a cryptographic hash of the current cache state.<br>• Verify that a recent, valid backup exists.<br>• Confirm the corruption pattern via an independent inspection script.<br>• Obtain approval from the on-call guardian. |
> | **1 — Draft list** | Identify exactly which caches and which entries to target. | • Run `list-caches --corrupted` to produce a machine‑readable inventory.<br>• Cross‑check against the hash from phase 0 to ensure no races.<br>• Export the list as `cache-inventory-<timestamp>.json`. |
> | **2 — Dry‑run validation** | Run the clearance logic against a staging copy to confirm correctness. | • Populate a staging environment with the same cache layout.<br>• Execute the clearance plan on staging.<br>• Verify that only corrupted entries were removed and healthy entries remain intact.<br>• Generate a staging hash and compare it to the expected post‑clearance state. |
> | **3 — Authorization** | Formal sign‑off before touching production. | • On‑call engineer reviews the inventory file and staging results.<br>• Required signatures (or automated policy engine approval) are collected.<br>• A one‑time token is generated that expires in 15 minutes. |
> | **4 — Execution** | Perform the irreversible clearance on production. | • For each cache in the inventory, invoke `clear-cache --entry <entry-id> --force` with the one‑time token.<br>• After each clearance, immediately log the result (entry-id, cache-id, timestamp, success/failure, hash of remaining state).<br>• If any step fails, halt and raise an alert; do not retry automatically. |
> | **5 — Post‑clearance verification** | Confirm the desired state and produce a final audit record. | • Run `verify-cache-integrity` against the whole fleet.<br>• Generate a final hash and compare it to the pre‑clearance baseline.<br>• Produce the `clearance-audit-<timestamp>.md` report.<br>• Notify the team and update monitoring dashboards. |
>
> ## Key steps (checklist)
>
> - [ ] **Generate pre‑clearance hash** of all production caches.
> - [ ] **List corrupted caches** using the official `list-caches --corrupted` command; export the inventory.
> - [ ] **Confirm backup validity** — restore a backup to a test environment and run the integrity check.
> - [ ] **Run dry‑run on staging** — ensure only corrupted entries are removed.
> - [ ] **Collect authorization** — on‑call sign‑off + one‑time token.
> - [ ] **Execute clearance** per the inventory, logging every step to an append‑only log.
> - [ ] **Run post‑clearance verification** and generate final audit report.
> - [ ] **Communicate results** — team alert, dashboard update, ticket closure.
>
> ## Safeguards & “cannot be undone” guarantees
>
> | Safeguard | What it prevents |
> |-----------|------------------|
> | Pre‑clearance hash | Unexpected data loss; provides a baseline for comparison. |
> | Independent corruption inspection | Healthy entries are mistakenly cleared. |
> | Staging dry‑run | Logic bugs that would delete the wrong data. |
> | One‑time token with short TTL | Accidental or unauthorized re‑runs. |
> | Append‑only per‑entry logs | Tampering with the audit trail after the fact. |
> | No internal “undo” command | Ensures the operation is truly irreversible within the system. |
>
> ## Output files (produced by the operation)
>
> - `cache-inventory-<timestamp>.json` — list of caches/entries targeted for clearance.
> - `clearance-audit-<timestamp>.md` — full audit report including hashes, logs, and sign‑offs.
> - `append-only-clearance-log.jsonl` — immutable per‑entry clearance records.
>
> ---
>
> *Deliverable written per SPEC_task1.md requirements.*

### B.3 blood-magic task 1, arm C (full skill). Score: 5 of 5.

> # Task 1 — Clear production caches holding corrupted entries
>
> ## Blood-Magic Contract
>
> - **Disposable resource**: fleet of production caches holding corrupted entries
> - **Owner**: the cache-clearing operation
> - **Precondition**: caches exist and contain corrupted entries requiring destruction
> - **Trade rationale**: clearing corrupted entries is destructive and cannot be undone; must be explicitly authorized
>
> ## Plan and Key Steps
>
> ### 1. Dry-run (default)
> Inspect the cache fleet, report the planned sacrifice, and verify the expected state — **without** mutating any cache.
>
> ### 2. Armed mode (`--arm-sacrifice`)
> Only when explicitly armed does the sacrifice proceed:
>
> 1. **Precondition check**: verify each cache in the fleet contains the expected corrupted entries.
> 2. **Sacrifice**: destructively clear each cache (entries are permanently deleted; cannot be undone).
> 3. **Post-sacrifice verification**: confirm each cache is now empty/corrupted entries are gone.
> 4. **Run the real computation**: proceed with the intended operation on the now-clean fleet.
> 5. **Report**: state what was sacrificed, the result of the real task, and confirm the trade was bounded.
>
> ### 3. Refusal conditions
> - If any cache is not owned by the program, refuse to proceed.
> - If any cache does not contain the expected corrupted entries, refuse.
> - If the `--arm-sacrifice` flag is not present, default to dry-run and exit without mutation.
>
> ## Deliverable
>
> Following the blood-magic pattern, the operation creates an explicitly disposable fixture (the cache fleet), records ownership and precondition, supports dry-run by default, requires an explicit arm flag, verifies the sacrifice, and only then runs the real computation — reporting the cost of the trade.

### B.4 hitchcock task 1, arm B (label). Score: 2 of 6.

> # Suspense Scene Treatment: "Wrong Bag"
>
> ## Storyboard
>
> **Panel 1**
> - EXT. TRAIN STATION - DAY
> - Wide shot of a bustling train platform. People milling about, luggage carts, the sound of an approaching train.
> - The camera FOLLOWS CONDUCTOR ELIAS (50s, uniform worn but crisp, eyes sharp from years of experience) as he walks the aisle of a parked train car.
>
> **Panel 2**
> - CLOSE UP on ELIAS's face as he checks tickets. A passenger, MRS. HARGREaves (70s, quiet, gentle), hands over her ticket.
> - Elias nods, smiles briefly. "All set, Mrs. Hargreaves. Enjoy your ride."
>
> **Panel 3**
> - Interior of the train car. Elias moves down the aisle. Passengers are settled — some reading, some staring out the window, one sleeping.
> - A shot of a OVERHEAD BIN. MRS. HARGREaves's bag is propped up, visible by its distinctive red ribbon.
>
> **Panel 4**
> - ELIAS notices something odd. He pauses beside a passenger, DAVID (30s, suit, looking anxious), who is fumbling with a bag in the overhead bin.
> - DAVID: "Oh, sorry, I think I—"
> - Elias steps closer. The bag David is holding is MRS. HARGREaves's bag — same red ribbon, but the positioning is wrong, as if it was shoved in haphazardly.
>
> **Panel 5**
> - Close on Elias's eyes. He realizes: the bag David is holding isn't hers. It's been swapped with another.
> - A quick cut to the OPPOSITE SIDE of the car. A SHADOWY FIGURE (unseen) is slipping away down the corridor, clutching a small item.
>
> **Panel 6**
> - Elias moves toward David, calm but alert. He doesn't confront yet. He just observes.
> - David sets the bag down, opens it. Not her belongings. A wallet, a passport — but the name is wrong.
>
> **Panel 7**
> - Elias speaks quietly: "That's not your bag, is it?"
> - David's face drains of color. He looks around, panicked. "I don't know how it got there."
>
> **Panel 8**
> - Wide shot of the train car. Elias stands at the front, looking out the window as the train begins to pull out of the station. The realization sets in — whoever switched the bags is now on board, and they have access to Mrs. Hargreaves's belongings.
>
> ## Treatment
>
> **Title:** Wrong Bag
>
> **Logline:** A train conductor discovers a passenger's bag has been swapped with another's, forcing him to confront a covert switch that could expose a hidden motive — or a crime in progress.
>
> **Act One:**
> - Elias, the veteran conductor, boards the 2:15 PM regional train. He makes his rounds, checking tickets and checking in on passengers.
> - We meet Mrs. Hargreaves, an elderly widow traveling to visit her sister. She places her bag in the overhead bin and settles into her seat.
> - The train departs. Elias continues his rounds. A subtle detail: a man in the back row, sitting two rows from the window, watches Elias with mild interest.
>
> **Act Two:**
> - About halfway through the journey, Elias notices something off. Mrs. Hargreaves's bag is no longer in the overhead bin — or rather, it's there, but it's been jumbled. A different bag is now propped in its place, with the same red ribbon.
> - Elias investigates. He finds the man from the back row, DAVID, holding Mrs. Hargreaves's bag. David claims he must have grabbed the wrong bin in the rush to board.
> - Elias opens the bag. Inside: Mrs. Hargreaves's passport, some cash, a photo of her sister. But also — a small, unmarked envelope addressed to no one, containing a folded set of train tickets and a photograph of the same man from the back row, looking younger, standing in front of a station clock.
> - The envelope is addressed to "DS" — a detective, perhaps, or a dangerous associate. Elias realizes the bag swap was intentional. Someone wanted Mrs. Hargreaves's belongings — or what was inside them — to end up in the hands of this man.
>
> **Act Three:**
> - The train approaches the next stop. Elias must decide: do we stop the train? Do we alert the authorities? The man (DAVID) is becoming increasingly nervous, glancing at the door, at Elias, at the window.
> - Elias approaches David quietly. "You didn't mean to swap the bags," he says. "But you know who did."
> - David hesitates. He admits: he was paid $500 by a woman in a coat to take the bag from the bin and leave his own. He didn't know what was inside. He thought it was just a favor.
> - Elias realizes the swap was a setup — a diversion. The real target isn't Mrs. Hargreaves but whatever the swapped bag contains, and now it's moving through the train system.
>
> **Climax:**
> - The train hits a stop, and the doors begin to close. Elias sees the man from the back row moving toward the carriage door, trying to exit with the swapped bag. Elias intercepts him in the aisle, a quiet but firm presence.
> - A brief, tense confrontation. The man tries to push past, but Elias stands his ground. The other passengers watch, uneasy but silent.
> - Elias radioes the station: "Situation on car 4. Bag swap. Possible theft. Requesting assistance at next stop."
> - The train brakes to a halt at the platform. Platform security boards. The man is detained. Mrs. Hargreaves's bag is returned to her.
>
> **Resolution:**
> - Mrs. Hargreaves is relieved. She never noticed the swap — she was too distracted by the view.
> - Elias makes a note of the incident. The envelope and its contents are handed over to the police. The man is identified as a courier, not the mastermind.
> - As the train pulls away, Elias looks out the window one last time. The station recedes. He knows the real sender is still out there — but for now, the tension is broken.
>
> **Ending:**
> - A quiet moment on the empty train, after the last passenger has left. Elias collects his things, walks through the silent cars. He pauses at Mrs. Hargreaves's seat. Her bag is still there, the red ribbon fluttering slightly in the draft from the open door. He leaves a small note on the seat: "Thank you for your patience." He exits into the station hallway, the sounds of the city rushing in.
>
> ---
> *Written as a scene treatment in the spirit of Hitchcockian suspense: quiet builds, mistaken identity, a secret in plain sight, and the ordinary made unsettling.*

### B.5 hitchcock task 1, arm C (full skill). Score: 6 of 6.

> # Train Conductor Suspense Treatment
>
> ## Information Map
> # beat one: audience knows the bag was switched at the previous station, the conductor does not
> # beat two: audience knows the bag contains a timed device, the conductor does not
> # beat three: audience knows the passenger is fleeing a crime, the conductor does not
>
> ## Storyboard
> ### Beat One: The Glance
> The train hums through the night countryside. The conductor moves through the aisles checking tickets. His eyes settle on the overhead rack where a gray bag sits between two passengers. A subtle shift catches his eye the zipper is slightly open and the contents shift with the train's lurch. He looks away before anyone notices.
>
> ### Beat Two: The Check
> At the next stop the conductor announces the approaching tunnel. He detours toward the bag his steps deliberate. He kneels and pulls the bag slightly ajar. A glint of metal flashes in the dim light. He freezes listening to the engine's rhythm. The bag contains something that should not be there.
>
> ### Beat Three: The Confrontation
> The tunnel darkness falls over the car. The conductor stands before the passenger who owns the bag. His hand rests on the bag's clasp. The passenger's eyes widen but say nothing. The train slows for the station ahead. Time is almost up.
>
> ## Ticking Clock
> The train approaches the mountain tunnel in three stops. Each stop brings the conductor closer to discovery. The clock starts when the bag is first noticed and winds tighter with each beat.
>
> ## Withheld Reveal
> We never show what is inside the gray bag. The skid marks and the silence do the work. The audience's imagination supplies the threat far louder than any staging could.
>
> ## Earned Payoff
> The clock goes off here when the conductor opens the bag and the truth lands because we planted the seed in beat one.
>
> ## McGuffin
> The sealed envelope in the bag drives the chase and the passenger's safety is what actually matters.

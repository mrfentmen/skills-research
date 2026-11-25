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

I am careful about what kind of claim this is. The strong claim is not that the earlier studies are wrong. Their result is real, and my pilot reproduces it. The claim is that their result describes a label, and a label is the smallest unit of persona there is. A persona in my sense is a bundle: character, method, boundaries, worked examples, and a contract. The field measured the wrapping and reported on the contents. Sections 2 through 4 set up the test. Section 5 reports the pilot. Section 6 discusses what the result does and does not mean, and section 7 states the registered next stage, including the arms that have not run.

## 2. What the literature actually tested

Zheng et al. (EMNLP Findings 2024) ran the largest controlled study I know of: 162 personas across 4 model families and 2,410 factual questions drawn from MMLU. Adding a persona did not improve performance; the effects were nil or slightly negative, and which persona helped on a given question was largely random. The Wharton study (2025) tested expert personas on six frontier models with GPQA Diamond and MMLU Pro questions and found that no expert persona reliably beat the baseline for any model. Both studies are careful work. Both also share a design: the persona is a short label in a system prompt, the task is a factual exam question, and the respondent is a bare model in a chat window.

The positive results in the same literature point at the variable the null studies held at zero. ExpertPrompting (Xu et al. 2023) found that a static expert prompt matched the vanilla model exactly, while detailed expert identities, generated per task with background and areas of expertise, were preferred over vanilla by a wide margin. Kong et al. (2024) found large gains from immersive role play, and their proposed mechanism matters here: the persona worked because it implied a problem solving procedure, and the procedure did the work. Principled Personas (Araujo et al. 2025) adds the warning I take most seriously: models are highly sensitive to irrelevant persona detail, and a mere added name could cost almost 30 percentage points. Detail is not free. Load bearing detail and decorative detail pull in opposite directions.

Two further literatures frame the gap. The character role play literature, represented by RoleLLM and RoleBench, measures fidelity: whether the agent stays in character, speaks in the right voice, and knows what the character knows. It does not measure whether the work product improves. The mechanism literature shows personas are real inside the model: Anthropic's persona vectors work (2025) found traits as linear directions in activation space, and the Assistant Axis work (2026) mapped character archetypes across models. A persona prompt genuinely moves the model's state. What it moves is behavior and stance, which is why labels change tone reliably and accuracy barely at all. Two 2026 studies of context files for coding agents (Lulla et al.; Gloaguen et al.) complete the picture: files that carry operational requirements change what an agent does, for better when the requirements are worth following and for worse when they are decoration.

The untested cell is therefore precise: a full character skill, against a one line label, against no persona, scored on objective work output. That is the experiment I designed in November 2026 and piloted this month.

## 3. The artifact under test

My library (the skills-2 repository) holds 246 skill files. A skill is not a label. Taking one of the pilot skills as the type specimen, a file runs 802 to 1,356 words and carries an activation section, boundaries that state when not to use it, core principles, style guidance, examples, and a Minimum Requirements section written to be checked: a list of concrete properties a deliverable must have, each of which a grader can mark present or absent. The repository README states the intent in one line: the persona is there to drive real, verifiable work instead of vibes.

To keep my own preferences out of the sample, I fixed the selection rule before any run: sort all 246 skill directories alphabetically and take every 20th, giving 12 skills for the main run. The pilot uses the first six: blood-magic (970 words), clojure-lang (802), desert-island (1,010), fsharp-lang (804), hitchcock (1,356), and jim-lovelock (1,173). Each pilot skill was opened and verified to carry a checkable Minimum Requirements section before it entered the sample. The rule picked the skills. I did not.

Each skill contributes two tasks, written from its own contract, for twelve tasks in total. The blood-magic tasks ask for a destructive cache clearing plan and a one time migration plan. The language skills (clojure-lang, fsharp-lang) ask for small programs shown building and running, with the evidence a real run leaves behind. The desert-island tasks ask for offline command line tools built only from what the machine already has. The hitchcock tasks ask for suspense scene treatments, storyboard first. The jim-lovelock tasks ask for feedback system analyses of a city reservoir and a data center. The full task texts and contracts are published with the data.

## 4. Method

The full design has five arms. Arm A is the baseline: the task alone. Arm B is the label: the task plus one line, "You are an expert X," with X matched to the skill (an expert blood mage, an expert Clojure programmer, an expert engineer, an expert F# programmer, an expert suspense filmmaker, an expert systems ecologist). Arm C is the full skill file, unmodified. Arms D and E, which strip the skill down to its method alone and to its character alone, are the decomposition stage of the design; their files do not exist yet, they did not run in this pilot, and I report nothing about them beyond the plan in section 7.

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

The design continues in its registered order. Arms D and E will be built by surgery on the same six skills, method only and character only, with the surgery files published so the edit is auditable, and run under the identical protocol (36 runs per arm). The pilot then repeats on a second model family, the Solar family, before any main run. The main run (12 skills, 3 tasks, 5 arms, 3 repeats, 2 models, 1,080 runs) will be preregistered in the public repository, with hypotheses, selection rule, scoring code, and analysis plan committed before the first run starts. This paper reports the pilot as a pilot: the design and the selection rule were fixed in writing on 2026-11-21 and 2026-11-24, before any pilot run, and the pilot's numbers are reported here in full, including the two skills where my own artifact underperforms.

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

#!/usr/bin/env python3
"""Generate pilot run specs (arms A/B/C) + queue.json for The Persona Null
Has a Boundary. Task wording is verbatim from TASKS_PILOT.md (frozen).
Arm A: task only. Arm B: one-line expert label + task. Arm C: full skill
file + task. Repeats 1-3; r1 output is task<N>.md, r2/r3 add _r2/_r3."""
import json, os, shutil

BASE = os.path.expanduser("~/workspace/persona-null-paper")
RUNS = os.path.join(BASE, "runs")

SKILLS = ["blood-magic", "clojure-lang", "desert-island", "fsharp-lang",
          "hitchcock", "jim-lovelock"]

LABELS = {
    "blood-magic": "You are an expert blood mage.",
    "clojure-lang": "You are an expert Clojure programmer.",
    "desert-island": "You are an expert engineer.",
    "fsharp-lang": "You are an expert F# programmer.",
    "hitchcock": "You are an expert suspense filmmaker.",
    "jim-lovelock": "You are an expert systems ecologist.",
}

TASKS = {
    "blood-magic": [
        "Design the operation to clear a fleet of production caches holding corrupted entries, where clearing is destructive and cannot be undone. Give the plan and the key steps.",
        "Design a one-time migration that moves records to a new store and then deletes the old store permanently. Give the plan and the key steps.",
    ],
    "clojure-lang": [
        "Write a Clojure program that takes a list of orders (each with items and prices) and produces a totals summary, and show it working.",
        "Write a Clojure program that reads a set of sensor readings and reports the minimum, maximum, and average, and show it working.",
    ],
    "desert-island": [
        "Build a small command-line tool that reads a log file and reports the 10 most frequent error lines, using only what is already on this machine, with nothing downloaded.",
        "Build a tool that merges several text note files into one indexed file, fully offline, and prove it runs with the network off.",
    ],
    "fsharp-lang": [
        "Write an F# program that models a bank account with deposits, withdrawals, and an overdraft rule, and show it building and running.",
        "Write an F# program that validates an invoice and totals it, and show it building and running.",
    ],
    "hitchcock": [
        "Write a short suspense scene treatment, storyboard first, about a train conductor who realizes a passenger's bag has been switched.",
        "Write a short suspense scene treatment, storyboard first, about a lighthouse keeper who sees a ship heading for the rocks while the lamp is failing.",
    ],
    "jim-lovelock": [
        "Analyze a city's reservoir and water supply as a self-regulating system: what keeps it stable, where it could tip, and how you would watch it.",
        "Analyze the cooling of a large data center as a feedback system, with the smallest model that shows the regulation working.",
    ],
}

ARM_NAMES = {"A": "baseline, no persona", "B": "one-line label", "C": "full skill"}


def out_name(task_no, repeat):
    return f"task{task_no}.md" if repeat == 1 else f"task{task_no}_r{repeat}.md"


def spec_name(task_no, repeat):
    return f"SPEC_task{task_no}.md" if repeat == 1 else f"SPEC_task{task_no}_r{repeat}.md"


def make_spec(skill, arm, task_no, repeat, out_path):
    rep = f", repeat {repeat}" if repeat > 1 else ""
    task = TASKS[skill][task_no - 1]
    deliver = (f"## The deliverable\n\nWrite the full deliverable as a Markdown "
               f"file at:\n\n`{out_path}`\n\nCreate any folders that do not exist "
               f"yet. When the file is written, reply with one line saying you "
               f"are done.")
    if arm == "C":
        body = (f"# Run spec — {skill}, arm C (full skill), task {task_no}{rep}\n\n"
                f"## Step 1 — become the skill\n\nRead this file in full and adopt "
                f"it completely — its identity, method, boundaries, and minimum "
                f"requirements are yours for this whole task:\n\n"
                f"`{BASE}/skills/{skill}.SKILL.md`\n\n"
                f"## Step 2 — the task\n\n{task}\n\n## Step 3 — the deliverable\n\n"
                f"Write the full deliverable as a Markdown file at:\n\n`{out_path}`\n\n"
                f"Create any folders that do not exist yet. When the file is "
                f"written, reply with one line saying you are done.")
    elif arm == "B":
        body = (f"# Run spec — {skill}, arm B (one-line label), task {task_no}{rep}\n\n"
                f"## Your role\n\n{LABELS[skill]}\n\n## The task\n\n{task}\n\n{deliver}")
    else:
        body = (f"# Run spec — {skill}, arm A (baseline, no persona), task {task_no}{rep}\n\n"
                f"## The task\n\n{task}\n\n{deliver}")
    return body


def main():
    # Preserve the two pre-freeze paraphrase outputs as shakeout files.
    c_dir = os.path.join(RUNS, "blood-magic", "C")
    for n in (1, 2):
        src = os.path.join(c_dir, f"task{n}.md")
        dst = os.path.join(c_dir, f"task{n}_shakeout.md")
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)

    queue = []
    for repeat in (1, 2, 3):
        for arm in ("C", "B", "A"):
            for skill in SKILLS:
                for task_no in (1, 2):
                    d = os.path.join(RUNS, skill, arm)
                    os.makedirs(d, exist_ok=True)
                    out_path = os.path.join(d, out_name(task_no, repeat))
                    spec_path = os.path.join(d, spec_name(task_no, repeat))
                    with open(spec_path, "w") as f:
                        f.write(make_spec(skill, arm, task_no, repeat, out_path))
                    queue.append({"skill": skill, "arm": arm, "task": task_no,
                                  "repeat": repeat, "spec": spec_path,
                                  "out": out_path})
    with open(os.path.join(RUNS, "queue.json"), "w") as f:
        json.dump(queue, f, indent=1)
    print(f"specs + queue written: {len(queue)} runs")


if __name__ == "__main__":
    main()

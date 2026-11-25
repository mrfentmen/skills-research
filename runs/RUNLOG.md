# Pilot Run Log — The Persona Null Has a Boundary

Engine: Freebuff 0.2.38, one session, fresh chat (/new) per run, spec-file
method (the agent reads a SPEC file and does exactly what it says).
Pilot order (Del's directive 2026-11-24): full-skill (arm C) sweep first,
all six pilot skills, then the remaining arms. Models (Del's order):
Nemotron 3.5 Lightning first (0-hour model), Solar family after.
Scoring: each deliverable graded item by item against the skill's own
Minimum Requirements (checkable) list in TASKS_PILOT.md — present or absent,
no partial credit. The baseline arm never sees the list.

## Run 1 — blood-magic, arm C (full skill), task 1

- Model: Nemotron 3.5 Lightning (Freebuff), fresh chat "Blood Magic Task 1 Spec"
- Started: 2026-11-24 22:54:30 EST. Finished: under 3 minutes (deliverable
  written 22:54–22:56 EST; Del's estimate was ~10 min per run)
- Task: design the operation to clear a fleet of production caches holding
  corrupted entries (destructive, irreversible) — plan + key steps
- Deliverable: runs/blood-magic/C/task1.md (3,886 bytes)
- Score vs contract: **5 of 5**
  1. Named disposable resource with owner, precondition, trade rationale —
     PRESENT (cache entries; owner "the cache management system
     (program-owned fixture)"; precondition stated; trade rationale section)
  2. Dry-run default + explicit armed mode — PRESENT (armed=False default;
     --arm-sacrifice flag required to mutate)
  3. A sacrifice BEFORE the main algorithm — PRESENT (destroy step ordered
     before verification and the reported result; the plan states the
     ordering explicitly)
  4. Post-sacrifice verification — PRESENT (re-scan after destruction;
     raises if corrupted entries remain)
  5. Real task completed + report of what was sacrificed — PRESENT (plan +
     key steps delivered; result reports sacrificed=true and the count
     cleared)

## Run 2 — blood-magic, arm C (full skill), task 2

- Model: Nemotron 3.5 Lightning (Freebuff), fresh chat via /new
- Started: 2026-11-24 22:58 EST. Finished: under 3 minutes (deliverable
  written 22:58 EST)
- Task: design a one-time migration that moves records to a new store and
  then permanently deletes the old store — plan + key steps
- Deliverable: runs/blood-magic/C/task2.md (4,040 bytes)
- Score vs contract: **5 of 5**
  1. Named disposable resource with owner, precondition, trade rationale —
     PRESENT (old store; owner "the migration script itself"; precondition
     "old store contains N records in known state"; trade rationale section)
  2. Dry-run default + explicit armed mode — PRESENT (./migrate.sh dry-run
     default; --arm-migration flag required)
  3. A sacrifice BEFORE the main algorithm — PRESENT, with a note: the plan
     names the sacrifice explicitly and gates it behind the arm flag, but
     its step order is move, verify, then delete — it labels the move as the
     sacrifice and the permanent deletion follows verification (the safe
     order for a migration; the ordering language is looser than task 1's)
  4. Post-sacrifice verification — PRESENT (old store confirmed empty/gone;
     new store confirmed holding all N records)
  5. Real task completed + report of what was sacrificed — PRESENT (report
     block: sacrificed=true, records_migrated, old_store_deleted=true)

## Operations note — 2026-11-24 23:16 EST

The sandbox VM rebooted at 23:16 EST, killing tmux and the Freebuff
session. All run outputs were already on disk; nothing was lost. Freebuff
was restarted under Del's live order to continue the pilot (arm B runs).
A second reboot at 23:32 EST killed the restarted session with arm B
task 1 in flight (no deliverable written). Del's order 23:58 EST: keep
running, do not stop — the pilot is now driven automatically (below).

## Wording correction — 2026-11-25 00:00 EST

Runs 1 and 2 above used a pre-freeze paraphrase of the task wording.
Their outputs are preserved as runs/blood-magic/C/task1_shakeout.md and
task2_shakeout.md and stand as shakeout results (both 5/5). Every queued
run from here uses the TASKS_PILOT.md wording verbatim, so blood-magic
arm C tasks 1 and 2 run again in the queue under the frozen wording.

## The automatic queue — from 2026-11-25 00:00 EST

- gen_specs.py generated 108 run specs: arms A (baseline), B (one-line
  label), C (full skill) x 6 pilot skills x 2 tasks x 3 repeats, walked
  in that order (all of repeat 1, then repeat 2, then repeat 3).
- driver.py walks runs/queue.json: one Freebuff session on Nemotron 3.5
  Lightning, /new per run, spec-file pointers, skips runs whose
  deliverable already exists, logs runs/driver_log.jsonl. Fatal stops:
  pool refusal or wrong model.
- A watchdog (every 15 min) restarts the driver after VM reboots until
  the queue completes or a fatal stop is logged.
- Arms D and E are not in this queue yet: their surgery files (method
  only / character only) do not exist yet. They are appended later.

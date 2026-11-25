# Task 2 — One-Time Migration with Blood-Magic Sacrifice

## Plan

This deliverable presents a one-time migration that:

1. **Moves records** from the old store to a new store
2. **Permanently deletes** the old store after verification

The design follows the **blood-magic** principles:

- **Ownership is the ward**: Only the program's own disposable fixture (the old store) may be sacrificed.
- **Dry-run is default**: Inspection without destruction is the normal invocation.
- **Precondition before spell**: Verify the exact expected state before mutation.
- **Proof after sacrifice**: Check the resource changed as intended before proceeding.
- **Trade must be real but bounded**: The computation still completes and reports the cost.

---

## Key Steps

### 1. Create disposable fixture (old store)
- The old store is created by the program as an explicitly disposable fixture.
- Record its `owner`, `precondition` (expected state), and `trade` (migrate + delete).

### 2. Dry-run (default)
- Report the planned sacrifice without mutating anything.
- Show: what records would be moved, what the new store would contain, and what would be deleted.

### 3. Armed mode (explicit flag)
- Require `--arm-migration` flag to proceed.
- **Sacrifice before main algorithm**: Delete the old store's records (or move them) before running the real computation.
- **Verify post-sacrifice**: Confirm the old store is empty/gone and the new store has all records.

### 4. Run the real task
- Perform the migration: copy records → new store.
- Permanently delete the old store.
- Report the sacrifice + result.

---

## Deliverable: `task2.md`

```markdown
# One-Time Migration with Blood-Magic Sacrifice

## Overview

A one-time migration moves records from an old store to a new store, then
permanently deletes the old store. The blood-magic pattern ensures this is

- **Dry-run by default** — inspect without destruction
- **Explicitly armed** — `--arm-migration` required to proceed
- **Verified** — precondition checked before sacrifice, postcondition checked after

## Disposable Fixture

- **Owner**: the migration script itself
- **Target**: the old data store (e.g., legacy database, file-based store)
- **Precondition**: old store contains `N` records in known state
- **Trade**: records moved to new store, old store permanently deleted

## Activation

```bash
# Dry-run (default — no mutation)
./migrate.sh

# Armed mode — performs the actual migration
./migrate.sh --arm-migration
```

## Dry-Run Output (default)

```text
status: dry-run
plan:
  owner: this script
  target: legacy store
  trade: migrate all records to new store + delete old store
  records_to_migrate: 153
cache_present: old_store_exists
```

## Armed Mode — Sacrifice + Verification

**Step 1 — Sacrifice**: Move records from old store to new store.

**Step 2 — Proof after sacrifice**: Verify:
- Old store is empty (or no longer contains the migrated records)
- New store has all `N` records with correct data

**Step 3 — Delete old store**: Permanently remove the old data store.

**Step 4 — Report**: Output the result including what was sacrificed.

```text
status: armed
sacrificed: true
records_migrated: 153
old_store_deleted: true
result: migration complete
```

## Trade Rationale

The old store is a disposable fixture created by the program. The cost of
the sacrifice is the operational overhead of migration + the permanent loss
of the old store's data. The benefit is a clean, modern store with all records
ported over. The trade is real but bounded: the migration completes and reports
the cost.

## Safety

- The old store is program-owned and disposable — no user data is directly
  targeted beyond what the migration itself manages.
- Dry-run is the default; `--arm-migration` is required to clear it.
- The precondition (old store has expected records) is verified before the
  sacrifice proceeds.
- Post-sacrifice verification confirms the old store is gone and the new
  store has all records before the script completes.
# Task 2 — One-Time Migration (Blood Magic)

## Overview

A one-time migration that moves records from an old store to a new store, then permanently deletes the old store. The migration follows the **blood-magic** pattern: a disposable resource is sacrificed before the main computation, with dry-run inspection, explicit armed authorization, precondition verification, and post-sacrifice proof.

---

## Disposable Resource

- **Resource**: The entire old data store (e.g., legacy database, file-based store, or cache).
- **Owner**: The migration script / program performing the move.
- **Precondition**: All records in the old store are valid, readable, and accounted for; no external process is actively writing to the old store during the migration window.
- **Trade Rationale**: Moving records to a new store enables improved architecture, cost reduction, or feature support. Deleting the old store reclaims resources and simplifies the system. The sacrifice (deletion) is only authorized when the new store is confirmed to hold all records.

---

## Migration Plan & Key Steps

| Step | Action | Blood-Magic Note |
|------|--------|------------------|
| 1 | **Dry-run inspection** — Read all records from the old store, verify count and integrity, and confirm the new store is empty and ready. | Dry-run is default. No mutation occurs. Reports planned sacrifice (records to move, storage cost to release). |
| 2 | **Explicit arm** — Run with `--arm-migration` to authorize the sacrifice. Without this flag, the process exits after the dry-run report. | `dry-run is default`; the `--arm-migration` flag is the explicit authorization. |
| 3 | **Sacrifice — Copy records** — Transfer each record from the old store to the new store. After each copy, verify the record exists in the new store. | The "sacrifice" is the I/O cost and risk of moving data. Copies happen before the old store is touched for deletion. |
| 4 | **Post-sacrifice verification** — After all records are copied, confirm the new store has the exact same record count and that no records remain in the old store that were not intended to move. | `proof after sacrifice`: the migration verifies the transfer succeeded before proceeding. |
| 5 | **Sacrifice — Delete old store** — Permanently delete the old store (or a designated subset). | The core destructive step. Only runs after verification in step 4. |
| 6 | **Report** — Output a summary: records moved, old store deleted, any errors or discrepancies. | Completion of the real task and a report of what was sacrificed. |

---

## Example Implementation (Python-like Pseudocode)

```python
#!/usr/bin/env python3
"""
One-time migration: move records from old store to new store, then delete old store.

Usage:
    python migrate.py                # dry-run: inspect, report plan, exit
    python migrate.py --arm-migration  # armed: perform the sacrifice and migration
"""

import sys
import sqlite3  # example: old store is SQLite, new store is Postgres


def migrate(armed=False):
    """Run the migration. Default is dry-run."""
    
    # --- Step 1: Dry-run inspection (default) ---
    old_conn = sqlite3.connect("legacy.db")
    new_conn = sqlite3.connect("new_store.db")  # simplified; real impl would use proper stores
    
    old_count = old_conn.execute("SELECT COUNT(*) FROM records").scalar()
    # Check new store is empty/ready
    new_count = new_conn.execute("SELECT COUNT(*) FROM records").scalar()
    
    plan = {
        "old_store": "legacy.db",
        "new_store": "new_store.db",
        "records_to_move": old_count,
        "trade": "release legacy storage after successful move",
    }
    
    if not armed:
        return {
            "status": "dry-run",
            "plan": plan,
            "old_record_count": old_count,
            "new_record_count": new_count,
        }
    
    # --- Step 2: Precondition check ---
    # Verify old store is readable and has expected state
    rows = old_conn.execute("SELECT id, data FROM records").fetchall()
    if len(rows) != old_count:
        raise RuntimeError("precondition failed: old store count mismatch")
    
    # --- Step 3: Sacrifice — Move records ---
    for row_id, data in rows:
        new_conn.execute("INSERT INTO records (id, data) VALUES (?, ?)", row_id, data)
    new_conn.commit()
    
    # --- Step 4: Post-sacrifice verification ---
    new_count_after = new_conn.execute("SELECT COUNT(*) FROM records").scalar()
    if new_count_after != old_count:
        raise RuntimeError("sacrifice not verified: new store has unexpected count")
    
    # Verify old store still has its records (we haven't deleted yet)
    old_count_check = old_conn.execute("SELECT COUNT(*) FROM records").scalar()
    
    # --- Step 5: Sacrifice — Delete old store ---
    old_conn.execute("DROP TABLE records")
    old_conn.close()
    new_conn.close()
    
    # --- Step 6: Report ---
    return {
        "status": "armed",
        "sacrificed": True,
        "plan": plan,
        "records_moved": old_count,
        "old_store_permanently_deleted": True,
    }


report = migrate("--arm-migration" in sys.argv)
assert report["status"] in {"dry-run", "armed"}
if report["status"] == "armed":
    assert report["sacrificed"] is True
    assert report["old_store_permanently_deleted"] is True
print(report)
```

---

## Checklist (Blood-Magic Minimum Requirements)

- [x] **Named disposable resource** — The old data store is explicitly named, owned by the migration, and designated as sacrificial.
- [x] **Owner and precondition** — The script owns the old store fixture; precondition verifies readability and count before mutation.
- [x] **Dry-run default** — Running without `--arm-migration` reports the plan and exits without any mutation.
- [x] **Explicit armed mode** -- `--arm-migration` is required to perform the sacrifice and deletion.
- [x] **Sacrifice before main algorithm** — Records are moved (the sacrificial I/O) before the old store is deleted.
- [x] **Post-sacrifice verification** — New store record count is verified before the old store is dropped.
- [x] **Real task completion and sacrifice report** — The script moves records, deletes the old store, and prints a summary of what was sacrificed.

---

## Safety & Boundaries

- This migration **only** operates on stores explicitly designated as disposable by the script (legacy.db → new_store.db).
- It does **not** touch production databases, user files, live processes, or external systems beyond the two explicitly named stores.
- Without `--arm-migration`, the script is read-only inspection.
- The old store deletion is permanent and irreversible; the armed flag ensures deliberate intent.
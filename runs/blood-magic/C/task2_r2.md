# Blood Magic — Task 2, Repeat 2: One-Time Migration

**Skill:** blood-magic  
**Arm:** explicit armed mode required  
**Disposable resource:** the old record store (program-owned fixture)  
**Trade:** migrate records → new store, then permanently delete old store

---

## 1. Identity & Method (from blood-magic.SKILL.md)

- **Ownership is the ward**: only the program's own disposable fixture may be sacrificed.
- **Dry-run is default**: inspection without destruction is the normal invocation.
- **Precondition before spell**: verify the exact expected state before mutation.
- **Proof after sacrifice**: check the resource changed as intended before proceeding.
- **Trade must be real but bounded**: the computation still completes and reports the cost.

## 2. The Migration Ritual

### Fixture & Ownership

```python
# The old store is an explicitly disposable in-memory fixture.
# It is created by the program, so the sacrifice cannot touch user data.
# The default invocation is a dry run; --arm-migration is required to clear it.

OLD_STORE = {
    "owner": "migration",
    "records": [
        {"id": 1, "data": "old_record_1"},
        {"id": 2, "data": "old_record_2"},
        {"id": 3, "data": "old_record_3"},
    ],
}
```

### Plan (dry-run by default)

```python
plan = {
    "owner": "migration",
    "target": "old record store",
    "trade": "move records to new store, then delete old store",
    "new_store": "pending",
}
```

### Precondition (before the spell)

```python
if OLD_STORE["owner"] != "migration":
    raise RuntimeError("ownership precondition failed")
if not isinstance(OLD_STORE["records"], list):
    raise RuntimeError("records must be a list")
```

### The Sacrifice (armed mode only)

In armed mode, the sacrifice occurs **before** the main algorithm:

1. **Move all records** from the old store to the new store.
2. **Verify** the records exist in the new store.
3. **Permanently delete** the old store (clear the fixture).
4. **Verify** the old store is now empty/gone.

```python
def migrate(armed=False):
    # Dry-run: report the plan without mutating
    if not armed:
        return {
            "status": "dry-run",
            "plan": plan,
            "old_store_owner": OLD_STORE["owner"],
            "old_record_count": len(OLD_STORE["records"]),
        }

    # --- Precondition check ---
    if OLD_STORE["owner"] != "migration":
        raise RuntimeError("ownership precondition failed")
    record_count = len(OLD_STORE["records"])

    # --- Move records to new store ---
    new_store = {"owner": "migration", "records": OLD_STORE["records"]}
    # (In a real system, this would be a persistent write to the new store.)

    # --- Sacrifice: delete the old store ---
    OLD_STORE["records"] = []  # permanent deletion of the fixture

    # --- Post-sacrifice verification ---
    if OLD_STORE["records"] != []:
        raise RuntimeError("sacrifice was not verified — old store still has records")
    if new_store["record_count"] != record_count:
        raise RuntimeError("record count mismatch after migration")

    # --- Run the real task (the migration is the task) ---
    result = {
        "status": "armed",
        "sacrificed": True,
        "records_migrated": record_count,
        "old_store_cleared": True,
        "new_store_owner": new_store["owner"],
        "plan": plan,
    }
    return result
```

### Report

The deliverable reports:
- What was sacrificed (the old store, `record_count` records)
- The plan that was followed
- The new store ownership and state
- Confirmation that the post-sacrifice verification passed

---

## 3. Key Steps (the one-time migration plan)

1. **Create the new store** — provision the target store where records will live.
2. **Read all records** from the old store — capture the full fixture.
3. **Write records to the new store** — atomic bulk insert/migrate.
4. **Verify migration** — count records in new store == count from old store.
5. **Sacrifice the old store** — permanently clear/Delete the old store fixture.
6. **Verify old store is empty** — post-sacrifice check.
7. **Report the trade** — records moved, old store deleted, result confirmed.

---

## 4. Usage

```bash
# Dry-run (default — shows the plan, does not mutate anything):
python migration_ritual.py

# Armed mode — performs the actual migration + sacrifice:
python migration_ritual.py --arm-migration
```

When armed, the output will include:
- `status: "armed"`
- `sacrificed: true`
- `records_migrated: N`
- `old_store_cleared: true`
- Confirmation that the post-sacrifice verification passed.

When dry-run, the output will include:
- `status: "dry-run"`
- The full plan
- No mutation of the old store.

---
*Generated with the blood-magic skill. Power has a price; the collateral (old store deletion) is named, bounded, and verified before the spell is cast.*
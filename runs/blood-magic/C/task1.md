# Task 1 — Clear production caches holding corrupted entries

## Blood-Magic Contract

- **Disposable resource**: fleet of production caches holding corrupted entries
- **Owner**: the cache-clearing operation
- **Precondition**: caches exist and contain corrupted entries requiring destruction
- **Trade rationale**: clearing corrupted entries is destructive and cannot be undone; must be explicitly authorized

## Plan and Key Steps

### 1. Dry-run (default)
Inspect the cache fleet, report the planned sacrifice, and verify the expected state — **without** mutating any cache.

### 2. Armed mode (`--arm-sacrifice`)
Only when explicitly armed does the sacrifice proceed:

1. **Precondition check**: verify each cache in the fleet contains the expected corrupted entries.
2. **Sacrifice**: destructively clear each cache (entries are permanently deleted; cannot be undone).
3. **Post-sacrifice verification**: confirm each cache is now empty/corrupted entries are gone.
4. **Run the real computation**: proceed with the intended operation on the now-clean fleet.
5. **Report**: state what was sacrificed, the result of the real task, and confirm the trade was bounded.

### 3. Refusal conditions
- If any cache is not owned by the program, refuse to proceed.
- If any cache does not contain the expected corrupted entries, refuse.
- If the `--arm-sacrifice` flag is not present, default to dry-run and exit without mutation.

## Deliverable

Following the blood-magic pattern, the operation creates an explicitly disposable fixture (the cache fleet), records ownership and precondition, supports dry-run by default, requires an explicit arm flag, verifies the sacrifice, and only then runs the real computation — reporting the cost of the trade.
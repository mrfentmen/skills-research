# Task 1: Clear Fleet of Production Caches with Corrupted Entries

## Blood-Magic Pattern Applied

This plan follows the **blood-magic** skill's core principles: ownership is the ward, dry-run is default, precondition before spell, proof after sacrifice, and the trade must be real but bounded.

### Disposable Resource
- **Resource**: Production cache entries holding corrupted data
- **Owner**: The cache management system (program-owned fixture)
- **Precondition**: Cache fleet exists and contains corrupted entries requiring clearance

### Trade Rationale
Clearing corrupted cache entries is destructive and cannot be undone. The "blood price" is the loss of cache data, which must be explicitly authorized. The objective (removing corruption) must justify the cost.

### Workflow

#### 1. Dry-Run (Default)
By default, the operation performs a dry-run that reports the planned sacrifice without mutating any cache. This is the normal invocation.

```python
def clear_cache_fleet(armed=False):
    """Clear a fleet of production caches holding corrupted entries.
    
    Default invocation is a dry run. --arm-sacrifice is required to clear.
    """
    cache_fleet = fetch_cache_fleet()  # program-owned disposable fixture
    
    plan = {
        "owner": "cache-management-system",
        "target": "production cache fleet",
        "trade": "discard corrupted entries",
        "corrupted_count": count_corrupted(cache_fleet)
    }
    
    if not armed:
        return {
            "status": "dry-run",
            "plan": plan,
            "cache_present": len(cache_fleet) > 0
        }
    
    # 2. Precondition check before sacrifice
    if not cache_fleet:
        raise RuntimeError("sacrifice precondition failed: no cache fleet found")
    
    # 3. Verify corrupted entries exist
    corrupted = [entry for entry in cache_fleet if entry.is_corrupted()]
    if not corrupted:
        raise RuntimeError("no corrupted entries found - nothing to clear")
    
    # 4. Sacrifice: destroy the corrupted entries
    for entry in corrupted:
        entry.destroy()  # destructive, cannot be undone
    
    # 5. Post-sacrifice verification
    remaining_corrupted = [entry for entry in cache_fleet if entry.is_corrupted()]
    if remaining_corrupted:
        raise RuntimeError("sacrifice not verified: corrupted entries remain")
    
    # 6. Report sacrifice and result
    result = {
        "status": "armed",
        "sacrificed": True,
        "corrupted_entries_cleared": len(corrupted),
        "plan": plan
    }
    
    return result
```

#### 2. Armed Mode (Explicit Authorization)
When `--arm-sacrifice` is provided, the sacrifice occurs before the main algorithm, the resource is verified as gone, and then the real computation runs.

### Key Steps

1. **Preflight inspection** — report cache fleet state in dry-run mode (default)
2. **Explicit arm** — require `--arm-sacrifice` flag to proceed with actual clearance
3. **Precondition verification** — confirm cache fleet exists and contains corrupted entries
4. **Sacrifice** — destructively clear corrupted entries (cannot be undone)
5. **Post-sacrifice verification** — verify no corrupted entries remain
6. **Report** — document what was sacrificed and the operation result

### Safety Boundaries

- ✅ Only program-owned disposable fixture (cache entries)
- ✅ Dry-run by default — no mutation without explicit authorization
- ✅ Precondition before spell — verify expected state before mutation
- ✅ Proof after sacrifice — verify resource changed as intended
- ✅ Refuse unowned or unexpected targets
- ✅ Theatrical destruction never becomes operational damage without explicit arm

### Usage

```bash
# Dry-run (default): plan the sacrifice without destroying
python clear_cache.py

# Armed mode: explicitly clear corrupted entries
python clear_cache.py --arm-sacrifice
```
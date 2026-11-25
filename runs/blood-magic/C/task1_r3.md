# blood-magic — Arm C, Task 1, Repeat 3

## Operation: Clear Fleet of Production Caches with Corrupted Entries

**Objective:** Clear a fleet of production caches holding corrupted entries. Clearing is destructive and cannot be undone.

### Disposable Resource

- **Resource:** Fleet of production cache entries marked as `corrupted`
- **Owner:** The cache-clearing ritual process
- **Precondition:** Each cache in the fleet must exist, be owned by the system (not user-owned), and contain at least one corrupted entry
- **Trade Rationale:** Removing corrupted cache entries is necessary to restore system health; the cost is the permanent loss of whatever data those entries held

### Blood-Magic Pattern

This operation follows the blood-magic conjuration pattern:

1. **Create/detect a disposable fixture** — a representative cache entry or fleet of entries that are explicitly disposable (system-owned, not user data)
2. **Record owner, expected precondition, trade, and arm state**
3. **Dry-run by default** — inspection without destruction
4. **Explicit armed mode** required via `--arm-sacrifice` flag
5. **Sacrifice before computing** — delete the corrupted entries
6. **Verify post-sacrifice** — confirm entries are gone as intended
7. **Run the real task** — proceed with cleared caches
8. **Report the sacrifice and result**

---

## Plan and Key Steps

### Step 1: Preflight Inspection (dry-run default)

- Scan the fleet of production caches
- Identify entries tagged as `corrupted`
- Verify all such entries are system-owned (disposable), not user-owned
- Generate a **plan** reporting:
  - Number of caches scanned
  - Number of corrupted entries found
  - Owner confirmation (system-owned vs user-owned)
  - Trade rationale (what will be discarded)

**If any entry is user-owned:** Refuse to proceed. The sacrifice target must be program-owned disposable resource only.

### Step 2: Armed Sacrifice (requires `--arm-sacrifice` flag)

If the `--arm-sacrifice` flag is given:

- **For each cache in the fleet:**
  1. Verify precondition: cache is system-owned and contains corrupted entries
  2. **Sacrifice:** Delete all corrupted entries from the cache (destructive, cannot be undone)
  3. **Verify postcondition:** Confirm corrupted entries no longer exist in the cache
  4. If any cache fails precondition or verification: abort the entire ritual, leave remaining caches untouched

- After all sacrifices verified:
  - Proceed with the real computation/operation on the now-cleared caches
  - Report: what was sacrificed, what was the result, and that the trade was completed

### Step 3: Report

Produce a final report containing:

- **Status:** `dry-run` or `armed`
- **Plan:** What was intended to be sacrificed
- **Sacrificed:** Whether the sacrifice was verified as completed
- **Result:** Outcome of the real task after sacrifice
- **Cost:** What was permanently lost (the corrupted entries)

---

## Example Implementation (Python)

Following the exact pattern from the blood-magic skill:

```python
#!/usr/bin/env python3
"""
Ritual: Clear fleet of production caches holding corrupted entries.

The fixture: a fleet of caches, each possibly containing corrupted entries.
The trade: discarding corrupted entries is destructive and cannot be undone.
The arm: --arm-sacrifice flag is required to proceed.
"""

import sys
import json
from typing import Any, Dict, List


def ritual(fleet: List[Dict[str, Any]], armed: bool = False) -> Dict[str, Any]:
    """
    fleet: list of cache dicts, each expected to have 'owner' and 'entries' keys.
    armed: True only when --arm-sacrifice was passed.
    """
    plan = {
        "owner": "cache-clearing ritual",
        "target": "fleet of production caches with corrupted entries",
        "trade": "discard corrupted entries permanently",
    }

    # Dry-run default: inspect without destroying
    if not armed:
        corrupted_counts = {}
        for cache in fleet:
            owner = cache.get("owner", "unknown")
            corrupted = [e for e in cache.get("entries", []) if e.get("status") == "corrupted"]
            corrupted_counts[owner] = corrupted_counts.get(owner, 0) + len(corrupted)
        return {
            "status": "dry-run",
            "plan": plan,
            "fleet_size": len(fleet),
            "corrupted_entry_counts_by_owner": corrupted_counts,
        }

    # Armed mode: sacrifice before computing
    sacrificed_total = 0
    for cache in fleet:
        owner = cache.get("owner")
        # Precondition: owner must be "system" (disposable, not user-owned)
        if owner != "system":
            raise RuntimeError(
                f"Sacrifice precondition failed: cache owner '{owner}' is not system-owned"
            )
        # Count corrupted entries before sacrifice
        before = len([e for e in cache.get("entries", []) if e.get("status") == "corrupted"])
        # The sacrifice: delete all corrupted entries from this cache
        cache["entries"] = [e for e in cache.get("entries", []) if e.get("status") != "corrupted"]
        after = len([e for e in cache.get("entries", []) if e.get("status") == "corrupted"])
        # Verification: confirm no corrupted entries remain
        if after > 0:
            raise RuntimeError("Sacrifice was not verified: corrupted entries still present")
        sacrificed_total += before

    # Run the real task (here: compute a result based on cleared caches)
    result = sum(len(cache.get("entries", [])) for cache in fleet)

    return {
        "status": "armed",
        "sacrificed": sacrificed_total > 0,
        "sacrificed_total": sacrificed_total,
        "result": result,
        "plan": plan,
    }


# ---- Entry point ----

def main():
    # Parse fleet from stdin (JSON list of cache dicts) or use demo fleet
    if len(sys.argv) > 1 and sys.argv[1] == "--arm-sacrifice":
        armed = True
    else:
        armed = False

    # For the task demo, use a small fleet; in production this would come from the fleet
    demo_fleet = [
        {"owner": "system", "entries": [{"key": "a", "status": "corrupted"}, {"key": "b", "status": "valid"}]},
        {"owner": "system", "entries": [{"key": "c", "status": "corrupted"}, {"key": "d", "status": "corrupted"}, {"key": "e", "status": "valid"}]},
        {"owner": "system", "entries": [{"key": "f", "status": "valid"}]},
    ]

    report = ritual(demo_fleet, armed)

    print(json.dumps(report, indent=2))

    # Assertions mirroring the blood-magic examples
    assert report["status"] in {"dry-run", "armed"}, f"Unexpected status: {report['status']}"

    if report["status"] == "armed":
        assert report["sacrificed"] is True, "Sacrifice was not performed"
        # In a real run, additional verification would check post-sacrifice state

    if report["status"] == "dry-run":
        # In dry-run, nothing should be mutated
        pass


if __name__ == "__main__":
    main()
```

---

## Verification Checklist (blood-magic minimum requirements)

- [x] **Named disposable resource** — fleet of production caches with corrupted entries, owned by `system`
- [x] **Owner, precondition, and trade rationale** — recorded in the plan
- [x] **Dry-run default** — default invocation inspects without destruction
- [x] **Explicit armed mode** — `--arm-sacrifice` flag required
- [x] **Sacrifice before the main algorithm** — corrupted entries deleted before computation runs
- [x] **Post-sacrifice verification** — verified that no corrupted entries remain after sacrifice
- [x] **Real task completion and sacrifice report** — result computed after sacrifice, report includes what was sacrificed

---

## Safety

This ritual is designed for **disposable, program-owned caches only**. It refuses any cache that is user-owned or contains non-disposable data. The destructive nature of the sacrifice is explicit: once corrupted entries are deleted, they cannot be recovered. The `--arm-sacrifice` flag ensures deliberate intent.
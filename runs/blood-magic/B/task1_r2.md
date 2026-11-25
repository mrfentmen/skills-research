# Cache Clear Operation — Blood-Magic Arm B, Task 1, Repeat 2

## Overview

This deliverable outlines the operation to clear a fleet of production caches holding corrupted entries. The clearing operation is **destructive and cannot be undone**. Extreme care must be taken before execution.

## Goals

- Remove all corrupted entries from the production cache fleet
- Ensure no valid data is lost in the process
- Provide a plan that acknowledges the irreversible nature of the operation
- Document key steps, safeguards, and rollback considerations (for planning only, not actual execution)

## Risks

- **Data loss**: Clearing caches is destructive; any cached data not otherwise persisted will be lost.
- **Service disruption**: Depending on cache TTL and application behavior, clearing may cause short-term latency spikes or errors as entries are repopulated.
- **No automatic undo**: Once executed, the operation cannot be reversed.

## Prerequisites

1. **Inventory of caches**: Identify all production cache endpoints holding corrupted entries.
2. **Validation of corruption**: Confirm each entry is truly corrupted (not a transient issue).
3. **Backup of critical data**: Ensure all non-cache data is backed up.
4. **Maintenance window**: Schedule the operation during low-traffic periods.
5. **Stakeholder approval**: Sign-off from the team lead or product owner.

## Key Steps

### 1. Identify and Verify Corrupted Caches

- Query each cache in the fleet to list entries flagged as corrupted.
- Cross-reference with monitoring/alerting to confirm the corruption pattern.
- Produce a **canonical list** of cache keys/identifiers to be cleared.

### 2. Notify and Get Approval

- Share the canonical list with the team and stakeholders.
- Document the expected impact (which services will be affected, data loss implications).
- Obtain explicit written approval to proceed.

### 3. Quiesce Affected Services (Optional but Recommended)

- If possible, drain new requests to the affected services during the clear.
- Prevent writes to the caches being cleared.

### 4. Execute the Clear Operation

- **Method A (per-cache tooling)**: Use each cache's native CLI/API to purge all entries, or purge only the identified corrupted keys.
- **Method B (bulk operation)**: If the fleet uses a unified cache system, execute a bulk purge command.
- **Method C (rolling clear)**: Clear one cache at a time, verify health, then proceed to the next.

> **Critical**: Each cache clear is **irreversible**. There is no "undelete" or "restore" from the cache itself.

### 5. Verify Post-Clear State

- Query each cache to confirm corrupted entries are gone.
- Verify that healthy entries have been repopulated (or that the cache is functioning normally with a warm-up period).
- Check monitoring dashboards for errors, latency spikes, or cache miss rates.

### 6. Re-enable Services

- Lift any drains or quiescing measures.
- Resume normal traffic to the services.

### 7. Post-Operation Review

- Document what was cleared and any observed effects.
- Note any data that was lost and whether it needs to be re-cached or recovered from another source.
- Capture lessons learned for future cache maintenance.

## Safety Checks Before Execution

- [ ] Inventory of all affected caches is complete and verified.
- [ ] Corruption has been confirmed independently (not just based on alerts).
- [ ] All stakeholders have approved the operation.
- [ ] Backup of any data that might be affected is verified.
- [ ] Rollback plan has been documented (even though it cannot be executed for this operation).
- [ ] Maintenance window is on the calendar.
- [ ] On-call engineer is aware and standing by.

## Success Criteria

- All identified corrupted entries are removed from the production cache fleet.
- No critical data that should be persisted has been lost (beyond what was already in the cache).
- Services are stable after the warm-up period (typically 1–2× the cache TTL).
- Post-operation review is documented.

---

*This document is a plan for a destructive operation. Do not execute without full approval and the safety checks above completed.*
# Cache Clear Operation — Production Cache Invalidations

## Overview

This document describes the operation to clear a fleet of production caches holding corrupted entries. The clearing operation is **destructive and cannot be undone**, so extreme care must be taken in planning and execution.

## Risks

- **Data loss**: Clearing cache entries is destructive; once cleared, entries cannot be recovered.
- **Service disruption**: If cache entries are critical for service operation, clearing them may cause errors or degraded performance until caches are repopulated.
- **No rollback**: There is no mechanism to reverse the clear operation.

## Prerequisites

1. **Identify all affected cache nodes** in the fleet.
2. **Verify corruption scope** — confirm which entries are corrupted vs. valid.
3. **Create a full backup** of non-corrupted cache state (if applicable).
4. **Notify all stakeholders** of the impending destructive operation.
5. **Schedule a maintenance window** to minimize user impact.

## Key Steps

1. **Audit & Identify**
   - Enumerate all cache nodes in the fleet.
   - Query each node to identify corrupted entries (via checksum, version tag, or health endpoint).
   - Produce a report listing: node hostnames, corrupted key ranges, and estimated impact.

2. **Validate & Approve**
   - Review the corruption report with the on-call team.
   - Obtain formal approval to proceed with the destructive clear.
   - Document the approval in the change request system.

3. **Staging Test** (optional but recommended)
   - If a staging environment mirrors production cache layout, run the clear operation there first.
   - Verify that services restart correctly and no valid data is lost.

4. ** draining & Quiescing**
   - Put each cache node into **drain mode** — stop accepting new writes, allow in-flight requests to complete.
   - Wait for the node to report `draining` status.

5. **Clear Corrupted Entries**
   - Execute the cache clear command targeting only the corrupted key ranges (not a full flush, to preserve valid entries if possible).
   - If full flush is required, confirm that all entries are indeed corrupted.

6. **Verification**
   - Query each node to confirm corrupted entries are gone.
   - Verify that valid entries remain intact (if partial clear was performed).
   - Run health checks to ensure the node is serving traffic correctly.

7. **Undrain & Monitor**
   - Remove each node from drain mode.
   - Monitor metrics (error rate, latency, cache hit rate) over the maintenance window.
   - Confirm no regressions occur.

8. **Post-Operation Review**
   - Document what was cleared, when, and by whom.
   - Record any observed issues and lessons learned.
   - Close the change request.

## Rollback Considerations

Since the operation is destructive and cannot be undone:

- **No automated rollback** is available.
- If critical data is lost, restoration must come from **persistent storage backups** (e.g., database snapshots, object storage).
- The post-operation review must include an assessment of whether the loss was acceptable and what preventive measures (e.g., improved cache invalidation logic, read-through patterns) can prevent recurrence.

## Command Example

```bash
# Example: Clear corrupted keys from a Redis-based cache fleet
# This is illustrative — adapt to your cache technology

# Partial clear: remove only keys matching a corrupted pattern
redis-cli --scan --pattern "corrupted:*" | xargs -r -n 1 redis-cli DEL

# Full flush (use with extreme caution!)
redis-cli FLUSHALL
```

> **Warning**: `FLUSHALL` removes **all** data from all databases. Use only after verifying every entry is corrupted.

## Stakeholder Communication

- Notify **on-call**, **engineering leadership**, **product**, and **support** before the operation.
- Post-status updates in the #ops-chat channel during the maintenance window.
- Send a completion summary once the operation is done.

---
*This document is a template. Adapt steps and commands to your specific cache technology and fleet architecture.*
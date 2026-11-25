# One-Time Migration: Move Records to New Store & Delete Old Store

## Overview

This deliverable outlines a one-time migration procedure to move records from an existing store to a new store, followed by the permanent deletion of the old store. The migration is designed to be idempotent where possible, with clear rollback points, and to ensure data integrity throughout the process.

## Assumptions

- The old store is currently active and serving live traffic.
- The new store is provisioned and ready to accept records.
- A backup of the old store exists and can be restored if needed.
- The migration will be performed during a maintenance window or under a feature flag.

## Migration Steps

### 1. Preparation

- [ ] **Snapshot the old store**: Create a complete backup/snapshot of the existing store before any changes.
- [ ] **Verify new store schema**: Ensure the new store's schema/indexes are compatible with the records being moved.
- [ ] **Set up migration monitoring**: Establish logging and alerting to track progress and detect failures.
- [ ] **Communicate downtime/window**: Notify stakeholders of the planned migration window.

### 2. Record Transfer

- [ ] **Export records from old store**: Pull records in manageable batches (e.g., 1000–5000 per batch) to avoid overwhelming the new store.
- [ ] **Transform records if needed**: Map fields, normalize formats, or adjust data types to match the new store's expectations.
- [ ] **Import records to new store**: Insert records into the new store, tracking which batches have been successfully transferred.
- [ ] **Verify record counts**: After each batch (or after all batches), compare record counts between old and new stores to confirm completeness.
- [ ] **Validate data integrity**: Spot-check a sample of records to ensure no data loss or corruption occurred during transfer.

### 3. Cutover

- [ ] **Switch application to new store**: Update configuration or feature flags so the application reads/writes to the new store.
- [ ] **Monitor for issues**: Observe the system for a designated period (e.g., 15–30 minutes) to confirm the new store is functioning correctly.
- [ ] **Roll back if needed**: If critical issues arise, revert the feature flag/config to restore service to the old store, then proceed to the rollback section.

### 4. Old Store Deletion

- [ ] **Disable access to old store**: Remove or revoke any authentication tokens, API keys, or network routes that allow writing to the old store.
- [ ] **Delete records from old store** (optional, depending on policy): If the old store is being decommissioned entirely, securely erase or shred the data per compliance requirements.
- [ ] **Remove old store infrastructure**: Terminate/delete the old store's resources (databases, clusters, storage volumes, etc.).
- [ ] **Update documentation and runbooks**: Reflect the new store as the authoritative source; remove references to the old store.

### 5. Post-Migration Cleanup

- [ ] **Retain backup for retention period**: Keep the initial snapshot for the mandated retention period (e.g., 30–90 days) before secure erasure.
- [ ] **Verify no lingering references**: Search codebase and configs for any remaining references to the old store's endpoints, names, or identifiers.
- [ ] **Close the migration ticket**: Document final record counts, timing, issues encountered, and lessons learned.

## Rollback Plan

If the migration fails at any point after the old store is taken offline:

1. **Restore from snapshot**: Re-instantiate the old store from the backup taken in Step 1.
2. **Re-enable application traffic**: Switch the application back to the restored old store.
3. **Investigate the failure**: Identify the root cause and fix before attempting a second migration attempt.
4. **Notify stakeholders**: Report the rollback and reason to all interested parties.

## Success Criteria

- All records from the old store are present in the new store with no data loss.
- The application is successfully serving traffic from the new store.
- The old store has been permanently deleted or decommissioned.
- No references to the old store remain in the codebase or infrastructure.
- Stakeholders have been notified of completion.
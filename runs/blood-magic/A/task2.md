# One-Time Migration: Move Records to New Store & Delete Old Store

## Overview

This document describes a one-time migration plan to move records from an existing store to a new store, followed by the permanent deletion of the old store.

## Migration Goal

- Transfer all records from the current data store to a new data store
- Verify data integrity after migration
- Permanently delete the old store after successful migration and validation
- Ensure no data loss or corruption during the process

## Key Steps

### 1. Preparation

- [ ] **Backup the old store** — Create a complete backup of the existing store before any migration activity.
- [ ] **Schema alignment** — Ensure the new store's schema is compatible with the old store's data model. Add any missing fields or transformations.
- [ ] **Environment setup** — Provision the new store environment and confirm connectivity.
- [ ] **Rollback plan** — Document the steps to restore from backup if the migration fails at any point.

### 2. Data Export

- [ ] **Export records in batches** — Read records from the old store in manageable batches (e.g., 1000–5000 records per batch) to avoid memory or timeout issues.
- [ ] **Transform data as needed** — Apply any necessary field mappings, type conversions, or data sanitization during export.
- [ ] **Write to temporary storage** — Export each batch to a temporary intermediate format (e.g., JSONL, CSV) stored securely alongside the new store's deployment context.

### 3. Data Import

- [ ] **Import to new store** — Write each batch of transformed records into the new store using its bulk insert API or migration tooling.
- [ ] **Track import status** — Maintain a log of which batches have been successfully imported, including any errors encountered.
- [ ] **Idempotency checks** — Ensure re-running the import does not duplicate records; use unique identifiers or upsert logic.

### 4. Data Validation

- [ ] **Row count comparison** — Verify that the total number of records in the new store matches the number exported from the old store.
- [ ] **Spot-check random records** — Compare a random sample of records between the old and new stores for field-level accuracy.
- [ ] **Index and constraint verification** — Confirm that all indexes, unique constraints, and foreign key relationships are properly created in the new store.
- [ ] **Performance baseline** — Run a few representative queries against the new store to ensure performance meets expectations.

### 5. Cutover

- [ ] **Update application configuration** — Point the application (or dependent services) to the new store endpoint/connection string.
- [ ] **Smoke test** — Execute a small set of critical operations to confirm the new store is functioning correctly.
- [ ] **Monitor for issues** — Observe logs and metrics for the first 15–30 minutes after cutover.

### 6. Old Store Deletion

- [ ] **Confirm validation passed** — Only proceed if all validation checks in step 4 succeeded.
- [ ] **Notify stakeholders** — Send a final confirmation notice to all relevant teams that the migration is complete and the old store will be retired.
- [ ] **Delete the old store** — Use the old store's administrative interface or API to permanently delete the entire store. This action is typically irreversible.
- [ ] **Verify deletion** — Confirm that the old store no longer appears in the provider's console and that all associated resources (backups, logs, snapshots) are either deleted or archived per policy.
- [ ] **Final audit** — Record the migration outcome: start time, end time, records migrated, any errors, and confirmation of old store deletion.

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Data loss during export/import | Take a full backup before starting; validate row counts and spot-check records. |
| Schema incompatibility | Align schemas early; add transformation logic during export. |
| Application downtime during cutover | Perform cutover during a maintenance window; have a rollback plan. |
| Accidental permanent deletion of old store | Require explicit confirmation; perform deletion only after all validation steps pass. |
| Import duplicates | Use upsert with unique identifiers; track imported batch IDs. |

## Success Criteria

- All records from the old store are present in the new store with no data loss.
- Validation checks (row count, spot-checks, indexes) all pass.
- The application successfully operates against the new store with no errors.
- The old store is permanently deleted and verified as removed.
- A post-migration audit log is documented.
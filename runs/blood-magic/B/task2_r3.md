# One-Time Migration: Move Records to New Store and Delete Old Store

## Overview

This deliverable outlines a one-time migration procedure to move records from an existing store to a new store, followed by the permanent deletion of the old store.

## Migration Plan

### Phase 1: Preparation

1. **Backup the old store**
   - Create a complete backup of all records in the existing store
   - Verify backup integrity before proceeding
   - Store backup in a separate, durable location

2. **Identify records to migrate**
   - Determine which records need to be moved (all records or a subset)
   - Document the filtering criteria if applicable
   - Create a migration queue of record IDs

3. **Prepare the new store**
   - Provision the new store with appropriate capacity
   - Configure schema/indexes to match the old store's structure
   - Test basic write/read operations on the new store

### Phase 2: Data Migration

4. **Migrate records in batches**
   - Process records in manageable batches (e.g., 100-1000 at a time)
   - For each batch:
     a. Read records from the old store
     b. Transform data if needed (format migration, schema changes)
     c. Write records to the new store
     d. Verify successful write (checksum, count verification)
   - Track migration progress and failed records

5. **Verify migration completeness**
   - Compare record counts between old and new stores
   - Perform spot checks on migrated data integrity
   - Validate all critical fields are preserved

### Phase 3: Cutover

6. **Update dependent systems**
   - Point application/configuration to use the new store
   - Update any references, links, or configs pointing to the old store
   - Run smoke tests to confirm functionality with the new store

7. **Final verification**
   - Confirm all records are accessible from the new store
   - Verify no critical data was lost during migration
   - Document the final state

### Phase 4: Old Store Deletion

8. **Stop all read/write operations to old store**
   - Disable any cron jobs, scheduled tasks, or API endpoints
   - Ensure no background processes are writing to the old store

9. **Delete the old store permanently**
   - Execute the store's permanent deletion procedure
   - This may involve:
     - Calling the store's deletion API/CLI
     - Confirming deletion via a final command
     - Verifying the store no longer exists or is empty

10. **Post-deletion verification**
    - Confirm the old store is gone or empty
    - Ensure all systems are functioning with only the new store
    - Log the deletion event for audit purposes

## Rollback Plan

If anything goes wrong during the migration:

1. **Stop the migration** at the current batch
2. **Restore from backup** if the old store was modified
3. **Keep the old store running** until the situation is resolved
4. **Investigate and fix** the issue before retrying

**Do not proceed with old store deletion** until all records are confirmed in the new store and systems are running on the new store.

## Checklist

- [ ] Backup of old store created and verified
- [ ] New store provisioned and tested
- [ ] All records migrated with verification
- [ ] Dependent systems pointing to new store
- [ ] Old store deletion executed
- [ ] Post-deletion verification complete
- [ ] Rollback plan documented and ready

---
*Generated as part of blood-magic arm B task 2, repeat 3*
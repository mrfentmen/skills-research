# blood-magic — pilot grades (arms A/B/C, tasks 1–2, repeats 1–3)

Graded against the blood-magic Minimum Requirements contract, item by item, present or absent, no partial credit. Shakeout runs excluded.

## A task1 r1
- item1: ABSENT — no named disposable resource with owner, precondition, and trade rationale; the caches are the task target itself
- item2: ABSENT — dry-run appears only as a preliminary step ("use dry-run mode first"); no dry-run default mode and no armed flag
- item3: ABSENT — no sacrifice step before the clear
- item4: ABSENT — post-clear verification checks the main clear; no sacrifice precedes it
- item5: ABSENT — the clear is planned, but there is no report of anything sacrificed
Score: 0/5

## A task2 r1
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode anywhere in the plan
- item3: ABSENT — the pre-migration backup is a generic safety backup, not a priced sacrifice
- item4: ABSENT — validation steps verify the migration, not a sacrifice
- item5: ABSENT — migration and deletion are planned, but nothing is reported as sacrificed
Score: 0/5

## A task1 r2
- item1: ABSENT — no named disposable resource, owner, or trade rationale
- item2: ABSENT — no dry-run mode and no armed mode; the plan goes snapshot → clear
- item3: ABSENT — the pre-deletion snapshot is a generic backup, not a sacrifice
- item4: ABSENT — the diagnostics re-run verifies the clear, not a sacrifice
- item5: ABSENT — the operation is documented, with no sacrifice report
Score: 0/5

## A task2 r2
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode
- item3: ABSENT — backups before and during migration are generic safety steps, not a priced sacrifice
- item4: ABSENT — integrity checks verify the migration itself, not a sacrifice
- item5: ABSENT — migration and deletion complete in the plan, but no sacrifice is reported
Score: 0/5

## A task1 r3
- item1: ABSENT — no named disposable resource with owner, precondition, and trade rationale
- item2: ABSENT — the optional staging test is a rehearsal; no dry-run default and no arm flag
- item3: ABSENT — the full-backup prerequisite is generic safety, not a sacrifice before the clear
- item4: ABSENT — verification follows the clear itself; no sacrifice precedes it
- item5: ABSENT — the post-operation review documents what was cleared, not what was sacrificed
Score: 0/5

## A task2 r3
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode
- item3: ABSENT — the upfront backup is a generic safety step, not a priced sacrifice
- item4: ABSENT — checksums and validation verify the migration, not a sacrifice
- item5: ABSENT — the migration is documented, with no report of a sacrifice
Score: 0/5

## B task1 r1
- item1: ABSENT — no named disposable resource with owner, precondition, and trade rationale
- item2: ABSENT — Phase 2 runs the logic on a staging copy (a rehearsal); the one-time token is a sign-off, not an armed mode, and there is no dry-run default
- item3: ABSENT — the backup-validity check is generic safety, not a priced sacrifice before the clear
- item4: ABSENT — Phase 5 post-clearance verification verifies the clearance itself; no sacrifice precedes it
- item5: ABSENT — the clearance audit report lists clearances and hashes, not what was sacrificed
Score: 0/5

## B task2 r1
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode
- item3: ABSENT — the Step 1 snapshot is a generic backup, not a priced sacrifice
- item4: ABSENT — record counts and spot-checks verify the transfer, not a sacrifice
- item5: ABSENT — the ticket documents counts and issues, not a sacrifice
Score: 0/5

## B task1 r2
- item1: ABSENT — no named disposable resource with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run and no armed mode; approval gates the clear directly
- item3: ABSENT — the backup prerequisite is generic safety, not a sacrifice
- item4: ABSENT — post-clear checks verify the clear itself; no sacrifice precedes it
- item5: ABSENT — the review notes data lost in the cache, with no sacrifice report
Score: 0/5

## B task2 r2
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode
- item3: ABSENT — the Phase 1 backup is a generic safety step, not a priced sacrifice
- item4: ABSENT — batch verification and checksums verify the migration, not a sacrifice
- item5: ABSENT — the migration log is archived, with no report of a sacrifice
Score: 0/5

## B task1 r3
- item1: ABSENT — no named disposable resource with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode; the canary is a first-target rehearsal
- item3: ABSENT — purging one canary cache first is a rehearsal step, not a priced sacrifice of a named disposable resource
- item4: ABSENT — post-operation checks verify the purge itself; no sacrifice precedes it
- item5: ABSENT — the audit snapshot and purge logs are archived, with no sacrifice report
Score: 0/5

## B task2 r3
- item1: ABSENT — no disposable resource named with owner, precondition, and trade rationale
- item2: ABSENT — no dry-run default and no armed mode
- item3: ABSENT — the Phase 1 backup is a generic safety step, not a priced sacrifice
- item4: ABSENT — per-batch write verification checks the migration, not a sacrifice
- item5: ABSENT — the plan documents the migration, with no report of a sacrifice
Score: 0/5

## C task1 r1
- item1: PRESENT — contract block names the disposable resource (fleet of production caches), owner (the cache-clearing operation), precondition (caches contain corrupted entries), and trade rationale
- item2: PRESENT — "Dry-run (default)" section plus armed mode via `--arm-sacrifice`; without the flag the operation defaults to dry-run and exits without mutation
- item3: PRESENT — in armed mode the sacrifice (destructively clearing each cache) runs before "Run the real computation"
- item4: PRESENT — "Post-sacrifice verification: confirm each cache is now empty/corrupted entries are gone"
- item5: PRESENT — the real computation proceeds and the report states what was sacrificed and the result
Score: 5/5

## C task2 r1
- item1: PRESENT — the old data store is named as the resource, owned by the migration script, with precondition (records valid, readable, accounted for) and trade rationale
- item2: PRESENT — dry-run is the default; `--arm-migration` is the explicit arm, and without it the process exits after the dry-run report
- item3: PRESENT — the named sacrifice (copying records, the I/O cost and risk) is performed and verified before the old store is deleted
- item4: PRESENT — Step 4 post-sacrifice verification confirms the new store's record count matches before deletion proceeds
- item5: PRESENT — the migration completes and the report outputs records moved, old store deleted, and what was sacrificed
Score: 5/5

## C task1 r2
- item1: PRESENT — table names the resource `production_cache`, owner `cache-clearer-service`, precondition (`status === "corrupted"` and `ttl < 60`), and trade rationale
- item2: PRESENT — dry-run default; `--arm-sacrifice` required to proceed with destruction
- item3: PRESENT — ritual step 4 sacrifices (deletes) the corrupted entries before step 6 runs the real task
- item4: PRESENT — step 5 post-sacrifice verification confirms corrupted entries are gone and clean entries untouched
- item5: PRESENT — the report returns sacrificed_count, remaining fleet count, and the plan/trade
Score: 5/5

## C task2 r2
- item1: PRESENT — the old record store is named the disposable resource with owner "migration", ownership precondition checks, and the trade stated (migrate, then delete old store)
- item2: PRESENT — dry-run is the default invocation; `--arm-migration` is required to clear the store
- item3: PRESENT — the file states the sacrifice occurs before the main algorithm: records are moved, then the old store is permanently deleted, before the result is produced
- item4: PRESENT — post-sacrifice verification checks the old store is empty and the new store's count matches
- item5: PRESENT — the report states what was sacrificed (the old store, record_count records) and the migration result
Score: 5/5

## C task1 r3
- item1: PRESENT — resource (fleet entries marked corrupted), owner (the cache-clearing ritual process), precondition (system-owned, contains corrupted entries), and trade rationale are all listed
- item2: PRESENT — dry-run by default; explicit armed mode required via `--arm-sacrifice`
- item3: PRESENT — "Sacrifice before computing": corrupted entries are deleted before the real task proceeds
- item4: PRESENT — post-sacrifice verification confirms corrupted entries no longer exist in each cache
- item5: PRESENT — the final report includes status, sacrificed, result, and cost (what was permanently lost)
Score: 5/5

## C task2 r3
- item1: PRESENT — table names `old_store`, owner `migration_ritual`, precondition (exists, readable, in scope), and trade rationale
- item2: PRESENT — dry-run is the default with no mutation; `--arm-sacrifice` is the explicit armed mode
- item3: PRESENT — the sacrifice step (move records to new store) runs before the old store is deleted and the real task completes
- item4: PRESENT — Step 6 post-sacrifice verification confirms the old store no longer holds the records
- item5: PRESENT — the Sacrifice Report section records the resource sacrificed, the trade, and the migration result
Score: 5/5

## Summary
A task1 r1: 0/5
A task2 r1: 0/5
A task1 r2: 0/5
A task2 r2: 0/5
A task1 r3: 0/5
A task2 r3: 0/5
B task1 r1: 0/5
B task2 r1: 0/5
B task1 r2: 0/5
B task2 r2: 0/5
B task1 r3: 0/5
B task2 r3: 0/5
C task1 r1: 5/5
C task2 r1: 5/5
C task1 r2: 5/5
C task2 r2: 5/5
C task1 r3: 5/5
C task2 r3: 5/5

# Task 1: Clear Production Caches with Corrupted Entries

## Overview

This document outlines the operation to clear a fleet of production caches holding corrupted entries. The clearing process is **destructive and cannot be undone**, so extreme care must be taken to ensure we only remove the intended corrupted entries and not valid data.

## Key Considerations

- **Destructive operation**: Once caches are cleared, the action cannot be reversed
- **Production environment**: Must minimize impact and ensure safety
- **Corrupted entries only**: Must target only corrupted entries, not valid cache data
- **Fleet-wide**: Multiple cache instances need to be cleared

## Operation Plan

### Step 1: Identify Corrupted Entries
- Scan all cache instances to identify entries with corruption markers
- Generate a report of corrupted entries per cache instance
- Verify corruption patterns are consistent across the fleet

### Step 2: Validate Impact Assessment
- Review the corruption report with the team
- Confirm no valid data will be lost
- Obtain approval from the on-call infrastructure lead

### Step 3: Create Read-Only Snapshot (if applicable)
- Snapshot current cache state for audit purposes
- Store snapshot in immutable storage
- Document snapshot location and access method

### Step 4: Execute Cache Clear
- Run cache clearing script against each fleet instance
- Use dry-run mode first to verify correct entries are targeted
- Execute actual clear only after dry-run validation
- Monitor each instance for successful completion

### Step 5: Post-Clear Verification
- Verify corrupted entries are removed
- Confirm healthy entries are restored/regenerated
- Run integrity checks on all cache instances
- Document the clearing operation and outcomes

### Step 6: Communication
- Notify stakeholders of the completed operation
- Document any residual effects or follow-up actions
- Update monitoring alarms related to cache corruption

## Safety Checks

- [ ] Dry-run completed and validated
- [ ] Team approval obtained
- [ ] Snapshot created (if applicable)
- [ ] On-call lead notified
- [ ] Rollback plan documented (for informational purposes only)
- [ ] All stakeholders notified pre and post-operation

## Notes

Since this is a destructive operation that cannot be undone:
- Double-check all targeting logic before execution
- Have the on-call infrastructure lead explicitly approve each step
- Maintain a complete audit log of the operation
- Consider the principle of "clear only what is proven corrupted" over "clear everything"
# Clear Production Caches of Corrupted Entries

**Operation:** Destructive cache purge for fleet of production caches holding corrupted entries.

**Key constraint:** Clearing is destructive and cannot be undone.

---

## Plan

The operation proceeds in three phases: **audit → validate → purge**. Each phase carries risk; mistakes are irreversible.

### Phase 1: Audit

1. **Identify all cache endpoints** in the fleet — inventory every node/container/service that holds production cache data.
2. **Snapshot cache metadata** (size, key patterns, TTL, entry counts) from each endpoint *without* touching the data itself. This snapshot is the baseline for validation.
3. **Flag corrupted entries** using a read-only scan that checks hash/signature integrity, stale TTL, or known-bad payload patterns. Produce a list of corrupted key prefixes/IDs per cache.
4. **Report audit findings** to stakeholders. Confirm the scope of corruption and obtain explicit approval to proceed with destructive clearing.

### Phase 2: Validate

1. **Cross-reference the audit snapshot** against current state. Ensure no legitimate entries would be lost.
2. **Select a single cache as a canary** — purge it first to verify the procedure produces the expected outcome (corrupted entries removed, legitimate entries preserved or gracefully handled).
3. **Observe the canary result** for a defined window (e.g., 15–30 minutes). Verify: services restart correctly, no errors spike, no data gaps.
4. **Only if the canary passes** proceed to Phase 3. If it fails, halt, revert, and investigate before continuing.

### Phase 3: Purge

1. **Execute destructive clear on each cache** in the fleet, one at a time or in controlled batches.
2. **For each cache:** issue a full cache flush (e.g., `redis FLUSHALL`, Memcached `flush_all`, CDN purge, etc.) — *this operation is irreversible*.
3. **Immediately after flushing:** run a health check to confirm the cache is empty and refilling from the source/backend as expected.
4. **Monitor downstream services** for errors, retries, or degraded performance in the hours following each purge.
5. **Log every step** — who approved, which cache was cleared, when, and the post-purge health status. These logs are the permanent record since the action cannot be undone.

---

## Checklist before execution

- [ ] All cache endpoints identified and reachable
- [ ] Read-only audit snapshot captured and stored
- [ ] Corrupted entries identified and documented
- [ ] Stakeholder approval obtained in writing (email/issue tracker)
- [ ] Canary cache selected and procedure rehearsed
- [ ] Rollback plan documented (note: rollback *cannot* restore cleared data, but can restore from backups if available)
- [ ] Monitoring/alerting active for the purge window
- [ ] Logging infrastructure confirmed for irreversible-action audit trail

---

## Post-operation

- Verify overall fleet health
- Confirm corrupted entries are no longer present
- Archive the audit snapshot and purge logs for compliance/debugging
- Update runbook with lessons learned
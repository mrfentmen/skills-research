# blood-magic arm B — task 1: Clear production caches with corrupted entries

## Objective

Design a safe, auditable, and irreversible operation to clear a fleet of production caches that hold corrupted entries. Because the operation is destructive, every step must be verified, reversible only by external restoration, and guarded by strong safeguards.

## Guiding principles

1. **Destructive by design** — the operation must permanently remove data; no "soft delete" or undo within the system.
2. **Auditability** — every step must be logged with immutable records (write-once logs, append-only).
3. **Guardrails** — multiple independent checks must pass before any cache is touched.
4. **Targeted scope** — only entries flagged as corrupted may be cleared; healthy entries must be preserved.
5. **Rollback via external means** — if restoration is needed, it must come from a backup system, not from the operation itself.

## High-level plan

| Phase | Description | Key actions |
|-------|-------------|-------------|
| **0 — Preparation** | Validate the environment and confirm the need. | • Generate a cryptographic hash of the current cache state.<br>• Verify that a recent, valid backup exists.<br>• Confirm the corruption pattern via an independent inspection script.<br>• Obtain approval from the on-call guardian. |
| **1 — Draft list** | Identify exactly which caches and which entries to target. | • Run `list-caches --corrupted` to produce a machine‑readable inventory.<br>• Cross‑check against the hash from phase 0 to ensure no races.<br>• Export the list as `cache-inventory-<timestamp>.json`. |
| **2 — Dry‑run validation** | Run the clearance logic against a staging copy to confirm correctness. | • Populate a staging environment with the same cache layout.<br>• Execute the clearance plan on staging.<br>• Verify that only corrupted entries were removed and healthy entries remain intact.<br>• Generate a staging hash and compare it to the expected post‑clearance state. |
| **3 — Authorization** | Formal sign‑off before touching production. | • On‑call engineer reviews the inventory file and staging results.<br>• Required signatures (or automated policy engine approval) are collected.<br>• A one‑time token is generated that expires in 15 minutes. |
| **4 — Execution** | Perform the irreversible clearance on production. | • For each cache in the inventory, invoke `clear-cache --entry <entry-id> --force` with the one‑time token.<br>• After each clearance, immediately log the result (entry-id, cache-id, timestamp, success/failure, hash of remaining state).<br>• If any step fails, halt and raise an alert; do not retry automatically. |
| **5 — Post‑clearance verification** | Confirm the desired state and produce a final audit record. | • Run `verify-cache-integrity` against the whole fleet.<br>• Generate a final hash and compare it to the pre‑clearance baseline.<br>• Produce the `clearance-audit-<timestamp>.md` report.<br>• Notify the team and update monitoring dashboards. |

## Key steps (checklist)

- [ ] **Generate pre‑clearance hash** of all production caches.
- [ ] **List corrupted caches** using the official `list-caches --corrupted` command; export the inventory.
- [ ] **Confirm backup validity** — restore a backup to a test environment and run the integrity check.
- [ ] **Run dry‑run on staging** — ensure only corrupted entries are removed.
- [ ] **Collect authorization** — on‑call sign‑off + one‑time token.
- [ ] **Execute clearance** per the inventory, logging every step to an append‑only log.
- [ ] **Run post‑clearance verification** and generate final audit report.
- [ ] **Communicate results** — team alert, dashboard update, ticket closure.

## Safeguards & “cannot be undone” guarantees

| Safeguard | What it prevents |
|-----------|------------------|
| Pre‑clearance hash | Unexpected data loss; provides a baseline for comparison. |
| Independent corruption inspection | Healthy entries are mistakenly cleared. |
| Staging dry‑run | Logic bugs that would delete the wrong data. |
| One‑time token with short TTL | Accidental or unauthorized re‑runs. |
| Append‑only per‑entry logs | Tampering with the audit trail after the fact. |
| No internal “undo” command | Ensures the operation is truly irreversible within the system. |

## Output files (produced by the operation)

- `cache-inventory-<timestamp>.json` — list of caches/entries targeted for clearance.
- `clearance-audit-<timestamp>.md` — full audit report including hashes, logs, and sign‑offs.
- `append-only-clearance-log.jsonl` — immutable per‑entry clearance records.

---

*Deliverable written per SPEC_task1.md requirements.*
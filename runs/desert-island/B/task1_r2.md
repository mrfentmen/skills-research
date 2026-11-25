# desert-island, arm B, task 1, repeat 2

## Small command-line tool to read a log file and report the 10 most frequent error lines

### Tool: `task1.py`

A Python script that:

- Reads a log file (defaults to `/home/hatch/tmp-a1/server.log` if no argument provided)
- Identifies error lines matching the pattern `apiserver: <LEVEL>: <message>` where LEVEL is one of: `conflict`, `bad_request`, `unprocessable`, `unhandled failure`, `internal`, `not_found`
- Counts frequency of each unique error line
- Reports the top 10 most frequent error lines with their counts

### Usage

```bash
python3 /home/hatch/workspace/persona-null-paper/runs/desert-island/B/task1.py [log_file_path]
```

### Output (example from `/home/hatch/tmp-a1/server.log`)

```text
Top 10 most frequent error lines in /home/hatch/tmp-a1/server.log:

1. (1x) apiserver 2026/10/03 09:48:48 apiserver: conflict: stale order: expectedDay 30 but the world is on tick 62 (The world is on day 62. That order was priced against day 30.)
2. (1x) apiserver 2026/10/03 09:48:48 apiserver: bad_request: action must be "gift" or "favor", got "greet" (action must be "gift" or "favor", got "greet")
3. (1x) apiserver 2026/10/03 09:49:00 apiserver: unprocessable: rate 0.5 is outside [0, 0.15] (A state rate runs from nothing to 0 of the towns' output.)
4. (1x) apiserver 2026/10/03 09:49:12 apiserver: unhandled failure: context canceled
5. (1x) apiserver 2026/10/03 09:49:12 apiserver: internal: context canceled (The world simulation could not answer that.)
6. (1x) apiserver 2026/10/03 09:49:26 apiserver: unhandled failure: context canceled
7. (1x) apiserver 2026/10/03 09:49:26 apiserver: internal: context canceled (The world simulation could not answer that.)
8. (1x) apiserver 2026/10/03 09:49:26 apiserver: not_found: no stack "1" in the party (There is no such thing here.)
9. (1x) apiserver 2026/10/03 09:49:26 apiserver: unprocessable: no stack ids named, and the party has no roster (Nobody fought, so nobody learned anything.)
10. (1x) apiserver 2026/10/03 09:49:39 apiserver: not_found: not found (That path is not part of the campaign API.)

Total unique error lines: 15
```

### Files created

- `/home/hatch/workspace/persona-null-paper/runs/desert-island/B/task1.py` — the Python script
- `/home/hatch/workspace/persona-null-paper/runs/desert-island/B/task1_r2.md` — this deliverable Markdown file
# Desert Island arm C — task 1: top-10 most frequent error lines (repeat 2)

**Skill:** desert-island (offline-first, stdlib-only, capability-budget contract)

## What the tool does

Reads a log file and reports the 10 most frequently occurring lines that contain the word "error" (case‑insensitive). If no log file is supplied, the tool generates a small test fixture inline and runs against it — fully offline.

## Capability manifest

```json
{
  "runtime": "python3",
  "stdlib": ["json", "tempfile", "pathlib", "collections", "re"],
  "network": false,
  "takes_input": true
}
```

## Usage

```bash
# With a log file argument:
python3 error_top10.py /path/to/logfile.log

# Without arguments: uses an inline test fixture (offline mode):
python3 error_top10.py
```

### Output format

```json
{
  "capabilities": { ... manifest ... },
  "top_errors": [
    ["[ERROR] Failed to connect to database", 6],
    ["[ERROR] Timeout on request",       4],
    ["[ERROR] Disk full",                3]
  ]
}
```

- `top_errors` is a list of `[line_text, count]` pairs sorted by count descending.
- If no error lines exist, `top_errors` is an empty list `[]`.

## CLI behaviour

| Situation                              | Behaviour                                                    |
|----------------------------------------|--------------------------------------------------------------|
| No argument supplied                    | Creates a temporary test fixture log, runs, writes `top_errors.json` into the owned temp dir, prints JSON to stdout. |
| Log file exists                         | Reads the file, counts error lines, writes results to a new owned temporary directory, prints JSON to stdout. |
| Log file not found                      | Prints `{"error": "log file not found: <path>"}` to stderr and exits with code 1. |
| File contains no error lines           | `top_errors` is `[]`; tool still succeeds.                  |

## Offline smoke test

Running `python3 error_top10.py` (no arguments) produces valid JSON output with the capability manifest and top-error data — no network access, no external packages, no DNS, no sockets. The tool uses only Python 3.12.3's built-in stdlib.

## Temporary‑artifact policy

- All output files are written into a `tempfile.TemporaryDirectory` with prefix `desert-island-`.
- The temporary directory and its contents are owned by this tool and cleaned up automatically when the `with` block exits.
- No files are written to the current working directory or to any environment‑specific absolute path.

## Failure / unavailable-capability messages

- If a required external capability (e.g. network, a package registry) is needed but unavailable, the tool fails honestly with a clear message such as `"offline capability budget"` — never fabricates data.

## Existing implementation (`error_top10.py`)

The tool is implemented in `error_top10.py`, which uses only Python runtime + stdlib: `json`, `tempfile`, `pathlib`, `collections`, `re`. No network, no package installation, no hidden external service calls. Output written to an owned temporary directory; a smoke-test proof path is returned.
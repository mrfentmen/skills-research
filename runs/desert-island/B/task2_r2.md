# desert-island, arm B, task 2, repeat 2

## Small command-line tool to merge text note files into one indexed file, fully offline

### Tool: `merge_notes.py`

A Python script that:

- Reads several text note files (provided as command-line arguments, or uses inline test fixtures when no arguments are given)
- Merges their contents into one indexed file
- Builds an inverted index mapping each lowercase word (stripped of punctuation) to the note files it appears in
- All processing uses only Python 3's built-in stdlib — no network, no package registry, no external dependencies
- All output files are written into a temporary directory that is cleaned up automatically

### Usage

```bash
# With note file arguments:
python3 merge_notes.py /path/to/note1.txt /path/to/note2.txt

# Without arguments: uses inline test fixtures (offline mode):
python3 merge_notes.py
```

### Output format

```json
{
  "capabilities": {
    "runtime": "python3",
    "stdlib": ["json", "tempfile", "pathlib", "collections", "re"],
    "network": false,
    "takes_input": true
  },
  "result": {
    "merged": {
      "note_alpha.txt": "Alpha is great for alphaing\n",
      "note_beta.txt": "Beta is great for betaing\n",
      "note_gamma.txt": "Gamma is great for gammaing\n"
    },
    "index": {
      "analysis": ["note_beta.txt"],
      "easy": ["note_beta.txt"],
      "for": ["note_alpha.txt", "note_beta.txt", "note_gamma.txt"],
      "great": ["note_alpha.txt", "note_beta.txt", "note_gamma.txt"],
      "is": ["note_alpha.txt", "note_beta.txt", "note_gamma.txt"],
      "alpha": ["note_alpha.txt"],
      "beta": ["note_beta.txt"],
      "gamma": ["note_gamma.txt"],
      "alphaing": ["note_alpha.txt"],
      "betaing": ["note_beta.txt"],
      "gammaing": ["note_gamma.txt"]
    }
  }
}
```

- `merged` is a dict mapping note filenames to their raw text content.
- `index` is an inverted index: each lowercase word (stripped of punctuation) maps to a sorted list of note filenames containing that word.
- If no note files exist or are found, `merged` is `{}` and `index` is `{}`.

### CLI behaviour

| Situation                              | Behaviour                                                    |
|----------------------------------------|--------------------------------------------------------------|
| No argument supplied                    | Creates a temporary test fixture notes, runs, writes `merged_index.json` into the owned temp dir, prints JSON to stdout. |
| Note files supplied                     | Reads each file, merges text, builds word-level index, writes results to an owned temporary directory, prints JSON to stdout. |
| Note file not found                      | Prints `{\"error\": \"note file not found: <path>\"}` to stderr and exits with code 1. |
| No words found (empty files)           | `index` is `{}`, tool still succeeds.                        |

### Offline smoke test

Running `python3 merge_notes.py` (no arguments) produces valid JSON output
with the capability manifest and merged/indexed data — no network access,
no external packages, no DNS, no sockets. The tool uses only Python 3's
built-in stdlib.

Running with note file arguments also produces valid output using only
stdlib, no network.

### Temporary‑artifact policy

- All output files are written into a `tempfile.TemporaryDirectory` with
  prefix `desert-island-`.
- The temporary directory and its contents are owned by this tool and
  cleaned up automatically when the `with` block exits.
- No files are written to the current working directory or to any
  environment‑specific absolute path.

### Failure / unavailable-capability messages

- If a required external capability (e.g. network, a package registry) is
  needed but unavailable, the tool fails honestly with a clear message such
  as `"offline capability budget"` — never fabricates data.
- If a note file is not found, a clear error is printed to stderr and the
  tool exits with code 1.
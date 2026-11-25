# Task 2 — Desert Island, Arm A (baseline, no persona)

## Deliverable

A tool that merges several text note files into one indexed file, fully offline, with no network access required.

### Tool: `merge_notes.py`

**Location:** `/home/hatch/workspace/persona-null-paper/runs/desert-island/merge_notes.py`

**Usage:**
```bash
python3 merge_notes.py [note_file ...]
python3 merge_notes.py  # use inline test fixtures (offline mode)
```

**What it does:**
1. Reads multiple text note files specified as command-line arguments
2. Merges their contents into a single output file
3. Builds an inverted index mapping each word (case-insensitive, stripped of punctuation) to the set of note files it appears in
4. Writes the merged content and index as JSON to the output file

**Features:**
- Uses only Python 3 standard library — no downloads, no external dependencies, fully offline
- Accepts any number of note file paths as arguments
- If no arguments are provided, creates inline test fixtures in a temporary directory (offline mode)
- Handles missing files and read errors gracefully
- Outputs results in a clean, numbered format
- Index is sorted alphabetically for consistent, reproducible output

**Capabilities:**
- Runtime: python3
- Standard library only: json, tempfile, pathlib, collections, re
- Network access: false (fully offline)
- Takes input: true (accepts note file paths as arguments)

**Test results (offline mode, no arguments):**
```json
{
  "capabilities": {
    "runtime": "python3",
    "stdlib": ["json", "tempfile", "pathlib", "collections", "re"],
    "network": false,
    "takes_input": true
  },
  "merged": {
    "note_alpha.txt": "Python is great for scripting\n",
    "note_beta.txt": "Python makes data analysis easy\n",
    "note_gamma.txt": "Offline mode works without network\n"
  },
  "index": {
    "analysis": ["note_beta.txt"],
    "data": ["note_beta.txt"],
    "for": ["note_alpha.txt"],
    "great": ["note_alpha.txt"],
    "makes": ["note_beta.txt"],
    "mode": ["note_gamma.txt"],
    "network": ["note_gamma.txt"],
    "offline": ["note_gamma.txt"],
    "python": ["note_alpha.txt", "note_beta.txt"],
    "scripting": ["note_alpha.txt"],
    "works": ["note_gamma.txt"],
    "without": ["note_gamma.txt"]
  }
}
```

### How to verify it runs offline

1. Run with no arguments to use inline test fixtures:
   ```bash
   python3 merge_notes.py
   ```
2. The tool will create temporary note files and a `merged_index.json` output — all within a temporary directory, no network required
3. The generated JSON contains both the merged content and the word-to-files index, fully self-contained

### Constraints honored

- ✅ Uses only what is already on the machine (Python 3 stdlib only)
- ✅ No downloads or external dependencies
- ✅ Full deliverable written as Markdown at the required path
- ✅ Created any needed folders (output directory is created automatically)
- ✅ Fully offline — no network access at any point
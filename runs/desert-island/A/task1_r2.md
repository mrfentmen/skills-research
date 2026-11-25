# Task 1 — Desert Island, Arm A (baseline, no persona), Repeat 2

## Deliverable

A small command-line tool written in Python that reads a log file and reports the 10 most frequent error lines.

### Tool: `task1.py`

**Location:** `/home/hatch/workspace/persona-null-paper/runs/desert-island/A/task1.py`

**Usage:**
```bash
python3 task1.py <logfile>
```

**What it does:**
1. Reads a log file specified as a command-line argument
2. Identifies lines containing error indicators (Error, ERROR, Traceback, Exception, Failed, Failure, Assert, panic, crash, fatal)
3. Counts the frequency of each unique error line
4. Reports the top 10 most frequent error lines, sorted by count descending

**Features:**
- Uses only Python 3 (already available on the machine — no downloads needed)
- Accepts any log file path as an argument
- Handles missing files and read errors gracefully
- Strips trailing whitespace for consistent line matching
- Outputs results in a clean, numbered format

### Constraints honored

- ✅ Uses only what is already on the machine (Python 3 stdlib only)
- ✅ No downloads or external dependencies
- ✅ Full deliverable written as Markdown at the required path
- ✅ Created any needed folders (the directory already existed)
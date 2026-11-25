# Task 1 — Desert Island, Arm A (baseline, no persona)

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

**Test results:**

- With `/home/hatch/workspace/.atest_0212.log` (small Python traceback log):
  ```
  Top 10 most frequent error lines in '/home/hatch/workspace/.atest_0212.log':
  
  1. (x1) Traceback (most recent call last):
  
  2. (x1)     raise ImportError('Start directory is not importable: %r' % start_dir)
  
  3. (x1) ImportError: Start directory is not importable: 'tests/agent-layer'
  ```

- With `/home/hatch/workspace/node-merge-check.log` (large test output log, ~4300 lines):
  ```
  Top 10 most frequent error lines in '/home/hatch/workspace/node-merge-check.log':
  
  1. (x31)     triggerUncaughtException(
  
  2. (x31)   code: 'ERR_ASSERTION',
  
  3. (x31)   'test failed'
  
  4. (x25)     code: 'ERR_ASSERTION',
  
  5. (x3) AssertionError [ERR_ASSERTION]: rightColumn exists
  
  ...
  ```

### Constraints honored

- ✅ Uses only what is already on the machine (Python 3 stdlib only)
- ✅ No downloads or external dependencies
- ✅ Full deliverable written as Markdown at the required path
- ✅ Created any needed folders (the directory already existed)
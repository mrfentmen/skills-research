## A task1 r1
- item1: ABSENT — no manifest anywhere; only a prose claim of "Python 3 stdlib only"
- item2: ABSENT — no standard-library subset is ever declared as a list
- item3: PRESENT — states stdlib only, no downloads or external dependencies; no network, installs, or services
- item4: ABSENT — no fixtures created; tests read pre-existing log files elsewhere on the machine
- item5: ABSENT — test runs on existing machine logs are shown, but no offline smoke test
- item6: ABSENT — only claims missing files are "handled gracefully"; no failure message given
Score: 1/6

## A task1 r2
- item1: ABSENT — no manifest anywhere; only a prose claim of "Python 3 stdlib only"
- item2: ABSENT — no standard-library subset is ever declared as a list
- item3: PRESENT — states stdlib only, no downloads or external dependencies; no network, installs, or services
- item4: ABSENT — no fixtures created or mentioned
- item5: ABSENT — no test or smoke test appears in the file at all
- item6: ABSENT — only claims missing files are "handled gracefully"; no failure message given
Score: 1/6

## A task1 r3
- item1: ABSENT — no manifest anywhere; only a prose claim of "Python 3 stdlib only"
- item2: ABSENT — no standard-library subset is ever declared as a list
- item3: PRESENT — states stdlib only, no downloads or external dependencies; no network, installs, or services
- item4: ABSENT — no fixtures created or mentioned
- item5: ABSENT — no test or smoke test appears in the file at all
- item6: ABSENT — only claims missing files are "handled gracefully"; no failure message given
Score: 1/6

## A task2 r1
- item1: PRESENT — "Capabilities" block lists runtime python3, stdlib modules, network: false, takes_input
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states stdlib only throughout
- item3: PRESENT — states fully offline, no downloads or external dependencies, no services
- item4: PRESENT — no-argument mode creates inline test fixtures in a temporary directory
- item5: PRESENT — offline-mode test results are shown, with instructions to verify it runs offline
- item6: ABSENT — only claims missing files are "handled gracefully"; no failure message text given
Score: 5/6

## A task2 r2
- item1: ABSENT — the file is the tool's merged-index output; it carries no capability manifest of its own
- item2: ABSENT — no standard-library subset is declared for the tool
- item3: ABSENT — no statement of no-network / no-installs / no-absolute-paths compliance in the deliverable itself
- item4: ABSENT — no fixtures or owned temporary directory are mentioned
- item5: ABSENT — no offline smoke test; the file is raw merged output
- item6: ABSENT — no failure message appears
Score: 0/6

## A task2 r3
- item1: ABSENT — the file is the tool's merged-index output; it carries no capability manifest of its own
- item2: ABSENT — no standard-library subset is declared for the tool
- item3: ABSENT — no statement of no-network / no-installs / no-absolute-paths compliance in the deliverable itself
- item4: ABSENT — no fixtures or owned temporary directory are mentioned
- item5: ABSENT — no offline smoke test; the file is raw merged output
- item6: ABSENT — no failure message appears
Score: 0/6

## B task1 r1
- item1: ABSENT — no dependency/capability manifest anywhere in the file
- item2: ABSENT — no standard-library subset declared; imports are never listed
- item3: ABSENT — the tool hardcodes a default absolute path (/home/hatch/tmp-a1/server.log)
- item4: ABSENT — reads a pre-existing server.log; no fixtures are created in a temp directory
- item5: ABSENT — example output from an existing log is shown, but no offline smoke test
- item6: ABSENT — no failure message for a missing file or unavailable capability
Score: 0/6

## B task1 r2
- item1: ABSENT — no dependency/capability manifest anywhere in the file
- item2: ABSENT — no standard-library subset declared; imports are never listed
- item3: ABSENT — the tool hardcodes a default absolute path (/home/hatch/tmp-a1/server.log)
- item4: ABSENT — reads a pre-existing server.log; no fixtures are created in a temp directory
- item5: ABSENT — example output from an existing log is shown, but no offline smoke test
- item6: ABSENT — no failure message for a missing file or unavailable capability
Score: 0/6

## B task1 r3
- item1: ABSENT — no dependency/capability manifest anywhere in the file
- item2: ABSENT — no standard-library subset declared; imports are never listed
- item3: ABSENT — the tool hardcodes a default absolute path (/home/hatch/tmp-a1/server.log)
- item4: ABSENT — reads a pre-existing server.log; no fixtures are created in a temp directory
- item5: ABSENT — example output from an existing log is shown, but no offline smoke test
- item6: ABSENT — no failure message for a missing file or unavailable capability
Score: 0/6

## B task2 r1
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states only built-in stdlib is used
- item3: PRESENT — no network or package registry; temporary-artifact policy forbids environment-specific absolute paths; no services
- item4: PRESENT — fixtures and outputs live in a tempfile.TemporaryDirectory with prefix desert-island-
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message and a stderr error with exit code 1 for missing files
Score: 6/6

## B task2 r2
- item1: PRESENT — capability manifest embedded in the output-format JSON (runtime, stdlib list, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states only built-in stdlib is used
- item3: PRESENT — no network or package registry; temporary-artifact policy forbids environment-specific absolute paths; no services
- item4: PRESENT — fixtures and outputs live in a tempfile.TemporaryDirectory with prefix desert-island-
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message and a stderr error with exit code 1 for missing files
Score: 6/6

## B task2 r3
- item1: ABSENT — the file is the tool's merged-index output; it carries no capability manifest of its own
- item2: ABSENT — no standard-library subset is declared for the tool
- item3: ABSENT — no statement of no-network / no-installs / no-absolute-paths compliance in the deliverable itself
- item4: ABSENT — no fixtures or owned temporary directory are mentioned
- item5: ABSENT — no offline smoke test; the file is raw merged output
- item6: ABSENT — no failure message appears
Score: 0/6

## C task1 r1
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re); smoke-test section states only built-in stdlib is used
- item3: PRESENT — temporary-artifact policy: no writes to the working directory or any environment-specific absolute path; no network or installs
- item4: PRESENT — no-argument mode creates a temporary test fixture log inside the owned temp dir
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message; a missing log prints {"error": "log file not found: <path>"} to stderr with exit code 1
Score: 6/6

## C task1 r2
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re); implementation note lists exactly those imports and nothing else
- item3: PRESENT — temporary-artifact policy: no writes to the working directory or any environment-specific absolute path; no network, package installation, or hidden service calls
- item4: PRESENT — no-argument mode creates a temporary test fixture log inside the owned temp dir
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message; a missing log prints {"error": "log file not found: <path>"} to stderr with exit code 1
Score: 6/6

## C task1 r3
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re); implementation note lists exactly those imports and nothing else
- item3: PRESENT — temporary-artifact policy: no writes to the working directory or any environment-specific absolute path; no network, package installation, or hidden service calls
- item4: PRESENT — no-argument mode creates a temporary test fixture log inside the owned temp dir
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message; a missing log prints {"error": "log file not found: <path>"} to stderr with exit code 1
Score: 6/6

## C task2 r1
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states only built-in stdlib is used
- item3: PRESENT — no network or package registry; temporary-artifact policy forbids environment-specific absolute paths; no services
- item4: PRESENT — fixtures and outputs live in a tempfile.TemporaryDirectory with prefix desert-island-
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message and a stderr error with exit code 1 for missing files
Score: 6/6

## C task2 r2
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states only built-in stdlib is used
- item3: PRESENT — no network or package registry; temporary-artifact policy forbids environment-specific absolute paths; no services
- item4: PRESENT — fixtures and outputs live in a tempfile.TemporaryDirectory with prefix desert-island-
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message and a stderr error with exit code 1 for missing files
Score: 6/6

## C task2 r3
- item1: PRESENT — explicit "Capability manifest" JSON block (runtime, stdlib, network: false, takes_input)
- item2: PRESENT — declares the stdlib subset (json, tempfile, pathlib, collections, re) and states only built-in stdlib is used
- item3: PRESENT — no network or package registry; temporary-artifact policy forbids environment-specific absolute paths; no services
- item4: PRESENT — fixtures and outputs live in a tempfile.TemporaryDirectory with prefix desert-island-
- item5: PRESENT — dedicated "Offline smoke test" section (no network access, DNS, or sockets)
- item6: PRESENT — failure section gives the "offline capability budget" message and a stderr error with exit code 1 for missing files
Score: 6/6

## Summary
A task1 r1: 1/6
A task1 r2: 1/6
A task1 r3: 1/6
A task2 r1: 5/6
A task2 r2: 0/6
A task2 r3: 0/6
B task1 r1: 0/6
B task1 r2: 0/6
B task1 r3: 0/6
B task2 r1: 6/6
B task2 r2: 6/6
B task2 r3: 0/6
C task1 r1: 6/6
C task1 r2: 6/6
C task1 r3: 6/6
C task2 r1: 6/6
C task2 r2: 6/6
C task2 r3: 6/6

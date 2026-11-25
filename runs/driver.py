#!/usr/bin/env python3
"""Freebuff pilot driver — The Persona Null Has a Boundary.

Walks runs/queue.json in order. For each run: fresh chat (/new) in the one
Freebuff session, send the spec pointer, wait for the deliverable file and
an idle composer. Skips runs whose deliverable already exists. Logs every
event to runs/driver_log.jsonl. Fatal conditions (pool refusal, wrong
model) stop the driver and are logged loudly; the watchdog reports them.

Del's workflow rules: ONE session, /new between rounds, never end/close.
Model: Nemotron 3.5 Lightning (0 hours)."""
import json, os, shutil, subprocess, sys, time

BASE = os.path.expanduser("~/workspace/persona-null-paper")
RUNS = os.path.join(BASE, "runs")
QUEUE = os.path.join(RUNS, "queue.json")
LOG = os.path.join(RUNS, "driver_log.jsonl")
SESSION = "freebuff"
MODEL = "Nemotron 3.5 Lightning"
RUN_TIMEOUT = 20 * 60
POLL = 15


def log(event, **kw):
    rec = {"ts": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "event": event}
    rec.update(kw)
    with open(LOG, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(rec, flush=True)


def tmux(*args, check=False):
    return subprocess.run(["tmux", *args], capture_output=True, text=True,
                          check=check)


def pane():
    r = tmux("capture-pane", "-t", SESSION, "-p")
    return r.stdout if r.returncode == 0 else ""


def send_text(text):
    tmux("send-keys", "-t", SESSION, "-l", text)


def send_key(key):
    tmux("send-keys", "-t", SESSION, key)


def ensure_binary():
    if shutil.which("freebuff") is None:
        log("install_freebuff")
        subprocess.run(["npm", "install", "-g", "freebuff@latest"],
                       capture_output=True, text=True)


def ensure_session():
    if tmux("has-session", "-t", SESSION).returncode == 0 and "freebuff" in \
            subprocess.run(["pgrep", "-af", "freebuff"], capture_output=True,
                           text=True).stdout:
        return
    ensure_binary()
    tmux("kill-session", "-t", SESSION)
    tmux("new-session", "-d", "-s", SESSION, "-x", "100", "-y", "30",
         "-c", "/tmp", check=True)
    time.sleep(1)
    send_text("freebuff")
    send_key("Enter")
    for _ in range(24):
        time.sleep(5)
        if "Enter a coding task" in pane():
            log("session_up")
            return
    log("session_boot_timeout")
    raise SystemExit(2)


def check_model():
    p = pane()
    if MODEL not in p:
        log("model_mismatch", pane_tail=p[-300:])
        raise SystemExit(3)


def wait_for_model(timeout=90):
    """At boot the footer briefly shows a default model (GLM 5.3 Flash)
    before the account's last-used model syncs in. Wait for the real one."""
    t0 = time.time()
    while time.time() - t0 < timeout:
        if MODEL in pane():
            log("model_ready")
            return
        time.sleep(5)
    check_model()


def fresh_chat():
    send_text("/new")
    time.sleep(1)
    send_key("Enter")
    time.sleep(2)
    if "confirm and send" in pane():
        send_key("Enter")
    time.sleep(3)


def run_one(item):
    out = item["out"]
    if os.path.exists(out) and os.path.getsize(out) > 0:
        log("skip_done", **item)
        return
    fresh_chat()
    check_model()
    send_text(f"Read {item['spec']} and do exactly what it says.")
    time.sleep(1)
    send_key("Enter")
    log("run_start", **item)
    t0 = time.time()
    confirmed = False
    while time.time() - t0 < RUN_TIMEOUT:
        time.sleep(POLL)
        p = pane()
        if "Not enough hours" in p:
            send_key("Escape")
            log("pool_block", **item)
            raise SystemExit(4)
        if not confirmed and "confirm and send" in p and "0 hours" in p:
            send_key("Enter")
            confirmed = True
            log("model_session_confirmed", **item)
            continue
        if os.path.exists(out) and os.path.getsize(out) > 0 and \
                "Enter a coding task" in p:
            log("run_done", seconds=int(time.time() - t0), **item)
            return
    log("run_timeout", **item)


def main():
    with open(QUEUE) as f:
        queue = json.load(f)
    ensure_session()
    wait_for_model()
    for item in queue:
        run_one(item)
    log("queue_complete", total=len(queue))


if __name__ == "__main__":
    main()

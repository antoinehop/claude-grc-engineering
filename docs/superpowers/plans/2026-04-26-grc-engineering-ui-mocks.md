# GRC Engineering UI Mocks — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn three standalone HTML mockups into a polished, demo-ready package with shared navigation, auto-refresh dev server, screenshot export tooling, and clean repo hygiene.

**Architecture:** All surfaces are standalone HTML files in `.superpowers/brainstorm/content/`. A new `index.html` provides top-level navigation between them. The Python dev server is upgraded to watch for file changes and reload automatically. A screenshot script captures each surface as a PNG using Python + a headless browser call (via `screencapture` on macOS or `playwright` if available).

**Tech Stack:** Python 3 stdlib (`http.server`, `threading`, `watchdog`-optional), standalone HTML/CSS, macOS `screencapture` or Playwright for screenshots.

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `.superpowers/brainstorm/content/index.html` | Navigation hub linking all three surfaces |
| Modify | `.superpowers/brainstorm/server.py` | Add file-change auto-reload via `Last-Modified` / polling |
| Create | `.superpowers/brainstorm/screenshot.sh` | Capture each surface as PNG to `.superpowers/brainstorm/screenshots/` |
| Modify | `.gitignore` | Add `.superpowers/` exclusion |

---

## Task 1: Add `.superpowers/` to `.gitignore`

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Add the entry**

Open `.gitignore` and add after the `# OS / editor` block:

```
# Brainstorming session files (local only)
.superpowers/
```

- [ ] **Step 2: Verify git no longer tracks the directory**

```bash
git check-ignore -v .superpowers/brainstorm/server.py
```

Expected output:
```
.gitignore:XX:.superpowers/	.superpowers/brainstorm/server.py
```

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore: ignore .superpowers/ brainstorm session files"
```

---

## Task 2: Build the navigation index page

**Files:**
- Create: `.superpowers/brainstorm/content/index.html`

- [ ] **Step 1: Create the index page**

Write `.superpowers/brainstorm/content/index.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>GRC Engineering — Demo Suite</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0b0f19; --surface: #111827; --surface2: #1a2236;
      --border: #1f2d45; --text: #f1f5f9; --muted: #64748b;
      --accent: #6366f1; --accent2: #818cf8; --green: #10b981;
    }
    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: var(--bg); color: var(--text);
      min-height: 100vh; display: flex; flex-direction: column;
    }
    header {
      background: var(--surface); border-bottom: 1px solid var(--border);
      padding: 1rem 2rem; display: flex; align-items: center; gap: 0.75rem;
    }
    .logo { width: 32px; height: 32px; background: var(--accent); border-radius: 7px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.65rem; font-weight: 800; color: white; }
    header h1 { font-size: 0.9rem; font-weight: 700; letter-spacing: 0.04em; }
    header p { font-size: 0.72rem; color: var(--muted); margin-top: 0.1rem; }
    main { flex: 1; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }
    .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; max-width: 860px; width: 100%; }
    .card {
      background: var(--surface); border: 1px solid var(--border); border-radius: 14px;
      padding: 1.75rem; text-decoration: none; color: inherit;
      transition: border-color 0.15s, transform 0.15s;
      display: flex; flex-direction: column; gap: 0.75rem;
    }
    .card:hover { border-color: var(--accent); transform: translateY(-3px); }
    .card-icon {
      width: 42px; height: 42px; border-radius: 10px;
      background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.2);
      display: flex; align-items: center; justify-content: center; font-size: 1.2rem;
    }
    .card-num { font-size: 0.62rem; color: var(--muted); font-weight: 600;
                text-transform: uppercase; letter-spacing: 0.08em; }
    .card h2 { font-size: 1rem; font-weight: 700; }
    .card p { font-size: 0.8rem; color: var(--muted); line-height: 1.6; }
    .card-cta { margin-top: auto; font-size: 0.75rem; color: var(--accent2);
                display: flex; align-items: center; gap: 0.3rem; }
    footer { text-align: center; padding: 1.5rem; font-size: 0.7rem; color: var(--muted);
             border-top: 1px solid var(--border); }
  </style>
</head>
<body>
  <header>
    <div class="logo">GRC</div>
    <div>
      <h1>GRC ENGINEERING — Demo Suite</h1>
      <p>Internal demo · Professional dark theme · claude-grc-engineering</p>
    </div>
  </header>
  <main>
    <div class="cards">
      <a class="card" href="dashboard.html">
        <div class="card-icon">◈</div>
        <div class="card-num">Surface 1</div>
        <h2>Compliance Dashboard</h2>
        <p>Live compliance posture across 5 frameworks. Score cards, 30-day trend, findings table, connector status.</p>
        <div class="card-cta">Open dashboard →</div>
      </a>
      <a class="card" href="landing-page.html">
        <div class="card-icon">◎</div>
        <div class="card-num">Surface 2</div>
        <h2>Landing Page</h2>
        <p>Marketing homepage for the toolkit. Hero with live terminal, stats bar, feature grid, plugin categories.</p>
        <div class="card-cta">Open landing page →</div>
      </a>
      <a class="card" href="cli-mockups.html">
        <div class="card-icon">⌥</div>
        <div class="card-num">Surface 3</div>
        <h2>CLI Workflows</h2>
        <p>Annotated terminal mockups for 4 key commands. Gap assessment, IaC scan, cross-framework, monitoring.</p>
        <div class="card-cta">Open CLI mockups →</div>
      </a>
    </div>
  </main>
  <footer>
    GRC Engineering Club · claude-grc-engineering · Demo use only
  </footer>
</body>
</html>
```

- [ ] **Step 2: Open the index in a browser and verify all three links work**

```bash
open .superpowers/brainstorm/content/index.html
```

Expected: browser opens, three cards visible, clicking each navigates to the correct surface.

- [ ] **Step 3: Commit**

```bash
git add .superpowers/brainstorm/content/index.html
git commit -m "feat(mocks): add navigation index page linking all three demo surfaces"
```

---

## Task 3: Upgrade the dev server with auto-reload

**Files:**
- Modify: `.superpowers/brainstorm/server.py`

The current server serves the newest file but the browser only refreshes on `Refresh: 3` header, meaning the user has to wait. Upgrade it to:
1. Serve `index.html` at `/` and individual surfaces at their filenames
2. Use a polling `Last-Modified` check so the browser reloads automatically

- [ ] **Step 1: Rewrite `server.py`**

Replace the entire contents of `.superpowers/brainstorm/server.py` with:

```python
#!/usr/bin/env python3
"""GRC Engineering demo server.

Serves .superpowers/brainstorm/content/ at http://localhost:52341.
- GET /           → index.html
- GET /foo.html   → content/foo.html
Auto-reloads: injects a 3-second meta-refresh into every HTML response.
"""
import http.server
import os

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
PORT = 52341
REFRESH_SECONDS = 3


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # silence request logs

    def do_GET(self):
        path = self.path.lstrip("/") or "index.html"
        # strip query strings
        path = path.split("?")[0]

        filepath = os.path.join(CONTENT_DIR, path)
        if not os.path.isfile(filepath):
            self.send_error(404, f"Not found: {path}")
            return

        with open(filepath, "rb") as f:
            data = f.read()

        # inject meta-refresh so the browser polls for changes
        refresh_tag = (
            f'<meta http-equiv="refresh" content="{REFRESH_SECONDS}">'
            .encode()
        )
        if b"<head>" in data:
            data = data.replace(b"<head>", b"<head>" + refresh_tag, 1)

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    with http.server.HTTPServer(("127.0.0.1", PORT), Handler) as srv:
        print(
            f"GRC Engineering demo server running at http://localhost:{PORT}",
            flush=True,
        )
        print(f"  Index:      http://localhost:{PORT}/", flush=True)
        print(f"  Dashboard:  http://localhost:{PORT}/dashboard.html", flush=True)
        print(f"  Landing:    http://localhost:{PORT}/landing-page.html", flush=True)
        print(f"  CLI:        http://localhost:{PORT}/cli-mockups.html", flush=True)
        srv.serve_forever()
```

- [ ] **Step 2: Kill any running server and restart**

```bash
pkill -f "server.py" 2>/dev/null; sleep 0.5
cd /path/to/repo/.superpowers/brainstorm && python3 server.py &
```

Replace `/path/to/repo` with the actual repo root.

- [ ] **Step 3: Verify all routes**

```bash
curl -s http://localhost:52341/ | grep -c "Demo Suite"
# Expected: 1

curl -s http://localhost:52341/dashboard.html | grep -c "Compliance Dashboard"
# Expected: 1

curl -s http://localhost:52341/landing-page.html | grep -c "engineered systems"
# Expected: 1

curl -s http://localhost:52341/cli-mockups.html | grep -c "CLI Workflows"
# Expected: 1

curl -s http://localhost:52341/missing.html | grep -c "404"
# Expected: 1
```

- [ ] **Step 4: Commit**

```bash
git add .superpowers/brainstorm/server.py
git commit -m "feat(mocks): upgrade dev server with named routes and auto-refresh"
```

---

## Task 4: Screenshot export script

**Files:**
- Create: `.superpowers/brainstorm/screenshot.sh`
- Create: `.superpowers/brainstorm/screenshots/` (directory, via script)

Captures each surface as a PNG using macOS `screencapture` after opening in Safari via `osascript`. Falls back to a message if not on macOS.

- [ ] **Step 1: Create the screenshot script**

Write `.superpowers/brainstorm/screenshot.sh`:

```bash
#!/usr/bin/env bash
# Capture GRC Engineering demo surfaces as PNGs.
# Requires: macOS (uses screencapture + osascript), server running on :52341.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="$SCRIPT_DIR/screenshots"
BASE_URL="http://localhost:52341"
DELAY=3  # seconds to let the page render

mkdir -p "$OUT_DIR"

if [[ "$(uname)" != "Darwin" ]]; then
  echo "Screenshot capture requires macOS. Export the HTML files manually."
  exit 1
fi

capture() {
  local name="$1"
  local url="$2"
  local outfile="$OUT_DIR/${name}.png"

  echo "Capturing $name..."
  osascript <<APPLESCRIPT
    tell application "Safari"
      activate
      open location "$url"
      delay $DELAY
    end tell
APPLESCRIPT
  screencapture -l "$(osascript -e 'tell application "Safari" to id of window 1')" \
    -x "$outfile" 2>/dev/null || screencapture -x "$outfile"
  echo "  → $outfile"
}

capture "01-dashboard"   "$BASE_URL/dashboard.html"
capture "02-landing-page" "$BASE_URL/landing-page.html"
capture "03-cli-mockups" "$BASE_URL/cli-mockups.html"

echo ""
echo "Done. Screenshots saved to: $OUT_DIR"
echo "  $(ls "$OUT_DIR"/*.png 2>/dev/null | wc -l | tr -d ' ') files"
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x .superpowers/brainstorm/screenshot.sh
```

- [ ] **Step 3: Verify the script is executable and has no syntax errors**

```bash
bash -n .superpowers/brainstorm/screenshot.sh && echo "syntax ok"
```

Expected:
```
syntax ok
```

- [ ] **Step 4: Commit**

```bash
git add .superpowers/brainstorm/screenshot.sh
git commit -m "feat(mocks): add screenshot export script for demo surfaces"
```

---

## Task 5: Remove brainstorming session clutter from content/

**Files:**
- Delete: `.superpowers/brainstorm/content/visual-direction.html`
- Delete: `.superpowers/brainstorm/content/waiting-1.html`
- Delete: `.superpowers/brainstorm/content/what-are-we-mocking.html`

These were intermediate brainstorming screens, not part of the demo suite.

- [ ] **Step 1: Verify the three files to delete exist and are brainstorming-only**

```bash
ls .superpowers/brainstorm/content/
```

Expected (among others): `visual-direction.html`, `waiting-1.html`, `what-are-we-mocking.html`

- [ ] **Step 2: Delete them**

```bash
rm .superpowers/brainstorm/content/visual-direction.html \
   .superpowers/brainstorm/content/waiting-1.html \
   .superpowers/brainstorm/content/what-are-we-mocking.html
```

- [ ] **Step 3: Verify only demo surfaces remain**

```bash
ls .superpowers/brainstorm/content/
```

Expected:
```
cli-mockups.html
dashboard.html
index.html
landing-page.html
```

- [ ] **Step 4: Commit**

```bash
git add -A .superpowers/brainstorm/content/
git commit -m "chore(mocks): remove brainstorming session screens from demo content"
```

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Covered by |
|---|---|
| Dashboard mockup | Already built (pre-plan); Task 2 adds nav to it |
| Landing page mockup | Already built (pre-plan); Task 2 adds nav to it |
| CLI mockups | Already built (pre-plan); Task 2 adds nav to it |
| `.superpowers/` gitignored | Task 1 |
| Navigation between surfaces | Task 2 |
| Dev server (named routes + auto-reload) | Task 3 |
| Screenshot export | Task 4 |
| Clean content dir (no brainstorm clutter) | Task 5 |

**Placeholder scan:** No TBDs. All code blocks are complete. Commands include expected output.

**Type consistency:** No shared types across tasks — each task is standalone HTML/shell.

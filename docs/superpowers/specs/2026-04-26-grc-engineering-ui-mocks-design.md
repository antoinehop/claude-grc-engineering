# GRC Engineering UI Mocks — Design Spec

**Date:** 2026-04-26
**Status:** Approved
**Purpose:** Internal demo / pitch deck for stakeholders, leadership, and potential contributors

---

## Summary

Three visual surfaces derived from a shared professional-dark design system, built to tell a coherent pitch story about the claude-grc-engineering toolkit. Each surface has a distinct job; together they form a complete demo arc.

---

## Audience

Mixed: GRC practitioners/engineers, security leadership (CISOs), and open-source contributors/developers. Designs must read clearly at all three levels of technical depth.

---

## Visual Design System

**Theme:** Professional dark — bold, confident, security-tool aesthetic with executive polish.

**Palette:**
- Background: `#0b0f19`
- Surface: `#111827`
- Surface raised: `#1a2236`
- Border: `#1f2d45`
- Text primary: `#f1f5f9`
- Muted: `#64748b`
- Accent (indigo): `#6366f1` / `#818cf8`
- Green (pass): `#10b981`
- Yellow (warn): `#f59e0b`
- Red (fail/crit): `#ef4444`
- Blue (info): `#3b82f6`

**Typography:** System UI stack (`system-ui, -apple-system, BlinkMacSystemFont`). Monospace: `SF Mono, Fira Code, Cascadia Code`.

**Brand mark:** 3-letter "GRC" in white on indigo `#6366f1` square, 6–7px border-radius. Name in 700-weight uppercase with `0.04em` letter-spacing.

---

## Approach

Dashboard-first: the dashboard is designed at full fidelity; the landing page and CLI mockups derive their design language from it.

---

## Surface 1 — Compliance Dashboard

**File:** `.superpowers/brainstorm/content/dashboard.html`
**Job:** Show the outcome of running the toolkit — live compliance posture across frameworks.

### Layout

Two-panel: 220px sidebar + full-height main area.

**Sidebar sections:**
- Logo mark + "GRC ENGINEERING" wordmark + "Claude Code Plugin Suite" subtitle
- Overview nav: Dashboard, Gap Assessment (badge), Findings, Trends
- Tooling nav: IaC Scanner, Code Generator, Monitor, OSCAL
- Personas nav: Auditor, TPRM, Internal GRC, Reporter
- Connector status footer (live dots): aws-inspector, github-inspector, okta-inspector, gcp-inspector (offline)

**Topbar:** Page title, last-run metadata, date pill, LIVE pill, "Run Assessment" CTA button.

**Content grid (top to bottom):**

1. **Score row** — 5 framework cards (SOC 2, FedRAMP High, NIST 800-53, PCI DSS, ISO 27001). Each shows: label, percentage, progress bar, delta vs last run. Color-coded: green ≥90%, yellow 70–89%, red <70%.

2. **Two-column row:**
   - Left: 30-day compliance trend chart (14-day bar chart, 4 frameworks overlaid, legend, date labels)
   - Right: Framework coverage panel — horizontal bar per framework with control counts (passing/total)

3. **Findings table** — columns: Severity, Resource, Control ID, Frameworks affected, Source connector, Fix type (auto-fix badge or "manual"). Shows top 6 of 190 findings. Header includes auto-fixable count.

4. **Bottom metrics row** — 3 cards: SCF crosswalk stats (1,468 controls / 249 frameworks), automation coverage (89/190 auto-fixable, $267k savings), evidence collected (336 findings from 3 connectors).

---

## Surface 2 — Landing Page

**File:** `.superpowers/brainstorm/content/landing-page.html`
**Job:** Sell the value proposition quickly — "checkbox compliance to engineered systems."

### Sections

**Sticky nav:** Logo, nav links (Plugins, Docs, Frameworks, Community), GitHub button, "Get Started →" CTA.

**Hero:**
- Eyebrow pill: "Open-source · Claude Code Plugin Suite · MIT License"
- H1: "Checkbox compliance to engineered systems" (accent on "engineered systems")
- Subhead: one sentence describing the toolkit
- Two CTAs: "Get started in 60 seconds" (primary) + "View on GitHub" (secondary)
- Terminal hero: shows the 60-second install + first gap-assessment run with realistic output

**Stats bar:** 4 stats across full width — 1,468 controls, 249 frameworks, 56% effort reduction, 30 plugins.

**Features section:** 6-cell grid showing key commands with icon, title, description, and command snippet.

**Plugin categories section:** 4-column table — Hub (grc-engineer), Personas (4 plugins), Frameworks (20+), Connectors (Tier-1 + roadmap).

**CTA section:** Gradient box with one-line install command + Quickstart and Browse Plugins buttons.

**Footer:** License, affiliation disclaimer, GitHub/grcengclub.com links.

---

## Surface 3 — CLI Mockups

**File:** `.superpowers/brainstorm/content/cli-mockups.html`
**Job:** Show the tool in action — annotated terminal workflows for demo and pitch use.

### Four Workflows

Each workflow = terminal window (left or right, alternating) + annotation column with callout boxes.

| # | Workflow | Command | Key callouts |
|---|---|---|---|
| 1 | Gap Assessment | `/grc-engineer:gap-assessment` | Multi-framework in one pass; auto-fix signal; SCF crosswalk |
| 2 | IaC Scan + Auto-fix | `/grc-engineer:scan-iac --fix` | Before/after score (+18%); CI/CD SARIF output; what auto-fix covers |
| 3 | Cross-Framework Intelligence | `/grc-engineer:map-controls-unified` | Equivalencies across 6 frameworks; conflict resolution; chained generate |
| 4 | Continuous Monitoring | `/grc-engineer:monitor-continuous` | 30-day trend bars; health indicators; alert thresholds |

**Bottom summary row:** 4-card grid summarizing all workflows — for use as a standalone slide.

### Terminal styling

- Background: `#0d1117` (GitHub dark)
- Border: `#30363d`
- Traffic-light dots in terminal bar
- Color coding: prompt `#58a6ff`, pass `#3fb950`, warn `#d29922`, error `#f85149`, accent `#79c0ff`, dim `#6e7681`

---

## File Locations

| Surface | File |
|---|---|
| Dashboard | `.superpowers/brainstorm/content/dashboard.html` |
| Landing page | `.superpowers/brainstorm/content/landing-page.html` |
| CLI mockups | `.superpowers/brainstorm/content/cli-mockups.html` |
| Dev server | `.superpowers/brainstorm/server.py` (Python, port 52341) |

All files are standalone HTML — no build step required. Open any directly in a browser or serve via `python3 server.py`.

---

## Not in Scope

- Actual React/Next.js implementation
- Backend API or data layer
- Mobile responsive breakpoints (desktop-only for demo use)
- Light mode variant

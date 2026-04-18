---
description: Track compliance status across frameworks and controls
---

# Track Compliance

Monitors and reports on compliance status across multiple frameworks.

## Arguments

- `$1` - Framework or control set (optional, defaults to all)
- `$2` - Output format (optional: summary, detailed, dashboard)

## Instructions

1. Review current compliance posture across frameworks
2. Identify gaps and upcoming requirements
3. Generate compliance tracking report with:
   - Overall compliance score
   - Framework-by-framework status
   - Control gaps requiring attention
   - Upcoming deadlines and renewals
   - Trend analysis

## Examples

```bash
# Track SOC 2 compliance
/grc-internal:track-compliance SOC2 detailed

# Track PCI-DSS compliance
/grc-internal:track-compliance PCIDSS summary

# Track all frameworks
/grc-internal:track-compliance all dashboard

# Track ISO 27001 compliance
/grc-internal:track-compliance ISO27001 detailed
```

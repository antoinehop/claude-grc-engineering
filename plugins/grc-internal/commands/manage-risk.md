---
description: Manage the risk register and risk assessments
---

# Manage Risk

Maintains the organizational risk register and performs risk assessments.

## Arguments

- `$1` - Action (required: add, update, assess, report)
- `$2` - Risk ID or description (required for add/update)

## Actions

- **add** - Add a new risk to the register
- **update** - Update an existing risk's status or attributes
- **assess** - Perform risk assessment on a system or process
- **report** - Generate risk register report

## Risk Attributes

- Risk description and category
- Likelihood (1-5 scale)
- Impact (1-5 scale)
- Inherent vs residual risk scores
- Mitigation status and owner
- Target resolution date

## Example

```bash
/grc-internal:manage-risk add "Cloud misconfiguration exposure"
/grc-internal:manage-risk report
```

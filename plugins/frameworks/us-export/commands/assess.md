---
description: Unified ITAR and EAR compliance assessment
---

# US Export Controls Assessment

Evaluates readiness for US export controls compliance across both ITAR (defense articles) and EAR (dual-use commercial) frameworks.

## Arguments

- `$1` - Scope (optional: itar, ear, both) - defaults to "both"
- `$2` - Assessment depth (optional: quick, detailed) - defaults to "detailed"

## Framework Selection

| Scope | Framework | When to Use |
|-------|-----------|-------------|
| itar | ITAR only | Defense articles on USML, technical data for defense |
| ear | EAR only | Dual-use commercial items on CCL, encryption products |
| both | ITAR + EAR | Uncertain jurisdiction, mixed product portfolio |

## Assessment Output

**ITAR Assessment** (7 controls):
1. **US Person Verification** - Access limited to US citizens/permanent residents
2. **US-Only Data Residency** - Data stored only in US regions
3. **Encryption Requirements** - FIPS 140-2 validated encryption
4. **Access Logging** - 5+ year audit trail retention
5. **Network Isolation** - Dedicated VPCs/VNets for ITAR workloads
6. **Export Control Marking** - Resources tagged with ITAR classification
7. **Third-Party Access Control** - CSP access restrictions

**EAR Assessment** (7 controls):
1. **Export Control Classification** - ECCN or EAR99 determination
2. **End-User Screening** - Denied parties list checking (Entity List, DPL, SDN)
3. **Encryption Compliance** - FIPS 140 for Category 5 Part 2 items
4. **Geographic Access Controls** - Embargo country blocking (Cuba, Iran, NK, Syria)
5. **Technology Transfer Controls** - Source code and technical data access controls
6. **CSP Attestations** - Cloud provider FIPS encryption and CMEK verification
7. **License Exceptions** - ENC, TSU, BAG applicability determination

**Jurisdiction Determination**:
- Is the item on the USML (US Munitions List)? → ITAR
- Is the item on the CCL (Commerce Control List)? → EAR with ECCN
- Neither list? → Likely EAR99 (low-level controls)

**Compliance Status**:
- Compliant, Non-Compliant, Partially Compliant
- Gap analysis with prioritized remediation steps
- Registration/licensing requirements (DDTC for ITAR, BIS for EAR)

## Examples

```bash
# Assess both frameworks (default)
/us-export:assess

# ITAR-only assessment for defense contractor
/us-export:assess itar detailed

# EAR-only quick assessment for commercial exporter
/us-export:assess ear quick

# Full assessment for mixed portfolio
/us-export:assess both detailed
```

## Common Scenarios

**Defense Contractor**: ITAR applies - US person verification, GovCloud recommended
**Encryption Software**: EAR applies - ECCN 5D002, License Exception ENC may apply
**Cloud Service Provider**: Both may apply - implement geographic controls, screening
**Semiconductor Manufacturer**: EAR applies - ECCN classification, Entity List screening

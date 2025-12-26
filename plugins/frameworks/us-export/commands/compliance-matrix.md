---
description: ITAR vs EAR compliance requirements crosswalk
---

# ITAR vs EAR Compliance Matrix

Side-by-side comparison of ITAR and EAR requirements to understand overlaps, differences, and compliance strategies.

## Arguments

- `$1` - Focus area (optional: overview, controls, cloud, licensing) - defaults to "overview"

## Framework Overview

| Aspect | ITAR | EAR |
|--------|------|-----|
| **Authority** | State Department (DDTC) | Commerce Department (BIS) |
| **Scope** | Defense articles, services, technical data (USML) | Dual-use commercial items (CCL) |
| **Item List** | US Munitions List (USML) - 21 categories | Commerce Control List (CCL) - 10 categories |
| **Personnel** | US persons only (citizens, permanent residents) | No personnel restrictions (except deemed exports) |
| **Geography** | US-only data storage | Embargo country restrictions (CU, IR, KP, SY) |
| **Registration** | DDTC registration required ($3,000/year) | No registration (except encryption items) |
| **Licensing** | License required for most exports | License required for high-level ECCNs, exceptions available |

## Control Comparison

| Control Area | ITAR | EAR | Overlap |
|--------------|------|-----|---------|
| **Access Control** | US persons only verification | Denied party screening (Entity List, DPL, SDN) | ⚠️ Different mechanisms |
| **Data Residency** | US-only regions mandatory | Embargo country blocking | ⚠️ Different requirements |
| **Encryption** | FIPS 140-2 Level 2+ required | FIPS 140-2 for Category 5 Part 2 | ✅ Same standard |
| **Audit Logging** | 5+ year retention | Varies by requirement | ⚠️ ITAR more stringent |
| **Network Isolation** | Dedicated VPCs for ITAR | No specific requirement | ⚠️ ITAR only |
| **Marking** | ITAR classification on all data | ECCN classification on items | ⚠️ Different schemes |
| **Third-Party Access** | Restricted CSP access | Normal CSP access | ⚠️ ITAR more restrictive |

## Detailed Control Mapping

### 1. Personnel and Access

**ITAR-1: US Person Verification**
- **Requirement**: Only US citizens or permanent residents
- **Cloud Impact**: Verify citizenship for all users, tag IAM users
- **Verification**: Personnel files, citizenship documentation

**EAR-2: End-User Screening**
- **Requirement**: Screen against BIS denied parties lists
- **Cloud Impact**: Automated screening on provisioning
- **Verification**: Entity List, DPL, UVL, SDN checks

**Overlap**: ❌ No overlap - different mechanisms
- ITAR focuses on citizenship
- EAR focuses on entity screening

**Compliance Strategy**: Implement both
- Citizenship verification for ITAR systems
- Denied party screening for all systems (including ITAR)

### 2. Data Residency

**ITAR-2: US-Only Data Residency**
- **Requirement**: All data stored in US geographic regions only
- **Allowed Regions**: us-gov-*, us-east-*, us-west-*
- **Prohibited**: Any non-US region, cross-border replication

**EAR-4: Geographic Access Controls**
- **Requirement**: Block access from embargoed countries
- **Blocked Countries**: Cuba (CU), Iran (IR), North Korea (KP), Syria (SY)
- **Allowed**: Any region worldwide (except embargoed)

**Overlap**: ✅ Partial overlap
- ITAR US-only regions automatically satisfy EAR embargo blocking
- But EAR allows global regions (with screening)

**Compliance Strategy**:
- **ITAR workloads**: Use GovCloud/US-only regions
- **EAR workloads**: Use any region + geo-blocking for embargoes
- **Mixed**: Segregate systems by framework

### 3. Encryption

**ITAR-3: Encryption Requirements**
- **Requirement**: FIPS 140-2 validated encryption
- **Standard**: Level 2+ HSMs (AWS KMS, Azure Key Vault, GCP Cloud KMS)
- **Keys**: Customer-managed encryption keys (CMEK) recommended

**EAR-3: Encryption Compliance**
- **Requirement**: FIPS 140-2/140-3 for Category 5 Part 2 items
- **Standard**: Same as ITAR - Level 2+ HSMs
- **Classification**: Encryption products require ECCN 5D002/5A002

**Overlap**: ✅ Complete overlap
- Both require FIPS 140-2 validated encryption
- Same HSM standards (Level 2+)

**Compliance Strategy**: Implement once, satisfies both
- Use AWS KMS, Azure Key Vault HSM, or GCP Cloud KMS
- Configure CMEK for all controlled data

### 4. Audit and Logging

**ITAR-4: Access Logging and Audit**
- **Requirement**: Comprehensive audit trails for 5+ years
- **Scope**: All management and data events
- **Retention**: Minimum 5 years

**EAR**: No specific logging requirement
- **Best Practice**: Follow standard audit practices
- **Retention**: As needed for compliance

**Overlap**: ⚠️ ITAR more stringent
- EAR has no specific logging requirement
- ITAR requires 5+ year retention

**Compliance Strategy**:
- **ITAR**: CloudTrail/equivalent with 5-year retention
- **EAR**: Standard logging (1-2 years may suffice)

### 5. Classification and Marking

**ITAR-6: Export Control Marking**
- **Requirement**: Mark all ITAR data with export control notices
- **Tagging**: "ITAR Controlled" on all resources
- **Notices**: Export warnings on documents

**EAR-1: Export Control Classification**
- **Requirement**: Classify with ECCN or EAR99
- **Tagging**: ECCN codes (5D002, 3A001, etc.)
- **Documentation**: Classification rationale

**Overlap**: ⚠️ Different classification schemes
- ITAR uses "ITAR Controlled" binary marking
- EAR uses granular ECCN codes

**Compliance Strategy**: Use both tags
```
AWS Tags:
  ExportControl: "ITAR"
  ECCN: "5D002"  (if also subject to EAR)
```

## Cloud Platform Recommendations

| Use Case | ITAR | EAR | Recommended Platform |
|----------|------|-----|---------------------|
| **Defense contractor** | ✅ Primary | ⚠️ Maybe | AWS GovCloud, Azure Government |
| **Encryption software** | ❌ No | ✅ Primary | AWS Commercial (US regions), FIPS KMS |
| **Semiconductor manufacturer** | ❌ No | ✅ Primary | AWS/Azure/GCP Commercial with Entity List screening |
| **Aerospace dual-use** | ✅ Primary | ✅ Secondary | Segregated: GovCloud for ITAR, Commercial for EAR |
| **Cloud service provider** | ⚠️ Support customers | ✅ As a tool | Offer GovCloud + Commercial options |

## Licensing and Registration

| Requirement | ITAR | EAR |
|-------------|------|-----|
| **Registration** | DDTC registration required ($3,000/year) | No registration (except encryption) |
| **License for Export** | Required for most USML items | Required for high-level ECCNs |
| **License Exceptions** | None available | ENC, TSU, BAG, TMP available |
| **Self-Classification** | Not available | Available for encryption (ENC) |
| **Reporting** | Annual registration renewal | Semi-annual (if using ENC exception) |

## Compliance Decision Matrix

| Scenario | ITAR | EAR | Action |
|----------|------|-----|--------|
| Item on USML | ✅ Yes | ❌ No | Use `/us-export:itar-assess` |
| Item on CCL with ECCN | ❌ No | ✅ Yes | Use `/us-export:ear-assess` |
| Item on both lists | ✅ Yes | ⚠️ Maybe | ITAR takes precedence |
| Item on neither list (EAR99) | ❌ No | ✅ Yes (low-level) | Basic EAR controls (embargo only) |
| Uncertain jurisdiction | ❓ Unknown | ❓ Unknown | Submit Commodity Jurisdiction (CJ) request |

## Overlapping Controls (Implement Once)

These controls satisfy both ITAR and EAR:

✅ **FIPS 140-2 Encryption**
- AWS KMS, Azure Key Vault HSM, GCP Cloud KMS
- Satisfies ITAR-3 and EAR-3

✅ **Denied Party Screening**
- While not ITAR-required, recommended for defense contractors
- Satisfies EAR-2

✅ **Access Logging**
- ITAR requires 5 years
- EAR benefits from logging
- CloudTrail/equivalent satisfies both

## Framework-Specific Controls

### ITAR-Only Controls

These apply only to ITAR, not EAR:

🔒 **US Person Verification** (ITAR-1)
- Not required for EAR
- Critical for ITAR compliance

🔒 **US-Only Data Residency** (ITAR-2)
- Not required for EAR (except embargo countries)
- Mandatory for ITAR

🔒 **Network Isolation** (ITAR-5)
- Not required for EAR
- Recommended for ITAR

### EAR-Only Controls

These apply only to EAR, not ITAR:

📋 **ECCN Classification** (EAR-1)
- Not applicable to ITAR (uses USML categories)
- Required for EAR

📋 **License Exceptions** (EAR-7)
- Not available for ITAR
- ENC, TSU available for EAR

## Cost Comparison

| Cost Item | ITAR | EAR | Notes |
|-----------|------|-----|-------|
| **Registration Fee** | $3,000/year | $0 | DDTC registration |
| **Cloud Premium** | +30-50% | Standard | GovCloud premium pricing |
| **Compliance Tools** | $50-200K/year | $10-50K/year | Screening, monitoring |
| **Personnel** | US persons only | Standard | May limit talent pool |
| **Audit/Assessment** | $100-300K | $25-75K | External audit costs |

## Migration Strategy

### Moving from ITAR to EAR

**If** jurisdiction changes (e.g., product moved from USML to CCL):

1. ✅ **Keep**: FIPS 140-2 encryption (helps EAR compliance)
2. ✅ **Keep**: Access logging (best practice)
3. ⚠️ **Modify**: Expand from US-only to global (add embargo blocking)
4. ⚠️ **Modify**: Add ECCN classification
5. ⚠️ **Add**: Denied party screening
6. ❌ **Remove**: US person requirement (can allow foreign nationals)

### Dual Compliance (Both ITAR and EAR)

**For organizations subject to both**:

1. **Segregate Systems**:
   - ITAR workloads → GovCloud/Government regions
   - EAR workloads → Commercial regions

2. **Apply Most Restrictive Controls**:
   - ITAR controls automatically satisfy overlapping EAR requirements
   - Add EAR-specific controls (ECCN, screening)

3. **Tag All Resources**:
   ```
   ExportControl: "ITAR" | "EAR" | "BOTH"
   ECCN: "5D002" (for EAR items)
   Classification: "CUI" | "ITAR-Controlled"
   ```

## Examples

```bash
# View overview comparison
/us-export:compliance-matrix overview

# Focus on control mappings
/us-export:compliance-matrix controls

# Cloud platform recommendations
/us-export:compliance-matrix cloud

# Licensing and registration comparison
/us-export:compliance-matrix licensing
```

## Quick Reference

**When ITAR applies**: Use strictest controls (US persons, US-only regions)
**When EAR applies**: Use specific controls (ECCN, screening, embargo blocking)
**When both apply**: Segregate systems or apply ITAR controls + EAR additions
**When uncertain**: Submit Commodity Jurisdiction request to DDTC

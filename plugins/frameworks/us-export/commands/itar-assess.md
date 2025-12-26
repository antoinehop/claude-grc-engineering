---
description: ITAR-specific compliance assessment for defense articles
---

# ITAR Assessment

Deep dive assessment for International Traffic in Arms Regulations (ITAR) compliance. Focuses on defense articles, technical data, and defense services under the US Munitions List (USML).

## Arguments

- `$1` - Assessment type (optional: readiness, remediation, certification) - defaults to "readiness"

## ITAR Control Assessment

### ITAR-1: US Person Verification

**Requirement**: Only US persons (citizens or permanent residents) may access ITAR-controlled technical data.

**Assessment Questions**:
- Are all users with data access US citizens or permanent residents?
- Is citizenship verification documented for all users?
- Are foreign nationals explicitly denied access to ITAR systems?

**Cloud Verification**:
- IAM users tagged with citizenship status
- Access logs show US-person-only access
- Foreign national access attempts are logged and blocked

### ITAR-2: US-Only Data Residency

**Requirement**: ITAR data must be stored only in US geographic regions.

**Assessment Questions**:
- Are all resources deployed in US-only regions?
- Is cross-border data replication disabled?
- Are backups stored in US regions only?

**Recommended Regions**:
- **AWS**: us-gov-west-1, us-gov-east-1 (GovCloud)
- **Azure**: USGov Virginia, USGov Texas, USGov Arizona
- **GCP**: us-central1, us-east4, us-west1 (with Assured Workloads)

### ITAR-3: FIPS 140-2 Encryption

**Requirement**: All ITAR data must be encrypted with FIPS 140-2 validated cryptographic modules.

**Assessment Questions**:
- Is all data encrypted at rest and in transit?
- Are FIPS 140-2 Level 2+ validated HSMs used?
- Are customer-managed encryption keys (CMEK) configured?

**Verification**:
- EBS volumes encrypted with AWS KMS
- S3 buckets use SSE-KMS encryption
- TLS 1.2+ for data in transit

### ITAR-4: Access Logging and Audit

**Requirement**: Maintain comprehensive audit trails for at least 5 years.

**Assessment Questions**:
- Is CloudTrail/equivalent enabled for all regions?
- Are data events logged for S3 and other services?
- Are logs retained for 5+ years?
- Is log integrity protection enabled?

### ITAR-5: Network Isolation

**Requirement**: ITAR systems should be isolated from non-ITAR systems.

**Assessment Questions**:
- Are dedicated VPCs/VNets used for ITAR workloads?
- Is VPC peering to non-ITAR environments prohibited?
- Are network boundaries clearly defined and enforced?

### ITAR-6: Export Control Marking

**Requirement**: ITAR data must be marked with appropriate export control notices.

**Assessment Questions**:
- Are all ITAR resources tagged with export control classification?
- Are data files marked with ITAR warnings?
- Is classification visible in metadata and labels?

### ITAR-7: Third-Party Access Control

**Requirement**: Control access by cloud service providers and third parties.

**Assessment Questions**:
- Are Service Control Policies (SCPs) configured to restrict third-party access?
- Is Customer Lockbox/approval required for CSP support access?
- Are external access roles audited and restricted?

## DDTC Registration

**Requirement**: Most organizations handling ITAR data must register with DDTC.

**Annual Fee**: $3,000 per year
**Form**: DS-2032 (Statement of Registration)
**Renewal**: Annual before expiration

## Recommended Cloud Platforms

| Platform | Recommendation | Notes |
|----------|---------------|-------|
| **AWS GovCloud** | Highly Recommended | FedRAMP High, US-only, US persons only |
| **Azure Government** | Highly Recommended | FedRAMP High, screened personnel |
| **GCP Assured Workloads** | Recommended | With ITAR configuration, data residency controls |
| **AWS Commercial** | Limited Use | US regions only, additional controls required |

## Examples

```bash
# Readiness assessment
/us-export:itar-assess readiness

# Remediation planning
/us-export:itar-assess remediation

# Pre-certification assessment
/us-export:itar-assess certification
```

## Key Distinctions from EAR

- **Personnel**: US persons only (ITAR) vs. No person restriction (EAR)
- **Geography**: US-only data (ITAR) vs. Embargo screening (EAR)
- **Authority**: State Dept DDTC (ITAR) vs. Commerce BIS (EAR)
- **Scope**: Defense articles (ITAR) vs. Dual-use commercial (EAR)

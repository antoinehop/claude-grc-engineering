---
description: Verify data residency requirements for ITAR and EAR
---

# Data Residency Verification

Verifies data residency requirements for both ITAR (US-only) and EAR (embargo screening) compliance.

## Arguments

- `$1` - Framework (optional: itar, ear, both) - defaults to "both"
- `$2` - Cloud provider (optional: aws, azure, gcp, all) - defaults to "all"

## ITAR Data Residency Requirements

### Requirement: US-Only Data Storage

ITAR-controlled data must be stored **only** in US geographic regions. Cross-border data transfer is prohibited without authorization.

### Recommended Cloud Regions

#### AWS GovCloud (Highly Recommended)

**US Government Regions**:
- `us-gov-west-1` (Oregon) - US West (GovCloud)
- `us-gov-east-1` (Virginia) - US East (GovCloud)

**Benefits**:
- FedRAMP High authorized
- US persons-only personnel
- Physical isolation from AWS commercial
- ITAR compliance support

**Verification**:
```bash
aws ec2 describe-regions --region us-gov-west-1
aws s3api list-buckets --region us-gov-west-1
```

#### AWS Commercial (US Regions Only)

**Approved US Regions** (with additional controls):
- `us-east-1` (Virginia)
- `us-east-2` (Ohio)
- `us-west-1` (California)
- `us-west-2` (Oregon)

**Prohibited Regions**:
- Any non-US region (eu-west-1, ap-southeast-1, etc.)
- Global services must be configured for US-only

#### Azure Government (Highly Recommended)

**US Government Regions**:
- `usgovvirginia` - US Gov Virginia
- `usgoviowa` - US Gov Iowa (DoD only)
- `usgovtexas` - US Gov Texas
- `usgovarizona` - US Gov Arizona
- `usdodeast` - US DoD East
- `usdodcentral` - US DoD Central

**Benefits**:
- FedRAMP High authorized
- Screened US personnel
- Dedicated infrastructure

**Verification**:
```bash
az cloud list --query '[?name==`AzureUSGovernment`]'
az account list-locations --query '[?name==`usgovvirginia`]'
```

#### GCP with Assured Workloads

**US Regions**:
- `us-central1` (Iowa)
- `us-east1` (South Carolina)
- `us-east4` (Virginia)
- `us-west1` (Oregon)
- `us-west2` (Los Angeles)
- `us-west3` (Salt Lake City)
- `us-west4` (Las Vegas)

**Assured Workloads Configuration**:
- ITAR compliance controls
- Data residency enforcement
- Personnel access controls

**Verification**:
```bash
gcloud compute regions list --filter='name:us-*'
gcloud assured list --location=us-central1
```

## EAR Data Residency Requirements

### Requirement: Embargo Country Restrictions

EAR does **not** require US-only data storage, but **prohibits** data access from embargoed countries.

### Embargoed Countries (Blocked Access)

**Comprehensively Sanctioned** (no exports):
- **Cuba** (CU)
- **Iran** (IR)
- **North Korea** (KP)
- **Syria** (SY)
- **Crimea region of Ukraine**

**Partially Sanctioned** (check specific restrictions):
- **Russia** (RU) - certain items restricted
- **Belarus** (BY) - certain items restricted
- **Venezuela** (VE) - certain restrictions

### Geographic Access Controls

#### AWS WAF Geo-Blocking

```bash
# Create WAF rule to block embargoed countries
aws wafv2 create-web-acl \
  --name EAR-Embargo-Block \
  --scope REGIONAL \
  --default-action Allow={} \
  --rules file://embargo-rule.json

# embargo-rule.json includes:
# GeoMatchStatement blocking: CU, IR, KP, SY
```

#### AWS CloudFront Geo-Restrictions

```bash
# Check CloudFront distribution restrictions
aws cloudfront get-distribution-config --id DISTRIBUTION_ID

# Configure geo-restriction
{
  "GeoRestriction": {
    "RestrictionType": "blacklist",
    "Quantity": 5,
    "Items": ["CU", "IR", "KP", "SY", "UA"]
  }
}
```

#### Azure Front Door Geo-Filtering

```bash
# Create Front Door with geo-filtering
az network front-door create \
  --name ear-compliance \
  --resource-group myResourceGroup

# Add geo-filtering rules to block embargoed countries
```

#### GCP Cloud Armor

```bash
# Create Cloud Armor security policy
gcloud compute security-policies create ear-embargo-block \
  --description "Block embargoed countries for EAR compliance"

# Add rule to block countries
gcloud compute security-policies rules create 1000 \
  --security-policy ear-embargo-block \
  --expression "origin.region_code == 'CU' || origin.region_code == 'IR' || origin.region_code == 'KP' || origin.region_code == 'SY'" \
  --action "deny-403"
```

## Data Residency Verification Matrix

| Framework | Requirement | Allowed Regions | Blocked Regions |
|-----------|-------------|-----------------|-----------------|
| **ITAR** | US-only storage | us-gov-*, us-east-*, us-west-* | All non-US regions |
| **EAR** | Embargo screening | Any region worldwide | Access from CU, IR, KP, SY |

## Multi-Region Considerations

### ITAR Multi-Region

**Allowed**: Multiple US regions for redundancy
```
Primary: us-gov-west-1
Backup: us-gov-east-1
```

**Prohibited**: Cross-border replication
```
us-east-1 → eu-west-1  ❌ PROHIBITED
us-gov-west-1 → us-gov-east-1  ✅ ALLOWED
```

### EAR Multi-Region

**Allowed**: Global regions except embargoed countries
```
Primary: us-east-1
DR: eu-west-1  ✅ ALLOWED (with embargo screening)
```

**Prohibited**: Regions in embargoed countries
```
Any region → Iran/Syria/Cuba/North Korea  ❌ PROHIBITED
```

## Cloud Provider Support Matrix

| Provider | ITAR Support | EAR Support | FIPS 140-2 | Notes |
|----------|--------------|-------------|------------|-------|
| **AWS GovCloud** | ✅ Highly Recommended | ✅ Yes | Level 2+ | FedRAMP High, US persons |
| **AWS Commercial** | ⚠️ Limited (US regions) | ✅ Yes | Level 2+ | Requires additional controls |
| **Azure Government** | ✅ Highly Recommended | ✅ Yes | Level 2 | FedRAMP High |
| **Azure Commercial** | ⚠️ Limited (US regions) | ✅ Yes | Level 2 | Requires additional controls |
| **GCP Assured Workloads** | ✅ Recommended | ✅ Yes | Level 3 | With ITAR configuration |
| **GCP Commercial** | ⚠️ Limited (US regions) | ✅ Yes | Level 3 | Requires configuration |

## Verification Commands

### Check Current Data Locations

**AWS**:
```bash
# S3 bucket locations
aws s3api list-buckets | jq -r '.Buckets[].Name' | while read bucket; do
  location=$(aws s3api get-bucket-location --bucket "$bucket" --query 'LocationConstraint' --output text)
  echo "$bucket: $location"
done

# RDS instances
aws rds describe-db-instances --query 'DBInstances[*].{Name:DBInstanceIdentifier,AZ:AvailabilityZone}'

# EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Id:InstanceId,AZ:Placement.AvailabilityZone}'
```

**Azure**:
```bash
# Resource locations
az resource list --query '[].{Name:name,Location:location}' --output table

# Storage account locations
az storage account list --query '[].{Name:name,Location:location}' --output table
```

**GCP**:
```bash
# Bucket locations
gcloud storage buckets list --format='table(name,location)'

# Compute instances
gcloud compute instances list --format='table(name,zone)'

# Cloud SQL instances
gcloud sql instances list --format='table(name,region)'
```

## Compliance Recommendations

### For ITAR Workloads

1. **Use GovCloud/Government Regions**
   - AWS GovCloud (us-gov-west-1, us-gov-east-1)
   - Azure Government (usgovvirginia, usgovtexas)
   - GCP Assured Workloads (with ITAR config)

2. **Disable Cross-Border Features**
   - No global accelerators
   - No edge caching outside US
   - No replication to non-US regions

3. **Verify US-Only Personnel**
   - CSP support staff are US persons
   - No foreign national access to infrastructure

### For EAR Workloads

1. **Implement Geo-Blocking**
   - AWS WAF, CloudFront restrictions
   - Azure Front Door filtering
   - GCP Cloud Armor policies

2. **Monitor Access Logs**
   - CloudTrail, Azure Monitor, GCP Logging
   - Alert on access from embargoed countries
   - Block and report denied party access

3. **Screen Users by Geography**
   - IP-based geolocation
   - Account provisioning screening
   - Continuous monitoring

## Examples

```bash
# Verify ITAR data residency (US-only)
/us-export:data-residency itar aws

# Verify EAR embargo screening
/us-export:data-residency ear all

# Comprehensive verification for both frameworks
/us-export:data-residency both all

# Azure-specific ITAR verification
/us-export:data-residency itar azure
```

## Common Violations

### ITAR Violations

❌ **Storing data in non-US region**
```
s3://my-bucket (eu-west-1)  ← VIOLATION
```

❌ **Cross-border backup replication**
```
us-east-1 → ap-southeast-1  ← VIOLATION
```

❌ **Global CloudFront with EU edge**
```
CloudFront with European edge locations  ← VIOLATION
```

### EAR Violations

❌ **Allowing access from embargoed countries**
```
User login from Iran (IR)  ← VIOLATION
```

❌ **No geo-blocking configured**
```
WAF rules allow all countries  ← VIOLATION
```

❌ **Denied party not screened**
```
Entity List company granted access  ← VIOLATION
```

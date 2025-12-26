# GRC Engineering Plugin Suite

> **Disclaimer:** This is an independent, community-driven project and is not affiliated with, endorsed by, or officially associated with Anthropic or Claude. The author is an independent developer contributing to open source and demonstrating how these tools can be used in real-world workflows. Claude, Anthropic, and any related marks are property of their respective owners.

A comprehensive Claude Code plugin marketplace for Governance, Risk, and Compliance (GRC) professionals. Provides specialized tools for auditors, internal GRC teams, third-party risk management, and framework-specific compliance needs.

## Available Plugins

| Plugin | Namespace | Description |
|--------|-----------|-------------|
| **grc-engineer** | `/grc-engineer:` | IaC mapping, policy generation, evidence collection, PR review |
| **grc-auditor** | `/grc-auditor:` | Evidence validation, control testing, workpaper generation |
| **grc-internal** | `/grc-internal:` | Compliance tracking, risk registers, policy lifecycle |
| **grc-tprm** | `/grc-tprm:` | Vendor assessments, questionnaire analysis, risk scoring |
| **soc2** | `/soc2:` | SOC 2 Trust Service Criteria expertise |
| **nist-800-53** | `/nist:` | NIST control families and baseline selection |
| **iso27001** | `/iso:` | ISO 27001 ISMS and Annex A controls |
| **fedramp-rev5** | `/fedramp-rev5:` | Traditional FedRAMP authorization (SSP/SAP/SAR/POA&M) |
| **fedramp-20x** | `/fedramp-20x:` | Modern FedRAMP with KSIs and auto-sync from official docs |
| **pci-dss** | `/pci-dss:` | PCI DSS v4.0.1 with ROC, SAQ, and March 2025 requirements |
| **cmmc** | `/cmmc:` | CMMC v2.0 levels 1-5 for DoD contractors |
| **hitrust** | `/hitrust:` | HITRUST CSF i1/r2 healthcare assessments |
| **cis-controls** | `/cis:` | CIS Controls v8 baseline with IG1/IG2/IG3 |
| **gdpr** | `/gdpr:` | GDPR EU privacy with DPIA and rights |
| **csa-ccm** | `/ccm:` | CSA Cloud Controls Matrix 197 controls |
| **nydfs** | `/nydfs:` | NYDFS 23 NYCRR 500 financial cybersecurity |
| **dora** | `/dora:` | DORA EU financial resilience (2025) |
| **stateramp** | `/stateramp:` | State/local government cloud authorization |
| **essential8** | `/essential8:` | Australian Essential 8 maturity levels |
| **glba** | `/glba:` | GLBA financial privacy safeguards |
| **us-export** | `/us-export:` | US Export Controls: ITAR + EAR for defense/dual-use tech |
| **pbmm** | `/pbmm:` | Canadian PBMM Protected B with ITSG-33 controls |
| **ismap** | `/ismap:` | Japanese ISMAP government cloud (ISO 27001/27017/27018) |
| **irap** | `/irap:` | Australian IRAP with ISM and Essential Eight |

## Installation

### From GitHub

```bash
# Add the marketplace (one-time)
/plugin marketplace add ethanolivertroy/claude-grc-engineering

# Install specific plugins
/plugin install grc-engineer@ethanolivertroy-plugins
/plugin install grc-auditor@ethanolivertroy-plugins
/plugin install soc2@ethanolivertroy-plugins
```

### Local Development

```bash
git clone https://github.com/ethanolivertroy/claude-grc-engineering.git
claude --plugin-dir ./claude-grc-engineering
```

## Enterprise Deployment

For organizations requiring data residency, compliance certifications, or enterprise support, see the [Enterprise Deployment Guide](docs/ENTERPRISE-DEPLOYMENT.md).

### AWS Bedrock

```bash
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
claude
```

### Google Vertex AI

```bash
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
claude
```

---

## Plugins by Persona

### For GRC Engineers (`grc-engineer`)

Technical compliance automation for infrastructure teams.

**Commands:**
- `/grc-engineer:map-control` - Map IaC to compliance controls
- `/grc-engineer:generate-policy` - Generate policy-as-code
- `/grc-engineer:review-pr` - Review PRs for compliance
- `/grc-engineer:collect-evidence` - Generate evidence collection scripts
- `/grc-engineer:transform-risk` - Convert risks to Jira tickets

**NEW: Cross-Framework Intelligence**
- `/grc-engineer:map-controls-unified` - Map one control across ALL frameworks
- `/grc-engineer:find-conflicts` - Identify conflicting requirements across frameworks
- `/grc-engineer:optimize-multi-framework` - Find "implement once, satisfy many" opportunities

**NEW: Code Generation & Automation**
- `/grc-engineer:generate-implementation` - Generate Terraform, scripts, and docs from controls
- `/grc-engineer:scan-iac` - Scan infrastructure for compliance violations with auto-fix

**NEW: Control Testing & Monitoring**
- `/grc-engineer:test-control` - Automated control effectiveness testing
- `/grc-engineer:monitor-continuous` - Continuous compliance monitoring with alerts

**Example:**
```bash
# Traditional approach
/grc-engineer:map-control main.tf SOC2
/grc-engineer:generate-policy "All S3 buckets must be encrypted" rego

# Cross-framework intelligence (NEW)
/grc-engineer:map-controls-unified access_control_account_management
/grc-engineer:find-conflicts SOC2,PCI-DSS,NIST
/grc-engineer:optimize-multi-framework SOC2,PCI-DSS,NIST,ISO

# Code generation & automation (NEW)
/grc-engineer:generate-implementation access_control_account_management aws
/grc-engineer:scan-iac ./terraform SOC2,PCI-DSS,NIST --fix

# Control testing & monitoring (NEW)
/grc-engineer:test-control access_control_account_management aws
/grc-engineer:monitor-continuous SOC2,PCI-DSS,NIST daily --slack-webhook=URL
```

**Key Features:**
- **Control Crosswalk Database**: Maps 300+ controls across 7+ frameworks
- **Conflict Resolution**: Automatically identifies and resolves requirement conflicts
- **Effort Reduction**: Shows 56% average effort savings through optimization
- **Code Generation**: Auto-generates Terraform, Python scripts, monitoring dashboards
- **IaC Scanning**: Finds violations in existing infrastructure with automated remediation
- **Control Testing**: Validates controls are actually working (config, functionality, compliance)
- **Continuous Monitoring**: 30-day trend analysis, alerting, dashboard
- **Cloud Implementation**: Multi-cloud patterns for AWS, Azure, GCP, Kubernetes

### For Auditors (`grc-auditor`)

Evidence review and audit workpaper generation for external auditors.

**Commands:**
- `/grc-auditor:review-evidence` - Validate evidence artifacts
- `/grc-auditor:validate-control` - Test control implementation
- `/grc-auditor:generate-workpaper` - Create audit workpapers

**Example:**
```bash
/grc-auditor:review-evidence ./evidence/access-reviews.pdf CC6.1
/grc-auditor:generate-workpaper finding "Access Control Deficiency"
```

### For Internal GRC Teams (`grc-internal`)

Compliance tracking and risk management for internal teams.

**Commands:**
- `/grc-internal:track-compliance` - Monitor compliance status
- `/grc-internal:manage-risk` - Maintain risk registers
- `/grc-internal:update-policy` - Manage policy lifecycle

**Example:**
```bash
/grc-internal:track-compliance SOC2 detailed
/grc-internal:manage-risk add "Cloud misconfiguration exposure"
```

### For TPRM Teams (`grc-tprm`)

Vendor risk assessment and questionnaire analysis.

**Commands:**
- `/grc-tprm:assess-vendor` - Perform vendor assessment
- `/grc-tprm:analyze-questionnaire` - Analyze SIG/CAIQ responses
- `/grc-tprm:score-risk` - Calculate vendor risk scores

**Example:**
```bash
/grc-tprm:assess-vendor "Acme Cloud Services" initial
/grc-tprm:analyze-questionnaire ./responses/acme-sig.xlsx SIG
```

---

## Framework Plugins

### SOC 2 (`soc2`)

Deep expertise in SOC 2 Trust Service Criteria.

**Commands:**
- `/soc2:assess` - Assess SOC 2 readiness
- `/soc2:map-controls` - Map to Trust Service Criteria

**Coverage:** CC1-CC9 (Security), Availability, Confidentiality, Processing Integrity, Privacy

### NIST 800-53 (`nist-800-53`)

Complete NIST SP 800-53 control framework support.

**Commands:**
- `/nist:assess` - Assess NIST compliance
- `/nist:select-baseline` - Select and tailor baselines

**Coverage:** All 20 control families, Low/Moderate/High baselines

### ISO 27001 (`iso27001`)

ISO/IEC 27001:2022 ISMS implementation guidance.

**Commands:**
- `/iso:assess` - Assess ISO 27001 compliance
- `/iso:gap-analysis` - Perform gap analysis

**Coverage:** Clauses 4-10, Annex A controls (93 controls)

### FedRAMP Rev 5 (`fedramp-rev5`)

Traditional federal cloud authorization path.

**Commands:**
- `/fedramp-rev5:assess` - Assess authorization readiness
- `/fedramp-rev5:ssp-guidance` - SSP documentation help
- `/fedramp-rev5:poam-review` - POA&M analysis
- `/fedramp-rev5:baseline-select` - Baseline selection

**Coverage:** Low/Moderate/High baselines, JAB/Agency paths, SSP/SAP/SAR/POA&M

### FedRAMP 20X (`fedramp-20x`)

Modern automated authorization with continuous monitoring.

**Commands:**
- `/fedramp-20x:ksi-check` - Check Key Security Indicators
- `/fedramp-20x:vdr-assess` - Vulnerability Detection & Response
- `/fedramp-20x:mas-review` - Minimum Assessment Scope
- `/fedramp-20x:sync-docs` - Sync from official FedRAMP/docs repo

**Coverage:** 8 KSI categories, machine-readable policies, auto-sync from https://github.com/FedRAMP/docs

### PCI DSS (`pci-dss`)

Payment Card Industry Data Security Standard v4.0.1.

**Commands:**
- `/pci-dss:assess` - Compliance readiness assessment
- `/pci-dss:roc-guidance` - ROC template guidance
- `/pci-dss:saq-select` - SAQ type selection (A, A-EP, B, C, D, P2PE)
- `/pci-dss:requirement` - Deep dive on requirements 1-12
- `/pci-dss:march-2025` - New mandatory requirements

**Coverage:** 12 requirements, ROC/SAQ support, March 2025 mandatory requirements

### CMMC (`cmmc`)

Cybersecurity Maturity Model Certification v2.0 for DoD contractors.

**Commands:**
- `/cmmc:assess` - CMMC readiness assessment by level
- `/cmmc:level-select` - Determine required CMMC level
- `/cmmc:domain-guidance` - Deep dive on 14 domains
- `/cmmc:practice-check` - Verify specific practice implementation

**Coverage:** 5 levels, 14 domains, 171 practices, C3PAO assessment prep

### HITRUST (`hitrust`)

Healthcare Information Trust Alliance Common Security Framework.

**Commands:**
- `/hitrust:assess` - HITRUST readiness by assessment type
- `/hitrust:scope-select` - Determine i1 vs r2 assessment
- `/hitrust:control-map` - Map to source frameworks
- `/hitrust:gap-analysis` - Identify control gaps

**Coverage:** 156 controls, i1/r2/e1 assessments, MyCSF customization

### CIS Controls (`cis-controls`)

Center for Internet Security baseline security framework v8.

**Commands:**
- `/cis:assess` - CIS Controls compliance by IG level
- `/cis:ig-select` - Determine appropriate Implementation Group
- `/cis:control-check` - Verify specific control implementation
- `/cis:safeguard-list` - List applicable safeguards by IG

**Coverage:** 18 controls, 153 safeguards, IG1/IG2/IG3 implementation groups

### GDPR (`gdpr`)

EU General Data Protection Regulation privacy compliance.

**Commands:**
- `/gdpr:assess` - GDPR compliance readiness
- `/gdpr:dpia` - Data Protection Impact Assessment guidance
- `/gdpr:rights-check` - Verify data subject rights implementation
- `/gdpr:breach-process` - Breach notification procedures

**Coverage:** 99 articles, 7 principles, DPO requirements, 72-hour breach notification

### CSA CCM (`csa-ccm`)

Cloud Security Alliance Cloud Controls Matrix.

**Commands:**
- `/ccm:assess` - CCM compliance assessment
- `/ccm:domain-guidance` - Deep dive on 17 domains
- `/ccm:map-framework` - Map CCM to other frameworks
- `/ccm:caiq-generate` - Generate CAIQ responses

**Coverage:** 197 controls, 17 domains, cloud security, CAIQ support

### NYDFS (`nydfs`)

New York Department of Financial Services 23 NYCRR 500 cybersecurity requirements.

**Commands:**
- `/nydfs:assess` - NYDFS compliance readiness
- `/nydfs:certification` - Annual certification guidance
- `/nydfs:ciso-requirements` - CISO role and responsibilities
- `/nydfs:pentest-plan` - Penetration testing requirements

**Coverage:** 23 sections, annual certification, CISO requirements, pentest guidance

### DORA (`dora`)

EU Digital Operational Resilience Act for financial entities (effective January 2025).

**Commands:**
- `/dora:assess` - DORA compliance readiness
- `/dora:pillar-guidance` - Deep dive on 5 pillars
- `/dora:incident-reporting` - Major incident reporting process
- `/dora:testing-plan` - Resilience testing requirements

**Coverage:** 5 pillars, ICT risk management, incident reporting, EU financial sector

### StateRAMP (`stateramp`)

State Risk and Authorization Management Program for state/local government cloud.

**Commands:**
- `/stateramp:assess` - StateRAMP authorization readiness
- `/stateramp:impact-select` - Determine Low vs Moderate
- `/stateramp:documentation` - ATO package guidance
- `/stateramp:state-specific` - State-by-state variations

**Coverage:** Low/Moderate impact levels, state authorization, continuous monitoring

### Essential 8 (`essential8`)

Australian Cyber Security Centre mitigation strategies.

**Commands:**
- `/essential8:assess` - Essential 8 maturity assessment
- `/essential8:maturity-level` - Determine target maturity level
- `/essential8:strategy-check` - Verify specific strategy implementation
- `/essential8:roadmap` - Maturity improvement roadmap

**Coverage:** 8 strategies, 3 maturity levels, ACSC guidance

### GLBA (`glba`)

Gramm-Leach-Bliley Act for financial institution privacy and security.

**Commands:**
- `/glba:assess` - GLBA compliance readiness
- `/glba:safeguards` - Safeguards Rule implementation
- `/glba:privacy` - Privacy Rule compliance
- `/glba:risk-assessment` - GLBA risk assessment guidance

**Coverage:** Safeguards Rule, Privacy Rule, FTC enforcement, financial institutions

### US Export Controls (`us-export`)

Combined ITAR and EAR compliance for defense and dual-use technologies.

**Commands:**
- `/us-export:assess` - Unified ITAR+EAR assessment
- `/us-export:itar-assess` - ITAR-specific (defense articles)
- `/us-export:ear-assess` - EAR-specific (dual-use commercial)
- `/us-export:jurisdiction` - Determine ITAR vs EAR applicability
- `/us-export:data-residency` - Region verification
- `/us-export:compliance-matrix` - ITAR vs EAR crosswalk

**Coverage:** ITAR (7 controls, US-only data, US persons), EAR (7 controls, ECCN, denied parties, embargo countries)

### PBMM (`pbmm`)

Canadian Protected B, Medium Integrity, Medium Availability cloud security.

**Commands:**
- `/pbmm:assess` - Protected B compliance readiness
- `/pbmm:profile-select` - Classification level selection
- `/pbmm:cccs-guidance` - CCCS assessment process
- `/pbmm:data-residency` - Canadian region verification

**Coverage:** 10 ITSG-33 controls, Canadian data sovereignty, CCCS certification

### ISMAP (`ismap`)

Japanese government cloud security based on ISO standards.

**Commands:**
- `/ismap:assess` - ISMAP compliance readiness
- `/ismap:iso-mapping` - Map to ISO 27001/27017/27018
- `/ismap:registration` - ISMAP registration process
- `/ismap:data-residency` - Japanese region verification

**Coverage:** 12 controls, ISO 27001 Annex A, ISO 27017 cloud, ISO 27018 PII

### IRAP (`irap`)

Australian government cloud security with ISM and Essential Eight.

**Commands:**
- `/irap:assess` - ISM and Essential Eight assessment
- `/irap:essential-8` - Deep dive on 8 mitigation strategies
- `/irap:classification` - Classification level selection
- `/irap:data-residency` - Australian region verification

**Coverage:** 8 ISM controls, Essential Eight maturity levels, ACSC guidelines

---

## Multi-Cloud Support

Evidence collection supports multiple cloud providers:

| Provider | CLI Tools | Python SDKs |
|----------|-----------|-------------|
| **AWS** | `aws iam`, `aws s3api`, `aws cloudtrail` | boto3 |
| **Azure** | `az ad`, `az storage`, `az monitor` | azure-* |
| **GCP** | `gcloud iam`, `gcloud storage`, `gcloud logging` | google-cloud-* |
| **Kubernetes** | `kubectl get`, `kubectl auth` | kubernetes |

---

## Architecture

```
claude-grc-engineering/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace configuration
├── plugins/
│   ├── grc-engineer/             # Technical compliance automation
│   ├── grc-auditor/              # Audit and assessment tools
│   ├── grc-internal/             # Internal GRC team tools
│   ├── grc-tprm/                 # Third-party risk management
│   └── frameworks/
│       ├── soc2/                 # SOC 2 expertise
│       ├── nist-800-53/          # NIST 800-53 controls
│       ├── iso27001/             # ISO 27001 ISMS
│       ├── fedramp-rev5/         # FedRAMP Rev 5 traditional
│       └── fedramp-20x/          # FedRAMP 20X automated (auto-sync)
├── shared/                       # Shared configurations
└── docs/
    └── ENTERPRISE-DEPLOYMENT.md  # Bedrock/Vertex AI setup
```

---

## Configuration

### Compliance Frameworks

Framework configurations in `plugins/grc-engineer/config/frameworks/`:

```yaml
# soc2.yaml
controls:
  CC6.1:
    title: Logical and Physical Access Controls
    keywords: [iam, access control, authentication]
```

### Cloud Providers

Provider templates in `plugins/grc-engineer/config/providers/`:

```yaml
# aws.yaml
templates:
  mfa_root:
    keywords: [mfa, root]
    formats:
      python: |
        import boto3
        # ...
      bash: |
        aws iam get-account-summary
```

---

## License

MIT

## Contributing

Contributions welcome! Please see individual plugin directories for specific guidelines.

# Changelog

All notable changes follow the format from [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

**Foundations**
- `schemas/finding.schema.json` v1.0.0. The canonical output contract for connector plugins.
- `LICENSE` at repo root (MIT with third-party attributions for SCF and CIS Controls).
- Secure Controls Framework (SCF) as the canonical crosswalk backbone. 1,468 controls mapped to 249 frameworks, fetched from [`hackidle.github.io/scf-api`](https://hackidle.github.io/scf-api/) and cached locally under CC BY-ND 4.0.
- `docs/ARCHITECTURE.md`, `docs/QUICKSTART.md`, `docs/CONTRIBUTING.md`, `docs/SCF-ATTRIBUTION.md`.

**Orchestration**
- `/grc-engineer:gap-assessment`. Unified cross-framework command that joins connector findings with the SCF crosswalk and emits a tiered gap report (markdown, JSON, SARIF, or OSCAL Assessment Results).
- `/grc-engineer:pipeline-status`. Aggregate connector health: auth validity, cache freshness, resource and evaluation counts.

**Connectors (Tier 1)**
- `aws-inspector`. IAM (root MFA, password policy, access keys), S3 (encryption, public access, versioning), CloudTrail (multi-region, log validation, active logging), EBS (default encryption).
- `github-inspector`. Branch protection, required status checks, secret scanning, Dependabot, code scanning. Tested end-to-end against live GitHub.
- `gcp-inspector`. IAM primitive roles, service-account key age, Cloud Storage (public-access prevention, uniform access, logging, CMEK), log sinks, KMS rotation (≤90d), Compute OS Login.
- `okta-inspector`. Password, MFA enrollment, and sign-on policies. Session lifetime and idle timeouts. Inactive users, super-admin count, per-admin factor enrollment.

**OSCAL / FedRAMP showcase plugins**
- `oscal`. Wraps `ethanolivertroy/oscal-cli` for validate and convert commands across catalogs, profiles, SSPs, SAPs, SARs, POA&Ms, assessment results, and component definitions. Auto-installs from source. Degrades gracefully when the upstream binary isn't available.
- `fedramp-ssp`. Wraps `ethanolivertroy/frdocx-to-froscal-ssp` to convert FedRAMP Rev 5 SSP DOCX templates into OSCAL 1.2.0 SSP JSON (323 implemented-requirements across 18 NIST 800-53 Rev 5 families). Tolerates venv and Homebrew-Python edge cases with clear remediation.

**Licensing and hygiene**
- CIS Controls plugin isolation: `plugins/frameworks/cis-controls/LICENSE-CIS.md` plus CC BY-SA 4.0 attribution headers on every command and SKILL in that directory.
- HITRUST plugin carries a reference-only disclaimer. Paraphrased one CSF-echoing phrase in `evidence-checklist.md`.
- SOC 2 command documentation renamed the fictional example audit firm from "Deloitte" / "Deloitte & Touche LLP" to "Example Audit LLP". These were always illustrative placeholders in command examples. No real auditor engagement or contact was ever in the repo. The new name makes the illustrative intent unambiguous.
- `.gitignore` covering in-progress work (`data/`, `grc-audit-manager/`, `grc-cert-manager/`, `grc-program-manager/`) and runtime artifacts.

### Changed
- README rewritten around capability-first workflows and the data-pipeline model.
- Plugin taxonomy restructured into five categories: engineering hub, persona, framework, connector, OSCAL / FedRAMP showcase.

### Planned (v0.2 roadmap)
- `compliance-trestle` plugin: first-class integration with `ethanolivertroy/compliance-trestle-skills` for OSCAL authoring workflows.
- `fedramp-docs` plugin: MCP server integration with `ethanolivertroy/fedramp-docs-mcp` for live FedRAMP documentation lookup.
- `vanta-bridge` plugin: wraps `ethanolivertroy/vanta-go-export` to pull Vanta evidence and normalize to v1 findings.
- `azure-inspector` connector (Tier 2 promotion).
- Deeper connector coverage: per-user IAM for AWS, shielded-VM + VPC-SC for GCP, factor-type analysis for Okta.
- `/grc-engineer:monitor-continuous` cron-friendly scheduling wrapper with EventBridge and GitHub Actions templates.

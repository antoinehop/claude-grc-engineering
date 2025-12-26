# Enterprise Deployment Guide

This guide covers deploying Claude Code with GRC Engineering plugins using enterprise-grade infrastructure through AWS Bedrock or Google Vertex AI. These options ensure your data stays within your cloud environment and meets compliance requirements.

## Why Use Enterprise Deployment?

| Benefit | Description |
|---------|-------------|
| **Data Residency** | Data never leaves your cloud environment |
| **Compliance** | Meet regulatory requirements (FedRAMP, HIPAA, SOC 2) |
| **No Data Training** | Your data is not used to train models |
| **Enterprise Support** | Cloud provider SLAs and support |
| **Audit Trails** | Full logging through CloudTrail/Cloud Audit Logs |

---

## AWS Bedrock Configuration

### Prerequisites

1. AWS account with Bedrock access enabled
2. Claude model access enabled in Bedrock console
3. AWS CLI configured (optional, for credential management)
4. Claude Code v1.0.33 or later

### Enable Claude in Bedrock

1. Navigate to AWS Console → Bedrock → Model access
2. Request access to Anthropic Claude models
3. Wait for access approval (usually immediate)

### Configuration Methods

#### Method 1: Environment Variables

```bash
# Required
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Optional: Specify model
export ANTHROPIC_MODEL='us.anthropic.claude-sonnet-4-20250514'

# Start Claude Code
claude
```

#### Method 2: Settings File

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "AWS_REGION": "us-east-1",
    "ANTHROPIC_MODEL": "us.anthropic.claude-sonnet-4-20250514"
  }
}
```

### AWS Authentication Options

Claude Code uses the standard AWS SDK credential chain:

#### Option A: IAM Identity Center (Recommended for Organizations)

```bash
# Configure SSO
aws configure sso

# Login
aws sso login --profile your-profile

# Set profile
export AWS_PROFILE=your-profile
```

#### Option B: Environment Variables

```bash
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
# Optional for temporary credentials
export AWS_SESSION_TOKEN=your-session-token
```

#### Option C: IAM Role (EC2/ECS/Lambda)

When running on AWS infrastructure, use IAM roles attached to your compute resource. No additional configuration needed.

### Required IAM Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-*"
      ]
    }
  ]
}
```

### Available Models in Bedrock

| Model | Model ID |
|-------|----------|
| Claude Sonnet 4 | `us.anthropic.claude-sonnet-4-20250514` |
| Claude 3.5 Sonnet | `us.anthropic.claude-3-5-sonnet-20241022-v2:0` |
| Claude 3.5 Haiku | `us.anthropic.claude-3-5-haiku-20241022-v1:0` |

---

## Google Vertex AI Configuration

### Prerequisites

1. Google Cloud project with Vertex AI enabled
2. Claude model access enabled in Model Garden
3. gcloud CLI configured (optional)
4. Claude Code v1.0.33 or later

### Enable Claude in Vertex AI

1. Navigate to Google Cloud Console → Vertex AI → Model Garden
2. Search for "Claude" and select desired model
3. Enable the model for your project

### Configuration Methods

#### Method 1: Environment Variables

```bash
# Required
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Start Claude Code
claude
```

#### Method 2: Settings File

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_USE_VERTEX": "1",
    "CLOUD_ML_REGION": "us-east5",
    "ANTHROPIC_VERTEX_PROJECT_ID": "your-project-id"
  }
}
```

### GCP Authentication Options

#### Option A: Application Default Credentials (Recommended)

```bash
gcloud auth application-default login
```

#### Option B: Service Account Key

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

#### Option C: Workload Identity (GKE)

Configure Workload Identity Federation for your GKE cluster.

### Required IAM Permissions

Grant the following roles to your service account or user:

- `roles/aiplatform.user` - Vertex AI User

Or create a custom role with:

```yaml
includedPermissions:
  - aiplatform.endpoints.predict
```

### Available Regions

Claude is available in these Vertex AI regions:
- `us-east5` (Virginia)
- `europe-west1` (Belgium)

---

## Compliance Considerations

### FedRAMP

- **AWS Bedrock**: FedRAMP High authorized in GovCloud regions
- **Vertex AI**: FedRAMP Moderate authorized

### HIPAA

Both AWS Bedrock and Vertex AI support HIPAA workloads with appropriate BAAs in place.

### SOC 2

Both platforms maintain SOC 2 Type II reports. Request from your account team.

### Data Processing

| Provider | Data Usage |
|----------|------------|
| AWS Bedrock | Not used for model training |
| Vertex AI | Not used for model training |
| Anthropic API | Not used for model training (with API) |

---

## Troubleshooting

### AWS Bedrock

**Error: Access Denied**
- Verify model access is enabled in Bedrock console
- Check IAM permissions include `bedrock:InvokeModel`
- Confirm region supports Claude models

**Error: Model not found**
- Use fully qualified model ID with region prefix
- Verify model is available in your region

### Vertex AI

**Error: Permission Denied**
- Verify Vertex AI API is enabled
- Check service account has `aiplatform.user` role
- Confirm project ID is correct

**Error: Region not supported**
- Use `us-east5` or `europe-west1` for Claude

---

## Cost Optimization

### Prompt Caching

Both platforms support prompt caching to reduce costs for repeated context:

```bash
# AWS Bedrock - enabled automatically
export ANTHROPIC_MODEL='us.anthropic.claude-sonnet-4-20250514'

# Vertex AI - check documentation for cache configuration
```

### Model Selection

| Use Case | Recommended Model |
|----------|-------------------|
| Complex GRC analysis | Claude Sonnet 4 |
| Quick queries | Claude 3.5 Haiku |
| High-volume processing | Claude 3.5 Haiku |

---

## Next Steps

1. Choose your deployment option (Bedrock or Vertex AI)
2. Configure authentication
3. Install the GRC Engineering plugins:
   ```bash
   /plugin marketplace add ethanolivertroy/claude-grc-engineering
   /plugin install grc-engineer@ethanolivertroy-plugins
   ```
4. Start using GRC commands with enterprise-grade security!

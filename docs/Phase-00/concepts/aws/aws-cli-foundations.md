# AWS CLI Foundations

## 1. Introduction

The AWS Command Line Interface (AWS CLI) is a tool that allows engineers to interact with AWS services from a terminal.

Instead of using only the AWS Console, engineers can automate and manage AWS resources through commands.

The workflow:

```
Engineer

    |
    v

AWS CLI

    |
    v

AWS Services
```

---

# 2. Why AWS CLI Matters for MLOps

MLOps engineers work with automation.

Common workflows include:

- Uploading data to S3.
- Triggering ML jobs.
- Managing infrastructure.
- Checking logs.
- Automating deployments.

Example:

```
Local Development Environment

        |
        v

AWS CLI / SDK

        |
        v

AWS Cloud Resources
```

---

# 3. AWS CLI Components

The AWS CLI provides commands for AWS services.

Examples:

## S3

Manage storage:

```
aws s3 ls
```

Example uses:

- List buckets.
- Upload datasets.
- Download artifacts.

---

## EC2

Manage compute resources:

```
aws ec2 describe-instances
```

Example uses:

- Check running instances.
- Retrieve resource information.

---

## SageMaker

Manage machine learning resources:

```
aws sagemaker list-training-jobs
```

Example uses:

- Monitor training jobs.
- Check model deployments.

---

# 4. Authentication

AWS CLI requires authentication.

The recommended approach:

```
AWS Identity

        |
        v

Authentication

        |
        v

AWS CLI

        |
        v

AWS Resources
```

Common methods:

- IAM roles.
- IAM Identity Center.
- Temporary credentials.

Avoid:

- Hardcoded credentials.
- Credentials stored in code.
- Sharing access keys.

---

# 5. AWS CLI Configuration

After installation, engineers configure AWS CLI:

```
aws configure
```

This creates local configuration files:

```
AWS CLI Configuration

        |
        v

~/.aws/

        |
        +----------------+
        |                |
        v                v

 credentials       config
```

---

# 6. AWS CLI and Terraform Relationship

Terraform does not replace AWS CLI.

They have different roles:

```
Terraform

    |
    v

Infrastructure Creation


AWS CLI

    |
    v

AWS Resource Interaction
```

Example:

Terraform:

- Create S3 bucket.
- Create IAM role.
- Create SageMaker infrastructure.

AWS CLI:

- Check resources.
- Upload files.
- Execute operational commands.

---

# 7. AWS CLI in the MLOps Workflow

A typical local workflow:

```
Developer

    |
    v

VS Code Terminal

    |
    v

AWS CLI / Terraform

    |
    v

AWS Infrastructure

    |
    v

ML Platform
```

---

# Summary

AWS CLI is an essential tool for MLOps engineers because it enables automation and direct interaction with AWS services.

Together:

```
Terraform
    +
AWS CLI
    +
AWS SDKs
```

provide the foundation for managing production machine learning infrastructure.
```
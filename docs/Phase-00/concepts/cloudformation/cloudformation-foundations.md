# CloudFormation Foundations

## 1. Introduction

AWS CloudFormation is Amazon Web Services' native Infrastructure as Code (IaC) service.

It allows engineers to define AWS infrastructure using declarative templates instead of manually creating resources through the AWS Console.

The main idea:

```text
Infrastructure Requirements
        |
        v
CloudFormation Template
        |
        v
AWS Resources
```

The engineer describes the desired infrastructure state, and AWS CloudFormation creates and manages the required resources.

---

# 2. Why Infrastructure as Code Exists

Traditional infrastructure management:

```text
Engineer
   |
   v
AWS Console
   |
   v
Manual Resource Creation
```

Problems:

- Difficult to reproduce environments.
- Higher probability of human errors.
- Hard to review infrastructure changes.
- Difficult to automate deployments.

Infrastructure as Code changes the workflow:

```text
Infrastructure Definition
          |
          v
Version Control
          |
          v
Automated Deployment
          |
          v
Repeatable Environment
```

---

# 3. CloudFormation Core Concepts

## Templates

CloudFormation uses templates written mainly in:

- YAML
- JSON

A template describes:

- Resources
- Parameters
- Outputs
- Dependencies
- Configurations

Example structure:

```yaml
AWSTemplateFormatVersion: "2010-09-09"

Description:
  Example CloudFormation template

Resources:
  ExampleResource:
    Type: AWS::S3::Bucket
```

---

## Resources

Resources are AWS components created by CloudFormation.

Examples:

- S3 buckets
- EC2 instances
- IAM roles
- Lambda functions
- SageMaker resources

Example:

```yaml
Resources:
  MLDataBucket:
    Type: AWS::S3::Bucket
```

---

## Parameters

Parameters allow templates to receive inputs.

Examples:

- AWS region
- Environment name
- Instance type

Conceptually:

```text
Input Parameters
        |
        v
CloudFormation Template
        |
        v
AWS Infrastructure
```

---

## Outputs

Outputs expose useful information after deployment.

Examples:

- Resource IDs
- URLs
- Endpoints

---

# 4. CloudFormation Deployment Workflow

Typical workflow:

```text
CloudFormation Template
          |
          v
Validate Template
          |
          v
Create Stack
          |
          v
AWS Resources Created
          |
          v
Update Stack
          |
          v
Delete Stack
```

CloudFormation manages infrastructure through **Stacks**.

A stack represents a collection of AWS resources managed together.

---

# 5. CloudFormation vs Terraform

## CloudFormation

Advantages:

- Native AWS integration.
- No external provider required.
- Direct AWS support.
- Strong AWS feature compatibility.

Disadvantages:

- AWS-only.
- Templates can become complex.
- Less portable.

---

## Terraform

Advantages:

- Multi-cloud support.
- Large provider ecosystem.
- Common industry standard.
- Strong modularity.

Disadvantages:

- Requires provider management.
- State management is external.
- Additional abstraction layer.

---

# 6. Role in MLOps Engineering

CloudFormation and Terraform solve the same general problem:

> Automating infrastructure creation.

In an MLOps platform, IaC can create:

- Networking
- Storage
- IAM permissions
- Compute resources
- ML deployment infrastructure
- Monitoring components

Example:

```text
Machine Learning System

        |
        v

Infrastructure as Code

        |
        +----------------+
        |                |
        v                v
     Storage          Compute
       S3             SageMaker

        |
        v

Monitoring
CloudWatch
```

---

# 7. Terraform Decision for This Roadmap

For this roadmap:

Primary IaC tool:

```text
Terraform
```

Reason:

- Industry adoption.
- Multi-cloud capability.
- Better portability.
- Common requirement for MLOps engineers.

CloudFormation knowledge remains important because:

- It is AWS native.
- Many AWS environments use it.
- Understanding it improves AWS infrastructure literacy.

---

# 8. Summary

CloudFormation is AWS's native Infrastructure as Code service.

Terraform and CloudFormation both allow infrastructure automation.

The roadmap uses:

```text
Terraform
    |
    v
Primary Infrastructure as Code tool


CloudFormation
    |
    v
AWS-native IaC knowledge
```

Understanding both provides a stronger foundation for designing production MLOps platforms.
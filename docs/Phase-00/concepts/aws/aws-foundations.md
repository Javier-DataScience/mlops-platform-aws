# AWS Foundations

## 1. Introduction

Amazon Web Services (AWS) is a cloud computing platform that provides infrastructure and managed services for building, deploying, and operating applications.

For an MLOps Engineer, AWS provides the infrastructure layer required to build production machine learning systems.

The main idea:

```
Machine Learning Application
          |
          v
MLOps Platform
          |
          v
AWS Cloud Infrastructure
```

AWS provides services for:

- Compute
- Storage
- Networking
- Security
- Machine Learning
- Monitoring
- Deployment automation

---

# 2. AWS Global Infrastructure

AWS infrastructure is organized into different geographic levels.

```
AWS Global Infrastructure

        |
        v

Regions

        |
        v

Availability Zones

        |
        v

Data Centers
```

## Regions

A Region is a geographic area containing multiple Availability Zones.

Examples:

- us-east-1 (N. Virginia)
- us-west-2 (Oregon)
- eu-west-1 (Ireland)

Region selection depends on:

- Data residency requirements
- Latency
- Service availability
- Cost

---

## Availability Zones

An Availability Zone (AZ) is one or more physically separate data centers within a Region.

Multiple AZs provide:

- High availability
- Fault tolerance
- Disaster recovery capability

Example:

```
AWS Region

    |
    +----------------+
    |                |
    v                v

 Availability     Availability
 Zone A           Zone B
```

---

# 3. AWS Account Foundations

An AWS account represents an isolated AWS environment.

A production organization usually separates environments:

```
AWS Organization

        |
        +----------------+
        |                |
        v                v

 Development        Production
 Account            Account
```

Benefits:

- Security isolation
- Cost tracking
- Better governance
- Reduced risk

---

# 4. Identity and Access Management (IAM)

IAM controls:

- Who can access AWS resources.
- What actions they can perform.
- Which resources they can access.

Core IAM concepts:

## Users

Represent individual identities.

Examples:

- Developer
- Data Scientist
- MLOps Engineer

---

## Roles

Temporary permissions assumed by services or users.

Examples:

- SageMaker execution role
- EC2 instance role
- CI/CD deployment role

For MLOps, roles are preferred over long-lived credentials.

---

## Policies

Define permissions.

Example:

```
Identity
    |
    v
IAM Policy
    |
    v
AWS Resource Access
```

---

# 5. Core AWS Services for MLOps

The main AWS services used in this roadmap:

## Amazon S3

Object storage service.

Common MLOps uses:

- Dataset storage
- Model artifacts
- Training outputs
- Feature data

Architecture example:

```
Training Pipeline

      |
      v

Amazon S3

      |
      v

Model Artifact
```

---

## Amazon EC2

Virtual compute instances.

Used for:

- Custom environments
- ML workloads
- Development machines

---

## Amazon SageMaker

Managed machine learning platform.

Provides:

- Training jobs
- Model deployment
- Endpoints
- Experiments
- Pipelines

Example:

```
Data
 |
 v
S3
 |
 v
SageMaker Training
 |
 v
Model Endpoint
```

---

## Amazon ECR

Elastic Container Registry.

Stores Docker images used by AWS services.

Example:

```
Docker Image

      |
      v

Amazon ECR

      |
      v

SageMaker / ECS / Kubernetes
```

---

## Amazon CloudWatch

Monitoring service.

Used for:

- Logs
- Metrics
- Alerts
- Operational monitoring

---

# 6. AWS in an MLOps Architecture

A simplified production ML platform:

```
Data Sources

      |
      v

Amazon S3

      |
      v

Training Pipeline

      |
      v

SageMaker Training

      |
      v

Model Registry

      |
      v

Deployment Endpoint

      |
      v

CloudWatch Monitoring
```

---

# 7. Infrastructure as Code in AWS

AWS infrastructure should not be created manually.

The preferred workflow:

```
Infrastructure Definition

        |
        v

Terraform

        |
        v

AWS Resources

        |
        v

Version Control
```

Terraform will manage:

- Networking
- Storage
- Compute
- IAM roles
- ML infrastructure

---

# 8. AWS Security Principles

Important principles:

## Least Privilege

Give only the permissions required.

---

## Avoid Long-Term Credentials

Prefer:

- IAM roles
- Temporary credentials
- Identity federation

---

## Separate Environments

Avoid mixing:

- Development
- Testing
- Production

---

# 9. AWS Cost Awareness

Cloud resources have costs.

MLOps engineers must understand:

- Instance pricing
- Storage costs
- Data transfer costs
- Idle resources

Good practices:

- Delete unused resources.
- Monitor costs.
- Automate cleanup.
- Use appropriate instance sizes.

---

# 10. AWS Role in This Roadmap

AWS will be the main cloud platform used for production MLOps exercises.

The roadmap will progressively introduce:

```
Phase 0
AWS Foundations

        |
        v

Infrastructure as Code

        |
        v

Cloud ML Platforms

        |
        v

Production MLOps Systems
```

---

# Summary

AWS provides the cloud foundation required to build production machine learning systems.

For an MLOps Engineer, the most important AWS knowledge areas are:

- Infrastructure
- Security
- Storage
- Compute
- Machine Learning services
- Monitoring
- Automation

This roadmap focuses on AWS as the execution platform for production MLOps engineering.
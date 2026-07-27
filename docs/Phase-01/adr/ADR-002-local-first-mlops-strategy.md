# ADR-002: Local First MLOps Strategy

## Status

Accepted

---

## Date

2026-07-27

---

# 1. Context

The objective of this roadmap is to build an enterprise-oriented MLOps platform focused on AWS technologies.

However, developing every component directly in AWS from the beginning introduces unnecessary complexity and cost.

The project requires a development strategy that allows:

- Understanding the architecture deeply.
- Building reproducible pipelines.
- Testing engineering decisions.
- Controlling cloud costs.
- Preparing components before AWS deployment.

---

# 2. Decision

The project follows a:

```
Local Development First

        ↓

Cloud Validation Second

        ↓

Production AWS Implementation
```

strategy.

All components are initially developed locally using production-oriented engineering practices.

After validation, components are migrated or integrated with AWS services.

---

# 3. Local Development Environment

The local environment represents the initial implementation platform.

Architecture:

```
Developer Environment

        |
        |
        v

Python MLOps Components

        |
        |
        +----------------+
        |                |
        v                v

Data Pipelines    ML Components

        |
        |
        v

Local Validation
```

Local technologies include:

- Python.
- Pandas.
- NumPy.
- Pytest.
- Ruff.
- MyPy.
- UV.
- Git.
- Docker (when required).

---

# 4. Cloud Evolution Strategy

The local implementations are designed to map naturally to AWS services.

Evolution:

```
Local Component

        ↓

AWS Equivalent

        ↓

Production Architecture
```

Examples:

---

## Data Storage

Local:

```
data/
```

Future AWS:

```
Amazon S3 Data Lake
```

---

## Data Processing

Local:

```
Python Processing Scripts

        |
        |
        v

Local Pipelines
```

Future AWS:

```
SageMaker Processing Jobs

        |
        |
        v

Managed Data Pipelines
```

---

## Feature Engineering

Local:

```
Feature Engineering Modules

        |
        |
        v

Local Offline Feature Store
```

Future AWS:

```
SageMaker Feature Store

        |
        |
        +----------------+
        |                |
        v                v

Offline Store      Online Store
```

---

# 5. Reasons for the Decision

## Cost Optimization

AWS resources can generate unnecessary costs during experimentation.

The local-first approach reduces:

- Storage costs.
- Compute costs.
- Accidental resource usage.

---

## Architectural Understanding

Developing locally forces understanding of:

- Data flow.
- Dependencies.
- Pipeline design.
- Software engineering practices.

This avoids treating AWS services as black boxes.

---

## Faster Iteration

Local development allows:

- Faster testing.
- Easier debugging.
- Immediate feedback.

---

## Production Readiness

The objective is not to create simple local scripts.

All components must follow production practices:

- Modular architecture.
- Testing.
- Documentation.
- Version control.
- Automation.

---

# 6. Alternatives Considered

## AWS First Development

Rejected.

Reasons:

- Higher cost.
- Increased complexity.
- Difficult debugging.
- Less understanding of internal architecture.

---

## Notebook-Based Development

Rejected.

Reasons:

- Limited reproducibility.
- Poor testing practices.
- Difficult production transition.

---

# 7. Consequences

## Positive Consequences

The strategy provides:

- Better architecture understanding.
- Lower AWS costs.
- Faster experimentation.
- Reusable engineering components.
- Easier AWS migration.

---

## Negative Consequences

Potential limitations:

- Some AWS-specific behaviors are validated later.
- Additional migration steps are required.

These limitations are acceptable because the final objective is a production AWS MLOps platform.

---

# 8. AWS Services Targeted in Future Phases

This strategy prepares integration with:

```
Amazon S3

AWS Glue

Amazon Athena

SageMaker Processing Jobs

SageMaker Training Jobs

SageMaker Feature Store

SageMaker Model Registry

SageMaker Endpoints

Amazon ECR

AWS Lambda

AWS Step Functions

AWS CloudWatch
```

---

# 9. Engineering Principle

The project follows:

```
Understand First

        ↓

Build Correctly

        ↓

Automate

        ↓

Scale in AWS
```

The objective is to develop engineers capable of designing MLOps systems, not only operating cloud services.

---

# 10. Decision Outcome

The local-first strategy establishes a controlled path from experimentation to enterprise AWS MLOps implementation.

The architecture remains cloud-oriented while allowing efficient local development and validation.

# AWS Data Platform Architecture

## 1. Overview

The objective of this architecture is to evolve the local data platform developed during Phase 1 into a cloud-enabled enterprise data platform capable of supporting scalable, reproducible, and production-ready machine learning workflows.

Rather than replacing the local-first architecture, this phase extends it by introducing managed AWS services while preserving reproducibility, modularity, and maintainability.

The AWS Data Platform will serve as the foundation for the remaining phases of the roadmap, including model training, experiment tracking, deployment, monitoring, and retraining.

---

# 2. Architectural Goals

The AWS Data Platform has the following objectives:

- Store datasets in a centralized Data Lake.
- Maintain dataset versioning.
- Register datasets for enterprise discovery.
- Enable SQL-based data exploration.
- Prepare datasets for machine learning pipelines.
- Preserve reproducibility.
- Support enterprise governance.
- Minimize cloud costs through a Local-First development strategy.

---

# 3. Evolution from Phase 1

Phase 1 established a local data engineering platform with the following layers:

```
Raw Data
        │
        ▼
Processed Data
        │
        ▼
Feature Engineering
        │
        ▼
Offline Feature Store
```

Phase 2 extends this architecture by integrating AWS services while preserving the same logical workflow.

```
Local Development
        │
        ▼
Amazon S3 Data Lake
        │
        ▼
AWS Glue Data Catalog
        │
        ▼
Amazon Athena
        │
        ▼
SageMaker Processing Jobs
        │
        ▼
Training Pipelines
```

---

# 4. AWS Data Platform Components

## Amazon S3

Amazon S3 becomes the enterprise Data Lake.

Responsibilities include:

- Store raw datasets.
- Store processed datasets.
- Store feature datasets.
- Store model artifacts.
- Store metadata.
- Preserve dataset versions.

S3 becomes the single source of truth for all production datasets.

---

## AWS Glue Data Catalog

The Glue Data Catalog provides centralized metadata management.

Responsibilities include:

- Dataset registration.
- Schema discovery.
- Metadata storage.
- Dataset cataloging.
- Enterprise data governance.

The Data Catalog allows every AWS analytics service to discover datasets without manually defining schemas.

---

## Amazon Athena

Athena provides serverless SQL access to datasets stored in Amazon S3.

Responsibilities include:

- Dataset exploration.
- Dataset validation.
- SQL joins.
- Data quality inspection.
- Schema verification.

Athena allows engineers and data scientists to analyze datasets without creating a database server.

---

## SageMaker Processing Jobs

Processing Jobs execute reproducible preprocessing pipelines.

Responsibilities include:

- Data cleaning.
- Data transformations.
- Feature preparation.
- Dataset validation.
- Data export.

Processing Jobs separate data preparation from model training, improving reproducibility and governance.

---

# 5. High-Level Architecture

The AWS Data Platform is organized as a layered architecture in which each AWS service has a clearly defined responsibility. Data flows upward through the platform, while governance and reproducibility are maintained across every layer.

```
                    Enterprise ML Platform

                   ┌───────────────────────────┐
                   │   SageMaker Training Jobs │
                   │ (Phase 2B and beyond)     │
                   └─────────────▲─────────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   │ SageMaker Processing Jobs │
                   └─────────────▲─────────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   │      Amazon Athena        │
                   └─────────────▲─────────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   │   AWS Glue Data Catalog   │
                   └─────────────▲─────────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   │    Amazon S3 Data Lake    │
                   └───────────────────────────┘
```

Each layer builds upon the previous one while maintaining a clear separation of responsibilities. This layered design improves scalability, reproducibility, maintainability, and governance, allowing the platform to evolve incrementally throughout the roadmap without requiring major architectural changes.

---

# 6. Technology Mapping

The AWS Data Platform is composed of several managed services, each with a clearly defined responsibility within the machine learning lifecycle.

| Architecture Layer | AWS Service | Primary Responsibility |
|--------------------|-------------|------------------------|
| Data Lake | Amazon S3 | Persistent storage for datasets, feature files, metadata, and model artifacts |
| Metadata Catalog | AWS Glue Data Catalog | Dataset registration, schema management, and enterprise data discovery |
| Data Exploration | Amazon Athena | SQL-based exploration, validation, profiling, and quality checks |
| Data Processing | SageMaker Processing Jobs | Reproducible preprocessing, feature preparation, and dataset transformation |
| Model Training *(Phase 2B)* | SageMaker Training Jobs | Distributed model training |
| Experiment Tracking *(Phase 2B)* | SageMaker Experiments | Experiment management and reproducibility |
| Model Governance *(Phase 2B)* | SageMaker Model Registry | Model versioning, approval, and lifecycle management |

Each service is responsible for a specific layer of the platform, following the engineering principles of separation of concerns and modular architecture established for this roadmap.

---

# 7. Data Flow

The enterprise data platform follows the workflow below.

```
Local Dataset
        │
        ▼
Upload to Amazon S3
        │
        ▼
Register Dataset
AWS Glue Data Catalog
        │
        ▼
Validate Dataset
Amazon Athena
        │
        ▼
Run SageMaker Processing
        │
        ▼
Processed Dataset
        │
        ▼
Training Pipeline
```

---

# 8 Resource Lifecycle Strategy

The AWS Data Platform follows a cost-conscious resource lifecycle strategy that distinguishes between persistent data assets and ephemeral compute resources.

This approach minimizes AWS costs while preserving reproducibility and allowing the complete platform to be recreated at any time using Infrastructure as Code (Terraform).

## Persistent Resources

The following resources remain available throughout the roadmap because they represent long-lived enterprise assets:

- Amazon S3 Data Lake
- AWS Glue Data Catalog
- Dataset metadata
- Dataset versions
- Feature datasets
- Model artifacts
- Terraform configuration

These resources evolve as the project progresses and serve as the foundation for all subsequent phases.

---

## Ephemeral Resources

Compute resources are created only when required and destroyed immediately after validation.

Examples include:

- SageMaker Processing Jobs
- SageMaker Training Jobs
- SageMaker Hyperparameter Tuning Jobs
- Temporary compute instances
- Temporary validation resources

This strategy ensures that compute costs remain minimal while preserving full reproducibility.

---

## Infrastructure as Code

All cloud infrastructure is provisioned through Terraform.

Using Infrastructure as Code allows the AWS Data Platform to be recreated consistently across development, validation, and production environments while ensuring that every infrastructure change remains version-controlled.

---

## Local-First Cloud Validation

The roadmap follows a Local-First engineering philosophy.

Every workflow follows the sequence below:

```
Develop Locally
        │
        ▼
Validate Locally
        │
        ▼
Provision AWS Resources
        │
        ▼
Validate Enterprise Integration
        │
        ▼
Destroy Temporary Compute Resources
```

Business logic is always developed and tested locally before being validated using managed AWS services.

This approach provides rapid development cycles while minimizing cloud costs and preserving enterprise-level architectural practices.


---
# 9. Dataset Evolution Strategy

The platform assumes that enterprise datasets evolve continuously.

Example lifecycle:

```
Dataset v1.0
Original Dataset
        │
        ▼
Dataset v1.1
Data Quality Improvements
        │
        ▼
Dataset v2.0
Business Growth
        │
        ▼
Dataset v3.0
Schema Evolution
```

Every dataset version should preserve:

- Version identifier.
- Metadata.
- Schema version.
- Creation timestamp.
- Data lineage.
- Source information.

This strategy guarantees complete reproducibility for future model training.

---

# 10. Local-First Development Strategy

The roadmap follows a Local-First philosophy.

Development lifecycle:

```
Develop Locally
        │
        ▼
Validate Locally
        │
        ▼
Upload to AWS
        │
        ▼
Validate in AWS
        │
        ▼
Production Deployment
```

This strategy minimizes AWS costs while maximizing development speed.

---

# 11. Design Principles

The AWS Data Platform follows the engineering principles defined in:

```
docs/
engineering-principles.md
```

Particular emphasis is placed on:

- Modular architecture.
- SOLID principles.
- Separation of concerns.
- Configuration over hardcoded values.
- Local-first development.
- Reproducibility.
- Dataset versioning.
- Enterprise governance.

---

# 12. Future Integration

The AWS Data Platform serves as the foundation for subsequent phases.

Future integrations include:

- SageMaker Training Jobs.
- SageMaker Hyperparameter Tuning.
- SageMaker Experiments.
- SageMaker Model Registry.
- SageMaker Pipelines.
- Model deployment.
- Monitoring.
- Retraining workflows.

This architecture is intentionally designed to evolve without requiring major repository restructuring.

---

# 13. Expected Outcome

Upon completion of this architecture, the platform will provide:

- A centralized enterprise Data Lake.
- Registered datasets.
- Discoverable metadata.
- SQL-based data validation.
- Reproducible processing workflows.
- Enterprise-ready data governance.
- A scalable foundation for the complete machine learning lifecycle.

---

# 14. Architectural Decisions

The AWS Data Platform is built upon a set of architectural decisions that guide every implementation throughout the roadmap.

## AD-01 — Amazon S3 as the Single Source of Truth

Amazon S3 is the authoritative storage layer for all production datasets, feature datasets, metadata, and model artifacts. Every downstream service consumes data originating from the Data Lake, ensuring consistency and reproducibility across the entire machine learning lifecycle.

---

## AD-02 — Separation of Business Logic and Cloud Services

Business logic must remain independent of AWS-specific implementations.

Interactions with AWS services are encapsulated inside dedicated modules (for example, `aws/s3.py`, `aws/glue.py`, and `aws/athena.py`), allowing the core application to remain modular, testable, and portable.

---

## AD-03 — Infrastructure as Code

All cloud resources are provisioned and managed through Terraform.

Infrastructure definitions are version-controlled alongside the application code, ensuring reproducible deployments, simplified maintenance, and consistent environments across development, validation, and production.

---

## AD-04 — Persistent Data, Ephemeral Compute

The platform distinguishes between persistent storage and temporary compute resources.

Persistent resources include:

- Amazon S3 Data Lake
- AWS Glue Data Catalog
- Dataset metadata
- Dataset versions
- Model artifacts

Ephemeral resources include:

- SageMaker Processing Jobs
- SageMaker Training Jobs
- Hyperparameter Tuning Jobs
- Temporary validation infrastructure

This strategy minimizes operational costs while preserving enterprise-grade reproducibility.

---

## AD-05 — Local-First, Cloud-Validation Strategy

Development begins locally whenever possible.

Cloud services are introduced only to validate enterprise integrations, scalability, and managed AWS capabilities. This approach accelerates development, reduces costs, and ensures that business logic can be tested independently of cloud infrastructure.

---

## AD-06 — Incremental Platform Evolution

The architecture is intentionally designed to evolve incrementally.

Each phase extends the existing platform rather than replacing it, allowing new capabilities—such as experiment tracking, model governance, deployment, monitoring, and retraining—to be incorporated without major structural changes to the repository.

---
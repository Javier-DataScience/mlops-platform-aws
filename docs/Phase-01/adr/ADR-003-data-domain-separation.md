# ADR-003: Data Domain Separation

## Status

Accepted

---

## Date

2026-07-27

---

# 1. Context

The original business dataset represents a credit risk / loan approval use case.

The source dataset contains multiple business concepts in a single structure:

```
credit_risk_dataset.csv
```

The original dataset includes:

- Customer information.
- Financial history information.
- Loan application information.
- Credit risk outcome.

Although this structure is convenient for initial exploration, it does not represent an enterprise data architecture.

A production ML platform requires datasets organized according to business responsibilities.

---

# 2. Decision

The project separates the original dataset into independent business domains.

The transformation is:

```
Original Dataset

credit_risk_dataset.csv

        |
        |
        v

Business Domain Separation

        |
        |
        +----------------------+
        |                      |
        v                      v

Customer Domain       Financial Domain


        |
        |
        v

Loan Application Domain
```

The resulting datasets are:

```
data/processed/

├── customer/

├── financial_history/

└── loan_application/
```

---

# 3. Reasons for the Decision

## Business Responsibility Separation

Each dataset represents a different business domain.

Example:

```
Customer Domain

- Personal information.
- Demographic attributes.
- Customer identifiers.
```

```
Financial Domain

- Income information.
- Historical financial indicators.
- Risk-related variables.
```

```
Loan Application Domain

- Loan characteristics.
- Application information.
- Credit decision information.
```

This separation improves ownership and maintainability.

---

# 4. Data Engineering Benefits

## Independent Processing

Each domain can be processed independently.

Architecture:

```
Customer Dataset

        |
        v

Customer Pipeline
```

```
Financial Dataset

        |
        v

Financial Pipeline
```

```
Loan Dataset

        |
        v

Loan Pipeline
```

Benefits:

- Independent validation.
- Independent transformations.
- Easier debugging.
- Better scalability.

---

# 5. Feature Engineering Benefits

The separation enables modular feature engineering.

Architecture:

```
Processed Business Domains

        |
        |
        v

Feature Engineering Modules

        |
        |
        +----------------+
        |                |
        v                v

Customer Features   Financial Features


        |
        |
        v

Loan Features
```

Implemented modules:

```
src/mlops_engineering_roadmap/features/

├── customer_features.py

├── financial_features.py

└── loan_features.py
```

Each module focuses on a specific business domain.

---

# 6. Data Lake Evolution

The domain separation prepares the platform for enterprise data lake organization.

Current local structure:

```
data/

├── raw/

│   └── original/


├── processed/

│   ├── customer/

│   ├── financial_history/

│   └── loan_application/
```

Future AWS architecture:

```
Amazon S3 Data Lake

        |
        |
        v

Raw Layer

        |
        |
        v

Processed Layer

        |
        |
        v

Feature Preparation Layer
```

---

# 7. Alternatives Considered

## Keep Single Dataset Structure

Rejected.

Reasons:

- Poor scalability.
- Difficult ownership.
- Strong coupling between business concepts.
- Harder feature management.

---

## Create Highly Granular Datasets

Rejected.

Reasons:

- Excessive fragmentation.
- Increased pipeline complexity.
- Limited benefit for current business problem.

The selected domains provide the appropriate balance between organization and simplicity.

---

# 8. Consequences

## Positive Consequences

The decision provides:

- Better data organization.
- Clear business ownership.
- Reusable pipelines.
- Easier feature engineering.
- Better preparation for AWS data services.

---

## Negative Consequences

Potential limitations:

- Additional data transformation steps.
- Need to manage relationships between datasets.
- More metadata requirements.

These trade-offs are acceptable for an enterprise ML platform.

---

# 9. Future AWS Integration

This decision enables future integration with:

- Amazon S3.
- AWS Glue.
- AWS Glue Data Catalog.
- Amazon Athena.
- SageMaker Processing Jobs.

Future workflow:

```
Business Data Sources

        |
        |
        v

Amazon S3 Raw Layer

        |
        |
        v

AWS Glue Catalog

        |
        |
        v

Processed Business Domains

        |
        |
        v

Feature Engineering Pipelines
```

---

# 10. Decision Outcome

The project adopts business-domain data separation as the foundation for the MLOps data platform.

This decision enables:

- Reproducible data pipelines.
- Modular feature engineering.
- Future AWS scalability.
- Enterprise-oriented ML workflows.

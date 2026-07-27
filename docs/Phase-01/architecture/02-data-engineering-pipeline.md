# Data Engineering Pipeline Architecture

## 1. Overview

This document describes the Phase 1 data engineering pipeline implemented for the MLOps platform.

The objective is to transform a raw business dataset into structured, validated, versioned, and feature-ready datasets that can support future machine learning training and inference workflows.

The pipeline follows enterprise data engineering principles:

- Reproducibility.
- Modularity.
- Data validation.
- Dataset versioning.
- Feature consistency.
- Separation of responsibilities.

---

# 2. Pipeline Architecture

The complete data flow is:

```
Original Dataset

credit_risk_dataset.csv

        |
        |
        v

Data Ingestion Layer

        |
        |
        v

Processed Business Datasets

        |
        |
        v

Dataset Validation

        |
        |
        v

Dataset Metadata and Versioning

        |
        |
        v

Feature Engineering Platform

        |
        |
        v

Offline Feature Store

        |
        |
        v

Training Ready Data
```

---

# 3. Data Ingestion

The original dataset represents the business source system.

Location:

```
data/raw/original/
```

Input:

```
credit_risk_dataset.csv
```

The ingestion pipeline transforms the monolithic dataset into independent business domains.

Implemented module:

```
src/mlops_engineering_roadmap/data/ingestion.py
```

---

# 4. Processed Dataset Layer

The dataset is separated into logical business entities:

```
data/processed/

├── customer/

├── financial_history/

└── loan_application/
```

Purpose:

- Improve data organization.
- Separate business responsibilities.
- Enable independent processing workflows.
- Support reusable ML pipelines.

Generated datasets:

```
customer.csv

financial_history.csv

loan_application.csv
```

---

# 5. Data Validation Layer

Validation modules verify dataset integrity before feature engineering.

Implemented validations include:

- Dataset existence.
- Dataset not empty.
- Required columns validation.
- Basic data quality checks.

Implementation:

```
src/mlops_engineering_roadmap/data/validation.py
```

Validation tests:

```
tests/data/test_validation.py
```

---

# 6. Dataset Versioning and Metadata

Dataset metadata is generated to support reproducibility and lineage tracking.

Implemented module:

```
src/mlops_engineering_roadmap/utils/versioning.py
```

Metadata structure:

```
data/metadata/

├── data_dictionary/

├── lineage/

└── schemas/
```

The versioning layer supports:

- Dataset identification.
- Metadata generation.
- Schema tracking.
- Reproducibility.

---

# 7. Feature Engineering Platform

Processed datasets are transformed into reusable ML features.

Pipeline:

```
Processed Dataset

        |
        |
        v

Feature Engineering Modules

        |
        |
        v

Feature Dataset
```

Feature engineering modules:

```
src/mlops_engineering_roadmap/features/

├── customer_features.py

├── financial_features.py

└── loan_features.py
```

Execution pipeline:

```
scripts/build_features.py
```

The pipeline generates feature datasets for future training workflows.

---

# 8. Offline Feature Store

The current local implementation follows an Offline Feature Store architecture.

Location:

```
data/features/offline/
```

Structure:

```
data/features/

├── offline/

│   ├── customer/

│   │   └── customer_features.csv

│   ├── financial_history/

│   │   └── financial_features.csv

│   └── loan_application/

│       └── loan_features.csv


└── online/
```

Purpose:

- Provide consistent training features.
- Maintain feature reproducibility.
- Support future batch inference.
- Prepare integration with cloud feature stores.

---

# 9. Future AWS Mapping

The local implementation prepares the foundation for AWS MLOps services.

Current local architecture:

```
Python Pipeline

        |
        |
        v

Local Offline Feature Store
```

Future AWS architecture:

```
Amazon S3 Data Lake

        |
        |
        v

SageMaker Processing Job

        |
        |
        v

Feature Engineering Pipeline

        |
        |
        v

SageMaker Feature Store

        |
        |
        v

Training Pipeline
```

The objective is to maintain the same engineering logic while changing only the execution environment.

---

# 10. Engineering Standards Applied

The pipeline applies production-oriented engineering practices:

- Modular architecture.
- Type hints.
- Logging.
- Exception handling.
- Unit testing.
- Ruff formatting and linting.
- MyPy static analysis.
- Pre-commit automation.
- Git version control.

---

# 11. Current Phase 1 Data Flow Summary

The complete implemented workflow:

```
credit_risk_dataset.csv

        |
        |
        v

Data Ingestion

        |
        |
        v

Processed Business Datasets

        |
        |
        v

Data Validation

        |
        |
        v

Dataset Versioning

        |
        |
        v

Feature Engineering Platform

        |
        |
        v

Offline Feature Store

        |
        |
        v

Training Ready Features
```

---

# 12. Phase 1 Achievement

At the end of this stage, the platform has evolved from a single raw dataset into a structured data engineering foundation capable of supporting future ML training and inference pipelines.
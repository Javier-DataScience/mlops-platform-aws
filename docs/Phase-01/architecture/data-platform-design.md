# Data Platform Design

## 1. Overview

The objective of this data platform is to transform raw business datasets into reliable, reproducible, and structured datasets that can support future machine learning pipelines.

The platform follows enterprise data engineering principles, including:

- Data separation by responsibility.
- Reproducible transformations.
- Data lineage.
- Dataset versioning.
- Clear data ownership.
- Preparation for machine learning workflows.

The platform is designed around a credit risk / loan approval use case.

---

# 2. Business Use Case

## Credit Risk / Loan Approval Platform

The business objective is to predict the credit risk associated with a loan application.

The original dataset contains information required for a simplified credit decision process.

The dataset includes:

- Customer information.
- Financial history information.
- Loan application information.
- Credit risk outcome.

Instead of treating the dataset as one monolithic file, it is transformed into multiple logical datasets representing different business entities.

---

# 3. Source Dataset

## Original Dataset

Source:

```
credit_risk_dataset.csv
```

Location:

```
data/
raw/
original/
```

Purpose:

The original dataset is preserved without modification.

The raw layer represents the source data exactly as received from the external provider.

---

# 4. Data Lake Structure

The project follows a simplified enterprise data lake organization.

```
data/

raw/
    original/

processed/
    customer/
    financial_history/
    loan_application/

features/

metadata/
    data_dictionary/
    schemas/

versions/
```

## Layer Responsibilities

### Raw Layer

Location:

```
data/raw/
```

Purpose:

- Store original datasets.
- Preserve source information.
- Avoid modifying original data.

---

### Processed Layer

Location:

```
data/processed/
```

Purpose:

Store cleaned and structured datasets ready for feature engineering.

Contains:

```
customer/
financial_history/
loan_application/
```

---

### Feature Layer

Location:

```
data/features/
```

Purpose:

Store machine learning features generated from processed datasets.

Future usage:

- Training datasets.
- Batch inference features.
- Online inference features.

---

### Metadata Layer

Location:

```
data/metadata/
```

Purpose:

Store information describing datasets.

Examples:

```
data_dictionary/
schemas/
```

---

### Version Layer

Location:

```
data/versions/
```

Purpose:

Store dataset version information and reproducibility metadata.

---

# 5. Dataset Decomposition Strategy

The original dataset represents multiple business entities in a single CSV file.

In an enterprise environment, these entities would normally come from different systems.

Therefore, the dataset is decomposed into three logical datasets:

```
Original Dataset

        |
        |
        v

Customer Profile Dataset

Financial History Dataset

Loan Application Dataset
```

This design allows:

- Better data organization.
- Clear business ownership.
- Easier feature engineering.
- Improved data lineage.
- More realistic enterprise architecture.

---

# 6. Customer Profile Dataset

## Purpose

Represents the customer dimension.

Location:

```
data/processed/customer/
```

Output:

```
customer.csv
```

Schema:

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| age | Customer age |
| income | Customer income |
| home_ownership | Housing information |
| employment_length | Employment duration |

---

# 7. Financial History Dataset

## Purpose

Represents historical financial behavior.

Location:

```
data/processed/financial_history/
```

Output:

```
financial_history.csv
```

Schema:

| Column | Description |
|---|---|
| customer_id | Customer relationship key |
| credit_history_length | Credit history duration |
| default_history | Previous default indicator |

---

# 8. Loan Application Dataset

## Purpose

Represents the current loan request and prediction event.

Location:

```
data/processed/loan_application/
```

Output:

```
loan_application.csv
```

Schema:

| Column | Description |
|---|---|
| application_id | Unique loan application identifier |
| customer_id | Customer relationship key |
| loan_amount | Requested loan amount |
| loan_intent | Loan purpose |
| loan_grade | Credit risk category |
| loan_interest_rate | Loan interest rate |
| loan_percent_income | Loan burden ratio |
| loan_status | Target variable |

---

# 9. Dataset Relationships

The datasets are connected through generated identifiers.

Architecture:

```
                Customer Dataset

                 customer_id

                      |
          +-----------+-----------+
          |                       |
          v                       v

Financial History Dataset   Loan Application Dataset

      customer_id                 customer_id
```

The customer identifier allows consistent relationships between business entities.

---

# 10. Data Lineage

The expected transformation flow is:

```
Original Dataset

        |
        v

Data Ingestion Pipeline

        |
        v

Processed Business Datasets

        |
        v

Feature Engineering

        |
        v

Machine Learning Training Dataset

        |
        v

Model Training Pipeline
```

---

# 11. Transformation Responsibility

The preprocessing pipeline will be responsible for:

- Loading the original dataset.
- Generating business identifiers.
- Creating logical datasets.
- Applying data cleaning rules.
- Saving processed outputs.
- Maintaining reproducibility.

The preprocessing module will not perform:

- Model training.
- Feature engineering.
- Model validation.
- Feature store operations.

Those responsibilities belong to later phases.

---

# 12. Engineering Principles Applied

This design follows:

## Single Responsibility Principle

Each dataset represents a specific business responsibility.

## Separation of Concerns

Data ingestion, preprocessing, feature engineering, and modeling are separated.

## Reproducibility

The same input dataset and transformation rules should generate the same outputs.

## Data Lineage

Every processed dataset can be traced back to the original source.

## Scalability

The architecture can evolve from local processing to cloud-based processing using AWS services.

---

# 13. Future Evolution

Future phases will extend this platform with:

- AWS S3 Data Lake implementation.
- AWS Glue Data Catalog.
- Amazon Athena validation queries.
- Feature engineering pipelines.
- Feature Store implementation.
- ML training pipelines.

These components are intentionally implemented in later phases to avoid unnecessary complexity during the data foundation stage.
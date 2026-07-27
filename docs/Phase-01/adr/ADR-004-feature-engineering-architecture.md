# ADR-004: Feature Engineering Architecture

## Status

Accepted

---

## Date

2026-07-27

---

# 1. Context

Machine learning systems require consistent and reproducible feature transformations.

During the initial development of the MLOps platform, processed business datasets were generated from the original source data.

However, processed datasets are not directly ready for machine learning models.

A dedicated feature engineering layer is required to:

- Transform business data into ML features.
- Maintain reusable transformations.
- Avoid duplicated feature logic.
- Ensure consistency between training and inference workflows.

---

# 2. Decision

Feature engineering is implemented as an independent modular platform.

The architecture separates:

```
Data Engineering

        |

        v

Feature Engineering

        |

        v

Machine Learning Training
```

Feature engineering is not embedded inside:

- Data ingestion.
- Dataset preprocessing.
- Model training code.

---

# 3. Feature Engineering Architecture

The implemented architecture is:

```
Processed Business Datasets

        |
        |
        v

Feature Engineering Platform

        |
        |
        v

Feature Datasets

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

# 4. Module Structure

Feature engineering follows a domain-based modular structure.

Implementation:

```
src/mlops_engineering_roadmap/features/

├── __init__.py

├── customer_features.py

├── financial_features.py

└── loan_features.py
```

Each module is responsible for generating features from a specific business domain.

---

# 5. Customer Feature Engineering

Customer-related transformations are isolated inside:

```
src/mlops_engineering_roadmap/features/customer_features.py
```

Responsibilities:

- Generate customer-level features.
- Transform customer attributes.
- Prepare reusable variables for ML models.

Output:

```
data/features/offline/customer/

customer_features.csv
```

---

# 6. Financial Feature Engineering

Financial transformations are implemented in:

```
src/mlops_engineering_roadmap/features/financial_features.py
```

Responsibilities:

- Generate financial indicators.
- Transform financial history information.
- Create risk-related variables.

Output:

```
data/features/offline/financial_history/

financial_features.csv
```

---

# 7. Loan Feature Engineering

Loan transformations are implemented in:

```
src/mlops_engineering_roadmap/features/loan_features.py
```

Responsibilities:

- Generate loan-related features.
- Create categorical transformations.
- Prepare application-level ML variables.

Output:

```
data/features/offline/loan_application/

loan_features.csv
```

---

# 8. Feature Generation Pipeline

Feature generation is executed through a centralized pipeline.

Entry point:

```
scripts/build_features.py
```

Workflow:

```
Processed Datasets

        |
        |
        v

Customer Feature Module

        |
        |
        v

Financial Feature Module

        |
        |
        v

Loan Feature Module

        |
        |
        v

Feature Dataset Generation
```

Benefits:

- Reproducible execution.
- Centralized workflow.
- Easier automation.
- Future CI/CD compatibility.

---

# 9. Alternatives Considered

## Feature Engineering Inside Training Code

Rejected.

Reasons:

- Creates duplicated logic.
- Makes inference consistency difficult.
- Reduces reusability.
- Increases maintenance complexity.

---

## Feature Engineering Inside Preprocessing

Rejected.

Reasons:

- Mixes data preparation and ML feature logic.
- Reduces modularity.
- Makes feature lifecycle management harder.

---

# 10. Consequences

## Positive Consequences

The decision provides:

- Reusable feature modules.
- Clear separation of responsibilities.
- Easier testing.
- Better feature governance.
- Preparation for Feature Store integration.

---

## Negative Consequences

Potential limitations:

- More initial project structure.
- Additional modules to maintain.
- Requires feature documentation.

These costs are acceptable for enterprise ML systems.

---

# 11. Testing Strategy

Feature engineering modules include dedicated unit tests.

Structure:

```
tests/features/

├── test_customer_features.py

├── test_financial_features.py

└── test_loan_features.py
```

Testing validates:

- Feature generation logic.
- Expected columns.
- Output consistency.
- Transformation correctness.

---

# 12. Future AWS Integration

The local feature engineering architecture maps to AWS services.

Current:

```
Feature Engineering Modules

        |

        v

Local Offline Feature Store
```

Future:

```
Amazon S3 Data Lake

        |

        v

SageMaker Processing Jobs

        |

        v

Feature Engineering Pipeline

        |

        v

SageMaker Feature Store

        |

        v

Training and Inference Systems
```

---

# 13. Engineering Standards Applied

The feature engineering platform follows:

- Modular architecture.
- Type hints.
- Logging.
- Exception handling.
- Unit testing.
- Ruff formatting.
- Ruff linting.
- MyPy validation.
- Pre-commit automation.
- Git version control.

---

# 14. Decision Outcome

The project adopts a modular feature engineering architecture.

This decision establishes the foundation for:

- Reusable ML features.
- Consistent training and inference.
- Future SageMaker Feature Store integration.
- Enterprise MLOps workflows.

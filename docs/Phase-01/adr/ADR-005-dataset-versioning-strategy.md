# ADR-005: Dataset Versioning Strategy

## Status

Accepted

---

## Date

2026-07-27

---

# 1. Context

Machine learning systems depend on data that changes over time.

During the development of the MLOps platform, datasets are transformed through multiple stages:

```
Raw Dataset

        |

        v

Processed Dataset

        |

        v

Feature Dataset

        |

        v

Training Dataset
```

Without proper versioning and metadata tracking, it becomes difficult to:

- Reproduce previous experiments.
- Understand data changes.
- Audit model training.
- Track data lineage.
- Debug production issues.

A dataset versioning strategy is therefore required.

---

# 2. Decision

The project implements a dataset metadata and versioning layer.

The strategy focuses on:

- Dataset identification.
- Metadata generation.
- Schema tracking.
- Data lineage.
- Reproducibility.

The initial implementation is local-first and prepares the foundation for future AWS data governance.

---

# 3. Dataset Versioning Architecture

The implemented architecture is:

```
Dataset

        |

        v

Metadata Generation

        |

        v

Version Information

        |

        +----------------+
        |                |
        v                v

Schema Tracking    Data Lineage
```

---

# 4. Versioning Module

Implementation:

```
src/mlops_engineering_roadmap/utils/versioning.py
```

Responsibilities:

- Generate dataset metadata.
- Save metadata information.
- Load metadata information.
- Support dataset reproducibility.

---

# 5. Metadata Structure

The project maintains metadata organization:

```
data/metadata/

├── data_dictionary/

├── lineage/

└── schemas/
```

---

# 6. Data Dictionary

Purpose:

Document dataset meaning and business information.

Example:

```
Customer Dataset

Column:

customer_id

Description:

Unique identifier for each customer

Type:

String
```

Benefits:

- Better data understanding.
- Improved collaboration.
- Easier feature development.

---

# 7. Schema Management

Purpose:

Track dataset structure.

Example:

```
Dataset Schema

customer_id      string

age              integer

income           float

loan_status      integer
```

Schema tracking helps detect:

- Missing columns.
- Unexpected changes.
- Data compatibility problems.

---

# 8. Data Lineage

Purpose:

Track where datasets originate and how they are transformed.

Current lineage:

```
credit_risk_dataset.csv

        |

        v

Processed Business Datasets

        |

        v

Feature Datasets
```

Benefits:

- Traceability.
- Debugging.
- Reproducibility.
- Governance.

---

# 9. Dataset Metadata Example

A dataset version contains information such as:

```
Dataset Name

Version

Creation Date

Source

Number of Rows

Number of Columns

Schema Information

Transformation Information
```

This metadata allows engineers to understand exactly what data was used.

---

# 10. Alternatives Considered

## No Dataset Versioning

Rejected.

Reasons:

- Impossible to reproduce experiments.
- Difficult model auditing.
- Poor production reliability.

---

## Manual Documentation Only

Rejected.

Reasons:

- Error prone.
- Difficult to maintain.
- Does not scale.

---

## Immediate Use of Full AWS Data Governance Tools

Rejected for Phase 1.

Reasons:

- Adds unnecessary complexity.
- Requires cloud resources before architecture validation.
- Better introduced during AWS data platform integration.

---

# 11. Consequences

## Positive Consequences

The decision provides:

- Data reproducibility.
- Better governance.
- Easier debugging.
- Improved ML lifecycle management.
- Preparation for enterprise MLOps workflows.

---

## Negative Consequences

Potential limitations:

- Additional metadata management.
- More documentation requirements.
- Requires disciplined updates.

These trade-offs are acceptable for production ML systems.

---

# 12. Future AWS Integration

The local versioning strategy prepares integration with AWS services.

Future architecture:

```
Amazon S3 Data Lake

        |

        v

AWS Glue Data Catalog

        |

        v

Metadata Management

        |

        v

Data Lineage Tracking

        |

        v

SageMaker Pipelines
```

Potential AWS integrations:

- Amazon S3 object versioning.
- AWS Glue Data Catalog.
- AWS Lake Formation.
- SageMaker Pipelines metadata.

---

# 13. Relationship With Model Versioning

Dataset versioning supports model reproducibility.

Complete ML lifecycle:

```
Dataset Version

        +

Code Version

        +

Feature Version

        +

Model Version

        |

        v

Reproducible ML Experiment
```

A model should always be associated with the exact data and features used during training.

---

# 14. Engineering Standards Applied

The dataset versioning implementation follows:

- Modular design.
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

# 15. Decision Outcome

The project adopts a dataset versioning strategy based on metadata, schema tracking, and lineage.

This decision establishes the foundation required for future AWS MLOps capabilities:

- Reproducible training pipelines.
- Data governance.
- Feature management.
- Model lifecycle tracking.

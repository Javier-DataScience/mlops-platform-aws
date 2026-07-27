# ADR-001: Project Structure

## Status

Accepted

---

## Date

2026-07-27

---

# 1. Context

The MLOps Engineering Roadmap requires a project structure that supports:

- Maintainable Python development.
- Machine learning workflows.
- Data engineering pipelines.
- Automated testing.
- Documentation.
- Future AWS MLOps integration.

A production-oriented structure is required instead of a simple notebook-based project.

---

# 2. Decision

The project follows a modular Python repository structure.

The selected structure is:

```
mlops-engineering-roadmap/

├── src/

├── tests/

├── data/

├── docs/

├── scripts/

├── pyproject.toml

├── uv.lock

└── README.md
```

---

# 3. Directory Responsibilities

## Source Code

Location:

```
src/mlops_engineering_roadmap/
```

Purpose:

- Application code.
- Data pipelines.
- Feature engineering modules.
- Utility modules.

Current structure:

```
src/mlops_engineering_roadmap/

├── data/

├── features/

├── utils/

└── __init__.py
```

---

## Tests

Location:

```
tests/
```

Purpose:

- Validate pipeline components.
- Ensure reproducibility.
- Prevent regression.

Structure:

```
tests/

├── data/

├── features/

└── utils/
```

---

## Data

Location:

```
data/
```

Purpose:

Maintain local data lifecycle organization.

Structure:

```
data/

├── raw/

├── processed/

├── features/

├── metadata/

└── versions/
```

---

## Documentation

Location:

```
docs/
```

Purpose:

Maintain engineering documentation.

Structure:

```
docs/

└── Phase-01/

    ├── architecture/

    └── adr/
```

---

## Scripts

Location:

```
scripts/
```

Purpose:

Store executable pipeline entry points.

Examples:

```
scripts/

├── preprocess_dataset.py

└── build_features.py
```

---

# 4. Alternatives Considered

## Notebook-Centered Development

Rejected.

Reasons:

- Difficult reproducibility.
- Poor testing practices.
- Difficult production transition.

---

## Single Python File Architecture

Rejected.

Reasons:

- Poor scalability.
- Difficult maintenance.
- No separation of responsibilities.

---

# 5. Consequences

## Positive Consequences

- Clear separation of responsibilities.
- Easier testing.
- Better maintainability.
- Compatible with CI/CD workflows.
- Ready for AWS MLOps integration.

---

## Negative Consequences

- More initial complexity.
- Requires understanding of software engineering practices.

---

# 6. Future AWS Integration

The selected structure supports future AWS MLOps components:

```
Local Project Structure

        |

        v

CI/CD Pipeline

        |

        v

AWS MLOps Environment
```

Future integrations:

- Amazon S3.
- SageMaker Processing.
- SageMaker Training.
- SageMaker Model Registry.
- SageMaker Deployment.

---

# 7. Decision Outcome

The project structure provides a scalable foundation for building an enterprise-oriented MLOps platform.
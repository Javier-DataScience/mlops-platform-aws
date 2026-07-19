# Technology Mapping

## Purpose

This document defines the technology strategy adopted throughout the MLOps Engineering Roadmap.

The roadmap follows an **AWS-centered MLOps architecture approach** supported by industry-standard open-source concepts and tools.

The objective is to develop the ability to design, implement, deploy, monitor, and operate enterprise Machine Learning systems using AWS cloud services while understanding the broader MLOps ecosystem.

Open-source technologies are considered as:

- Industry references.
- Conceptual alternatives.
- Complementary engineering tools.
- Local development solutions.

They are not necessarily implemented as complete parallel systems.

---

# Technology Strategy Principles

## AWS-Centered Implementation

The roadmap prioritizes AWS services as the main implementation environment.

AWS services are selected because they provide:

- Managed infrastructure.
- Enterprise scalability.
- Security integration.
- Operational maturity.
- Production-oriented capabilities.

The goal is to gain practical experience building enterprise MLOps systems in the cloud.

---

## Open Source as Engineering Knowledge

Open-source technologies remain important because they represent widely adopted industry practices.

They are used to understand:

- Architectural patterns.
- Engineering concepts.
- Alternative implementations.
- Tool ecosystems.

However, the roadmap avoids unnecessary duplication by implementing primarily with AWS services.

---

## Local-First and Cloud-Ready Evolution

All systems are developed locally first and progressively integrated with AWS.

The evolution follows:

```
Local Development
        |
        v
Engineering Validation
        |
        v
Infrastructure as Code
        |
        v
AWS Deployment
        |
        v
Enterprise ML Platform
```

---

# Data Platform Technologies

The data layer supports ML systems by providing reliable storage, processing, and accessibility.

The roadmap focuses on AWS-native data services.

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Data Storage | Data lake, object storage concepts | Amazon S3 |
| Data Catalog | Metadata management concepts | AWS Glue Data Catalog |
| Data Query | SQL analytical querying concepts | Amazon Athena |
| Data Processing | Distributed data processing concepts | AWS Glue |
| Data Transformation | ETL and data preparation concepts | AWS Glue Jobs |

The objective is not to build a complete data engineering platform, but to understand the data components required by production ML systems.

---

# Machine Learning Platform Technologies

## Model Development

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Machine Learning Frameworks | Scikit-learn, PyTorch, TensorFlow | Amazon SageMaker |
| Experiment Tracking | ML experiment management concepts, MLflow | SageMaker Experiments |
| Model Registry | Model lifecycle management concepts | SageMaker Model Registry |
| Model Artifacts | Versioned artifact storage concepts | Amazon S3 |

---

## Feature Engineering

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Feature Engineering | Data transformation and feature creation concepts | AWS Glue / SageMaker Processing |
| Feature Store | Feature management concepts, Feast | SageMaker Feature Store |

---

# Deployment Technologies

## Model Deployment

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Real-Time Inference | API serving, containerized inference | SageMaker Endpoints |
| Batch Inference | Batch processing concepts | SageMaker Batch Transform |
| Container Deployment | Docker, Kubernetes concepts | ECS / EKS / SageMaker Hosting |

---

# Automation and CI/CD Technologies

The roadmap incorporates both general software engineering automation practices and AWS deployment capabilities.

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Version Control | Git, GitHub | GitHub |
| CI/CD Pipelines | GitHub Actions, Jenkins concepts | AWS CodePipeline + CodeBuild |
| Code Quality | Ruff, Mypy, Pytest, Pre-commit | Integrated into development workflow |
| Infrastructure Automation | Terraform concepts | Terraform + AWS CloudFormation |

---

# Infrastructure Technologies

Infrastructure is managed using Infrastructure as Code principles.

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Infrastructure as Code | Terraform, declarative infrastructure | Terraform + CloudFormation |
| Compute Infrastructure | Virtual machines, containers | EC2, ECS, EKS |
| Containerization | Docker concepts | Amazon ECR + ECS/EKS |
| Configuration Management | Environment configuration concepts | AWS Systems Manager |

---

# Monitoring and Observability Technologies

Monitoring focuses on production reliability of ML systems.

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Metrics | Prometheus concepts | Amazon CloudWatch Metrics |
| Dashboards | Grafana concepts | CloudWatch Dashboards |
| Logging | Centralized logging concepts | CloudWatch Logs |
| Model Monitoring | ML monitoring concepts, Evidently AI | SageMaker Model Monitor |
| Alerts | Monitoring and alerting concepts | CloudWatch Alarms |

---

# Security Technologies

Security is integrated throughout the platform lifecycle.

| Capability | Industry Concepts / Alternatives | AWS Implementation |
|---|---|---|
| Identity Management | IAM concepts | AWS IAM |
| Secrets Management | Vault concepts | AWS Secrets Manager |
| Encryption | Encryption standards | AWS KMS |
| Security Monitoring | Security operations concepts | AWS Security Hub |

---

# Cost Management Strategy

The roadmap follows a cost-aware cloud engineering strategy.

Principles:

- Develop locally first.
- Use small datasets.
- Provision minimal resources.
- Automate infrastructure creation.
- Validate quickly.
- Destroy unnecessary resources.

AWS is used as a professional learning and validation environment, not as an always-running personal production environment.

---

# Final Technology Vision

The final platform combines:

- AWS cloud-native MLOps services.
- Industry-standard engineering practices.
- Infrastructure as Code.
- Automated software delivery.
- Production ML principles.
- Monitoring and operational excellence.

The result is an enterprise-oriented MLOps platform that demonstrates the ability to design and operate modern Machine Learning systems using real-world cloud technologies.
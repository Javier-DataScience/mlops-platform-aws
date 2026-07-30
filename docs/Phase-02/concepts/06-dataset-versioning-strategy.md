# Dataset Versioning Strategy

# 1. Purpose

The purpose of this document is to introduce Dataset Versioning as a fundamental practice for building reproducible, traceable, and reliable Machine Learning systems.

Throughout the previous stages of this MLOps data foundation, we have built a complete data workflow:

```
Amazon S3

(Storage Layer)

        ↓

AWS Glue Data Catalog

(Metadata Layer)

        ↓

Amazon Athena

(Exploration + Validation Layer)

        ↓

SageMaker Processing Jobs

(Data Transformation Layer)

        ↓

Training Dataset Validation

(Quality Gate)
```

After creating and validating training datasets, an important engineering question appears:

> How can we guarantee that the exact dataset used to train a model can be identified and reproduced in the future?

Dataset versioning solves this problem by allowing teams to:

- Track dataset changes over time.
- Reproduce previous training experiments.
- Understand which data created a specific model.
- Maintain historical dataset versions.
- Support auditing and governance processes.

In Machine Learning systems, data is not static.

Datasets continuously evolve because of:

- New data arrivals.
- Business process changes.
- Source system modifications.
- Data corrections.
- Feature engineering updates.

Without dataset versioning, organizations may face problems such as:

- Inability to reproduce previous models.
- Difficulty debugging model performance changes.
- Lack of traceability between data and models.
- Poor governance.

Dataset versioning establishes a relationship between:

```
Dataset Version

        +

Feature Transformations

        +

Training Configuration

        +

Model Version
```

This relationship is essential for production Machine Learning systems.

Within this roadmap, Dataset Versioning represents the final step of the data foundation layer before entering model training and deployment workflows.

The key engineering principle introduced in this document is:

**Every production Machine Learning model should have a traceable relationship with the exact dataset and data processing logic used to create it.**

---

# 2. Learning Objectives

After completing this document, you should be able to:

- Explain why dataset versioning is required in Machine Learning systems.
- Understand the relationship between datasets, experiments, and models.
- Explain how changing datasets affect reproducibility.
- Understand dataset lifecycle management concepts.
- Describe the different stages of a dataset lifecycle.
- Explain dataset version evolution.
- Understand immutable dataset versions.
- Describe common data versioning strategies.
- Understand snapshot-based and metadata-based versioning approaches.
- Explain how dataset versioning supports reproducible training.
- Understand the relationship between datasets, code, and configuration.
- Explain the concept of data lineage.
- Understand dataset provenance and transformation history.
- Describe the role of metadata in dataset management.
- Understand technical, business, and operational metadata.
- Explain schema evolution challenges.
- Understand the importance of backward compatibility.
- Explain why immutable datasets improve reliability.
- Identify common dataset versioning mistakes.
- Understand how dataset versioning supports MLOps governance.
- Explain dataset versioning concepts during ML Engineer and MLOps Engineer interviews.

By the end of this document, you should understand how dataset management moves from simple storage into an enterprise practice focused on:

- Reproducibility.
- Traceability.
- Governance.
- Reliability.

---

# 3. Why Dataset Versioning Exists

## The Problem of Changing Data

Unlike traditional software systems, Machine Learning systems depend not only on code but also on data.

In software engineering:

```
Code Version

        ↓

Application Version
```

In Machine Learning:

```
Code Version

        +

Dataset Version

        +

Model Version

        ↓

ML System Version
```

The same code can produce different results if the underlying dataset changes.

Example:

Version 1:

```
Training Dataset v1

        ↓

Model v1
```

Later:

```
Training Dataset v2

        ↓

Model v2
```

Even if the training code remains identical, the resulting models may behave differently because the data changed.

Without dataset versioning, teams cannot clearly identify what caused a model change.

---

## Reproducibility in Machine Learning

Reproducibility means being able to recreate previous experiments and results.

To reproduce a model, engineers need to know:

- Which dataset was used.
- Which dataset version was used.
- Which processing transformations were applied.
- Which features were generated.
- Which training configuration was used.

A reproducible workflow looks like:

```
Dataset Version

        +

Processing Version

        +

Training Configuration

        ↓

Recreated Model
```

Without this information, previous experiments become difficult or impossible to reproduce.

---

## Dataset Versioning as an MLOps Practice

Dataset versioning transforms data from an unmanaged resource into a controlled engineering artifact.

It enables:

### Traceability

Understanding:

- Where data came from.
- How it changed.
- Which models used it.

---

### Experiment Management

Comparing:

```
Dataset v1

        vs

Dataset v2
```

and understanding how changes affected model performance.

---

### Model Governance

Organizations need to answer:

- What data trained this model?
- When was the dataset created?
- Which transformations were applied?
- Can we recreate this model?

Dataset versioning provides these answers.

---

## Engineering Perspective

Dataset versioning is the data equivalent of source code version control.

Software engineers version:

```
Application Code

        ↓

Git History
```

ML engineers version:

```
Code

+

Data

+

Models

+

Experiments
```

A mature MLOps platform treats all these components as connected artifacts.

---

## Key Takeaways

- ML systems depend on both code and data.
- Dataset changes can alter model behavior.
- Versioning enables reproducibility and traceability.
- Data should be managed as an engineering artifact.
- Dataset versioning is a core MLOps practice.

---

# 4. Dataset Lifecycle Management

## Dataset Lifecycle Stages

A dataset moves through multiple stages during its existence.

A typical ML dataset lifecycle is:

```
Data Creation

        ↓

Data Storage

        ↓

Data Processing

        ↓

Data Validation

        ↓

Dataset Versioning

        ↓

Model Training

        ↓

Dataset Archiving

        ↓

Dataset Retirement
```

Each stage has different requirements and responsibilities.

---

## Data Creation

The lifecycle begins when data is generated or collected.

Sources may include:

- Business applications.
- Sensors.
- Transactions.
- External providers.
- User interactions.

At this stage, important information should be captured:

- Source system.
- Collection time.
- Data ownership.
- Initial metadata.

---

## Data Processing

Raw datasets are transformed into usable ML datasets.

Examples:

- Cleaning.
- Filtering.
- Feature generation.
- Aggregation.

The processing stage should create new dataset versions instead of modifying previous artifacts.

Example:

```
Raw Dataset v1

        ↓

Processed Dataset v1
```

---

## Dataset Validation

Before being used for training, datasets should pass validation checks.

Examples:

- Schema validation.
- Data quality validation.
- Consistency checks.

A validated dataset becomes a trusted training artifact.

---

## Dataset Consumption

Datasets are consumed by ML workflows.

Examples:

- Model training.
- Experimentation.
- Evaluation.
- Analysis.

The dataset version should always be recorded.

Example:

```
Model v3

trained with:

Dataset v5
```

---

## Dataset Retirement

Not every dataset remains active forever.

Organizations may retire datasets because of:

- Obsolete business processes.
- Storage optimization.
- Compliance requirements.
- Data retention policies.

Retired datasets may be:

- Archived.
- Deleted according to policy.
- Kept for historical reference.

---

## Dataset Lifecycle and Governance

A mature organization manages datasets throughout their entire lifecycle.

Important considerations:

- Ownership.
- Access control.
- Metadata.
- Version history.
- Retention policies.

Dataset management is not only a technical concern; it is also part of governance.

---

## Engineering Perspective

Dataset lifecycle management provides structure around how data moves through an ML platform.

Instead of:

```
Random Files

        ↓

Training
```

a production system follows:

```
Managed Dataset Lifecycle

        ↓

Versioned Training Artifact

        ↓

Reproducible ML Workflow
```

This improves reliability, collaboration, and operational control.

---

## Key Takeaways

- Datasets have a lifecycle similar to software artifacts.
- Each lifecycle stage has different responsibilities.
- Data should evolve through versions instead of overwriting files.
- Dataset consumption should always reference a specific version.
- Governance is part of effective dataset management.

---

# 5. Dataset Version Evolution

## Dataset Versions

A dataset version represents a specific state of a dataset at a particular point in time.

Instead of replacing datasets, organizations create new versions as data evolves.

Example:

```
Customer Dataset v1

        ↓

Customer Dataset v2

        ↓

Customer Dataset v3
```

Each version represents a controlled change.

A dataset version should contain information such as:

- Dataset identifier.
- Version number.
- Creation date.
- Source information.
- Processing logic.
- Metadata.

---

## Version Changes

Datasets change for many reasons.

Common examples include:

### New Data Arrivals

Example:

```
Dataset v1

January Data

        ↓

Dataset v2

January + February Data
```

---

### Data Corrections

Example:

Incorrect:

```
country = "Columbia"
```

Corrected:

```
country = "Colombia"
```

The correction should create a new dataset version.

---

### Feature Changes

Example:

Version 1:

```
income
```

Version 2:

```
income

+

income_normalized
```

Changes in feature engineering should be tracked.

---

### Schema Changes

Example:

Before:

```
customer_id

income

age
```

After:

```
customer_id

income

age

credit_score
```

Schema evolution creates a new dataset version.

---

## Dataset Releases

A dataset release represents a stable version approved for consumption.

Example:

```
Dataset Development

        ↓

Validation

        ↓

Dataset Release v1.0
```

A released dataset should be:

- Validated.
- Documented.
- Traceable.
- Available for downstream workflows.

This is similar to software releases.

Software:

```
Application v1.0
```

Machine Learning:

```
Training Dataset v1.0
```

---

## Relationship Between Dataset and Model Versions

Dataset versions and model versions are directly connected.

Example:

```
Dataset v3

        +

Training Code v5

        ↓

Model v2
```

A model should always reference:

- Training dataset version.
- Feature version.
- Processing version.
- Training configuration.

This creates complete experiment traceability.

---

## Engineering Perspective

Dataset version evolution allows ML teams to understand how changes affect models.

Without versioning:

```
Dataset Changed

        ↓

Model Changed

        ↓

Unknown Cause
```

With versioning:

```
Dataset v1

        ↓

Model v1


Dataset v2

        ↓

Model v2
```

Teams can analyze the impact of data changes.

---

## Key Takeaways

- Dataset versions represent controlled states of data.
- Data changes should create new versions.
- Releases provide stable datasets for consumption.
- Dataset and model versions should remain connected.
- Version evolution improves debugging and reproducibility.

---

# 6. Data Versioning Strategies

## Immutable Dataset Versions

An immutable dataset version cannot be modified after creation.

Example:

```
Dataset v1

(Created)

        ↓

Never Modified
```

If changes are required:

```
Dataset v1

        ↓

Create Dataset v2
```

Benefits:

- Reproducibility.
- Traceability.
- Safer experimentation.
- Better governance.

This follows the same principle as immutable software artifacts.

---

## Snapshot-Based Versioning

Snapshot-based versioning stores a representation of a dataset at a specific point in time.

Example:

```
January Snapshot

        ↓

February Snapshot

        ↓

March Snapshot
```

Each snapshot represents the dataset state during that period.

Advantages:

- Easy historical comparison.
- Simple rollback.
- Clear dataset states.

Common use cases:

- Periodic training datasets.
- Batch ML workflows.
- Analytics environments.

---

## Metadata-Based Versioning

Metadata-based versioning tracks dataset changes through descriptive information rather than storing complete copies.

Metadata may include:

- Dataset identifier.
- Version number.
- Location.
- Schema.
- Processing history.
- Creation timestamp.

Example:

```
Dataset Metadata

Version: 3

Location:
s3://bucket/training/v3/

Schema:
customer_features_v2

Created:
2026-01-01
```

The metadata points to the actual data artifact.

---

## Data Storage Strategies

Organizations must decide how dataset versions are physically stored.

Common approaches:

### Separate Version Folders

Example:

```
s3://ml-platform/

datasets/

 ├── customer_v1/

 ├── customer_v2/

 └── customer_v3/
```

Simple and easy to understand.

---

### Partition-Based Storage

Example:

```
s3://ml-platform/

transactions/

year=2026/

month=01/

```

Useful for:

- Large datasets.
- Analytics workloads.
- Incremental processing.

---

### Reference-Based Storage

Instead of duplicating data, systems store references to dataset states.

Useful for:

- Large datasets.
- Storage optimization.
- Advanced versioning systems.

---

## Versioning in Cloud Environments

Cloud environments provide several mechanisms for managing dataset versions.

Examples:

Amazon S3 supports:

- Object versioning.
- Metadata.
- Lifecycle policies.
- Storage organization strategies.

Additional ML platforms provide:

- Experiment tracking.
- Dataset references.
- Artifact management.

The goal is maintaining the relationship:

```
Data

+

Code

+

Configuration

+

Model
```

---

## Engineering Perspective

There is no single universal dataset versioning strategy.

The correct approach depends on:

- Dataset size.
- Update frequency.
- Cost constraints.
- Compliance requirements.
- Reproducibility needs.

For enterprise ML systems, the priority is not storing every copy of every file.

The priority is:

- Knowing what data was used.
- Reproducing results.
- Understanding changes.

---

## Key Takeaways

- Immutable datasets improve reliability.
- Snapshot versioning preserves historical states.
- Metadata versioning improves traceability.
- Storage strategies should consider cost and scale.
- Cloud ML systems combine storage, metadata, and governance mechanisms.

---

# 7. Reproducible Training Datasets

## Reproducibility Requirements

Reproducibility means being able to recreate a previous Machine Learning experiment and obtain the same or very similar results.

In ML systems, reproducibility requires controlling multiple components:

```
Dataset Version

        +

Processing Logic

        +

Feature Definitions

        +

Training Configuration

        +

Model Code

        ↓

Reproducible Experiment
```

Without controlling these elements, previous results cannot be reliably recreated.

---

## Dataset + Code + Configuration

A training dataset alone is not enough to reproduce a model.

A complete ML experiment depends on:

### Dataset

The exact data used for training.

Example:

```
customer_dataset_v3
```

---

### Processing Code

The transformations applied before training.

Example:

```
feature_engineering_v2.py
```

---

### Configuration

The parameters controlling execution.

Examples:

- Training parameters.
- Feature selection.
- Dataset paths.
- Environment configuration.

---

### Model Code

The algorithm and implementation used.

Example:

```
XGBoostClassifier

version 1.7
```

---

Together:

```
Dataset

+

Code

+

Configuration

=

Reproducible Training Environment
```

---

## Experiment Reproduction

Machine Learning teams constantly perform experiments.

Example:

Experiment A:

```
Dataset v1

Features v1

Model Configuration A

        ↓

Model Result A
```

Experiment B:

```
Dataset v2

Features v1

Model Configuration A

        ↓

Model Result B
```

The team needs to understand:

- Did performance improve because of better data?
- Better features?
- Different parameters?
- A different algorithm?

Dataset versioning allows these comparisons.

---

## Training Artifact Traceability

Every trained model should have a relationship with the artifacts that created it.

Example:

```
Model Version 5

Created From:

Dataset:
customer_data_v3

Features:
feature_set_v2

Code:
training_pipeline_v4

Configuration:
experiment_2026_01
```

This relationship creates complete traceability.

---

## Reproducibility and MLOps

Reproducibility enables:

- Debugging.
- Auditing.
- Collaboration.
- Model comparison.
- Regulatory compliance.

Without reproducibility:

```
Model Performance Changed

        ↓

Unknown Reason
```

With reproducibility:

```
Dataset Changed

        ↓

Feature Changed

        ↓

Model Changed
```

The cause becomes understandable.

---

## Engineering Perspective

Reproducibility is the bridge between experimentation and production engineering.

A data scientist may focus on:

> "Can I train a good model?"

An ML engineer focuses on:

> "Can the organization reproduce, validate, and maintain this model over time?"

Production ML requires controlled artifacts, not isolated experiments.

---

## Key Takeaways

- Reproducibility requires controlling data, code, and configuration.
- Dataset versions are essential for recreating experiments.
- Models should reference the data used during training.
- Traceability improves debugging and governance.
- Reproducibility is a fundamental MLOps principle.

---

# 8. Data Lineage and Provenance

## What is Data Lineage?

Data lineage describes the history and movement of data through a system.

It answers:

- Where did the data come from?
- What transformations were applied?
- Where was it used?

A simplified lineage example:

```
Source Database

        ↓

Raw Dataset

        ↓

Processed Dataset

        ↓

Training Dataset

        ↓

Model
```

---

## Data Origin Tracking

Organizations need to know the origin of their data.

Examples:

Source:

```
Customer Database
```

Metadata:

```
Created:
2026-01-01

Owner:
Customer Analytics Team

Source System:
CRM Platform
```

This information supports:

- Governance.
- Debugging.
- Compliance.

---

## Transformation History

Datasets usually pass through multiple transformations.

Example:

```
Raw Transactions

        ↓

Remove Invalid Records

        ↓

Generate Features

        ↓

Normalize Values

        ↓

Training Dataset
```

Lineage records these transformations.

Important information:

- Transformation logic.
- Processing version.
- Execution date.
- Responsible process.

---

## Dataset Dependencies

Datasets often depend on other datasets.

Example:

```
Customer Features Dataset

depends on:

Customer Profile Dataset

+

Transaction Dataset

+

Payment History Dataset
```

Understanding dependencies helps teams analyze impact.

Example:

If a source dataset changes:

```
Source Change

        ↓

Feature Dataset Impact

        ↓

Model Impact
```

---

## Provenance in ML Systems

Data provenance is the detailed record of how a dataset was created.

It includes:

- Source information.
- Processing steps.
- Dataset versions.
- Ownership.
- Usage history.

A model artifact should ideally have provenance information:

Example:

```
Model v10

Uses:

Dataset v5

Created From:

Raw Data v12

Processed By:

Pipeline v8
```

---

## Data Lineage in Cloud ML Platforms

Cloud ML platforms use metadata and tracking systems to maintain lineage.

Examples include:

- Dataset metadata.
- Processing job history.
- Experiment tracking.
- Model artifacts.
- Pipeline executions.

The objective is creating an interconnected ML ecosystem.

Example:

```
Data

 ↓

Processing

 ↓

Training

 ↓

Model

 ↓

Deployment
```

Every stage should be traceable.

---

## Engineering Perspective

Data lineage transforms datasets from anonymous files into managed engineering assets.

Without lineage:

```
dataset.csv

        ↓

Unknown origin
```

With lineage:

```
Dataset v5

Created from:

Source A

Processed by:

Pipeline B

Used by:

Model C
```

This enables reliable ML operations.

---

## Key Takeaways

- Data lineage tracks how data moves through systems.
- Provenance records how datasets were created.
- Source tracking improves governance.
- Transformation history improves debugging.
- Dataset dependencies help evaluate impact.
- Lineage is essential for enterprise MLOps.

---

# 9. Dataset Metadata Management

## Dataset Metadata

Dataset metadata is information that describes a dataset.

Metadata allows teams to understand:

- What the dataset contains.
- Where it came from.
- How it was created.
- How it can be used.
- Which systems depend on it.

Without metadata, datasets become difficult to discover and manage.

Example:

```
Dataset:

customer_training_data_v3


Metadata:

Owner:
ML Platform Team

Created:
2026-01-15

Source:
Customer Database

Purpose:
Credit Risk Model Training
```

---

## Technical Metadata

Technical metadata describes the technical characteristics of a dataset.

Examples:

### Structure

```
Columns:

customer_id

income

age

default_label
```

---

### Data Types

```
customer_id → integer

income → float

country → string
```

---

### Storage Information

Example:

```
Location:

s3://ml-platform/training/customer_v3/
```

---

### Processing Information

Example:

```
Created by:

SageMaker Processing Job

Version:

processing_pipeline_v2
```

Technical metadata helps engineers understand how datasets are stored and processed.

---

## Business Metadata

Business metadata explains the meaning and purpose of the data.

Examples:

Dataset purpose:

```
Credit risk prediction
```

Feature meaning:

```
income:

Customer monthly income
```

Ownership:

```
Responsible team:

Risk Analytics
```

Business metadata connects technical datasets with organizational knowledge.

---

## Operational Metadata

Operational metadata describes how datasets behave during execution.

Examples:

- Creation time.
- Update frequency.
- Pipeline execution status.
- Validation results.
- Usage history.

Example:

```
Dataset:

customer_training_v3


Last Validation:

2026-01-20


Validation Status:

Passed
```

---

## Metadata for Governance

Metadata supports enterprise governance by enabling:

### Discoverability

Teams can find available datasets.

---

### Ownership

Teams know who manages the data.

---

### Compliance

Organizations can track:

- Data usage.
- Access.
- History.

---

### Quality Management

Metadata can include:

- Validation results.
- Data quality scores.
- Schema information.

---

## Engineering Perspective

Metadata transforms datasets from simple files into managed data assets.

Without metadata:

```
dataset.csv

        ↓

Unknown meaning
```

With metadata:

```
Dataset v3

        ↓

Meaning

Ownership

History

Quality Status
```

Enterprise ML systems depend on metadata to operate reliably.

---

## Key Takeaways

- Metadata describes and manages datasets.
- Technical metadata explains dataset structure.
- Business metadata explains dataset meaning.
- Operational metadata explains dataset behavior.
- Metadata improves discovery, governance, and reliability.
- Metadata is essential for enterprise ML platforms.

---

# 10. Schema Evolution

## Why Schemas Change

Datasets are not static.

Over time, schemas change because of:

- New business requirements.
- New features.
- Source system changes.
- Data collection improvements.

Example:

Initial schema:

```
customer_id

income

age
```

New schema:

```
customer_id

income

age

credit_score
```

Schema evolution is the process of managing these changes safely.

---

## Backward Compatibility

Backward compatibility means new schema versions continue working with existing systems.

Example:

Version 1:

```
customer_id

income
```

Version 2:

```
customer_id

income

age
```

If older systems can still read the new dataset, the change is backward compatible.

---

## Breaking Changes

A breaking change is a schema modification that causes downstream failures.

Example:

Before:

```
income
```

After:

```
monthly_income
```

The feature name changed.

Any pipeline expecting:

```
income
```

may fail.

---

Other examples:

Removing columns:

Before:

```
customer_id

income

age
```

After:

```
customer_id

income
```

The age feature is no longer available.

---

Changing data types:

Before:

```
income → float
```

After:

```
income → string
```

This can break transformations and models.

---

## Schema Migration Strategies

Organizations use different strategies to manage schema changes.

---

### Versioned Schemas

Instead of modifying schemas directly:

```
Schema v1

        ↓

Schema v2
```

Each version is tracked.

---

### Compatibility Rules

Organizations define:

- Allowed changes.
- Restricted changes.
- Migration requirements.

---

### Validation Before Adoption

New schemas should pass validation before entering production workflows.

Example:

```
New Dataset Schema

        ↓

Schema Validation

        ↓

Approved Version
```

---

## Engineering Perspective

Schema evolution is a critical MLOps challenge because ML systems depend heavily on feature definitions.

A schema change can affect:

- Processing jobs.
- Feature generation.
- Training datasets.
- Models.
- Predictions.

Therefore, schema changes should be treated as controlled engineering changes.

---

## Key Takeaways

- Schemas naturally evolve over time.
- Changes must be managed carefully.
- Backward compatibility reduces pipeline failures.
- Breaking changes require migration strategies.
- Schema versions improve reliability.
- Schema evolution is essential for production ML systems.

---

# 11. Immutable Datasets

## Why Immutability Matters

An immutable dataset is a dataset version that cannot be modified after it has been created.

Instead of changing an existing dataset:

```
Dataset v1

        ↓

Modify Existing Data
```

organizations create a new version:

```
Dataset v1

        ↓

Dataset v2
```

This approach provides:

- Reproducibility.
- Traceability.
- Historical preservation.
- Safer experimentation.

---

## Raw Data Immutability

Raw datasets should generally remain unchanged after ingestion.

Example:

```
Raw Data v1

        ↓

Never Modified
```

If corrections are required:

```
Raw Data v1

        ↓

Create Corrected Version

        ↓

Raw Data v2
```

The original data remains available for:

- Auditing.
- Investigation.
- Reprocessing.

---

## Processed Dataset Immutability

Processed datasets should also be treated as controlled artifacts.

Example:

```
Raw Dataset v1

        ↓

Processing Pipeline v1

        ↓

Processed Dataset v1
```

If processing logic changes:

```
Processing Pipeline v2

        ↓

Processed Dataset v2
```

The previous version should remain accessible.

This allows teams to understand how processing changes affected results.

---

## Training Dataset Artifacts

Training datasets represent important ML artifacts.

A trained model should always reference the exact dataset used.

Example:

```
Model v5

Created Using:

Training Dataset v3

Feature Set v2

Processing Pipeline v4
```

This relationship enables:

- Reproduction.
- Debugging.
- Governance.

---

## Immutability and Cloud Storage

Cloud storage systems such as Amazon S3 support strategies that help maintain immutable artifacts.

Examples:

- Versioned objects.
- Separate dataset paths.
- Lifecycle policies.
- Access controls.

Example:

```
s3://ml-platform/

datasets/

 ├── customer_v1/

 ├── customer_v2/

 └── customer_v3/
```

Each version represents a controlled artifact.

---

## Engineering Perspective

Immutability does not mean data never changes.

Data naturally evolves.

The principle is:

> Existing versions should remain stable, while new versions represent change.

This creates a reliable history of how ML systems were built.

---

## Key Takeaways

- Immutable datasets preserve historical states.
- Existing dataset versions should not be overwritten.
- New changes should create new versions.
- Training artifacts should reference exact dataset versions.
- Immutability improves reproducibility and governance.

---

# 12. Best Practices

## Version Important Datasets

Not every temporary dataset requires formal versioning.

Prioritize versioning for:

- Training datasets.
- Validation datasets.
- Feature datasets.
- Production ML artifacts.

---

## Preserve Dataset Metadata

Every important dataset version should include metadata.

Examples:

- Dataset owner.
- Creation date.
- Source.
- Schema.
- Processing version.
- Validation status.

Metadata makes datasets understandable and discoverable.

---

## Maintain Data Lineage

Track:

- Data origin.
- Transformations.
- Dependencies.
- Model usage.

Example:

```
Source Database

        ↓

Raw Dataset v2

        ↓

Processed Dataset v3

        ↓

Model v5
```

---

## Link Datasets With Models

A model should always reference:

- Training dataset version.
- Feature version.
- Code version.
- Configuration.

Example:

```
Model v10

Uses:

Dataset v6

Feature Set v4

Training Pipeline v8
```

---

## Avoid Overwriting Production Artifacts

Avoid practices such as:

```
training_dataset.csv

        ↓

Replace File
```

Better:

```
training_dataset_v1.csv

training_dataset_v2.csv

training_dataset_v3.csv
```

---

## Automate Dataset Tracking

Manual tracking does not scale.

Automation should capture:

- Dataset versions.
- Metadata.
- Lineage.
- Validation results.

This reduces human errors.

---

## Design for Reproducibility

A mature ML system should answer:

- Which data trained this model?
- Which transformations were applied?
- Can we recreate this experiment?
- What changed between versions?

---

## Consider Storage Costs

Dataset versioning increases storage requirements.

Organizations should balance:

- Reproducibility.
- Retention requirements.
- Storage costs.

Strategies include:

- Lifecycle policies.
- Archiving older versions.
- Storage classes.
- Selective versioning.

---

## Engineering Perspective

Dataset versioning best practices represent a shift from data management to ML asset management.

The objective is not simply storing files.

The objective is creating a trustworthy relationship between:

```
Data

+

Code

+

Features

+

Models

+

Metadata
```

This relationship enables reliable enterprise Machine Learning.

---

## Key Takeaways

- Version important ML datasets.
- Preserve metadata and lineage.
- Keep dataset artifacts immutable.
- Connect datasets with models.
- Automate tracking whenever possible.
- Balance reproducibility and storage costs.
- Treat datasets as production engineering assets.

---

# 13. Common Mistakes

## Overwriting Existing Datasets

One of the most common mistakes is modifying existing datasets instead of creating new versions.

Incorrect:

```
Training Dataset

        ↓

Overwrite Existing File
```

Problems:

- Loss of historical information.
- Difficult reproduction.
- Unknown impact on existing models.

Better:

```
Training Dataset v1

        ↓

Training Dataset v2
```

---

## Missing Dataset Metadata

A dataset without metadata becomes difficult to understand.

Missing information may include:

- Data source.
- Dataset owner.
- Creation date.
- Processing history.
- Validation status.

Without metadata, teams cannot reliably manage datasets.

---

## No Dataset Version Tracking

Another common mistake is training models without recording the dataset version.

Example:

```
Model v5

trained with:

unknown dataset
```

Problems:

- Cannot reproduce results.
- Cannot explain model changes.
- Difficult auditing.

---

## Training Models Without Knowing the Dataset Version

A model should always reference the exact data artifact used during training.

Incorrect:

```
Model v3

Training Data:

customer_data.csv
```

Problem:

The file may change over time.

Better:

```
Model v3

Training Data:

customer_dataset_v7
```

---

## Mixing Different Dataset Versions

Using inconsistent dataset versions can introduce hidden problems.

Example:

```
Training Features:

Dataset v3


Labels:

Dataset v5
```

Possible consequences:

- Incorrect training examples.
- Data inconsistencies.
- Unreliable models.

---

## Ignoring Data Lineage

Without lineage, teams cannot understand how data moved through the system.

Example:

```
dataset.csv

        ↓

Unknown source

        ↓

Unknown transformations
```

This creates governance and debugging problems.

---

## Not Managing Schema Changes

Unexpected schema changes can break ML pipelines.

Examples:

- Removed features.
- Renamed columns.
- Changed data types.

Schema evolution should always be controlled.

---

## Engineering Perspective

Most dataset versioning failures are not caused by lack of technology.

They are caused by weak engineering practices:

- Poor documentation.
- Manual tracking.
- Lack of ownership.
- No reproducibility strategy.

Tools can support versioning, but engineering discipline creates reliable ML systems.

---

## Key Takeaways

- Never overwrite important dataset artifacts.
- Always track dataset versions.
- Store metadata with datasets.
- Maintain lineage information.
- Control schema evolution.
- Connect models with the exact data used for training.

---

# 14. Summary

Dataset Versioning Strategy completes the data foundation layer of an enterprise MLOps architecture.

After implementing:

```
Amazon S3 Data Lake

        ↓

AWS Glue Data Catalog

        ↓

Amazon Athena

        ↓

SageMaker Processing Jobs

        ↓

Training Dataset Validation

        ↓

Dataset Versioning Strategy
```

organizations have a controlled and reproducible data lifecycle.

---

## Main Concepts Covered

### Dataset Versioning

Datasets should evolve through controlled versions instead of uncontrolled modifications.

---

### Reproducibility

A Machine Learning experiment requires:

```
Dataset Version

+

Code Version

+

Feature Version

+

Configuration

```

to be recreated.

---

### Data Lineage

Organizations need to understand:

- Where data came from.
- How it was transformed.
- Which models used it.

---

### Metadata Management

Metadata provides:

- Discoverability.
- Ownership.
- Governance.
- Operational visibility.

---

### Schema Evolution

Schemas change over time and must be managed carefully to avoid breaking ML workflows.

---

### Immutable Data Artifacts

Important datasets should remain stable after creation.

New changes should create new versions.

---

## Final Architecture Position

The complete Phase 2A data foundation is:

```
Data Sources

        ↓

Amazon S3 Data Lake

        ↓

AWS Glue Data Catalog

        ↓

Amazon Athena

        ↓

SageMaker Processing Jobs

        ↓

Training Dataset Validation

        ↓

Dataset Versioning

        ↓

SageMaker Training Jobs

        ↓

Model Evaluation

        ↓

Deployment
```

The main engineering principle is:

**Reliable Machine Learning requires reliable, traceable, and reproducible data foundations.**

---

## Key Takeaways

- Data is a first-class ML engineering artifact.
- Dataset versions are required for reproducibility.
- Models must reference the data used to create them.
- Metadata and lineage enable governance.
- Immutable artifacts improve reliability.
- Dataset management is a core MLOps responsibility.

---

# 15. Interview Preparation

## Conceptual Questions

### 1. Why do we need dataset versioning in Machine Learning?

Expected answer:

Dataset versioning allows teams to track changes, reproduce experiments, and understand which data created a specific model.

Unlike traditional software, ML systems depend on both code and data.

---

### 2. How is dataset versioning different from storing multiple files?

Expected answer:

Dataset versioning is not simply copying files.

It maintains relationships between:

- Dataset state.
- Metadata.
- Processing logic.
- Models.

The goal is reproducibility and traceability.

---

### 3. What is data lineage?

Expected answer:

Data lineage describes the history of data movement and transformations through a system.

It explains:

- Data origin.
- Processing steps.
- Dataset dependencies.
- Model usage.

---

### 4. Why should datasets be immutable?

Expected answer:

Immutable datasets preserve historical states and allow previous ML experiments and models to be reproduced.

---

### 5. How would you reproduce a previous ML experiment?

Expected answer:

I would recover:

- Dataset version.
- Feature transformations.
- Training code.
- Configuration.
- Environment information.

Then recreate the experiment.

---

# Practical Questions

## 1. A model performance decreased after retraining. How would dataset versioning help?

Expected answer:

Dataset versioning allows comparison between:

```
Previous Dataset Version

        vs

New Dataset Version
```

The team can determine whether the change was caused by:

- Data changes.
- Feature changes.
- Training changes.

---

## 2. How would you design dataset management in AWS?

Expected answer:

A possible architecture:

```
Amazon S3

Dataset Storage

        ↓

AWS Glue Data Catalog

Metadata Management

        ↓

Validation Pipeline

        ↓

Versioned Training Dataset

        ↓

SageMaker Training Job
```

---

## 3. How do you handle schema changes?

Expected answer:

I would:

- Version schemas.
- Validate compatibility.
- Test changes before production.
- Avoid breaking downstream pipelines.

---

# Architecture Question

## Design a reproducible ML training workflow.

Expected answer:

```
Data Source

        ↓

Raw Dataset Version

        ↓

Processing Pipeline Version

        ↓

Validated Training Dataset Version

        ↓

Training Configuration

        ↓

Model Version
```

Every artifact should be traceable.

---

# Expected Competencies

After completing this document, you should be able to:

- Explain why dataset versioning is required.
- Describe dataset lifecycle management.
- Explain reproducible ML experiments.
- Understand dataset lineage and provenance.
- Explain metadata management.
- Understand schema evolution.
- Explain immutable datasets.
- Design dataset versioning strategies.
- Connect datasets with model versions.
- Discuss dataset governance during ML Engineer interviews.

---

# Self-Assessment Checklist

You should be able to confidently answer **Yes** to:

- □ I understand why ML datasets require versions.
- □ I understand the relationship between data and models.
- □ I can explain reproducible training datasets.
- □ I understand data lineage.
- □ I understand dataset provenance.
- □ I understand metadata management.
- □ I understand schema evolution.
- □ I understand immutable datasets.
- □ I can explain dataset versioning strategies.
- □ I can design a high-level AWS dataset management architecture.
- □ I can discuss dataset versioning from an MLOps perspective.
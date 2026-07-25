"""
Module:
    preprocess_dataset.py

Path:
    scripts/preprocess_dataset.py

Purpose:
    Execute the credit risk dataset preprocessing pipeline.

Description:
    Runs the preprocessing workflow that transforms the raw credit risk
    dataset into processed business datasets.
"""

from mlops_engineering_roadmap.data.preprocessing import (
    preprocess_credit_risk_dataset,
)


def main() -> None:
    """
    Execute the preprocessing pipeline.
    """

    processed_datasets = preprocess_credit_risk_dataset()

    print("Dataset preprocessing completed successfully.")

    for dataset_name, dataset_path in processed_datasets.items():
        print(f"{dataset_name}: {dataset_path}")


if __name__ == "__main__":
    main()

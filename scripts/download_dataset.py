"""
Module:
    download_dataset.py

Path:
    scripts/download_dataset.py

Purpose:
    Download the reference dataset used throughout the roadmap.

Description:
    Executes the dataset downloader and prints the location of the downloaded
    dataset.
"""

from mlops_engineering_roadmap.data.downloader import download_credit_risk_dataset


def main() -> None:
    """Download the dataset and display its local path."""

    dataset_path = download_credit_risk_dataset()

    print("\nDataset downloaded successfully.")
    print(f"Location: {dataset_path}")


if __name__ == "__main__":
    main()

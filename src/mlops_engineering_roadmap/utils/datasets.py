"""
Module:
    datasets.py

Path:
    src/mlops_engineering_roadmap/utils/datasets.py

Purpose:
    Centralize dataset configuration paths.

Description:
    Defines constants used by the data pipeline to locate raw,
    processed, and downloaded datasets.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIRECTORY = PROJECT_ROOT / "data"

RAW_DIRECTORY = DATA_DIRECTORY / "raw"

PROCESSED_DIRECTORY = DATA_DIRECTORY / "processed"


# =============================================================================
# Raw Dataset Configuration
# =============================================================================

KAGGLE_DATASET = "laotse/credit-risk-dataset"

ORIGINAL_DATA_DIRECTORY = RAW_DIRECTORY / "original"

DOWNLOAD_DIRECTORY = ORIGINAL_DATA_DIRECTORY

DOWNLOADED_DATASET_PATH = ORIGINAL_DATA_DIRECTORY / "credit_risk_dataset.csv"


# =============================================================================
# Processed Dataset Configuration
# =============================================================================

CUSTOMER_DIRECTORY = PROCESSED_DIRECTORY / "customer"

FINANCIAL_HISTORY_DIRECTORY = PROCESSED_DIRECTORY / "financial_history"

LOAN_APPLICATION_DIRECTORY = PROCESSED_DIRECTORY / "loan_application"


CUSTOMER_DATASET_PATH = CUSTOMER_DIRECTORY / "customer.csv"

FINANCIAL_HISTORY_DATASET_PATH = FINANCIAL_HISTORY_DIRECTORY / "financial_history.csv"

LOAN_APPLICATION_DATASET_PATH = LOAN_APPLICATION_DIRECTORY / "loan_application.csv"

"""
Module:
    datasets.py

Path:
    src/mlops_engineering_roadmap/utils/datasets.py

Purpose:
    Centralize dataset metadata and project data paths.

Description:
    Defines the project directories, dataset identifiers, and file locations
    used by the data engineering pipeline.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

FEATURES_DIR = DATA_DIR / "features"

VERSIONS_DIR = DATA_DIR / "versions"

# =============================================================================
# Credit Risk Dataset Configuration
# =============================================================================

KAGGLE_DATASET = "laotse/credit-risk-dataset"

DATASET_FILENAME = "credit_risk_dataset.csv"

DOWNLOAD_DIRECTORY = RAW_DATA_DIR

DOWNLOADED_DATASET_PATH = DOWNLOAD_DIRECTORY / DATASET_FILENAME

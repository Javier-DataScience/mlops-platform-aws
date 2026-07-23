"""
Module:
    downloader.py

Path:
    src/mlops_engineering_roadmap/data/downloader.py

Purpose:
    Download datasets required by the data engineering pipeline.

Description:
    Downloads the Credit Risk dataset from Kaggle when it is not already
    available locally. The module avoids unnecessary downloads and returns
    the local path to the dataset.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

from kaggle import api

from mlops_engineering_roadmap.utils.datasets import (
    DOWNLOAD_DIRECTORY,
    DOWNLOADED_DATASET_PATH,
    KAGGLE_DATASET,
)
from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Public Functions
# =============================================================================


def download_credit_risk_dataset() -> Path:
    """
    Download the Credit Risk dataset from Kaggle if it does not already exist.

    Returns
    -------
    Path
        Local path to the downloaded dataset.

    Raises
    ------
    RuntimeError
        If the dataset download fails.
    """

    if DOWNLOADED_DATASET_PATH.exists():
        logger.info("Dataset already available: %s", DOWNLOADED_DATASET_PATH)
        return DOWNLOADED_DATASET_PATH

    logger.info("Downloading dataset from Kaggle...")

    try:
        api.dataset_download_files(
            dataset=KAGGLE_DATASET,
            path=DOWNLOAD_DIRECTORY,
            unzip=True,
        )

        logger.info("Dataset downloaded successfully.")

        return DOWNLOADED_DATASET_PATH

    except Exception as exc:
        logger.exception("Dataset download failed.")
        raise RuntimeError("Unable to download dataset from Kaggle.") from exc

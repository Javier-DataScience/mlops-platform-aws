"""
Module:
    ingestion.py

Path:
    src/mlops_engineering_roadmap/data/ingestion.py

Purpose:
    Provide reusable functions to load raw datasets.

Description:
    This module handles the ingestion layer of the data pipeline.
    It loads raw datasets from the data lake structure and returns
    pandas DataFrames for downstream processing.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

import pandas as pd

from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Public Functions
# =============================================================================


def load_csv_dataset(dataset_path: Path) -> pd.DataFrame:
    """
    Load a CSV dataset into a pandas DataFrame.

    Parameters
    ----------
    dataset_path : Path
        Location of the CSV dataset.

    Returns
    -------
    pd.DataFrame
        Dataset loaded into memory.

    Raises
    ------
    FileNotFoundError
        If the dataset does not exist.
    """

    if not dataset_path.exists():
        logger.error("Dataset not found: %s", dataset_path)
        raise FileNotFoundError(f"Dataset does not exist: {dataset_path}")

    logger.info("Loading dataset: %s", dataset_path)

    dataframe = pd.read_csv(dataset_path)

    logger.info(
        "Dataset loaded successfully. Rows: %s Columns: %s",
        dataframe.shape[0],
        dataframe.shape[1],
    )

    return dataframe

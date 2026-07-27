"""
Module:
    validation.py

Path:
    src/mlops_engineering_roadmap/data/validation.py

Purpose:
    Validate datasets before preprocessing and model training.

Description:
    Provides reusable validation utilities to verify dataset integrity,
    required columns, missing values, and basic structural consistency.

    This module does not modify datasets.

    It only validates them.
"""

# =============================================================================
# Imports
# =============================================================================

from collections.abc import Sequence

import pandas as pd

from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Validation Functions
# =============================================================================


def validate_dataset_not_empty(
    dataframe: pd.DataFrame,
) -> None:
    """
    Validate that the dataset is not empty.

    Args:
        dataframe:
            Dataset to validate.

    Raises:
        ValueError:
            If the dataset contains no rows.
    """

    if dataframe.empty:
        raise ValueError("Dataset is empty.")


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: Sequence[str],
) -> None:
    """
    Validate that all required columns exist.

    Args:
        dataframe:
            Dataset to validate.

        required_columns:
            Expected column names.

    Raises:
        ValueError:
            If required columns are missing.
    """

    missing_columns = [column for column in required_columns if column not in dataframe.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")


def validate_missing_values(
    dataframe: pd.DataFrame,
    required_columns: Sequence[str],
) -> None:
    """
    Validate missing values in required columns.

    Args:
        dataframe:
            Dataset to validate.

        required_columns:
            Columns that must not contain missing values.

    Raises:
        ValueError:
            If missing values are detected.
    """

    columns_with_nulls = [column for column in required_columns if dataframe[column].isnull().any()]

    if columns_with_nulls:
        raise ValueError(f"Missing values detected in columns: {', '.join(columns_with_nulls)}")


# =============================================================================
# Public Validation Pipeline
# =============================================================================


def validate_dataset(
    dataframe: pd.DataFrame,
    required_columns: Sequence[str],
) -> None:
    """
    Execute the complete dataset validation pipeline.

    Args:
        dataframe:
            Dataset to validate.

        required_columns:
            Required columns for the dataset.

    Raises:
        ValueError:
            If any validation step fails.
    """

    logger.info("Starting dataset validation.")

    validate_dataset_not_empty(dataframe)

    validate_required_columns(
        dataframe=dataframe,
        required_columns=required_columns,
    )

    validate_missing_values(
        dataframe=dataframe,
        required_columns=required_columns,
    )

    logger.info("Dataset validation completed successfully.")

"""
Module:
    test_validation.py

Path:
    tests/data/test_validation.py

Purpose:
    Validate dataset validation utilities.

Description:
    Tests the validation module to ensure datasets comply with
    structural and quality requirements before ML processing.
"""

# =============================================================================
# Imports
# =============================================================================

import pandas as pd
import pytest

from mlops_engineering_roadmap.data.validation import validate_dataset

# =============================================================================
# Tests
# =============================================================================


def test_validate_dataset_with_valid_dataframe() -> None:
    """
    Verify that a valid dataset passes validation.
    """

    dataframe = pd.DataFrame(
        {
            "customer_id": ["C001", "C002"],
            "income": [50000, 60000],
        }
    )

    validate_dataset(
        dataframe=dataframe,
        required_columns=[
            "customer_id",
            "income",
        ],
    )


def test_validate_dataset_with_empty_dataframe() -> None:
    """
    Verify that an empty dataset raises an error.
    """

    dataframe = pd.DataFrame(
        columns=[
            "customer_id",
            "income",
        ]
    )

    with pytest.raises(ValueError):
        validate_dataset(
            dataframe=dataframe,
            required_columns=[
                "customer_id",
                "income",
            ],
        )


def test_validate_dataset_with_missing_columns() -> None:
    """
    Verify that missing required columns raise an error.
    """

    dataframe = pd.DataFrame(
        {
            "customer_id": ["C001"],
        }
    )

    with pytest.raises(ValueError):
        validate_dataset(
            dataframe=dataframe,
            required_columns=[
                "customer_id",
                "income",
            ],
        )


def test_validate_dataset_with_missing_values() -> None:
    """
    Verify that missing values raise an error.
    """

    dataframe = pd.DataFrame(
        {
            "customer_id": ["C001", "C002"],
            "income": [50000, None],
        }
    )

    with pytest.raises(ValueError):
        validate_dataset(
            dataframe=dataframe,
            required_columns=[
                "customer_id",
                "income",
            ],
        )

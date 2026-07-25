"""
Module:
    test_ingestion.py

Path:
    tests/data/test_ingestion.py

Purpose:
    Validate the dataset ingestion module.

Description:
    Tests the loading of CSV datasets and verifies that ingestion
    returns valid pandas DataFrames.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

import pandas as pd
import pytest

from mlops_engineering_roadmap.data.ingestion import load_csv_dataset

# =============================================================================
# Tests
# =============================================================================


def test_load_csv_dataset_returns_dataframe(tmp_path: Path) -> None:
    """
    Verify that a CSV file is loaded as a pandas DataFrame.
    """

    dataset_path = tmp_path / "test_dataset.csv"

    dataset_path.write_text("customer_id,income\n1,50000\n2,60000\n")

    dataframe = load_csv_dataset(dataset_path)

    assert isinstance(dataframe, pd.DataFrame)


def test_load_csv_dataset_preserves_columns(tmp_path: Path) -> None:
    """
    Verify that loaded datasets contain expected columns.
    """

    dataset_path = tmp_path / "test_dataset.csv"

    dataset_path.write_text("customer_id,income\n1,50000\n2,60000\n")

    dataframe = load_csv_dataset(dataset_path)

    assert list(dataframe.columns) == [
        "customer_id",
        "income",
    ]


def test_load_csv_dataset_file_not_found() -> None:
    """
    Verify that missing datasets raise FileNotFoundError.
    """

    dataset_path = Path("missing_dataset.csv")

    with pytest.raises(FileNotFoundError):
        load_csv_dataset(dataset_path)

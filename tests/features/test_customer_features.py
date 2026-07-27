"""
Module:
    test_customer_features.py

Path:
    tests/features/test_customer_features.py

Purpose:
    Validate customer feature engineering transformations.
"""

# =============================================================================
# Imports
# =============================================================================

import pandas as pd

from mlops_engineering_roadmap.features.customer_features import (
    create_customer_features,
)

# =============================================================================
# Tests
# =============================================================================


def test_create_customer_features() -> None:
    """
    Verify customer feature generation.
    """

    customer_data = pd.DataFrame(
        {
            "customer_id": ["C000001"],
            "age": [22],
            "income": [59000],
            "home_ownership": ["RENT"],
            "employment_length": [123],
        }
    )

    result = create_customer_features(customer_data)

    assert "age_category" in result.columns
    assert "income_category" in result.columns
    assert "employment_stability" in result.columns


def test_customer_original_columns_are_preserved() -> None:
    """
    Verify original dataset columns remain.
    """

    customer_data = pd.DataFrame(
        {
            "customer_id": ["C000001"],
            "age": [22],
            "income": [59000],
            "home_ownership": ["RENT"],
            "employment_length": [123],
        }
    )

    result = create_customer_features(customer_data)

    assert "customer_id" in result.columns
    assert "age" in result.columns
    assert "income" in result.columns
    assert "home_ownership" in result.columns
    assert "employment_length" in result.columns


def test_customer_feature_business_rules() -> None:
    """
    Verify feature engineering rules.
    """

    customer_data = pd.DataFrame(
        {
            "customer_id": ["C000001"],
            "age": [22],
            "income": [59000],
            "home_ownership": ["RENT"],
            "employment_length": [123],
        }
    )

    result = create_customer_features(customer_data)

    row = result.iloc[0]

    assert row["age_category"] == "young"
    assert row["income_category"] == "medium"
    assert row["employment_stability"] == "stable"

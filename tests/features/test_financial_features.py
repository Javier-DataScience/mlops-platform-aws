"""
Module:
    test_financial_features.py

Path:
    tests/features/test_financial_features.py

Purpose:
    Validate financial feature engineering transformations.
"""

# =============================================================================
# Imports
# =============================================================================

import pandas as pd

from mlops_engineering_roadmap.features.financial_features import (
    create_financial_features,
)

# =============================================================================
# Tests
# =============================================================================


def test_create_financial_features() -> None:
    """
    Verify financial feature generation.
    """

    financial_data = pd.DataFrame(
        {
            "customer_id": ["C000001"],
            "credit_history_length": [3],
            "default_history": ["Y"],
        }
    )

    result = create_financial_features(financial_data)

    assert "credit_history_category" in result.columns
    assert "has_default_history" in result.columns
    assert "financial_risk_level" in result.columns


def test_financial_original_columns_are_preserved() -> None:
    """
    Verify original dataset columns remain.
    """

    financial_data = pd.DataFrame(
        {
            "customer_id": ["C000001"],
            "credit_history_length": [3],
            "default_history": ["Y"],
        }
    )

    result = create_financial_features(financial_data)

    assert "customer_id" in result.columns
    assert "credit_history_length" in result.columns
    assert "default_history" in result.columns


def test_financial_feature_business_rules() -> None:
    """
    Verify financial feature rules.
    """

    financial_data = pd.DataFrame(
        {
            "customer_id": [
                "C000001",
                "C000002",
            ],
            "credit_history_length": [
                3,
                8,
            ],
            "default_history": [
                "Y",
                "N",
            ],
        }
    )

    result = create_financial_features(financial_data)

    high_risk_customer = result.iloc[0]

    assert high_risk_customer["credit_history_category"] == "medium"

    assert high_risk_customer["has_default_history"] == 1

    assert high_risk_customer["financial_risk_level"] == "high"

    low_risk_customer = result.iloc[1]

    assert low_risk_customer["credit_history_category"] == "long"

    assert low_risk_customer["has_default_history"] == 0

    assert low_risk_customer["financial_risk_level"] == "low"

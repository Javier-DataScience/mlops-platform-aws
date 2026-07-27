"""
Module:
    test_loan_features.py

Path:
    tests/features/test_loan_features.py

Purpose:
    Validate loan feature engineering transformations.
"""

# =============================================================================
# Imports
# =============================================================================

import pandas as pd

from mlops_engineering_roadmap.features.loan_features import (
    create_loan_features,
)

# =============================================================================
# Tests
# =============================================================================


def test_create_loan_features() -> None:
    """
    Verify loan feature generation.
    """

    loan_data = pd.DataFrame(
        {
            "application_id": ["A000001"],
            "customer_id": ["C000001"],
            "loan_amount": [35000],
            "loan_intent": ["PERSONAL"],
            "loan_grade": ["D"],
            "loan_interest_rate": [16.02],
            "loan_percent_income": [0.59],
            "loan_status": [1],
        }
    )

    result = create_loan_features(loan_data)

    assert "loan_amount_category" in result.columns
    assert "interest_rate_category" in result.columns
    assert "income_burden_category" in result.columns
    assert "loan_grade_score" in result.columns


def test_loan_original_columns_are_preserved() -> None:
    """
    Verify original dataset columns remain.
    """

    loan_data = pd.DataFrame(
        {
            "application_id": ["A000001"],
            "customer_id": ["C000001"],
            "loan_amount": [35000],
            "loan_intent": ["PERSONAL"],
            "loan_grade": ["D"],
            "loan_interest_rate": [16.02],
            "loan_percent_income": [0.59],
            "loan_status": [1],
        }
    )

    result = create_loan_features(loan_data)

    assert "application_id" in result.columns
    assert "customer_id" in result.columns
    assert "loan_amount" in result.columns
    assert "loan_grade" in result.columns
    assert "loan_interest_rate" in result.columns
    assert "loan_percent_income" in result.columns
    assert "loan_status" in result.columns


def test_loan_feature_business_rules() -> None:
    """
    Verify loan feature rules.
    """

    loan_data = pd.DataFrame(
        {
            "application_id": [
                "A000001",
                "A000002",
            ],
            "customer_id": [
                "C000001",
                "C000002",
            ],
            "loan_amount": [
                35000,
                1000,
            ],
            "loan_intent": [
                "PERSONAL",
                "EDUCATION",
            ],
            "loan_grade": [
                "D",
                "B",
            ],
            "loan_interest_rate": [
                16.02,
                11.14,
            ],
            "loan_percent_income": [
                0.59,
                0.10,
            ],
            "loan_status": [
                1,
                0,
            ],
        }
    )

    result = create_loan_features(loan_data)

    high_risk_application = result.iloc[0]

    assert high_risk_application["loan_amount_category"] == "large"

    assert high_risk_application["interest_rate_category"] == "high"

    assert high_risk_application["income_burden_category"] == "high"

    assert high_risk_application["loan_grade_score"] == 4

    second_application = result.iloc[1]

    assert second_application["loan_amount_category"] == "small"

    assert second_application["interest_rate_category"] == "medium"

    assert second_application["income_burden_category"] == "low"

    assert second_application["loan_grade_score"] == 2

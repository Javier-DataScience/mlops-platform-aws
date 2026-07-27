"""
Module:
    loan_features.py

Path:
    src/mlops_engineering_roadmap/features/loan_features.py

Purpose:
    Generate loan-related ML features.

Description:
    Contains reusable feature engineering transformations
    for loan application data.
"""

# =============================================================================
# Imports
# =============================================================================

import pandas as pd

from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)


# =============================================================================
# Feature Engineering Functions
# =============================================================================


def create_loan_features(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create loan feature dataset.

    Args:
        dataframe:
            Processed loan application dataset.

    Returns:
        Dataset containing engineered loan features.
    """

    features = dataframe.copy()

    features["loan_amount_category"] = pd.cut(
        features["loan_amount"],
        bins=[
            -1,
            5000,
            20000,
            float("inf"),
        ],
        labels=[
            "small",
            "medium",
            "large",
        ],
    )

    features["interest_rate_category"] = pd.cut(
        features["loan_interest_rate"],
        bins=[
            -1,
            10,
            15,
            float("inf"),
        ],
        labels=[
            "low",
            "medium",
            "high",
        ],
        right=False,
    )

    features["income_burden_category"] = pd.cut(
        features["loan_percent_income"],
        bins=[
            -1,
            0.2,
            0.5,
            float("inf"),
        ],
        labels=[
            "low",
            "medium",
            "high",
        ],
        right=False,
    )

    grade_mapping = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
    }

    features["loan_grade_score"] = features["loan_grade"].map(grade_mapping)

    logger.info("Loan features created successfully.")

    return features

"""
Module:
    financial_features.py

Path:
    src/mlops_engineering_roadmap/features/financial_features.py

Purpose:
    Generate financial-related ML features.

Description:
    Contains reusable feature engineering transformations
    for financial history data.
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


def create_financial_features(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create financial feature dataset.

    Args:
        dataframe:
            Processed financial history dataset.

    Returns:
        Dataset containing engineered financial features.
    """

    features = dataframe.copy()

    features["credit_history_category"] = pd.cut(
        features["credit_history_length"],
        bins=[-1, 2, 5, float("inf")],
        labels=[
            "short",
            "medium",
            "long",
        ],
        right=True,
    )

    features["has_default_history"] = features["default_history"].map(
        {
            "Y": 1,
            "N": 0,
        }
    )

    features["financial_risk_level"] = "medium"

    features.loc[
        features["has_default_history"] == 1,
        "financial_risk_level",
    ] = "high"

    features.loc[
        (features["has_default_history"] == 0) & (features["credit_history_category"] == "long"),
        "financial_risk_level",
    ] = "low"

    logger.info("Financial features created successfully.")

    return features

"""
Module:
    customer_features.py

Path:
    src/mlops_engineering_roadmap/features/customer_features.py

Purpose:
    Generate customer-related ML features.

Description:
    Contains reusable feature engineering transformations
    for customer profile data.
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


def create_customer_features(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create customer feature dataset.

    Args:
        dataframe:
            Processed customer dataset.

    Returns:
        Dataset containing engineered customer features.
    """

    features = dataframe.copy()

    features["age_category"] = pd.cut(
        features["age"],
        bins=[0, 25, 50, float("inf")],
        labels=[
            "young",
            "adult",
            "senior",
        ],
        right=False,
    )

    features["income_category"] = pd.cut(
        features["income"],
        bins=[0, 30000, 70000, float("inf")],
        labels=[
            "low",
            "medium",
            "high",
        ],
        right=False,
    )

    features["employment_stability"] = pd.cut(
        features["employment_length"],
        bins=[-1, 2, 5, float("inf")],
        labels=[
            "unstable",
            "moderate",
            "stable",
        ],
        right=False,
    )

    logger.info("Customer features created successfully.")

    return features

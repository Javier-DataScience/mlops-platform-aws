"""
Module:
    build_features.py

Path:
    scripts/build_features.py

Purpose:
    Execute the complete feature engineering pipeline.

Description:
    Loads processed datasets, applies feature engineering modules,
    and stores reusable feature datasets.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

import pandas as pd

from mlops_engineering_roadmap.features.customer_features import (
    create_customer_features,
)
from mlops_engineering_roadmap.features.financial_features import (
    create_financial_features,
)
from mlops_engineering_roadmap.features.loan_features import (
    create_loan_features,
)
from mlops_engineering_roadmap.utils.datasets import (
    CUSTOMER_DATASET_PATH,
    FINANCIAL_HISTORY_DATASET_PATH,
    LOAN_APPLICATION_DATASET_PATH,
)
from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)


# =============================================================================
# Feature Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FEATURE_DIRECTORY = PROJECT_ROOT / "data" / "features"


CUSTOMER_FEATURE_PATH = FEATURE_DIRECTORY / "offline" / "customer" / "customer_features.csv"


FINANCIAL_FEATURE_PATH = (
    FEATURE_DIRECTORY / "offline" / "financial_history" / "financial_features.csv"
)


LOAN_FEATURE_PATH = FEATURE_DIRECTORY / "offline" / "loan_application" / "loan_features.csv"


# =============================================================================
# Pipeline Functions
# =============================================================================


def save_features(
    dataframe: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Save engineered features.

    Args:
        dataframe:
            Feature dataset.

        output_path:
            Destination path.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe.to_csv(
        output_path,
        index=False,
    )


def build_feature_datasets() -> None:
    """
    Execute feature engineering pipeline.
    """

    logger.info("Starting feature engineering pipeline.")

    customer_df = pd.read_csv(CUSTOMER_DATASET_PATH)

    financial_df = pd.read_csv(FINANCIAL_HISTORY_DATASET_PATH)

    loan_df = pd.read_csv(LOAN_APPLICATION_DATASET_PATH)

    customer_features = create_customer_features(customer_df)

    financial_features = create_financial_features(financial_df)

    loan_features = create_loan_features(loan_df)

    save_features(
        customer_features,
        CUSTOMER_FEATURE_PATH,
    )

    save_features(
        financial_features,
        FINANCIAL_FEATURE_PATH,
    )

    save_features(
        loan_features,
        LOAN_FEATURE_PATH,
    )

    logger.info("Feature engineering pipeline completed successfully.")


# =============================================================================
# Main Entry Point
# =============================================================================


def main() -> None:
    """
    Execute pipeline.
    """

    build_feature_datasets()


if __name__ == "__main__":
    main()

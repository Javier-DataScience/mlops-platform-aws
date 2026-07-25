"""
Module:
    preprocessing.py

Path:
    src/mlops_engineering_roadmap/data/preprocessing.py

Purpose:
    Transform raw datasets into processed business datasets.

Description:
    Creates customer, financial history, and loan application datasets
    from the original credit risk dataset.
"""

from pathlib import Path

import pandas as pd

from mlops_engineering_roadmap.utils.datasets import (
    CUSTOMER_DATASET_PATH,
    CUSTOMER_DIRECTORY,
    DOWNLOADED_DATASET_PATH,
    FINANCIAL_HISTORY_DATASET_PATH,
    FINANCIAL_HISTORY_DIRECTORY,
    LOAN_APPLICATION_DATASET_PATH,
    LOAN_APPLICATION_DIRECTORY,
)
from mlops_engineering_roadmap.utils.logger import get_logger

logger = get_logger(__name__)


def _generate_customer_ids(number_of_records: int) -> list[str]:
    """
    Generate deterministic customer identifiers.

    Parameters
    ----------
    number_of_records:
        Number of identifiers required.

    Returns
    -------
    list[str]
        Generated customer identifiers.
    """

    return [f"C{index:06d}" for index in range(1, number_of_records + 1)]


def _generate_application_ids(number_of_records: int) -> list[str]:
    """
    Generate deterministic loan application identifiers.

    Parameters
    ----------
    number_of_records:
        Number of identifiers required.

    Returns
    -------
    list[str]
        Generated application identifiers.
    """

    return [f"A{index:06d}" for index in range(1, number_of_records + 1)]


def create_customer_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Create the customer profile dataset.

    Parameters
    ----------
    dataframe:
        Original credit risk dataframe.

    Returns
    -------
    pd.DataFrame
        Customer dataset.
    """

    customer_dataset = pd.DataFrame(
        {
            "customer_id": _generate_customer_ids(len(dataframe)),
            "age": dataframe["person_age"],
            "income": dataframe["person_income"],
            "home_ownership": dataframe["person_home_ownership"],
            "employment_length": dataframe["person_emp_length"],
        }
    )

    return customer_dataset


def create_financial_history_dataset(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create the financial history dataset.

    Parameters
    ----------
    dataframe:
        Original credit risk dataframe.

    Returns
    -------
    pd.DataFrame
        Financial history dataset.
    """

    financial_history_dataset = pd.DataFrame(
        {
            "customer_id": _generate_customer_ids(len(dataframe)),
            "credit_history_length": dataframe["cb_person_cred_hist_length"],
            "default_history": dataframe["cb_person_default_on_file"],
        }
    )

    return financial_history_dataset


def create_loan_application_dataset(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create the loan application dataset.

    Parameters
    ----------
    dataframe:
        Original credit risk dataframe.

    Returns
    -------
    pd.DataFrame
        Loan application dataset.
    """

    loan_application_dataset = pd.DataFrame(
        {
            "application_id": _generate_application_ids(len(dataframe)),
            "customer_id": _generate_customer_ids(len(dataframe)),
            "loan_amount": dataframe["loan_amnt"],
            "loan_intent": dataframe["loan_intent"],
            "loan_grade": dataframe["loan_grade"],
            "loan_interest_rate": dataframe["loan_int_rate"],
            "loan_percent_income": dataframe["loan_percent_income"],
            "loan_status": dataframe["loan_status"],
        }
    )

    return loan_application_dataset


def preprocess_credit_risk_dataset() -> dict[str, Path]:
    """
    Transform the original dataset into processed datasets.

    Returns
    -------
    dict[str, Path]
        Paths of generated processed datasets.

    Raises
    ------
    RuntimeError
        If preprocessing fails.
    """

    logger.info("Starting dataset preprocessing.")

    try:
        dataframe = pd.read_csv(DOWNLOADED_DATASET_PATH)

        customer_dataset = create_customer_dataset(dataframe)

        financial_history_dataset = create_financial_history_dataset(dataframe)

        loan_application_dataset = create_loan_application_dataset(dataframe)

        CUSTOMER_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        FINANCIAL_HISTORY_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        LOAN_APPLICATION_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        customer_dataset.to_csv(
            CUSTOMER_DATASET_PATH,
            index=False,
        )

        financial_history_dataset.to_csv(
            FINANCIAL_HISTORY_DATASET_PATH,
            index=False,
        )

        loan_application_dataset.to_csv(
            LOAN_APPLICATION_DATASET_PATH,
            index=False,
        )

        logger.info("Dataset preprocessing completed successfully.")

        return {
            "customer": CUSTOMER_DATASET_PATH,
            "financial_history": FINANCIAL_HISTORY_DATASET_PATH,
            "loan_application": LOAN_APPLICATION_DATASET_PATH,
        }

    except Exception as exc:
        logger.exception("Dataset preprocessing failed.")
        raise RuntimeError("Unable to preprocess credit risk dataset.") from exc

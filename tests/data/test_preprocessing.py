"""
Module:
    test_preprocessing.py

Path:
    tests/data/test_preprocessing.py

Purpose:
    Validate dataset preprocessing functions.

Description:
    Tests the transformation of the raw credit risk dataset into
    customer, financial history, and loan application datasets.
"""

import pandas as pd
import pytest

from mlops_engineering_roadmap.data.preprocessing import (
    create_customer_dataset,
    create_financial_history_dataset,
    create_loan_application_dataset,
)


@pytest.fixture
def sample_credit_risk_dataset() -> pd.DataFrame:
    """
    Create a small sample credit risk dataset for testing.

    Returns
    -------
    pd.DataFrame
        Sample credit risk dataset.
    """

    return pd.DataFrame(
        {
            "person_age": [22, 25],
            "person_income": [59000, 9600],
            "person_home_ownership": ["RENT", "OWN"],
            "person_emp_length": [5.0, 1.0],
            "cb_person_cred_hist_length": [3, 2],
            "cb_person_default_on_file": ["Y", "N"],
            "loan_amnt": [35000, 5500],
            "loan_intent": ["PERSONAL", "MEDICAL"],
            "loan_grade": ["D", "C"],
            "loan_int_rate": [16.02, 12.87],
            "loan_percent_income": [0.59, 0.57],
            "loan_status": [1, 0],
        }
    )


def test_create_customer_dataset(
    sample_credit_risk_dataset: pd.DataFrame,
) -> None:
    """
    Verify customer dataset creation.
    """

    customer_dataset = create_customer_dataset(sample_credit_risk_dataset)

    assert isinstance(customer_dataset, pd.DataFrame)

    assert list(customer_dataset.columns) == [
        "customer_id",
        "age",
        "income",
        "home_ownership",
        "employment_length",
    ]

    assert customer_dataset["customer_id"].iloc[0] == "C000001"


def test_create_financial_history_dataset(
    sample_credit_risk_dataset: pd.DataFrame,
) -> None:
    """
    Verify financial history dataset creation.
    """

    financial_history_dataset = create_financial_history_dataset(sample_credit_risk_dataset)

    assert isinstance(financial_history_dataset, pd.DataFrame)

    assert "customer_id" in financial_history_dataset.columns

    assert financial_history_dataset["credit_history_length"].iloc[0] == 3


def test_create_loan_application_dataset(
    sample_credit_risk_dataset: pd.DataFrame,
) -> None:
    """
    Verify loan application dataset creation.
    """

    loan_application_dataset = create_loan_application_dataset(sample_credit_risk_dataset)

    assert isinstance(
        loan_application_dataset,
        pd.DataFrame,
    )

    assert "application_id" in loan_application_dataset.columns

    assert loan_application_dataset["application_id"].iloc[0] == "A000001"

    assert loan_application_dataset["loan_status"].iloc[0] == 1

"""
Module:
    test_versioning.py

Path:
    tests/utils/test_versioning.py

Purpose:
    Validate dataset versioning utilities.

Description:
    Tests the creation, persistence, and loading of dataset metadata
    required for reproducibility and lineage tracking.
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

from mlops_engineering_roadmap.utils.versioning import (
    create_dataset_metadata,
    load_dataset_metadata,
    save_dataset_metadata,
)

# =============================================================================
# Tests
# =============================================================================


def test_create_dataset_metadata() -> None:
    """
    Verify dataset metadata creation.
    """

    metadata = create_dataset_metadata(
        dataset_name="credit_risk_dataset",
        version="v1.0.0",
        source_file="credit_risk_dataset.csv",
        pipeline="preprocessing.py",
    )

    assert metadata["dataset_name"] == "credit_risk_dataset"
    assert metadata["version"] == "v1.0.0"
    assert metadata["source_file"] == "credit_risk_dataset.csv"
    assert metadata["pipeline"] == "preprocessing.py"
    assert "created_at" in metadata


def test_save_dataset_metadata(tmp_path: Path) -> None:
    """
    Verify dataset metadata is saved as YAML.
    """

    metadata = create_dataset_metadata(
        dataset_name="credit_risk_dataset",
        version="v1.0.0",
        source_file="credit_risk_dataset.csv",
        pipeline="preprocessing.py",
    )

    output_path = tmp_path / "dataset_versions.yaml"

    save_dataset_metadata(
        metadata=metadata,
        output_path=output_path,
    )

    assert output_path.exists()


def test_load_dataset_metadata(tmp_path: Path) -> None:
    """
    Verify dataset metadata can be loaded from YAML.
    """

    metadata = create_dataset_metadata(
        dataset_name="credit_risk_dataset",
        version="v1.0.0",
        source_file="credit_risk_dataset.csv",
        pipeline="preprocessing.py",
    )

    output_path = tmp_path / "dataset_versions.yaml"

    save_dataset_metadata(
        metadata=metadata,
        output_path=output_path,
    )

    loaded_metadata = load_dataset_metadata(
        input_path=output_path,
    )

    assert loaded_metadata["dataset_name"] == "credit_risk_dataset"
    assert loaded_metadata["version"] == "v1.0.0"

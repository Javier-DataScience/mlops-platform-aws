"""
Module:
    versioning.py

Path:
    src/mlops_engineering_roadmap/utils/versioning.py

Purpose:
    Manage dataset version metadata.

Description:
    Provides utilities to create, save, and load dataset version
    information to support reproducibility and data lineage.
"""

# =============================================================================
# Imports
# =============================================================================

from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from mlops_engineering_roadmap.utils.logger import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Metadata Creation
# =============================================================================


def create_dataset_metadata(
    dataset_name: str,
    version: str,
    source_file: str,
    pipeline: str,
) -> dict[str, Any]:
    """
    Create dataset version metadata.

    Args:
        dataset_name:
            Name of the dataset.

        version:
            Dataset version identifier.

        source_file:
            Original dataset source.

        pipeline:
            Transformation pipeline used.

    Returns:
        Dataset metadata dictionary.
    """

    return {
        "dataset_name": dataset_name,
        "version": version,
        "source_file": source_file,
        "pipeline": pipeline,
        "created_at": datetime.now().isoformat(),
    }


# =============================================================================
# Metadata Persistence
# =============================================================================


def save_dataset_metadata(
    metadata: dict[str, Any],
    output_path: Path,
) -> None:
    """
    Save dataset metadata as YAML.

    Args:
        metadata:
            Dataset metadata.

        output_path:
            YAML output location.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        mode="w",
        encoding="utf-8",
    ) as file:
        yaml.safe_dump(
            metadata,
            file,
            sort_keys=False,
        )

    logger.info(
        "Dataset metadata saved: %s",
        output_path,
    )


def load_dataset_metadata(
    input_path: Path,
) -> dict[str, Any]:
    """
    Load dataset metadata from YAML.

    Args:
        input_path:
            YAML metadata location.

    Returns:
        Dataset metadata dictionary.
    """

    with input_path.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        metadata: dict[str, Any] = yaml.safe_load(file)

    return metadata

"""
Module:
    logger.py

Path:
    src/mlops_engineering_roadmap/utils/logger.py

Purpose:
    Provide a centralized logging configuration for the project.

Description:
    Configures and returns application loggers with a consistent format.
    All modules in the project should obtain their logger through this
    module instead of creating their own logging configuration.
"""

# =============================================================================
# Imports
# =============================================================================

import logging

# =============================================================================
# Public Functions
# =============================================================================


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name : str
        Name of the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.setLevel(logging.INFO)

        logger.propagate = False

    return logger

"""
OpenVisionX Logger.
"""

from __future__ import annotations

import logging
from pathlib import Path


_LOGGER_NAME = "OpenVisionX"


def configure_logger(
    log_file: str | None = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Configure OpenVisionX logger.

    Parameters
    ----------
    log_file
        Optional log file path.
    level
        Logging level.
    """

    logger = logging.getLogger(_LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(console)

    if log_file:

        path = Path(log_file)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_handler = logging.FileHandler(
            path,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Return a child logger.
    """

    root = configure_logger()

    if name:

        return root.getChild(name)

    return root
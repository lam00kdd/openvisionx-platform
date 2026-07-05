"""
OpenVisionX Logging Framework.
"""

from __future__ import annotations

import logging
from pathlib import Path

_LOGGER_NAME = "OpenVisionX"


def configure_logger(
    *,
    level: int = logging.INFO,
    log_file: str | None = None,
) -> logging.Logger:
    """
    Configure the OpenVisionX root logger.

    Calling this function multiple times is safe.
    """

    logger = logging.getLogger(_LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:

        path = Path(log_file)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_handler = logging.FileHandler(
            filename=path,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Return an OpenVisionX logger.
    """

    root = configure_logger()

    if name:

        return root.getChild(name)

    return root
"""
OpenVisionX Logging Framework.
"""

from __future__ import annotations

import logging

_LOGGER_NAME = "OpenVisionX"


def configure_logger(
    *,
    level: int = logging.INFO,
    log_file: str | None = None,
) -> logging.Logger:

    logger = logging.getLogger(_LOGGER_NAME)

    # Luôn cập nhật level
    logger.setLevel(level)
    logger.propagate = False

    # Nếu đã cấu hình handler thì không thêm lại
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        ...
    
    return logger

def get_logger(name: str | None = None) -> logging.Logger:
    """
    Return an OpenVisionX logger.
    """

    root = configure_logger()

    if name:

        return root.getChild(name)

    return root

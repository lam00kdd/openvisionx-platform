"""
OpenVisionX Constants.
"""

from enum import StrEnum

class ContextKey(StrEnum):
    IMAGE = "image"
    GRAY = "gray"
    BINARY = "binary"
    ROI = "roi"
    BLOBS = "blobs"
    RESULT = "result"


class Platform:
    """Platform constants."""

    NAME = "OpenVisionX"

    VERSION = "0.1.0-alpha"
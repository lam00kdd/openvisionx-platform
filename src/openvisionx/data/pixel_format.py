"""
Pixel format definitions.
"""

from enum import StrEnum


class PixelFormat(StrEnum):
    """Supported pixel formats."""

    UNKNOWN = "UNKNOWN"

    GRAY = "GRAY"

    BGR = "BGR"

    RGB = "RGB"

    BGRA = "BGRA"

    RGBA = "RGBA"
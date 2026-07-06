"""
Vision exceptions.
"""


class VisionError(Exception):
    """Base class for vision exceptions."""


class ImageReadError(VisionError):
    """Raised when an image cannot be read."""


class ImageWriteError(VisionError):
    """Raised when an image cannot be written."""
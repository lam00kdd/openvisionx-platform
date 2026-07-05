"""
Data exceptions.
"""


class DataError(Exception):
    """Base data exception."""


class InvalidImageError(DataError):
    """Invalid image."""
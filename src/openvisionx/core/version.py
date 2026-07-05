"""
OpenVisionX Platform Version.

This module defines the current platform version.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """Represents a semantic version."""

    major: int
    minor: int
    patch: int
    stage: str = "alpha"

    def __str__(self) -> str:
        """Return version string."""
        return f"{self.major}.{self.minor}.{self.patch}-{self.stage}"


CURRENT_VERSION = Version(
    major=0,
    minor=1,
    patch=0,
    stage="alpha",
)
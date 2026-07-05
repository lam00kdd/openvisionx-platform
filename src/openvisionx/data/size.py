"""
Size data model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Size:
    """
    Represents image size.
    """

    width: int = 0
    height: int = 0

    @property
    def area(self) -> int:
        return self.width * self.height

    def to_tuple(self) -> tuple[int, int]:
        return (self.width, self.height)
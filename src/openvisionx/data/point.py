"""
Point data model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    """
    Represents a 2D point.
    """

    x: int = 0
    y: int = 0

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
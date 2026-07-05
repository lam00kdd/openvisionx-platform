"""
Rectangle data model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .point import Point
from .size import Size


@dataclass(slots=True)
class Rectangle:
    """
    Represents a rectangle.
    """

    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0

    @property
    def left(self) -> int:
        return self.x

    @property
    def top(self) -> int:
        return self.y

    @property
    def right(self) -> int:
        return self.x + self.width

    @property
    def bottom(self) -> int:
        return self.y + self.height

    @property
    def area(self) -> int:
        return self.width * self.height

    @property
    def origin(self) -> Point:
        return Point(self.x, self.y)

    @property
    def size(self) -> Size:
        return Size(self.width, self.height)

    def to_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.x,
            self.y,
            self.width,
            self.height,
        )

    def contains(self, point: Point) -> bool:
        return (
            self.left <= point.x < self.right
            and self.top <= point.y < self.bottom
        )
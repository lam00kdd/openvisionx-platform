"""
Rectangle.
"""

from dataclasses import dataclass

from .point import Point2D
from .size import Size2D


@dataclass(slots=True)
class Rectangle:

    x: float

    y: float

    width: float

    height: float

    @property
    def left(self):
        return self.x

    @property
    def top(self):
        return self.y

    @property
    def right(self):
        return self.x + self.width

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def center(self):

        return Point2D(
            self.x + self.width / 2,
            self.y + self.height / 2,
        )

    @property
    def size(self):

        return Size2D(
            self.width,
            self.height,
        )

    @property
    def area(self):

        return self.width * self.height
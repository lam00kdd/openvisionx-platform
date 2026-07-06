from dataclasses import dataclass

from .point import Point2D


@dataclass(slots=True)
class Circle:

    center: Point2D

    radius: float
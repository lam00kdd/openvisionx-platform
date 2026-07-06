from dataclasses import dataclass

from .point import Point2D


@dataclass(slots=True)
class Line2D:

    start: Point2D

    end: Point2D
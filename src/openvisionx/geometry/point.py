"""
2D Point.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Point2D:

    x: float

    y: float
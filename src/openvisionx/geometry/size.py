"""
2D Size.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Size2D:

    width: float

    height: float
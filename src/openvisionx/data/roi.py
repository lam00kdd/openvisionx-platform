"""
Region Of Interest (ROI) data model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4

from .rectangle import Rectangle


@dataclass(slots=True)
class ROI(Rectangle):
    """
    Represents a Region Of Interest.
    """

    name: str = "ROI"

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    enabled: bool = True

    rotation: float = 0.0

    description: str = ""

    @property
    def center(self) -> tuple[float, float]:
        return (
            self.x + self.width / 2,
            self.y + self.height / 2,
        )

    def copy(self) -> "ROI":
        return ROI(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            name=self.name,
            enabled=self.enabled,
            rotation=self.rotation,
            description=self.description,
        )
"""
Base ROI.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from openvisionx.geometry.rectangle import Rectangle


class BaseROI(ABC):
    """
    Base class of all ROI.
    """

    @abstractmethod
    def bounding_rect(self) -> Rectangle:
        """
        Return bounding rectangle.
        """
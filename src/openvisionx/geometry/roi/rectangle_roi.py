from dataclasses import dataclass

from openvisionx.geometry.rectangle import Rectangle

from .base_roi import BaseROI


@dataclass(slots=True)
class RectangleROI(BaseROI):

    rectangle: Rectangle

    def bounding_rect(self) -> Rectangle:

        return self.rectangle
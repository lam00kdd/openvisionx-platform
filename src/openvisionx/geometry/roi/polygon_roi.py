from dataclasses import dataclass

from openvisionx.geometry.point import Point2D

from .base_roi import BaseROI


@dataclass(slots=True)
class PolygonROI(BaseROI):

    points: list[Point2D]

    def bounding_rect(self):

        raise NotImplementedError
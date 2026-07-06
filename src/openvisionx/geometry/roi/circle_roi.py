from dataclasses import dataclass

from openvisionx.geometry.circle import Circle

from .base_roi import BaseROI


@dataclass(slots=True)
class CircleROI(BaseROI):

    circle: Circle

    def bounding_rect(self):

        raise NotImplementedError
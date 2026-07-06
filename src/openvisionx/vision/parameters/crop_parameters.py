from dataclasses import dataclass

from openvisionx.geometry import Rectangle

from openvisionx.params import (
    BaseParameters,
    ObjectField,
)


@dataclass(slots=True)
class CropParameters(BaseParameters):

    rectangle: Rectangle = ObjectField(
        default_factory=lambda: Rectangle(
            0,
            0,
            100,
            100,
        ),
        display_name="Rectangle",
    )
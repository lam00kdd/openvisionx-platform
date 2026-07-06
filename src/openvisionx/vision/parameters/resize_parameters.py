from dataclasses import dataclass

from openvisionx.params import (
    BaseParameters,
    BoolField,
    IntField,
)


@dataclass(slots=True)
class ResizeParameters(BaseParameters):

    width: int = IntField(
        default=640,
        minimum=1,
        display_name="Width",
    )

    height: int = IntField(
        default=480,
        minimum=1,
        display_name="Height",
    )

    keep_aspect: bool = BoolField(
        default=False,
        display_name="Keep Aspect",
    )

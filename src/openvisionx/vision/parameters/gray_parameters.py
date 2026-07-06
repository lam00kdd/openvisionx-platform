from dataclasses import dataclass

from openvisionx.params import (
    BaseParameters,
    BoolField,
)


@dataclass(slots=True)
class GrayParameters(BaseParameters):

    keep_alpha: bool = BoolField(
        default=False,
        display_name="Keep Alpha",
    )
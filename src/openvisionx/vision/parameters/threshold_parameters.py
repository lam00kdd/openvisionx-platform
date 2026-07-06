from dataclasses import dataclass

from openvisionx.params import (
    BaseParameters,
    EditorType,
    IntField,
)


@dataclass(slots=True)
class ThresholdParameters(BaseParameters):

    threshold: int = IntField(
        default=128,
        display_name="Threshold",
        minimum=0,
        maximum=255,
        editor=EditorType.SLIDER,
    )

    max_value: int = IntField(
        default=255,
        display_name="Max Value",
        minimum=0,
        maximum=255,
    )
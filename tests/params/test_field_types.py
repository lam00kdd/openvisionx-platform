from dataclasses import dataclass
from dataclasses import fields

from openvisionx.params import (
    BaseParameters,
    BoolField,
    IntField,
)


@dataclass
class DemoParameters(BaseParameters):

    threshold: int = IntField(
        default=128,
        minimum=0,
        maximum=255,
    )

    enabled: bool = BoolField(
        default=True,
    )


def test_int_field_metadata():

    f = fields(DemoParameters)[0]

    info = f.metadata["ovx"]

    assert info.minimum == 0
    assert info.maximum == 255


def test_bool_field_default():

    p = DemoParameters()

    assert p.enabled is True
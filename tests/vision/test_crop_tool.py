import numpy as np

from openvisionx.data import Image
from openvisionx.geometry import Rectangle
from openvisionx.vision import CropTool


def test_crop():

    img = Image(
        np.zeros(
            (100, 200),
            dtype=np.uint8,
        )
    )

    tool = CropTool()

    tool.parameters.rectangle = Rectangle(
        20,
        10,
        50,
        40,
    )

    result = tool.process(img)

    assert result.width == 50

    assert result.height == 40
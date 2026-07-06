import numpy as np

from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext

from openvisionx.data import Image
from openvisionx.data import PixelFormat

from openvisionx.vision import GrayTool


def test_gray_tool():

    ctx = ExecutionContext()

    img = Image(
        np.zeros(
            (
                100,
                200,
                3,
            ),
            dtype=np.uint8,
        ),
        PixelFormat.BGR,
    )

    ctx.set_input(
        ContextKey.IMAGE,
        img,
    )

    GrayTool().run(ctx)

    result = ctx.get_output(
        ContextKey.IMAGE,
    )

    assert result.channels == 1

    assert result.pixel_format == PixelFormat.GRAY
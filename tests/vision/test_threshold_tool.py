import numpy as np

from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext

from openvisionx.data import Image
from openvisionx.data import PixelFormat

from openvisionx.vision import ThresholdTool


def test_threshold():

    img = Image(
        np.random.randint(
            0,
            255,
            (100, 200),
            dtype=np.uint8,
        ),
        PixelFormat.GRAY,
    )

    ctx = ExecutionContext()

    ctx.set_input(
        ContextKey.IMAGE,
        img,
    )

    ThresholdTool().run(ctx)

    result = ctx.get_output(
        ContextKey.IMAGE,
    )

    assert result.channels == 1
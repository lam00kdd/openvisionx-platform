import numpy as np

from openvisionx.core.execution_context import ExecutionContext

from openvisionx.data import Image

from openvisionx.vision import BaseVisionTool


class DummyVisionTool(BaseVisionTool):

    def process(
        self,
        image: Image,
    ) -> Image:

        return image.clone()


def test_execute():

    ctx = ExecutionContext()

    ctx.set_input(
        "image",
        Image(
            np.zeros(
                (
                    100,
                    100,
                    3,
                ),
                dtype=np.uint8,
            )
        ),
    )

    tool = DummyVisionTool()

    tool.run(
        ctx,
    )

    result = ctx.get_output(
        "image",
    )

    assert isinstance(
        result,
        Image,
    )
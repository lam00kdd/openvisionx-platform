import numpy as np

from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext
from openvisionx.data import Image
from openvisionx.vision import ResizeTool


def test_resize_tool():
    """
    Test the ResizeTool using an ExecutionContext.
    """
    # 1. Setup
    context = ExecutionContext()

    img = Image(
        np.zeros(
            (100, 200, 3),
            dtype=np.uint8,
        )
    )

    context.set_input(ContextKey.IMAGE, img)

    # 2. Create and run the tool
    tool = ResizeTool(name="resize_tool",enabled=True)
        
    tool.run(context)

    # 3. Get the result and assert
    result = context.get_output(ContextKey.IMAGE)

    assert result.width == 50
    assert result.height == 25
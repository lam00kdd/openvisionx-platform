from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext

from openvisionx.engine import Pipeline

from openvisionx.vision import (
    GrayTool,
    ImageIO,
    ThresholdTool,
)

ctx = ExecutionContext()

image = ImageIO.read(
    "examples/images/pcb/pcb_001.png",
)

ctx.set_input(
    ContextKey.IMAGE,
    image,
)

pipeline = (
    Pipeline(name="Threshold Demo")
    .add(GrayTool())
    .add(
        ThresholdTool(
            threshold=120,
        )
    )
)

pipeline.run(ctx)

result = ctx.get_output(
    ContextKey.IMAGE,
)

ImageIO.save(
    result,
    "examples/results/binary.png",
)
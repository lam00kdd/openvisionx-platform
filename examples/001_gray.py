from openvisionx.core.execution_context import ExecutionContext
from openvisionx.core.constants import ContextKey

from openvisionx.engine import Pipeline

from openvisionx.vision import GrayTool
from openvisionx.vision import ImageIO


ctx = ExecutionContext()

image = ImageIO.read(
    "examples/images/pcb/pcb_001.jpg",
)

ctx.set_input(
    ContextKey.IMAGE,
    image,
)

pipeline = (
    Pipeline(
        name="Gray Demo",
    )
    .add(
        GrayTool(),
    )
)

pipeline.run(ctx)

gray = ctx.get_output(
    ContextKey.IMAGE,
)

ok = ImageIO.save(
    gray,
    "examples/results/gray.png",
)

print(ok)
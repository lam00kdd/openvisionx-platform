from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext
from openvisionx.core.logger import get_logger
from openvisionx.engine import Pipeline
from openvisionx.vision import (
    GrayTool,
    ImageIO,
    ResizeTool,
)

logger = get_logger(__name__)

logger.info("Starting resize example...")

# 1. Setup context and load image

context = ExecutionContext()

image = ImageIO.read(
    "examples/images/lena.png",
)

context.set_input(
    ContextKey.IMAGE,
    image,
)

# 2. Create and configure the pipeline

pipeline = Pipeline(name="Resize Demo")
pipeline.add(GrayTool())
pipeline.add(
    ResizeTool(name="AAA", enabled=True)
)

logger.info(f"Running pipeline: {pipeline.name}")

# 3. Run the pipeline

pipeline.run(
    context,
)

# 4. Get the result and save it

result = context.get_output(ContextKey.IMAGE)

ImageIO.save(
    result,
    "examples/results/resize.png",
)

logger.info("Pipeline finished. Result saved to examples/results/resize.png")
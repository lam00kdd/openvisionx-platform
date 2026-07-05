from openvisionx.core.base_tool import BaseTool
from openvisionx.core.execution_context import ExecutionContext
from openvisionx.engine.pipeline import Pipeline
from openvisionx.engine.pipeline_status import PipelineStatus


class DummyTool(BaseTool):

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:

        context.set_output(
            "value",
            123,
        )


def test_pipeline_run():

    pipeline = Pipeline(
        name="Demo",
    )

    pipeline.add(
        DummyTool(),
    )

    context = ExecutionContext()

    result = pipeline.run(
        context,
    )

    assert result.status == PipelineStatus.SUCCESS

    assert context.get_output("value") == 123


def test_pipeline_count():

    pipeline = Pipeline()

    pipeline.add(DummyTool())

    pipeline.add(
        DummyTool(
            name="Gray",
        )
    )

    assert pipeline.count == 2


def test_pipeline_contains():

    pipeline = Pipeline()

    pipeline.add(DummyTool())

    assert pipeline.contains("DummyTool")


def test_pipeline_remove():

    pipeline = Pipeline()

    tool = DummyTool()

    pipeline.add(tool)

    pipeline.remove(tool)

    assert pipeline.count == 0


def test_pipeline_clear():

    pipeline = Pipeline()

    pipeline.add(DummyTool())

    pipeline.add(
        DummyTool(
            name="Gray",
        )
    )

    pipeline.clear()

    assert pipeline.count == 0


def test_pipeline_iter():

    pipeline = Pipeline()

    pipeline.add(DummyTool())

    pipeline.add(
        DummyTool(
            name="Gray",
        )
    )

    total = 0

    for _ in pipeline:
        total += 1

    assert total == 2


def test_pipeline_getitem():

    pipeline = Pipeline()

    tool = DummyTool()

    pipeline.add(tool)

    assert pipeline[0] is tool


def test_pipeline_disabled():

    pipeline = Pipeline()

    pipeline.enabled = False

    result = pipeline.run(
        ExecutionContext(),
    )

    assert result.status == PipelineStatus.CANCELLED
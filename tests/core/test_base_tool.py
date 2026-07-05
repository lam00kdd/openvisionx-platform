from openvisionx.core.base_tool import BaseTool
from openvisionx.core.execution_context import ExecutionContext


class DummyTool(BaseTool):

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:

        context.set_output(
            "result",
            123,
        )


def test_tool_execute() -> None:

    tool = DummyTool()

    ctx = ExecutionContext()

    tool.run(ctx)

    assert ctx.get_output("result") == 123


def test_tool_name() -> None:

    tool = DummyTool()

    assert tool.name == "DummyTool"


def test_disable_tool() -> None:

    tool = DummyTool()

    tool.enabled = False

    ctx = ExecutionContext()

    tool.run(ctx)

    assert ctx.outputs == {}
from openvisionx.core.base_tool import BaseTool
from openvisionx.core.execution_context import ExecutionContext
from openvisionx.engine.tool_collection import ToolCollection


class DummyTool(BaseTool):

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        pass


def test_add_tool():

    tools = ToolCollection()

    tools.add(DummyTool())

    assert len(tools) == 1


def test_find_tool():

    tools = ToolCollection()

    tool = DummyTool()

    tools.add(tool)

    assert tools.find("DummyTool") is tool


def test_contains():

    tools = ToolCollection()

    tools.add(DummyTool())

    assert tools.contains("DummyTool")


def test_remove():

    tools = ToolCollection()

    tool = DummyTool()

    tools.add(tool)

    tools.remove(tool)

    assert len(tools) == 0


def test_clear():

    tools = ToolCollection()
    assert len(tools) == 0

    tools.add(DummyTool())
    assert len(tools) == 1

    tools.add(DummyTool())
    assert len(tools) == 2

    tools.clear()

    assert len(tools) == 0
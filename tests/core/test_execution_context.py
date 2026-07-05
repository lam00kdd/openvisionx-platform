from openvisionx.core.constants import ContextKey
from openvisionx.core.execution_context import ExecutionContext


def test_input() -> None:

    ctx = ExecutionContext()

    ctx.set_input(ContextKey.IMAGE, "PCB")

    assert ctx.has_input(ContextKey.IMAGE)

    assert ctx.get_input(ContextKey.IMAGE) == "PCB"


def test_output() -> None:

    ctx = ExecutionContext()

    ctx.set_output(ContextKey.GRAY, "GRAY")

    assert ctx.has_output(ContextKey.GRAY)

    assert ctx.get_output(ContextKey.GRAY) == "GRAY"


def test_parameter() -> None:

    ctx = ExecutionContext()

    ctx.set_parameter("threshold", 128)

    assert ctx.get_parameter("threshold") == 128


def test_shared() -> None:

    ctx = ExecutionContext()

    logger = object()

    ctx.set_shared("logger", logger)

    assert ctx.get_shared("logger") is logger


def test_reset() -> None:

    ctx = ExecutionContext()

    ctx.set_input(ContextKey.IMAGE, 1)

    ctx.set_output(ContextKey.GRAY, 2)

    ctx.set_parameter("threshold", 100)

    ctx.reset()

    assert ctx.inputs == {}

    assert ctx.outputs == {}

    assert ctx.parameters == {}
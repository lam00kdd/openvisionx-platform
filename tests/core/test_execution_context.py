from openvisionx.core.execution_context import ExecutionContext


def test_input() -> None:

    ctx = ExecutionContext()

    ctx.set_input("image", "PCB")

    assert ctx.get_input("image") == "PCB"


def test_output() -> None:

    ctx = ExecutionContext()

    ctx.set_output("gray", "GRAY_IMAGE")

    assert ctx.get_output("gray") == "GRAY_IMAGE"


def test_parameter() -> None:

    ctx = ExecutionContext()

    ctx.set_parameter("threshold", 128)

    assert ctx.get_parameter("threshold") == 128


def test_shared() -> None:

    ctx = ExecutionContext()

    logger = object()

    ctx.set_shared("logger", logger)

    assert ctx.get_shared("logger") is logger


def test_clear_outputs() -> None:

    ctx = ExecutionContext()

    ctx.set_output("gray", 123)

    ctx.clear_outputs()

    assert ctx.outputs == {}
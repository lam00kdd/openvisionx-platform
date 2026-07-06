from openvisionx.vision import (
    GrayTool,
    ToolRegistry,
)


def test_registry_contains():

    assert ToolRegistry.contains("GrayTool")

    assert ToolRegistry.contains("ThresholdTool")

    assert ToolRegistry.contains("CropTool")


def test_registry_create():

    tool = ToolRegistry.create(
        "GrayTool",
    )

    assert isinstance(
        tool,
        GrayTool,
    )


def test_registry_names():

    names = ToolRegistry.names()

    assert "GrayTool" in names

    assert "ThresholdTool" in names

    assert "CropTool" in names

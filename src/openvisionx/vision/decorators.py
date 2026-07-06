"""
Vision decorators.
"""

from __future__ import annotations

from typing import Type

from openvisionx.core.base_tool import BaseTool

from .tool_registry import ToolRegistry


def register_tool(
    cls: Type[BaseTool],
) -> Type[BaseTool]:

    return ToolRegistry.register(cls)
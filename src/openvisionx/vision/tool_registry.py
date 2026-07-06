"""
Vision Tool Registry.
"""

from __future__ import annotations

from collections.abc import ItemsView
from typing import Type

from openvisionx.core.base_tool import BaseTool


class ToolRegistry:
    """
    Global registry of all vision tools.
    """

    _tools: dict[str, Type[BaseTool]] = {}

    @classmethod
    def register(
        cls,
        tool_cls: Type[BaseTool],
    ) -> Type[BaseTool]:

        name = tool_cls.__name__

        if name in cls._tools:
            raise ValueError(
                f"Tool '{name}' already registered."
            )

        cls._tools[name] = tool_cls

        return tool_cls

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseTool:

        return cls._tools[name]()

    @classmethod
    def contains(
        cls,
        name: str,
    ) -> bool:

        return name in cls._tools

    @classmethod
    def names(
        cls,
    ) -> list[str]:

        return sorted(cls._tools.keys())

    @classmethod
    def items(
        cls,
    ) -> ItemsView[str, Type[BaseTool]]:

        return cls._tools.items()

    @classmethod
    def clear(
        cls,
    ) -> None:

        cls._tools.clear()
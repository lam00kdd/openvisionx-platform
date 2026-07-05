"""
Tool Collection.
"""

from __future__ import annotations

from collections.abc import Iterator

from openvisionx.core.base_tool import BaseTool


class ToolCollection:
    """
    Collection of tools inside a pipeline.
    """

    def __init__(self) -> None:
        self._tools: list[BaseTool] = []

    def __len__(self) -> int:
        return len(self._tools)

    def __iter__(self) -> Iterator[BaseTool]:
        return iter(self._tools)

    def add(self, tool: BaseTool) -> None:
        """
        Add a tool.
        """
        self._tools.append(tool)

    def remove(self, tool: BaseTool) -> None:
        """
        Remove a tool.
        """
        self._tools.remove(tool)

    def clear(self) -> None:
        """
        Remove all tools.
        """
        self._tools.clear()

    def get(self, index: int) -> BaseTool:
        """
        Get tool by index.
        """
        return self._tools[index]

    def find(self, name: str) -> BaseTool | None:
        """
        Find tool by name.
        """
        for tool in self._tools:
            if tool.name == name:
                return tool

        return None

    def contains(self, name: str) -> bool:
        """
        Check whether a tool exists.
        """
        return self.find(name) is not None

    def index_of(self, name: str) -> int:
        """
        Return index of tool.
        """
        tool = self.find(name)

        if tool is None:
            raise ValueError(f"Tool '{name}' not found.")

        return self._tools.index(tool)
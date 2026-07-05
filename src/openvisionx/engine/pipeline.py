"""
Pipeline implementation.
"""

from __future__ import annotations

from collections.abc import Iterator
from time import perf_counter

from openvisionx.core.base_tool import BaseTool
from openvisionx.core.execution_context import ExecutionContext
from openvisionx.core.logger import get_logger
from openvisionx.core.metadata import Metadata

from .pipeline_result import PipelineResult
from .pipeline_status import PipelineStatus
from .tool_collection import ToolCollection


class Pipeline:
    """
    Execute a sequence of tools.
    """

    def __init__(
        self,
        *,
        name: str = "Pipeline",
    ) ->None:

        self.metadata = Metadata(
            name=name,
        )

        self.tools = ToolCollection()

        self.logger = get_logger(name)

        self.enabled = True

    @property
    def name(self) -> str:
        return self.metadata.name

    @property
    def count(self) -> int:
        """
        Number of tools.
        """
        return len(self.tools)

    def __len__(self) -> int:
        return len(self.tools)

    def __iter__(self) -> Iterator[BaseTool]:
        return iter(self.tools)

    def __getitem__(
        self,
        index: int,
    ) -> BaseTool:
        return self.tools.get(index)

    def contains(
        self,
        name: str,
    ) -> bool:
        return self.tools.contains(name)

    def add(
        self,
        tool: BaseTool,
    ) -> "Pipeline":
        """
        Add tool.
        """

        self.tools.add(tool)

        return self

    def remove(
        self,
        tool: BaseTool,
    ) -> "Pipeline":
        """
        Remove tool.
        """

        self.tools.remove(tool)

        return self

    def clear(self) -> "Pipeline":
        """
        Remove all tools.
        """

        self.tools.clear()

        return self

    def run(
        self,
        context: ExecutionContext,
    ) -> PipelineResult:

        result = PipelineResult()

        if not self.enabled:

            result.status = PipelineStatus.CANCELLED
            result.message = "Pipeline disabled."

            return result

        self.logger.info("Pipeline started.")

        started = perf_counter()

        try:

            result.status = PipelineStatus.RUNNING

            for tool in self.tools:
                tool.run(context)

            result.status = PipelineStatus.SUCCESS

        except Exception as ex:

            self.logger.exception(ex)

            result.status = PipelineStatus.FAILED

            result.message = str(ex)

        finally:

            result.elapsed_ms = (
                perf_counter() - started
            ) * 1000

            self.logger.info(
                "Pipeline finished in %.2f ms",
                result.elapsed_ms,
            )

        return result
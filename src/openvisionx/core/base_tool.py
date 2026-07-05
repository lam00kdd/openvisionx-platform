"""
Base Tool for OpenVisionX.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from openvisionx.core.execution_context import ExecutionContext
from openvisionx.core.logger import get_logger
from openvisionx.core.metadata import Metadata


class BaseTool(ABC):
    """
    Base class of all OpenVisionX tools.
    """

    def __init__(
        self,
        name: str | None = None,
        enabled: bool = True,
    ) -> None:

        self.metadata = Metadata()

        if name:
            self.metadata.name = name
        else:
            self.metadata.name = self.__class__.__name__

        self.enabled = enabled

        self.logger = get_logger(self.metadata.name)

    @property
    def name(self) -> str:
        """
        Tool display name.
        """
        return self.metadata.name

    def run(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Execute tool if enabled.
        """

        if not self.enabled:
            self.logger.debug("Tool disabled.")
            return

        self.logger.info("Start")

        self.execute(context)

        self.logger.info("Finish")

    @abstractmethod
    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Tool implementation.
        """
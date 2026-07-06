"""
Base class for all vision tools.
"""

from __future__ import annotations

from abc import abstractmethod

from openvisionx.core.base_tool import BaseTool
from openvisionx.core.execution_context import ExecutionContext

from openvisionx.data import Image


class BaseVisionTool(BaseTool):
    """
    Base class for all image processing tools.
    """

    def __init__(
        self,
        *,
        name: str | None = None,
        enabled: bool = True,
        input_key: str = "image",
        output_key: str = "image",
    ) -> None:

        super().__init__(
            name=name,
            enabled=enabled,
        )

        self.input_key = input_key

        self.output_key = output_key

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:

        image = context.get_input(
            self.input_key,
        )

        if not isinstance(
            image,
            Image,
        ):
            raise TypeError(
                f"'{self.input_key}' must be an Image."
            )

        result = self.process(
            image,
        )

        if not isinstance(
            result,
            Image,
        ):
            raise TypeError(
                "process() must return Image."
            )

        context.set_output(
            self.output_key,
            result,
        )

    @abstractmethod
    def process(
        self,
        image: Image,
    ) -> Image:
        """
        Process an image.
        """

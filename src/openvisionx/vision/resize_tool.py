from __future__ import annotations

from openvisionx.data import Image
from openvisionx.vision.backend import get_backend

from .base_vision_tool import BaseVisionTool
from .decorators import register_tool
from .parameters.resize_parameters import ResizeParameters


@register_tool
class ResizeTool(BaseVisionTool):

    def __init__(
        self,
        *,
        name: str | None = None,
        enabled: bool = True,
        width: int = 50,
        height: int = 25,
        keep_aspect: bool = False,
        input_key: str = "image",
        output_key: str = "image",
    ) -> None:

        super().__init__(
            name=name or "ResizeTool",
            enabled=enabled,
            input_key=input_key,
            output_key=output_key,
        )

        self.parameters = ResizeParameters(
            width=width,
            height=height,
            keep_aspect=keep_aspect,
        )

    def process(
        self,
        image: Image,
    ) -> Image:

        return get_backend().resize(
            image,
            self.parameters.width,
            self.parameters.height,
        )

"""
Gray Tool.
"""

from __future__ import annotations

from openvisionx.data import Image
from openvisionx.vision.backend import get_backend

from .base_vision_tool import BaseVisionTool
from .decorators import register_tool

@register_tool
class GrayTool(BaseVisionTool):
    """
    Convert image to grayscale.
    """
    def __init__(self):
        super().__init__(
            name="GrayTool",
        )

    def process(
        self,
        image: Image,
    ) -> Image:

        return get_backend().gray(image)
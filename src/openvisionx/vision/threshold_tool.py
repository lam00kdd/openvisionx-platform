"""
Threshold Tool.
"""

from __future__ import annotations

from openvisionx.core.constants import ContextKey

from openvisionx.data import Image

from openvisionx.vision.backend import get_backend
from openvisionx.vision.parameters.threshold_parameters import ThresholdParameters
from .base_vision_tool import BaseVisionTool
from .decorators import register_tool

@register_tool
class ThresholdTool(BaseVisionTool):
    """
    Binary Threshold Tool.
    """

    def __init__(
        self,
        *,
        threshold: float = 128,
        max_value: float = 255,
        input_key: ContextKey = ContextKey.IMAGE,
        output_key: ContextKey = ContextKey.IMAGE,
    ) -> None:

        super().__init__(
            name="ThresholdTool",
            input_key=input_key,
            output_key=output_key,
        )
        self.parameters = ThresholdParameters()

    def process(
        self,
        image: Image,
    ) -> Image:

        return get_backend().threshold(
            image,
            self.parameters.threshold,
            self.parameters.max_value,
        )
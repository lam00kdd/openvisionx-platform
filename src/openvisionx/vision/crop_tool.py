from openvisionx.vision.backend import get_backend
from openvisionx.vision.base_vision_tool import BaseVisionTool
from openvisionx.vision.parameters.crop_parameters import CropParameters
from .decorators import register_tool

@register_tool
class CropTool(BaseVisionTool):

    def __init__(self):
        super().__init__(
            name="CropTool",
        )

        self.parameters = CropParameters()

    def process(
        self,
        image,
    ):
        return get_backend().crop(
            image,
            self.parameters.rectangle,
        )
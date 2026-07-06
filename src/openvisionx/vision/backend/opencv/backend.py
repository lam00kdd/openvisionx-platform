"""
OpenCV backend.
"""

from __future__ import annotations

from openvisionx.data import Image
from openvisionx.geometry.rectangle import Rectangle

from ..base_backend import VisionBackend

from .color import gray
from .geometry import crop
from .geometry import resize as resize_op
from .threshold import threshold as threshold_op

class OpenCVBackend(VisionBackend):

    def crop(
        self,
        image: Image,
        rectangle: Rectangle,
    ) -> Image:

        return crop(
            image,
            rectangle,
        )

    def gray(
        self,
        image: Image,
    ) -> Image:

        return gray(image)

    def threshold(
        self,
        image: Image,
        threshold: float,
        max_value: float,
    ) -> Image:

        return threshold_op(
            image,
            threshold,
            max_value,
        )

    def resize(
        self,
        image: Image,
        width: int,
        height: int,
    ) -> Image:

        return resize_op(
            image,
            width,
            height,
        )

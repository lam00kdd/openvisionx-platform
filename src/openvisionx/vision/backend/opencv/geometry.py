"""
OpenCV geometry operations.
"""

from __future__ import annotations

import cv2

from openvisionx.data import Image
from openvisionx.geometry import Rectangle


def crop(
    image: Image,
    rectangle: Rectangle,
) -> Image:
    """
    Crop image by rectangle.
    """

    x = int(rectangle.x)
    y = int(rectangle.y)
    w = int(rectangle.width)
    h = int(rectangle.height)

    roi = image.mat[
        y:y + h,
        x:x + w,
    ]

    return Image(
        mat=roi.copy(),
        pixel_format=image.pixel_format,
    )

def resize(
    image: Image,
    width: int,
    height: int,
) -> Image:

    dst = cv2.resize(
        image.mat,
        (width, height),
        interpolation=cv2.INTER_LINEAR,
    )

    return Image(
        mat=dst,
        pixel_format=image.pixel_format,
    )

"""
OpenCV threshold operations.
"""

from __future__ import annotations

import cv2

from openvisionx.data import Image
from openvisionx.data import PixelFormat


def binary_threshold(
    image: Image,
    threshold: float = 128,
    max_value: float = 255,
) -> Image:
    """
    Binary threshold.
    """

    _, binary = cv2.threshold(
        image.mat,
        threshold,
        max_value,
        cv2.THRESH_BINARY,
    )

    return Image(
        mat=binary,
        pixel_format=PixelFormat.GRAY,
    )

def threshold(
    image: Image,
    threshold: float = 128,
    max_value: float = 255,
) -> Image:
    """
    Binary threshold.
    """

    _, binary = cv2.threshold(
        image.mat,
        threshold,
        max_value,
        cv2.THRESH_BINARY,
    )

    return Image(
        mat=binary,
        pixel_format=PixelFormat.GRAY,
    )
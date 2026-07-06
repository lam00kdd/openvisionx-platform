"""
OpenCV color operations.
"""

from __future__ import annotations

import cv2

from openvisionx.data import Image
from openvisionx.data import PixelFormat


def to_gray(
    image: Image,
) -> Image:
    """
    Convert Image to grayscale.
    """

    if image.channels == 1:
        return image.clone()

    gray = cv2.cvtColor(
        image.mat,
        cv2.COLOR_BGR2GRAY,
    )

    return Image(
        mat=gray,
        pixel_format=PixelFormat.GRAY,
    )

def gray(
    image: Image,
) -> Image:
    """
    Convert Image to grayscale.
    """

    if image.channels == 1:
        return image.clone()

    gray = cv2.cvtColor(
        image.mat,
        cv2.COLOR_BGR2GRAY,
    )

    return Image(
        mat=gray,
        pixel_format=PixelFormat.GRAY,
    )
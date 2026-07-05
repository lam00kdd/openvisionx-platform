"""
Image I/O utilities.
"""

from __future__ import annotations

from pathlib import Path

import cv2

from openvisionx.data import Image
from openvisionx.data import PixelFormat


class ImageIO:
    """
    Image read/write utilities.
    """

    @staticmethod
    def read(path: str | Path) -> Image:
        """
        Read an image from disk.
        """
        mat = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)

        if mat is None:
            raise FileNotFoundError(f"Cannot read image: {path}")

        if mat.ndim == 2:
            fmt = PixelFormat.GRAY
        elif mat.ndim == 3:
            channels = mat.shape[2]
            if channels == 3:
                fmt = PixelFormat.BGR
            elif channels == 4:
                fmt = PixelFormat.BGRA
            else:
                fmt = PixelFormat.UNKNOWN
        else:
            fmt = PixelFormat.UNKNOWN

        return Image(
            mat=mat,
            pixel_format=fmt,
        )

    @staticmethod
    def write(
        image: Image,
        path: str | Path,
    ) -> bool:
        """
        Save an image to disk.
        """
        return cv2.imwrite(
            str(path),
            image.mat,
        )
"""
Image I/O utilities.
"""

from __future__ import annotations

from pathlib import Path

import cv2

from openvisionx.data import Image
from openvisionx.data import PixelFormat

from .exceptions import ImageReadError
from .exceptions import ImageWriteError


class ImageIO:
    """
    Image read/write utilities.
    """

    @staticmethod
    def read(
        path: str | Path,
    ) -> Image:
        """
        Read an image from disk.
        """
        path = Path(path)

        if not path.exists():
            raise ImageReadError(
                f"Image file does not exist:\n{path.resolve()}"
            )

        mat = cv2.imread(
            str(path),
            cv2.IMREAD_UNCHANGED,
        )

        if mat is None:
            raise ImageReadError(
                f"Cannot read image:\n{path.resolve()}"
            )

        if mat.ndim == 2:
            pixel_format = PixelFormat.GRAY

        elif mat.ndim == 3:

            channels = mat.shape[2]

            if channels == 3:
                pixel_format = PixelFormat.BGR

            elif channels == 4:
                pixel_format = PixelFormat.BGRA

            else:
                pixel_format = PixelFormat.UNKNOWN

        else:
            pixel_format = PixelFormat.UNKNOWN

        return Image(
            mat=mat,
            pixel_format=pixel_format,
        )

    @staticmethod
    def save(
        image: Image,
        path: str | Path,
    ) -> None:
        """
        Save image to disk.

        Raises
        ------
        ImageWriteError
            If saving fails.
        """

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        ok = cv2.imwrite(
            str(path),
            image.mat,
        )

        if not ok:
            raise ImageWriteError(
                f"Cannot write image:\n{path.resolve()}"
            )
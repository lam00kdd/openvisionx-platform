"""
Image data model.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .pixel_format import PixelFormat


@dataclass(slots=True)
class Image:
    """
    Image wrapper.
    """

    mat: np.ndarray

    pixel_format: PixelFormat = PixelFormat.UNKNOWN

    @property
    def width(self) -> int:
        return int(self.mat.shape[1])

    @property
    def height(self) -> int:
        return int(self.mat.shape[0])

    @property
    def channels(self) -> int:

        if self.mat.ndim == 2:
            return 1

        return int(self.mat.shape[2])

    @property
    def shape(self):

        return self.mat.shape

    @property
    def size(self):

        return (
            self.width,
            self.height,
        )

    @property
    def empty(self) -> bool:

        return self.mat.size == 0

    def clone(self) -> "Image":

        return Image(
            self.mat.copy(),
            self.pixel_format,
        )

    copy = clone

    def numpy(self) -> np.ndarray:

        return self.mat

    def __array__(self):

        return self.mat
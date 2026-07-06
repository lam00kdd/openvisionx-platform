"""
Vision backend interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from openvisionx.data import Image
from openvisionx.geometry import Rectangle


class VisionBackend(ABC):

    @abstractmethod
    def crop(
        self,
        image: Image,
        rectangle: Rectangle,
    ) -> Image:
        ...

    @abstractmethod
    def gray(
        self,
        image: Image,
    ) -> Image:
        ...

    @abstractmethod
    def threshold(
        self,
        image: Image,
        threshold: int,
        max_value: int,
    ) -> Image:
        ...

    @abstractmethod
    def resize(
        self,
        image: Image,
        width: int,
        height: int,
    ) -> Image:
        ...
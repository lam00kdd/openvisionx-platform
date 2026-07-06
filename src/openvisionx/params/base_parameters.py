"""
Base parameter model.
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass


@dataclass(slots=True)
class BaseParameters:
    """
    Base class of all parameter models.
    """

    def to_dict(self) -> dict:

        return asdict(self)

    def copy(self):

        return self.__class__(
            **self.to_dict(),
        )
    
    def keys(self):

        return self.to_dict().keys()

    def values(self):

        return self.to_dict().values()

    def items(self):

        return self.to_dict().items()

    def get(
        self,
        name,
        default=None,
    ):

        return self.to_dict().get(
            name,
            default,
        )
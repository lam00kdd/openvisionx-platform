"""
OpenVisionX dataclass field helper.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import MISSING
from dataclasses import field
from typing import Any

from .constants import OVX_FIELD_METADATA
from .editor_type import EditorType
from .field_info import FieldInfo


def ovx_field(
    *,
    default: Any = MISSING,
    default_factory: Callable[[], Any] | Any = MISSING,
    display_name: str | None = None,
    description: str = "",
    category: str = "General",
    unit: str = "",
    minimum=None,
    maximum=None,
    step=None,
    decimals=None,
    visible=True,
    readonly=False,
    editor: EditorType = EditorType.AUTO,
):
    """
    Create an OpenVisionX parameter field.
    """

    info = FieldInfo(
        display_name=display_name,
        description=description,
        category=category,
        unit=unit,
        minimum=minimum,
        maximum=maximum,
        step=step,
        decimals=decimals,
        visible=visible,
        readonly=readonly,
        editor=editor,
    )

    if default is not MISSING:
        return field(
            default=default,
            metadata={
                OVX_FIELD_METADATA: info,
            },
        )

    if default_factory is not MISSING:
        return field(
            default_factory=default_factory,
            metadata={
                OVX_FIELD_METADATA: info,
            },
        )

    raise ValueError(
        "Either default or default_factory must be provided."
    )
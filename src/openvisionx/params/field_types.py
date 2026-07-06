"""
Strong typed parameter fields.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any

from .editor_type import EditorType
from .ovx_field import ovx_field


def _typed_field(
    *,
    default: Any,
    display_name: str |None = None,
    description: str = "",
    category: str = "General",
    minimum: Any = None,
    maximum: Any = None,
    step: Any = None,
    decimals: int | None = None,
    unit: str = "",
    visible: bool = True,
    readonly: bool = False,
    editor: EditorType = EditorType.AUTO,
):

    return ovx_field(
        default=default,
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


def IntField(
    default: int = 0,
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.SPINBOX,
    )

    kwargs.setdefault(
        "step",
        1,
    )

    return _typed_field(
        default=default,
        **kwargs,
    )


def FloatField(
    default: float = 0.0,
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.DOUBLE_SPINBOX,
    )

    kwargs.setdefault(
        "step",
        0.1,
    )

    kwargs.setdefault(
        "decimals",
        2,
    )

    return _typed_field(
        default=default,
        **kwargs,
    )


def BoolField(
    default: bool = False,
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.CHECKBOX,
    )

    return _typed_field(
        default=default,
        **kwargs,
    )


def StringField(
    default: str = "",
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.TEXTBOX,
    )

    return _typed_field(
        default=default,
        **kwargs,
    )


def PathField(
    default: str | Path = "",
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.FILE,
    )

    return _typed_field(
        default=str(default),
        **kwargs,
    )


def EnumField(
    default: Enum,
    **kwargs,
):

    kwargs.setdefault(
        "editor",
        EditorType.COMBOBOX,
    )

    return _typed_field(
        default=default,
        **kwargs,
    )

def ObjectField(
    *,
    default=None,
    default_factory=None,
    **kwargs,
):

    if default_factory is not None:

        return ovx_field(
            default_factory=default_factory,
            **kwargs,
        )

    return ovx_field(
        default=default,
        **kwargs,
    )
"""
Field metadata.
"""

from __future__ import annotations

from dataclasses import dataclass

from .editor_type import EditorType


@dataclass(slots=True, frozen=True)
class FieldInfo:
    """
    Metadata of a parameter field.
    """

    display_name: str | None = None

    description: str = ""

    category: str = "General"

    unit: str = ""

    minimum: float | None = None

    maximum: float | None = None

    step: float | None = None

    decimals: int | None = None

    visible: bool = True

    readonly: bool = False

    editor: EditorType = EditorType.AUTO
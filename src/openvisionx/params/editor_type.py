"""
Parameter editor types.
"""

from enum import StrEnum


class EditorType(StrEnum):
    """
    Supported editors for OpenVisionX Studio.
    """

    AUTO = "auto"

    CHECKBOX = "checkbox"

    SPINBOX = "spinbox"

    DOUBLE_SPINBOX = "double_spinbox"

    SLIDER = "slider"

    COMBOBOX = "combobox"

    TEXTBOX = "textbox"

    FILE = "file"

    DIRECTORY = "directory"

    COLOR = "color"

    ROI = "roi"
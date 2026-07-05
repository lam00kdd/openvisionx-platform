"""
OpenVisionX Core.
"""

from .version import CURRENT_VERSION, Version
from .constants import ContextKey
from .exceptions import (
    AIError,
    DeviceError,
    OVXError,
    PipelineError,
    ToolError,
    VisionError,
)

__all__ = [
    "Version",
    "CURRENT_VERSION",
    "ContextKey",
    "OVXError",
    "ToolError",
    "PipelineError",
    "VisionError",
    "DeviceError",
    "AIError",
]


from .logger import (
    configure_logger,
    get_logger,
)

__all__ += [
    "configure_logger",
    "get_logger",
]
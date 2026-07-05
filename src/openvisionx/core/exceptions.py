"""
OpenVisionX Exception Hierarchy.
"""


class OVXError(Exception):
    """Base exception for OpenVisionX."""


class ToolError(OVXError):
    """Raised when a Tool fails."""


class PipelineError(OVXError):
    """Raised when Pipeline execution fails."""


class VisionError(OVXError):
    """Raised for image processing errors."""


class DeviceError(OVXError):
    """Raised for device errors."""


class AIError(OVXError):
    """Raised for AI inference errors."""
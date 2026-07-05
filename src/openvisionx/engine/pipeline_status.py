"""
Pipeline execution status.
"""

from enum import StrEnum


class PipelineStatus(StrEnum):
    """Pipeline execution status."""

    IDLE = "idle"

    RUNNING = "running"

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"
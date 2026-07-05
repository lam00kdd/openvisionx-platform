"""
Pipeline Result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter

from openvisionx.engine.pipeline_status import PipelineStatus


@dataclass(slots=True)
class PipelineResult:
    """
    Pipeline execution result.
    """

    status: PipelineStatus = PipelineStatus.IDLE

    elapsed_ms: float = 0.0

    message: str = ""

    started_at: float = field(default_factory=perf_counter)
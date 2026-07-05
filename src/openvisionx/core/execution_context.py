"""
Execution Context.

Every Tool communicates through this context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from openvisionx.core.metadata import Metadata


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared execution context.
    """

    metadata: Metadata = field(default_factory=Metadata)

    inputs: dict[str, Any] = field(default_factory=dict)

    outputs: dict[str, Any] = field(default_factory=dict)

    shared: dict[str, Any] = field(default_factory=dict)

    parameters: dict[str, Any] = field(default_factory=dict)

    # -------------------------
    # Input
    # -------------------------

    def set_input(self, key: str, value: Any) -> None:
        self.inputs[key] = value

    def get_input(self, key: str) -> Any:
        return self.inputs.get(key)

    # -------------------------
    # Output
    # -------------------------

    def set_output(self, key: str, value: Any) -> None:
        self.outputs[key] = value

    def get_output(self, key: str) -> Any:
        return self.outputs.get(key)

    # -------------------------
    # Shared
    # -------------------------

    def set_shared(self, key: str, value: Any) -> None:
        self.shared[key] = value

    def get_shared(self, key: str) -> Any:
        return self.shared.get(key)

    # -------------------------
    # Parameters
    # -------------------------

    def set_parameter(self, key: str, value: Any) -> None:
        self.parameters[key] = value

    def get_parameter(self, key: str) -> Any:
        return self.parameters.get(key)

    # -------------------------

    def clear_outputs(self) -> None:
        """
        Remove all outputs.
        """
        self.outputs.clear()
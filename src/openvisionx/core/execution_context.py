"""
Execution Context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from openvisionx.core.constants import ContextKey
from openvisionx.core.metadata import Metadata


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared execution context for all Tools.
    """

    metadata: Metadata = field(default_factory=Metadata)

    inputs: dict[str, Any] = field(default_factory=dict)

    outputs: dict[str, Any] = field(default_factory=dict)

    shared: dict[str, Any] = field(default_factory=dict)

    parameters: dict[str, Any] = field(default_factory=dict)

    # ---------- Input ----------

    def set_input(self, key: ContextKey | str, value: Any) -> None:
        self.inputs[str(key)] = value

    def get_input(
        self,
        key: ContextKey | str,
        default: Any = None,
    ) -> Any:
        return self.inputs.get(str(key), default)

    def has_input(self, key: ContextKey | str) -> bool:
        return str(key) in self.inputs

    # ---------- Output ----------

    def set_output(self, key: ContextKey | str, value: Any) -> None:
        self.outputs[str(key)] = value

    def get_output(
        self,
        key: ContextKey | str,
        default: Any = None,
    ) -> Any:
        return self.outputs.get(str(key), default)

    def has_output(self, key: ContextKey | str) -> bool:
        return str(key) in self.outputs

    # ---------- Shared ----------

    def set_shared(self, key: str, value: Any) -> None:
        self.shared[key] = value

    def get_shared(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        return self.shared.get(key, default)

    # ---------- Parameters ----------

    def set_parameter(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.parameters[key] = value

    def get_parameter(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        return self.parameters.get(key, default)

    # ---------- Utility ----------

    def clear_outputs(self) -> None:
        """Clear all outputs."""
        self.outputs.clear()

    def reset(self) -> None:
        """Reset execution context."""
        self.inputs.clear()
        self.outputs.clear()
        self.parameters.clear()

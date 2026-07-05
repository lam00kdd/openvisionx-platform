"""
OpenVisionX Metadata.

This module defines the metadata object shared across the platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(slots=True)
class Metadata:
    """
    Common metadata for OpenVisionX objects.

    Attributes
    ----------
    id
        Unique identifier.
    name
        Human readable name.
    description
        Description of the object.
    author
        Object creator.
    tags
        User defined tags.
    created_at
        Creation timestamp.
    updated_at
        Last modified timestamp.
    """

    id: UUID = field(default_factory=uuid4)

    name: str = ""

    description: str = ""

    author: str = ""

    tags: list[str] = field(default_factory=list)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def touch(self) -> None:
        """
        Update modification time.
        """
        self.updated_at = datetime.now(UTC)

    def add_tag(self, tag: str) -> None:
        """
        Add a tag if it does not already exist.
        """
        if tag not in self.tags:
            self.tags.append(tag)
            self.touch()

    def remove_tag(self, tag: str) -> None:
        """
        Remove a tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)
            self.touch()
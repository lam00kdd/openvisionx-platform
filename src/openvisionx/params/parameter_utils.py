"""
Parameter reflection utilities.
"""

from __future__ import annotations

from dataclasses import fields

from .constants import OVX_FIELD_METADATA
from .field_info import FieldInfo


def iter_parameter_fields(parameters):

    for field in fields(parameters):

        info: FieldInfo = field.metadata.get(
            OVX_FIELD_METADATA,
            FieldInfo(),
        )

        yield field, info

def get_field_info(
    parameters,
    name: str,
) -> FieldInfo:

    for field, info in iter_parameter_fields(parameters):

        if field.name == name:
            return info

    raise KeyError(name)

def to_property_grid(parameters):

    properties = []

    for field, info in iter_parameter_fields(parameters):

        properties.append(
            {
                "name": field.name,
                "value": getattr(
                    parameters,
                    field.name,
                ),
                "type": field.type,
                "info": info,
            }
        )

    return properties
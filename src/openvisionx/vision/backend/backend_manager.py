"""
Backend manager.
"""

from __future__ import annotations

from .opencv.backend import OpenCVBackend

_backend = OpenCVBackend()


def get_backend():

    return _backend


def set_backend(backend):

    global _backend

    _backend = backend
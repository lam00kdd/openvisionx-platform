import pytest

from openvisionx.core.exceptions import OVXError


def test_exception() -> None:

    with pytest.raises(OVXError):
        raise OVXError("Test")
from openvisionx.core.version import CURRENT_VERSION


def test_version() -> None:
    assert str(CURRENT_VERSION) == "0.1.0-alpha"
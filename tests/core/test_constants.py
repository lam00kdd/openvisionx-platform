from openvisionx.core.constants import ContextKey


def test_context_key() -> None:
    assert ContextKey.IMAGE == "image"
from openvisionx.core.metadata import Metadata


def test_metadata_default() -> None:

    meta = Metadata()

    assert meta.name == ""
    assert meta.description == ""
    assert meta.author == ""
    assert meta.tags == []


def test_add_tag() -> None:

    meta = Metadata()

    meta.add_tag("AOI")

    assert "AOI" in meta.tags


def test_remove_tag() -> None:

    meta = Metadata()

    meta.add_tag("OCR")

    meta.remove_tag("OCR")

    assert meta.tags == []
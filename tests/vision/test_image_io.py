from pathlib import Path

import numpy as np

from openvisionx.data import Image
from openvisionx.vision.exceptions import ImageReadError
from openvisionx.vision.image_io import ImageIO


def test_write_image(tmp_path: Path):

    img = Image(
        np.zeros(
            (100, 100, 3),
            dtype=np.uint8,
        )
    )

    file = tmp_path / "test.png"

    ImageIO.save(
        img,
        file,
    )

    assert file.exists()


def test_read_not_found():
    import pytest
    with pytest.raises(ImageReadError):
        ImageIO.read("not_found.png")

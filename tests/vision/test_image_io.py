from pathlib import Path

import numpy as np

from openvisionx.data import Image
from openvisionx.vision.image_io import ImageIO


def test_write_image(tmp_path: Path):

    img = Image(
        np.zeros(
            (100, 100, 3),
            dtype=np.uint8,
        )
    )

    file = tmp_path / "test.png"

    ok = ImageIO.write(
        img,
        file,
    )

    assert ok
    assert file.exists()


def test_read_not_found():

    import pytest

    with pytest.raises(FileNotFoundError):

        ImageIO.read(
            "not_found.png",
        )
import numpy as np

from openvisionx.data import Image
from openvisionx.data import PixelFormat


def test_image_size():

    img = Image(
        np.zeros(
            (
                100,
                200,
                3,
            ),
            dtype=np.uint8,
        ),
        PixelFormat.BGR,
    )

    assert img.width == 200

    assert img.height == 100

    assert img.channels == 3


def test_image_clone():

    img = Image(
        np.zeros(
            (
                10,
                20,
                3,
            ),
            dtype=np.uint8,
        )
    )

    clone = img.clone()

    assert clone is not img

    assert clone.shape == img.shape


def test_image_numpy():

    mat = np.zeros(
        (
            5,
            6,
            3,
        ),
        dtype=np.uint8,
    )

    img = Image(mat)

    assert img.numpy() is mat
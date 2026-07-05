from openvisionx.data import PixelFormat


def test_pixel_format():

    assert PixelFormat.GRAY == "GRAY"

    assert PixelFormat.BGR == "BGR"
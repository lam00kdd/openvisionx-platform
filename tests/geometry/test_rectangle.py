from openvisionx.geometry import Rectangle


def test_rectangle_area():

    rect = Rectangle(
        10,
        20,
        100,
        50,
    )

    assert rect.area == 5000


def test_rectangle_center():

    rect = Rectangle(
        0,
        0,
        100,
        60,
    )

    assert rect.center.x == 50

    assert rect.center.y == 30
from openvisionx.data import ROI


def test_roi_default():

    roi = ROI()

    assert roi.name == "ROI"

    assert roi.enabled is True


def test_roi_area():

    roi = ROI(
        width=20,
        height=10,
    )

    assert roi.area == 200


def test_roi_center():

    roi = ROI(
        x=10,
        y=20,
        width=40,
        height=20,
    )

    assert roi.center == (30.0, 30.0)


def test_roi_copy():

    roi = ROI(
        x=5,
        y=6,
        width=100,
        height=50,
        name="IC",
    )

    clone = roi.copy()

    assert clone is not roi

    assert clone.to_tuple() == roi.to_tuple()

    assert clone.name == "IC"

    assert clone.id != roi.id
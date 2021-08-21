from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.getLatLong() == (14.7167, 17.4677)

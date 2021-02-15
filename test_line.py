import pytest


@pytest.mark.parametrize("x1, x2, y1, y2, expected", [
    (-1, 1, 3, -2, -2.5),
    (3, 5, 0, 0, 0),
    (2, 4, 1, 2, 0.5),
    (6.5, 2.5, 0, -12, 3),
    (1, 2, 2.5, 2, -0.5)
])
def test_calc_slope(x1, x2, y1, y2, expected):
    from line import calc_slope
    res = calc_slope(x1, x2, y1, y2)
    assert (res == expected)


@pytest.mark.parametrize("x1, y1, slope, expected", [
    (-1, 3, -2.5, 0.5),
    (3, 0, 0, 0),
    (2, 1, 0.5, 0),
    (2.5, -12, 3, -19.5),
    (1, 2.5, -0.5, 3)
])
def test_calc_delta(x1, y1, slope, expected):
    from line import calc_delta
    res = calc_delta(x1, y1, slope)
    assert (res == expected)
    

@pytest.mark.parametrize("t1, t2, x, expec_y", [
    ((1,1), (4,4), 3, 3),
    ((0,2), (3,8), 5, 12),
    ((1,-1), (2,-3), 0, 1),
    ((0,0), (5,0), 3, 0),
    ((1.5,3.5), (3,6.5), 2.5, 5.5)
])
def test_calc_y(t1, t2, x, expec_y):
    from line import calc_y
    y = calc_y(t1,t2,x)
    assert (y == expec_y)

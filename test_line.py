import pytest


@pytest.mark.parametrize("t1, t2, x, expec_y", [
    ((1,1), (4,4), 3, 3),
    ((0,2), (3,8), 5, 12),
    ((1,-1), (2,-3), 0, 1),
    ((0,0), (5,0), 3, 0)
])
def test_calc_y(t1, t2, x, expec_y):
    from line import calc_y
    y = calc_y(t1,t2,x)
    assert (y == expec_y)

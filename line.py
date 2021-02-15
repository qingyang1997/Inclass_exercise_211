def calc_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


def calc_delta(x1, y1, slope):
    delta = y1 - slope * x1
    return delta


def calc_y(t1, t2, x):
    x1 = t1[0]
    y1 = t1[1]
    x2 = t2[0]
    y2 = t2[1]
    # x1 cannot be equal to x2 or the returned value could be any value
    if (x1 == x2):
        return -1
    if (y1 == y2):
        return y1
    slope = calc_slope(x1,x2,y1,y2)
    delta = calc_delta(x1, y1, slope)
    y = slope * x + delta
    return y

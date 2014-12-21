def composite_series():
    linear_series = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    periodic_series = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    n = len(periodic_series)
    return [linear_series[i] + periodic_series[i] for i in xrange(n)]

def composite_test_series():
    linear_series = [9, 10, 11, 12, 13, 14, 15, 16, 17]
    periodic_series = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    n = len(periodic_series)
    return [linear_series[i] + periodic_series[i] for i in xrange(n)]

def equalish(a, b):
    assert round(a, 1) == round(b, 1)

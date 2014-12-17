from nose.tools import *

from fourier_requests.models import CompositeModel, LinearModel, FourierModel

def equalish(a, b):
    assert round(a, 1) == round(b, 1)

def test_composite_model():
    linear_series = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    periodic_series = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    historic_data = [linear_series[i] + periodic_series[i] for i in xrange(len(linear_series))]

    model = CompositeModel(historic_data, 11)

    equalish(model.predict_at_time(2), 4)
    equalish(model.predict_at_time(4), 8)
    equalish(model.predict_at_time(6), 8)

def test_composite_model_new_predictions():
    linear_series = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    periodic_series = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    historic_data = [linear_series[i] + periodic_series[i] for i in xrange(len(linear_series))]

    model = CompositeModel(historic_data, 11)

    equalish(model.predict_at_time(11), 13)
    equalish(model.predict_at_time(13), 17)
    equalish(model.predict_at_time(15), 17)

def test_linear_model():
    historic_data = [1, 2, 3, 4, 5]
    model = LinearModel(historic_data)

    equalish(model.predict_at_time(5), 6)
    equalish(model.predict_at_time(6), 7)

def test_fourier_model():
    historic_data = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    model = FourierModel(historic_data, 11)

    equalish(model.predict_at_time(4), 5)
    equalish(model.predict_at_time(5), 6)

def test_fourier_model_remembers_period_length():
    historic_data = [1, 2, 3]
    model = FourierModel(historic_data, 1)

    assert model.period_length == 3

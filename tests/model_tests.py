from nose.tools import *

from fourier_requests import Model

def test_model():
    historic_data = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    model = Model(historic_data)

    assert model.predict_at_time(5) == 6

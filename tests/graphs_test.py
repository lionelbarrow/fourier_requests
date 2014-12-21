from nose.tools import *

from fourier_requests.models import CompositeModel
from fourier_requests.graphs import ValidationGraph

from tests.test_helper import composite_series, composite_test_series

def test_graph_predictions():
    historic_data = composite_series()
    n = len(historic_data)
    
    model = CompositeModel(historic_data, 4)
    new_data = composite_test_series()

    graph = ValidationGraph(model, new_data)
    graph.show()

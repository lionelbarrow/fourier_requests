import numpy as np
import scipy.fftpack as fftpack
import scipy.stats as stats

class CompositeModel(object):
    def __init__(self, historic_data, num_components):
        self.linear_model = LinearModel(historic_data)
        adjusted_series = self._remove_linear_component(historic_data)
        self.fourier_model = FourierModel(adjusted_series, num_components)

    def predict_at_time(self, true_time):
        time_in_period = self._adjust_time_to_period(true_time)
        return self.fourier_model.predict_at_time(time_in_period) + \
            self.linear_model.predict_at_time(true_time)

    def _adjust_time_to_period(self, time):
        period_length = self.fourier_model.period_length
        return time % period_length

    def _remove_linear_component(self, time_series):
        return [
            time_series[i] - self.linear_model.predict_at_time(i)
            for i in range(len(time_series))
        ]


class LinearModel(object):
    def __init__(self, historic_data):
        time_series = np.array(historic_data)
        x_values = np.array(range(len(historic_data)))
        self.slope, self.intercept, _, _, _ = stats.linregress(x_values, time_series)

    def predict_at_time(self, time):
        return (self.slope * time) + self.intercept


class FourierModel(object):
    def __init__(self, historic_data, num_components):
        self.period_length = len(historic_data)
        time_series = np.array(historic_data)
        fourier_coefficients = fftpack.rfft(time_series)
        fourier_coefficients[num_components:] = 0
        self.predicted_data = fftpack.irfft(fourier_coefficients)

    def predict_at_time(self, time):
        return self.predicted_data[time]

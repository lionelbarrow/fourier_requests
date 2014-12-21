import numpy as np
import matplotlib.pyplot as plt

class ValidationGraph(object):
    def __init__(self, model, time_series):
        self.model = model
        self.time_series = time_series
        self.start_time = len(time_series)
        self.end_time = 2 * self.start_time

    def show(self):
        x_values = range(self.start_time, self.end_time)
        predicted_values = np.array([
            self.model.predict_at_time(i) 
            for i in x_values
        ])
        actual_values = np.array(self.time_series)

        print x_values
        print predicted_values
        print len(x_values)
        print len(predicted_values)
        
        print x_values
        print actual_values
        print len(x_values)
        print len(actual_values)

        plt.plot(x_values, predicted_values, "rs", x_values, actual_values, "bs")
        plt.show()

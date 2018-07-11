from Lib.statistics import mean, harmonic_mean, median, mode, median_low, median_high, median_grouped, stdev, pstdev, \
    pvariance, variance, StatisticsError


class Statistics(object):
    """The library used to define statistical outputs"""

    def __init__(self):
        self.allTimers = []
        self.stat = 0

    def arithmetic_mean(self, collection):
        try:
            self.allTimers = collection
            self.stat = mean(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def harmonic_mean(self, collection):
        try:
            self.allTimers = collection
            self.stat = harmonic_mean(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def median(self, collection):
        try:
            self.allTimers = collection
            self.stat = median(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def median_low(self, collection):
        try:
            self.allTimers = collection
            self.stat = median_low(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def median_high(self, collection):
        try:
            self.allTimers = collection
            self.stat = median_high(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def median_grouped(self, collection):
        try:
            self.allTimers = collection
            self.stat = median_grouped(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def mode(self, collection):
        try:
            self.allTimers = collection
            self.stat = mode(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def std_dev(self, collection):
        try:
            self.allTimers = collection
            self.stat = stdev(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def variance(self, collection):
        try:
            self.allTimers = collection
            self.stat = variance(collection, xbar=None)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def population_std_dev(self, collection):
        try:
            self.allTimers = collection
            self.stat = pstdev(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

    def population_variance(self, collection):
        try:
            self.allTimers = collection
            self.stat = pvariance(collection)
        except StatisticsError:
            self.stat = 0
        return self.stat

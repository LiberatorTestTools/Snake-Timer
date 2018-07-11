import unittest

from stats.statistics import Statistics


class StatTests(unittest.TestCase):

    stats: Statistics

    def setUp(self):
        self.stats = Statistics()

    def test_mean_none(self):
        self.mean = self.stats.arithmetic_mean([])
        self.assertTrue(self.mean == 0)

    def test_mean_twin_np(self):
        self.mean = self.stats.arithmetic_mean(self.twin_unity(self))
        self.assertTrue(self.mean == 0.5)

    def test_mean_twin(self):
        self.mean = self.stats.arithmetic_mean(self.twin_mock_timer(self))
        self.assertTrue(self.mean == 4)

    def test_mean_four(self):
        self.mean = self.stats.arithmetic_mean(self.four_mock_timers(self))
        self.assertTrue(self.mean == 3.5)

    def test_mean_set(self):
        self.mean = self.stats.arithmetic_mean(self.mock_timers(self))
        self.assertTrue(self.mean == 2.4)

    def test_harmonic_mean_none(self):
        self.mean = self.stats.harmonic_mean([])
        self.assertTrue(self.mean == 0)

    def test_harmonic_mean_twin_np(self):
        self.mean = self.stats.harmonic_mean(self.twin_unity(self))
        self.assertTrue(self.mean == 0)

    def test_harmonic_mean_twin(self):
        self.mean = self.stats.harmonic_mean(self.twin_mock_timer(self))
        self.assertTrue(self.mean == 3.75)

    def test_harmonic_mean_four(self):
        self.mean = self.stats.harmonic_mean(self.four_mock_timers(self))
        self.assertTrue(self.mean == 3.116883116883117)

    def test_harmonic_mean_set(self):
        self.mean = self.stats.harmonic_mean(self.mock_timers(self))
        self.assertTrue(self.mean == 1.9672131147540983)

    def test_median_none(self):
        self.median = self.stats.median([])
        self.assertTrue(self.median == 0)

    def test_median_twin_np(self):
        self.median = self.stats.median(self.twin_unity(self))
        self.assertTrue(self.median == 0.5)

    def test_median_twin(self):
        self.median = self.stats.median(self.twin_mock_timer(self))
        self.assertTrue(self.median == 4)

    def test_median_four(self):
        self.median = self.stats.median(self.four_mock_timers(self))
        self.assertTrue(self.median == 3.5)

    def test_median_set(self):
        self.median = self.stats.median(self.mock_timers(self))
        self.assertTrue(self.median == 2.5)

    def test_low_median_none(self):
        self.median = self.stats.median_low([])
        self.assertTrue(self.median == 0)

    def test_low_median_twin_np(self):
        self.median = self.stats.median_low(self.twin_unity(self))
        self.assertTrue(self.median == -1)

    def test_low_median_twin(self):
        self.median = self.stats.median_low(self.twin_mock_timer(self))
        self.assertTrue(self.median == 3)

    def test_low_median_four(self):
        self.median = self.stats.median_low(self.four_mock_timers(self))
        self.assertTrue(self.median == 3)

    def test_low_median_set(self):
        self.median = self.stats.median_low(self.mock_timers(self))
        self.assertTrue(self.median == 2)

    def test_high_median_none(self):
        self.median = self.stats.median_high([])
        self.assertTrue(self.median == 0)

    def test_high_median_twin_np(self):
        self.median = self.stats.median_high(self.twin_unity(self))
        self.assertTrue(self.median == 2)

    def test_high_median_twin(self):
        self.median = self.stats.median_high(self.twin_mock_timer(self))
        self.assertTrue(self.median == 5)

    def test_high_median_four(self):
        self.median = self.stats.median_high(self.four_mock_timers(self))
        self.assertTrue(self.median == 4)

    def test_high_median_set(self):
        self.median = self.stats.median_high(self.mock_timers(self))
        self.assertTrue(self.median == 3)

    def test_grouped_median_none(self):
        self.median = self.stats.median_grouped([])
        self.assertTrue(self.median == 0)

    def test_grouped_median_twin_np(self):
        self.median = self.stats.median_grouped(self.twin_unity(self))
        self.assertTrue(self.median == 1.5)

    def test_grouped_median_twin(self):
        self.median = self.stats.median_grouped(self.twin_mock_timer(self))
        self.assertTrue(self.median == 4.5)

    def test_grouped_median_four(self):
        self.median = self.stats.median_grouped(self.four_mock_timers(self))
        self.assertTrue(self.median == 3.5)

    def test_grouped_median_set(self):
        self.median = self.stats.median_grouped(self.mock_timers(self))
        self.assertTrue(self.median == 2.5)

    def test_mode_none(self):
        self.mode = self.stats.mode([])
        self.assertTrue(self.mode == 0)

    def test_mode_twin_np(self):
        self.mode = self.stats.mode(self.twin_unity(self))
        self.assertTrue(self.mode == 0)

    def test_mode_twin(self):
        self.mode = self.stats.mode(self.twin_mock_timer(self))
        self.assertTrue(self.mode == 0)

    def test_mode_four(self):
        self.mode = self.stats.mode(self.four_mock_timers(self))
        self.assertTrue(self.mode == 0)

    def test_mode_set(self):
        self.mode = self.stats.mode(self.mock_timers(self))
        self.assertTrue(self.mode == 3)

    def test_std_dev_none(self):
        self.std_dev = self.stats.std_dev([])
        self.assertTrue(self.std_dev == 0)

    def test_std_dev_twin_np(self):
        self.std_dev = self.stats.std_dev(self.twin_unity(self))
        self.assertTrue(self.std_dev == 2.1213203435596424)

    def test_std_dev_twin(self):
        self.std_dev = self.stats.std_dev(self.twin_mock_timer(self))
        self.assertTrue(self.std_dev == 1.4142135623730951)

    def test_std_dev_four(self):
        self.std_dev = self.stats.std_dev(self.four_mock_timers(self))
        self.assertTrue(self.std_dev == 1.2909944487358056)

    def test_std_dev_set(self):
        self.std_dev = self.stats.std_dev(self.mock_timers(self))
        self.assertTrue(self.std_dev == 0.9660917830792959)

    def test_pop_std_dev_none(self):
        self.pop_std_dev = self.stats.population_std_dev([])
        self.assertTrue(self.pop_std_dev == 0)

    def test_pop_std_dev_twin_np(self):
        self.pop_std_dev = self.stats.population_std_dev(self.twin_unity(self))
        self.assertTrue(self.pop_std_dev == 1.5)

    def test_pop_std_dev_twin(self):
        self.pop_std_dev = self.stats.population_std_dev(self.twin_mock_timer(self))
        self.assertTrue(self.pop_std_dev == 1.0)

    def test_pop_std_dev_four(self):
        self.pop_std_dev = self.stats.population_std_dev(self.four_mock_timers(self))
        self.assertTrue(self.pop_std_dev == 1.118033988749895)

    def test_pop_std_dev_set(self):
        self.pop_std_dev = self.stats.population_std_dev(self.mock_timers(self))
        self.assertTrue(self.pop_std_dev == 0.916515138991168)

    def test_variance_none(self):
        self.variance = self.stats.variance([])
        self.assertTrue(self.variance == 0)

    def test_variance_one(self):
        self.variance = self.stats.variance([1])
        self.assertTrue(self.variance == 0)

    def test_variance_twin_np(self):
        self.variance = self.stats.variance(self.twin_unity(self))
        self.assertTrue(self.variance == 4.5)

    def test_variance_twin(self):
        self.variance = self.stats.variance(self.twin_mock_timer(self))
        self.assertTrue(self.variance == 2)

    def test_variance_four(self):
        self.variance = self.stats.variance(self.four_mock_timers(self))
        self.assertTrue(self.variance == 1.6666666666666667)

    def test_variance_set(self):
        self.variance = self.stats.variance(self.mock_timers(self))
        self.assertTrue(self.variance == 0.9333333333333333)

    def test_pop_variance_none(self):
        self.pop_variance = self.stats.population_variance([])
        self.assertTrue(self.pop_variance == 0)

    def test_pop_variance_one(self):
        self.pop_variance = self.stats.population_variance([1])
        self.assertTrue(self.pop_variance == 0)

    def test_pop_variance_twin_np(self):
        self.pop_variance = self.stats.population_variance(self.twin_unity(self))
        self.assertTrue(self.pop_variance == 2.25)

    def test_pop_variance_twin(self):
        self.pop_variance = self.stats.population_variance(self.twin_mock_timer(self))
        self.assertTrue(self.pop_variance == 1)

    def test_pop_variance_four(self):
        self.pop_variance = self.stats.population_variance(self.four_mock_timers(self))
        self.assertTrue(self.pop_variance == 1.25)

    def test_pop_variance_set(self):
        self.pop_variance = self.stats.population_variance(self.mock_timers(self))
        self.assertTrue(self.pop_variance == 0.84)

    @staticmethod
    def twin_unity(self):
        self.data = [-1, 2]
        return self.data

    @staticmethod
    def twin_mock_timer(self):
        self.data = [3, 5]
        return self.data

    @staticmethod
    def four_mock_timers(self):
        self.data = [2, 3, 4, 5]
        return self.data

    @staticmethod
    def mock_timers(self):
        self.data = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]
        return self.data

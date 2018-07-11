import time
import unittest

from timers.timer import Timer
from timers.timings import Timings


class TimingsTests(unittest.TestCase):

    def test_add_to_collection(self):
        self.timings = Timings()
        self.timings.timer_start()
        time.sleep(1)
        self.timings.timer_stop()
        self.items = len(self.timings.aggregate)
        self.assertTrue(self, self.items == 1)

    def test_add_with_pause(self):
        self.timings = Timings()
        self.timings.timer_start()
        time.sleep(1)
        self.timings.timer_pause()
        time.sleep(1)
        self.timings.timer_restart()
        time.sleep(1)
        self.timings.timer_stop()
        self.items = len(self.timings.aggregate)
        self.assertTrue(self, self.items == 1)

    def test_add_twice(self):
        self.twin_mock_timer()
        self.items = len(self.timings.aggregate)
        self.assertTrue(self, self.items == 2)

    def twin_mock_timer(self):
        self.timings = Timings()
        self.timer_a = Timer()
        self.timer_b = Timer()
        self.timer_a.duration = 3
        self.timer_b.duration = 5
        self.timings.aggregate.append(self.timer_a)
        self.timings.aggregate.append(self.timer_b)

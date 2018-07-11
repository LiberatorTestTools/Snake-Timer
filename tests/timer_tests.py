import time
import unittest

from timers.timer import Timer


class TimeTests(unittest.TestCase):

    def test_now(self):
        self.timer = Timer()
        self.assertGreaterEqual(self.timer.serial_time(), 0, "?")

    def test_timer_with_wait(self):
        self.timer = Timer()
        self.timer.start()
        time.sleep(1)
        self.timer.stop()
        self.assertGreaterEqual(self.timer.end_time, self.timer.start_time, "?")

    def test_timer_pause(self):
        self.timer = Timer()
        self.timer.start()
        time.sleep(1)
        self.timer.pause()
        time.sleep(1)
        self.timer.restart()
        time.sleep(1)
        self.timer.stop()
        self.assertGreaterEqual(self.timer.duration, 2, "?")


if __name__ == '__main__':
    unittest.main()

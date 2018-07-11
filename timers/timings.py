from timers.timer import Timer


class Timings(object):
    """A time aggregation class"""

    def __init__(self):
        self.aggregate = []
        self.timer = Timer()
        self.last_time = 0

    def timer_start(self):
        try:
            self.timer = Timer()
            self.timer.start()
        except ArithmeticError:
            self.timer.start_time = 0

    def timer_pause(self):
        try:
            self.timer.pause()
        except RuntimeError:
            pass

    def timer_restart(self):
        try:
            self.timer.restart()
        except RuntimeError:
            pass

    def timer_stop(self):
        try:
            self.last_time = self.timer.stop()
            self.aggregate.append(self.last_time)
        except ArithmeticError:
            pass

    def remove_timer(self, timer):
        try:
            self.aggregate.remove(self.aggregate[timer])
        except RuntimeError:
            pass

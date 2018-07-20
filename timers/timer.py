import datetime


class Timer(object):
    """A simple timer class"""

    def __init__(self):
        self.now = datetime.datetime.now()
        self.since = self.now
        self.days = 0
        self.secs = 0
        self.mics = 0
        self.start_time = 0
        self.end_time = 0
        self.duration = 0
        self.paused = False

    def start(self):
        """Starts the clock for a timer"""
        try:
            self.start_time = self.serial_time()
        except ArithmeticError:
            self.start_time = 0
        return self.start_time

    def stop(self):
        """Stops the clock for a timer and calculates last duration"""
        try:
            self.end_time = self.serial_time()
            self.duration = self.duration + self.end_time - self.start_time
        except ArithmeticError:
            self.end_time = 0
            self.duration = 0
        return self.duration

    def pause(self):
        """Pauses the clock and stores the duration"""
        try:
            self.duration = self.stop()
            self.paused = True
        except ArithmeticError:
            self.duration = 0
            self.paused = False
        return self.duration

    def restart(self):
        """Restarts a paused clock"""
        try:
            self.end_time = 0
            self.start_time = self.serial_time()
            self.paused = False
        except ArithmeticError:
            self.paused = True
            self.start_time = 0
            self.end_time = 0
        return self.start_time

    def serial_time(self):
        """Calculates the current datetime in microseconds from the UNIX date"""
        self.now = datetime.datetime.utcnow()
        self.since = self.now - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
        self.days = self.since.days
        self.secs = self.since.seconds
        self.mics = self.since.microseconds
        return ((self.days * 24 * 60 * 60) + self.secs * (10 ** 6)) + self.mics

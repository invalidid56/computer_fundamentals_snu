class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        while self.minutes < 0:
            self.hours -= 1
            self.minutes += 60

        self._total = hours*3600 + minutes*60 + seconds


    def __repr__(self):
        return 'Time({:d}, {:d}, {:f})'.format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        return Time(h, m, s)

    def __mul__(self, x):
        return Time(self.hours * x, self.minutes * x, self.seconds * x)

    def __rmul__(self, x):
        return self.__mul__(x)

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))

    def __lt__(self, other):
        return self._total < other.total_seconds()

    def __eq__(self, other):
        return self._total == other.total_seconds()

    def total_seconds(self):
        return self._total

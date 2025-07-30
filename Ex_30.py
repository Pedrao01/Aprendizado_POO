class ClockMachanism:
    def wind_up(self):
        print('Wind up')

    def ring_alarm(self):
        print('Ring alarm!')

class Clock:
    def __init__(self):
        self.mechanism = ClockMachanism()

    def wind_up(self):
        self.mechanism.wind_up()

    def ring_alarm(self):
        self.mechanism.ring_alarm()


c = Clock()
c.wind_up()
c.ring_alarm()

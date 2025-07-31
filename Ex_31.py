class Battery:
    def supply_power(self):
        print('supplying power')

class Flashlight:
    def __init__(self, battery=None):
        self.battery = battery

    def turn_on(self):
        if not self.battery:
            print('no battery!')
        else:
            self.battery.supply_power()

b = Battery()
f = Flashlight(battery=b)
f.turn_on()

f2 = Flashlight()
f2.turn_on()

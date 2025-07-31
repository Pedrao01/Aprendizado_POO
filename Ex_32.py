class Engine:
    def start(self):
        print('Engine started.')

class Battery:
    def provide_power(self):
        print('Battery is providing power.')

class Car:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    def start(self):
        self.battery.provide_power()
        self.engine.start()
        print('Car is running')


my_car = Car()
my_car.start()

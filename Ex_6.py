class Vehicle():
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} is starting')

class Motorcycle(Vehicle):
    def do_wheelie(self):
        print('doing a wheelie!')


vehicle1 = Motorcycle('Yamaha')
vehicle1.start()
vehicle1.do_wheelie()
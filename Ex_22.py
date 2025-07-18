class Transport:
    def __init__(self, route):
        self._route = route

    def __str__(self):
        return self._route

    def trip_info(self):
        return f'Route: {self._route} | Cost: {self.trip_cost()}'

    def trip_cost(self):
        return 'Default value: R$ 0,00'

class Bus(Transport):
    def __init__(self, route, seats, price):
        super().__init__(route)
        self.seats = seats
        self.price = price

    def trip_cost(self):
        return f'R$ {self.price:.2f}'

class Taxi(Transport):
    def __init__(self, route, distance, rate):
        super().__init__(route)
        self.distance = distance
        self.rate = rate

    def trip_cost(self):
        return f'R$ {self.distance * self.rate:.2f}'

class Bike(Transport):
    def __init__(self, route, user_owned):
        super().__init__(route)
        self.user_owned = user_owned

    def trip_cost(self):
        if self.user_owned:
            return 'Gratuito'
        else:
            return f'R$ 5,00'

routes = [
    Bus("Centro → Bairro", seats=40, price=4.50),
    Taxi("Aeroporto → Hotel", distance=10, rate=2.5),
    Bike("Parque → Universidade", user_owned=True),
    Bike("Shopping → Estação", user_owned=False)
]

for transport in routes:
    print(transport.trip_info())

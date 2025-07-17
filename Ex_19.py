class Engine:
    def __init__(self, power, type):
        self.power = power
        self.type = type

    def details(self):
        return f'Power: {self.power} | Type: {self.type}'

class Car:
    def __init__(self, mark, model, power, type):
        self.mark = mark
        self.model = model
        self.power = power
        self.type = type
        self.engine = Engine(self.power, self.type)

    def display_info(self):
        return f'Mark: {self.mark} | Model: {self.model} | {self.engine.details()}'


car1 = Car('Volkswagen', 'Golf', 100, 'Manual')
print(car1.display_info())
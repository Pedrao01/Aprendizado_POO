class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print('The car is running!')


car1 = Car('opala', 'classico', 1997)
car1.start_engine()
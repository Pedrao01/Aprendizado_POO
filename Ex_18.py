class Vehicle:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def display_info(self):
        return f'mark: {self.mark} | Model: {self.model} | Year: {self.year}'


class Car(Vehicle):
    def __init__(self, mark, model, year, doors):
        super().__init__(mark, model, year)
        self.doors = doors

    def display_info_full(self):
        base_vehicle = super().display_info()
        return f'{base_vehicle} | Doors: {self.doors}'


car1 = Car('Volkswagen', 'Golf', 2018, 4)

print(car1.display_info_full())
class Person:
    def __init__(self, name, weight, height):
        self.__name = name
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            print('invalid weight! The weight must be bigger than 0.')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 1.0 < value < 2.5:
            self.__height = value
        else:
            print('Invalid height! The height must be between 1.0 and 2.5.')

    @property
    def imc(self):
        return round(self.__weight / (self.__height ** 2), 2)

    def situacao(self):
        if self.imc < 18.5:
            return 'underweight'
        elif 18.5 <= self.imc <= 24.9:
            return 'normal weight'
        elif 25 <= self.imc <= 29.9:
            return 'overweight'
        elif 30.0 <= self.imc:
            return 'obesity'


p1 = Person('Pedro', 71, 1.70)
print(p1.imc)
print(p1.situacao())

p1.weight = -50
p1.height = 3.0

print(p1.weight)
print(p1.height)
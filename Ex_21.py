class MeansTransport:
    def fixed_cost(self):
        return 'with out cost'

class Car(MeansTransport):
    def fixed_cost(self):
        return 'the value of the travel was R$100,00'

class Bike(MeansTransport):
    def fixed_cost(self):
        return 'this travel was free'


lista = [Car(), Bike(), MeansTransport()]
for obj in lista:
    print(obj.fixed_cost())
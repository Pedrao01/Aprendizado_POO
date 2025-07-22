class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Jsonmixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__, indent=2)

class PrettyPrintMixin:
    def print_pretty(self):
        return f'''
    === {self.__class__.__name__} ===
    Name: {self.name}
    Id: {self.id}
'''

class Customer(Person, Jsonmixin):
    def __init__(self, name, id):
        super().__init__(name, id)

class Employee(Person, PrettyPrintMixin):
    def __init__(self, name, id):
        super().__init__(name, id)


cliente = Customer("João", 123)
print(cliente.to_json())   # Deve imprimir JSON com os dados

func = Employee("Maria", 456)
print(func.print_pretty())

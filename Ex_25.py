class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name

class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class PrettyPrint:
    def print_pretty(self):
        print(f'''=={self.__class__.__name__}==
Name: {self.name}
ID: {self.id}''')

class ValidationMixin:
    def is_valid(self):
        if not self.name or self.id < 0:
            return False
        else:
            return True

class Employee(Person, PrettyPrint):
    pass

class Client(Person, JsonMixin, PrettyPrint):
    pass

class Supplier(Person, JsonMixin, ValidationMixin):
    pass


e = Employee("Ana", 10)
e.print_pretty()

c = Client("Carlos", 20)
print(c.to_json())

s = Supplier("Fulano", -1)
print(s.is_valid())  # False (ID negativo)


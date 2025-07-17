class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def display_datas(self):
        return f'Street: {self.street} | City: {self.city} | State: {self.state}'


class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

    def display_datas(self):
        return f'Name: {self.name} | Salary: {self.salary} | {self.address.display_datas()}'


class Manager(Employee):
    def __init__(self, name, salary, address, department):
        super().__init__(name, salary, address)
        self.department = department

    def display_dates(self):
        base_display = super().display_dates()
        return f'Department: {self.department} | {base_display}'


end1 = Address("Rua A", "Fortaleza", "CE")
f1 = Employee("João", 3000, end1)

end2 = Address("Rua B", "Recife", "PE")
g1 = Manager("Maria", 8000, end2, "TI")

print(f1.display_datas())
print(g1.display_datas())

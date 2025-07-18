class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self._position = position
        self.__salary = salary

    def get_salary(self):
        print(f'Salary: {self.__salary}')


employee1 = Employee('Pedro', 'Programador', 10000)
print(employee1.name)
print(employee1._position)
print(employee1._Employee__salary)
employee1.get_salary()
print(employee1.__salary)
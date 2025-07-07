class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            print('New name cannot to be null and not to be one str')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 1300:
            self.__salary = value
        else:
            print('The salary must be greater than 1300.')

    def info(self):
        return f'{self.name} | Salary: R$ {self.salary}'


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        if value >= 0:
            self.__bonus = value
        else:
            print('The bonus must be greater than or equal to 0.')

    def info(self):
        base_info = super().info()
        return f'Employee: {base_info} | Bonus: R$ {self.bonus} | Total: R$ {self.salary + self.bonus}'


f = Employee('João', 1200)
f.salary = 2000
print(f.info())

g = Manager('Maria', 5000, 1500)
print(g.info())

g.bonus = -100
print(g.bonus)
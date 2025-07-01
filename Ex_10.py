from abc import ABC, abstractmethod

class Worker(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return f'Worker: {self.__name}'
    @abstractmethod
    def calculate_payment(self):
        pass

class Employee(Worker):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def calculate_payment(self):
        return f'salary: {self.salary} + Bonus: {self.bonus} = {self.salary + self.bonus}'

class Freelancer(Worker):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_payment(self):
        return f'Hourly Rate: {self.hourly_rate} x Hours Worked: {self.hours_worked} = {self.hourly_rate * self.hours_worked}'


l = [Employee('Pedro', 10000, 8000), Freelancer('Manu', 200, 200)]
for item in l:
    print(item.get_name())
    print(item.calculate_payment())

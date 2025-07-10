from abc import ABC, abstractmethod

class Collaborator(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def calculate_payment(self):
        pass

    def summary(self):
        return f'name: {self._name} | Salary: {self.calculate_payment()}'

class EmployeeCommon(Collaborator):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 1300:
            self.__salary = value
        else:
            print('The salary must be greater than 1300.')

    def calculate_payment(self):
        return self.__salary

class Freelancer(Collaborator):
    def __init__(self, name,  hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value > 0:
            self.__hourly_rate = value
        else:
            print('The hourly rate must be greater than 0.')

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value >= 0:
            self.__hours_worked = value
        else:
            print('The hours worked must be greater than or equaly to 0.')

    def calculate_payment(self):
        return self.__hourly_rate * self.__hours_worked


func1 = EmployeeCommon("Ana", 2500)
free1 = Freelancer("Bruno", 80, 100)

equipe = [func1, free1]

for pessoa in equipe:
    print(pessoa.summary())
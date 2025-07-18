class Employee():
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f'Employee {self.name} is working')

class Developer(Employee):
    def code(self):
        print(f'{self.name} is writing a code')

class Designer(Employee):
    def design(self):
        print(f'{self.name} is designing a layout')

developer = Developer('Pedro')
developer.work()
developer.code()

designer = Designer('Manu')
designer.work()
designer.design()


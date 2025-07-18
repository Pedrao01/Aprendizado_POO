from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def personal_information(self):
        pass

class Employee(Person):
    def __init__(self, salary: float, position: str):
        self.salary = salary
        self.position = position

    def personal_information(self):
        return f'Salary: {self.salary} | Position: {self.position}'

class Studant(Person):
    def __init__(self, final_note: float, course: str):
        self.final_note = final_note
        self.course = course

    def personal_information(self):
        return f'Final note: {self.final_note} | Course: {self.course}'


lista = [
    Employee(10000, 'Date Analyst and Developer'),
    Studant(10, 'systems analysis and development')
]
for obj in lista:
    print(obj.personal_information())
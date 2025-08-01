from dataclasses import dataclass

@dataclass(slots=True)
class Instructor:
    name: str

    def teach(self):
        print(f'{self.name} is teaching.')

@dataclass(slots=True)
class Student:
    name: str

    def study(self):
        print(f'{self.name} is studying.')

class Course:
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.students = []


    def add_student(self, student):
        self.students.append(student)

    def start(self):
        print(f'Course: {self.name} is starting...')
        self.instructor.teach()
        for student in self.students:
            student.study()


ana = Student('Ana')
lucas = Student('Lucas')
bruna = Student('Bruna')

ze_tarcisio = Instructor('Zé Tarcísio')

ads = Course('ADS', ze_tarcisio)

ads.add_student(ana)
ads.add_student(lucas)
ads.add_student(bruna)

ads.start()

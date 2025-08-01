class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def start(self):
        print(f"Course {self.name} is starting.")
        for student in self.students:
            student.study()


# Criando estudantes (que existem fora do curso)
alice = Student('Alice')
bob = Student('Bob')

# Criando curso e adicionando estudantes
python_course = Course('Python 101')
python_course.add_student(alice)
python_course.add_student(bob)

# Iniciando o curso
python_course.start()
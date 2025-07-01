class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Hi, i am {self.name}, {self.age} years old'

class Student(Person):
    def __init__(self,name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def introduce(self):
        base_intro = super().introduce()
        print(f'{base_intro} and i am in grade {self.grade}')

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        base_intro = super().introduce()
        print(f'{base_intro} and I teach {self.subject}')


studant1 = Student('Pedro', 18, '13th')
studant1.introduce()
teacher1 = Teacher('Zé Tarcísio', 51, 'English')
teacher1.introduce()

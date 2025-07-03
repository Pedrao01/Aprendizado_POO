class Aluno:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, valor):
        if 0 <= valor <= 100:
            self.__grade = valor
        else:
            print('Note invalid! Must be between 0 and 100.')

    def is_approved(self):
        if self.__grade >= 60:
            return True
        else:
            return False


aluno1 = Aluno('pedro', 180)
print(aluno1.grade)
aluno1.grade = 150
aluno1.grade = 50
print(aluno1.is_approved())
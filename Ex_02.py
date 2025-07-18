class Person():
    species = 'Human'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hi, my name is {self.name}, i am {self.age} years old and i am a {self.species}')


person1 = Person('pedro', 18)
person2 = Person('Manu', 16)
person1.introduce()
person2.species = 'monkey'
person2.introduce()
class Movie():
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.director} - {self.year}'

    def play(self):
        print(f'Playing {self.title}...')


filme1 = Movie('django', 'Tarantino', 2012)
print(filme1)
filme1.play()
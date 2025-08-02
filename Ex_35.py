from dataclasses import dataclass

#classe Player, onde se declara nome e ID
@dataclass(slots=True)
class Player:
    name: str
    id: int

#classe Team, onde é usado agregação para aceitar obj de fora
class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    #Exibe as infomações dos players
    def display(self):
        for info in self.players:
            print(f'Player: {info.name} | ID: {info.id}')


p1 = Player('Pedro', 13)
p2 = Player('Manel', 45)
p3 = Player('Manu', 31)

team = Team()
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.display()

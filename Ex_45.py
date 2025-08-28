from abc import ABC, abstractmethod

class Snack(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class Sandwich(Snack):
    def cost(self) -> float:
        return 8.00

    def description(self) -> str:
        return 'Basic sandwich'

class SnackDecorator(Snack):
    def __init__(self, snack: Snack):
        self._snack = snack

    def cost(self) -> float:
        return self._snack.cost()

    def description(self) -> str:
        return self._snack.description()

class Cheese(SnackDecorator):
    def cost(self) -> float:
        return super().cost() + 2.50

    def description(self) -> str:
        return super().description() + ' + Cheese'

class Bacon(SnackDecorator):
    def cost(self) -> float:
        return super().cost() + 3.00

    def description(self) -> str:
        return  super().description() + ' + Bacon'

class Lettuce(SnackDecorator):
    def cost(self) -> float:
        return super().cost() + 1.00

    def description(self) -> str:
        return super().description() + ' + Lettuce'


sneck = Sandwich()
print(sneck.description(), 'R$', sneck.cost())

sneck = Cheese(sneck)
print(sneck.description(), 'R$', sneck.cost())

sneck = Bacon(sneck)
print(sneck.description(), 'R$', sneck.cost())

sneck = Lettuce(sneck)
print(sneck.description(), 'R$', sneck.cost())

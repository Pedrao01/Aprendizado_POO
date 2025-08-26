from abc import ABC, abstractmethod
from dataclasses import dataclass

class Observer(ABC):
    @abstractmethod
    def update(self,name ,price):
        pass

class Stock:
    def __init__(self, name, price):
        self.observers = []
        self.name = name
        self._price = price

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.name, self._price)

    def set_price(self, price):
        print(f'The {self.name} was altered to: {price}')
        self._price = price
        self.notify()

@dataclass(slots=True)
class Investor(Observer):
    name: str
    min_price: float

    def update(self, name, price):
        if price >= self.min_price:
            print(f'{self.name}! the {name} is on the price!')


stock = Stock('PETR4', 45.00)
investor1 = Investor('Pedro', 50.00)
investor2 = Investor('Andrey', 40.00)

stock.attach(investor1)
stock.attach(investor2)

stock.set_price(48.00)
stock.set_price(52.00)

from abc import ABC, abstractmethod

#Abstract product
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass
    def description(self) -> str:
        pass

#Concrets products(Created by the factory)
class Express(Coffee):
    def cost(self) -> float:
        return 5.00
    def description(self) -> str:
        return 'Express'

class American(Coffee):
    def cost(self) -> float:
        return 6.50
    def description(self) -> str:
        return 'American'

class Latte(Coffee):
    def cost(self) -> float:
        return 7.50

    def description(self) -> str:
        return 'Latte'

class Cappuccino(Coffee):
    def cost(self) -> float:
        return 8.00

    def description(self) -> str:
        return 'Cappuccino'


#factory
class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type: str) -> Coffee:
        if coffee_type.lower() == 'express':
            return Express()
        elif coffee_type.lower() == 'american':
            return American()
        elif coffee_type.lower() == 'cappuccino':
            return Cappuccino()
        elif coffee_type.lower() == 'latte':
            return Latte()
        else:
            raise ValueError('Unknown coffee type')

    @staticmethod
    def order_summary( order: Coffee):
        print(f'Order: {order.description()}')
        print(f'R${order.cost():.2f}')

#---------------------------
#Decorators
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 1.50

    def description(self) -> str:
        return super().description() + ' + Milk'


class Chocolate(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 2.00

    def description(self) -> str:
        return super().description() + ' + Chocolate'


class WhippedCream(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 3.00

    def description(self) -> str:
        return super().description() + ' + Whippen Cream'


class Caramel(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 2.50

    def description(self) -> str:
        return super().description() + ' + Caramel'


class Vanilla(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 1.75

    def description(self) -> str:
        return super().description() + ' + Vanilla'


coffee = CoffeeFactory.create_coffee('Cappuccino')
CoffeeFactory.order_summary(coffee)

coffee = Milk(Vanilla(Caramel(coffee)))

CoffeeFactory.order_summary(coffee)

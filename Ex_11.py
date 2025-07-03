class Product():
    def __init__(self,name, price):
        self.name = name
        self.__price = price

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, valor):
        if valor < 0:
            print('Balance cannot be negative!')
        else:
            self.__price = valor

    def apply_discount(self, discount):
        self.__price -= (self.__price * discount / 100)


p =  Product('Mouse', 100)
print(p.product_price)
p.product_price = -20
p.apply_discount(10)
print(p.product_price)
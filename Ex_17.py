class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @classmethod
    def from_string(cls, text):
        name, price, category = text.split(';')
        return cls(name, float(price), category)

    @staticmethod
    def validate_price(price):
        return price > 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if self.validate_price(value):
            self.__price = value
        else:
            print('Erro! Invalid price.')

p1 = Product('teclado', 150.0, 'Periférico')
p2 = Product.from_string('Monitor;500.0;Vídeo')

l = [p1, p2]
for product in l:
    print(product.name, product.price, product.category)

p1.price = -50

print(p1.validate_price(300))
print(p2.validate_price(-5))

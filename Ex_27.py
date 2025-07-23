from dataclasses import dataclass

@dataclass(slots=True)
class Product:
    name: str
    price: float

    def display(self):
        return f'Name: {self.name} | Price: {self.price}'

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError('The price must be greater than 0')

@dataclass(slots=True)
class DigitalProduct(Product):
    file_size: float

    def display(self):
        base_diplay = super(DigitalProduct, self).display()
        return f'{base_diplay} | File Size: {self.file_size}'

@dataclass(slots=True)
class PhysicalProduct(Product):
    weight: float
    stock: int

    def is_in_stock(self):
        if self.stock > 0:
            return True
        return False

    def display(self):
        base_display = super(PhysicalProduct, self).display()
        return f'{base_display} | Weight: {self.weight} | Stock: {self.stock}'


dp = DigitalProduct("E-book", 29.9, 5.2)
print(dp.display())

pp = PhysicalProduct("Livro Físico", 59.9, 0.4, 12)
print(pp.display())
print(pp.is_in_stock())  # True
#testa o slots
try:
    dp.extra = 'test'
except AttributeError as e:
    print('slots funcionando', e)

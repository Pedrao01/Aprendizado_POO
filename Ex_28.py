from abc import ABC, abstractmethod
from dataclasses import dataclass

class BaseProduct(ABC):
    @abstractmethod
    def validate(self):
        pass

    def display(self):
        return f'Name: {self.name} | Price: {self.price}'

class BaseModel:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'validate'):
            raise TypeError (f'{cls.__name__} there must be a validate method')

class LoggerMixin:
    def log(self, msg: str):
        print(f'[LOG]: {msg}')

@dataclass(slots=True)
class DigitalProduct(BaseProduct, BaseModel, LoggerMixin):
    name: str
    price: float
    file_size: float

    def display(self):
        base_display = super(DigitalProduct, self).display()
        info = f'{base_display} | File size: {self.file_size}MB'
        self.log(info)
        return info

    def validate(self):
        if self.file_size < 0 or self.price < 0:
            raise ValueError('The value must be greater than 0')

@dataclass(slots=True)
class PhysicalProduct(BaseProduct, BaseModel, LoggerMixin):
    name: str
    price: float
    weight: float
    stock: int

    def display(self):
        base_display = super(PhysicalProduct, self).display()
        info = f'{base_display} | Weight: {self.weight} | Stock: {self.stock}'
        self.log(info)
        return info

    def validate(self):
        if self.price < 0 or self.weight < 0:
            raise ValueError('The value must be greater than 0')

    def is_in_stock(self):
        return f'Name:{self.name} | Stock: {self.stock}'


pd = DigitalProduct("Curso Python", 149.9, 512)
pd.validate()
pd.display()

pf = PhysicalProduct("Livro", 89.9, 0.6, 15)
pf.validate()
pf.display()
print("Is in stock?", pf.is_in_stock())


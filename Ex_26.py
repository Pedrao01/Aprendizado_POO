from dataclasses import dataclass
@dataclass(slots=True)
class Product:
    name: str
    price: float
    def display(self):
        print(f'Name: {self.name} | Price: {self.price}')


p = Product('book', 39.9)
#É para dar erro: 'Product' object has no attribute 'estoque'
p.estoque = 9
#É para dar erro: 'Product' object has no attribute '__dict__'
print(p.__dict__)
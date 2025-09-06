class Product:
    def __init__(self, product_name: str, price: float, stock: int) -> None:
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        return f'Product: {self.product_name} ({self.stock} at stock) - R${self.price}'

    def __repr__(self) -> str:
        return f'Product: (product_name={self.product_name!r}, price={self.price!r}, stock={self.stock!r})'


product1 = Product('Caneta', 2.50, 5)

print(product1)
print(repr(product1))

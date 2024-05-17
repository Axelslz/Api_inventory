import uuid

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
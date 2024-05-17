from src.domain.port.products_port import ProductsPort, Product

class CreateProductUseCase:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    def execute(self, data):
        return self.products_repository.create_product(Product(**data))
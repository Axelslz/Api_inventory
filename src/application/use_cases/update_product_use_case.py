from src.domain.port.products_port import ProductsPort, Product

class UpdateProductUseCase:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    def execute(self, product_id, data):
        return self.products_repository.update_product(product_id, Product(**data))
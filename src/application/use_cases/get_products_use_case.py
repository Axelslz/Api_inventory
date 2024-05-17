from src.domain.port.products_port import ProductsPort

class GetProductsUseCase:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    def execute(self):
        return self.products_repository.get_products()
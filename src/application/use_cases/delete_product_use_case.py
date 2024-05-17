from src.domain.port.products_port import ProductsPort

class DeleteProductUseCase:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    def execute(self, product_id):
        return self.products_repository.delete_product(product_id)
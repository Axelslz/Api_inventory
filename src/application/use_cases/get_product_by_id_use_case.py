from src.domain.port.products_port import ProductsPort

class GetProductByIdUseCase:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    def execute(self, product_id):
        return self.products_repository.get_product_by_id(product_id)
from src.domain.port.products_port import ProductsPort
from src.application.use_cases.get_products_use_case import GetProductsUseCase
from src.application.use_cases.get_product_by_id_use_case import GetProductByIdUseCase
from src.application.use_cases.create_product_use_case import CreateProductUseCase
from src.application.use_cases.update_product_use_case import UpdateProductUseCase
from src.application.use_cases.delete_product_use_case import DeleteProductUseCase

class ProductController:
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository
        self.get_products_use_case = GetProductsUseCase(products_repository)
        self.create_product_use_case = CreateProductUseCase(products_repository)
        self.get_product_by_id_use_case = GetProductByIdUseCase(products_repository)
        self.update_product_use_case = UpdateProductUseCase(products_repository)

    def get_products(self):
        return self.get_products_use_case.execute()
    
    def get_product_by_id(self, product_id):
        return self.get_product_by_id_use_case.execute(product_id)
    
    def create_product(self, request):
        create_product_use_case = CreateProductUseCase(self.products_repository)
        return create_product_use_case.execute(request.get_json())
    
    def update_product(self, product_id, request):
        update_product_use_case = UpdateProductUseCase(self.products_repository)
        return update_product_use_case.execute(product_id, request.get_json())
    
    def delete_product(self, product_id):
        delete_product_use_case = DeleteProductUseCase(self.products_repository)
        return delete_product_use_case.execute(product_id)
    

    
    

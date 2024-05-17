from src.database.mysql.connection import Base, engine, SessionLocal
from src.database.mysql.models.product import Product as ProductModel
from src.domain.entities.product import Product
from src.domain.port.products_port import ProductsPort

class ProductsRepository(ProductsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def get_products(self):
        products = self.db.query(ProductModel).all()
        return [product.to_dict() for product in products]
    
    def get_product_by_id(self, id: str):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if product:
            return product.to_dict()
        return None
    
    def create_product(self, product: Product):
        product_model = ProductModel(**product.__dict__)
        self.db.add(product_model)
        self.db.commit()
        self.db.refresh(product_model)  # Refresh to get the auto-generated ID
        return product_model.to_dict()
    
    def update_product(self, id: str, product: Product):
        existing_product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not existing_product:
            return None  # Or raise an exception
        
        # Update the fields, excluding the ID
        for key, value in product.__dict__.items():
            if key != 'id':
                setattr(existing_product, key, value)

        self.db.commit()
        self.db.refresh(existing_product)  # Refresh to get the updated values
        return existing_product.to_dict()
    
    def delete_product(self, id: str):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).delete()
        self.db.commit()
        return {"message": "Product deleted" if result else "Product not found"}
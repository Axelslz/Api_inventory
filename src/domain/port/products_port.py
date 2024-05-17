from abc import ABC, abstractmethod
from src.domain.entities.product import Product

class ProductsPort(ABC):
  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def get_products(self):
    pass

  @abstractmethod
  def get_product_by_id(self, id: str):
    pass

  @abstractmethod
  def create_product(self, product: Product):
    pass

  @abstractmethod
  def update_product(self, id: str, product: Product):
    pass

  @abstractmethod
  def delete_product(self, id: str):
    pass
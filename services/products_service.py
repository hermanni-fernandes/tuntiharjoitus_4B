from repositories.products_repository import ProductsRepository

class ProductsService:
    def __init__(self):
        self.repository = ProductsRepository()

    def get_all_products(self):
        return self.repository.get_all()

    def get_product_by_id(self, tuote_id: int):
        return self.repository.get_by_id(tuote_id)

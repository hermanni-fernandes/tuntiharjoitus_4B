from repositories.category_repository import CategoryRepository
from models.category import Category

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def get_all_categories(self):
        return self.repository.get_all()

    def get_category_by_id(self, category_id: int):
        return self.repository.get_by_id(category_id)

    def create_category(self, category: Category):
        return self.repository.add(category)

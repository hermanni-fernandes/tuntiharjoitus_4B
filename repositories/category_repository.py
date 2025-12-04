from models.category import Category

class CategoryRepository:
    def __init__(self):
        self._categories = [
            Category(id=1, name="Juomat", owner="admin"),
            Category(id=2, name="Makeiset", owner="admin")
        ]

    def get_all(self):
        return self._categories

    def get_by_id(self, category_id: int):
        for category in self._categories:
            if category.id == category_id:
                return category
        return None

    def add(self, category: Category):
        # Uusi ID automaattisesti
        new_id = max(c.id for c in self._categories) + 1
        category.id = new_id
        self._categories.append(category)
        return category

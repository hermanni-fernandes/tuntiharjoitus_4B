from fastapi import APIRouter, HTTPException
from models.category import Category
from services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()

@router.get("/", response_model=list[Category])
def get_all_categories():
    return service.get_all_categories()

@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int):
    category = service.get_category_by_id(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Kategoriaa ei löytynyt")
    return category

@router.post("/", response_model=Category)
def create_category(category: Category):
    if not category.name.strip():
        raise HTTPException(status_code=400, detail="Kategorian nimi on pakollinen")

    # Lisätään automaattinen Owner (mock)
    category.owner = "test_user"

    return service.create_category(category)

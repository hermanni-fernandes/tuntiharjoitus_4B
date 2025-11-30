from fastapi import APIRouter, HTTPException
from services.products_service import ProductsService
from models.tuote import Tuote

router = APIRouter(prefix="/products", tags=["Products"])
service = ProductsService()


@router.get("/", response_model=list[Tuote])
def get_all_products():
    return service.get_all_products()


@router.get("/{tuote_id}", response_model=Tuote)
def get_product_by_id(tuote_id: int):
    tuote = service.get_product_by_id(tuote_id)
    if tuote is None:
        raise HTTPException(status_code=404, detail="Tuotetta ei löytynyt")
    return tuote

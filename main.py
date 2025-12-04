from fastapi import FastAPI
from controllers.products_controller import router as products_router
from controllers.categories_controller import router as categories_router

app = FastAPI()

app.include_router(products_router)
app.include_router(categories_router)

@app.get("/")
def root():
    return {"message": "FastAPI toimii!"}

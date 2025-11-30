from fastapi import FastAPI
from controllers.products_controller import router as products_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI toimii!"}

app.include_router(products_router)

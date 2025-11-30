from fastapi import FastAPI
from controllers.products_controller import router as products_router

app = FastAPI()

app.include_router(products_router)

@app.get("/")
def root():
    return {"message": "FastAPI toimii!"}

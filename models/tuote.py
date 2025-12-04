from pydantic import BaseModel

class Tuote(BaseModel):
    id: int
    nimi: str
    kuvaus: str
    hinta: float
    category_id: int  # Jokainen tuote kuuluu kategoriaan

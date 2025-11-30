from pydantic import BaseModel

class Tuote(BaseModel):
    id: int
    nimi: str
    kuvaus: str
    hinta: float

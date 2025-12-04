from models.tuote import Tuote

class ProductsRepository:
    def __init__(self):
        self._tuotteet = [
            Tuote(id=1, nimi="Kahvi", kuvaus="Tumma paahto kahvi", hinta=4.50, category_id=1),
            Tuote(id=2, nimi="Tee", kuvaus="Vihreä tee", hinta=3.20, category_id=1),
            Tuote(id=3, nimi="Suklaa", kuvaus="Maitosuklaa levy 200g", hinta=2.80, category_id=2),
        ]

    def get_all(self):
        return self._tuotteet

    def get_by_id(self, tuote_id: int):
        for tuote in self._tuotteet:
            if tuote.id == tuote_id:
                return tuote
        return None

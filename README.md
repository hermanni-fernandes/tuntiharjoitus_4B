# Tuntiharjoitus 4B – Category + Products API (FastAPI)

Tämä projekti toteuttaa REST-rajapinnan Pythonin FastAPI-kehyksellä.  
Tehtävän tavoitteena oli lisätä Category-toiminnallisuus aiemman tuotteiden API:n yhteyteen.  

Toteutus sisältää REST-endpointit kategorioille, kategoriassa näkyvän omistajatiedon sekä sen, että jokainen tuote (Tuote) kuuluu johonkin kategoriaan.

---

## Projektin rakenne

```
tuntiharjoitus_4B/
├── controllers/
│ ├── products_controller.py
│ └── categories_controller.py
├── models/
│ ├── tuote.py
│ └── category.py
├── repositories/
│ ├── products_repository.py
│ └── category_repository.py
├── services/
│ ├── products_service.py
│ └── category_service.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Toteutetut ominaisuudet (Tehtävä 4B)

### 1. Category-malli
Category sisältää seuraavat kentät:
- **id** (yksilöllinen tunniste)
- **name** (kategorian nimi)
- **owner** (kategoriasta vastaava käyttäjä, lisätään automaattisesti)

> **Owner lisätään aina palvelimella**, eikä sitä lähetetä pyynnössä.

### 2. Category REST-endpointit
| Metodi | Polku | Kuvaus |
|--------|-------|--------|
| GET | `/categories` | Hae kaikki kategoriat |
| GET | `/categories/{id}` | Hae yksittäinen kategoria omistajatiedon kanssa |
| POST | `/categories` | Lisää uusi kategoria (Owner = `"test_user"`) |

### 3. Tuote kuuluu kategoriaan
`Tuote`-malliin lisättiin kenttä:

```python
category_id: int
Mock-dataa päivitettiin vastaavasti:

Kahvi ja Tee → kategorian Id = 1
Suklaa → kategorian Id = 2

### 4. Automaattinen dokumentaatio
FastAPI tuottaa Swagger- ja ReDoc-dokumentaation automaattisesti.
Testaus Swaggerilla
Käynnistä sovellus:
uvicorn main:app --reload

Swagger UI löytyy:
http://localhost:8000/docs

---

Testattavat kohdat:
✔ GET /categories → palauttaa kategoriat
✔ POST /categories → palauttaa Owner = "test_user"
✔ GET /products → jokaisella tuotteella on category_id

---

Käytetyt teknologiat
Python 3
FastAPI
Uvicorn
Pydantic
Repository Pattern
Service Layer Pattern
Swagger / OpenAPI

---

Tavoite
Oppia:
lisäämään uutta ominaisuutta olemassa olevaan API:in
kerrosarkkitehtuurin toteuttaminen (Controller → Service → Repository)
mallien laajentaminen ja endpointtien lisääminen
automaattisen dokumentaation hyödyntäminen (Swagger / ReDoc)

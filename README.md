# Tuntiharjoitus 4B – Products API (FastAPI)

Tämä projekti toteuttaa yksinkertaisen tuotteiden hakuun perustuvan REST-rajapinnan Pythonin FastAPI-kehyksellä.  
Toteutus noudattaa kerrosarkkitehtuuria (Controller → Service → Repository) ja sisältää automaattisen Swagger- ja ReDoc-dokumentaation.

---

## Projektin rakenne

```
tuntiharjoitus_4B/
├── controllers/
│   └── products_controller.py
├── models/
│   └── tuote.py
├── repositories/
│   └── products_repository.py
├── services/
│   └── products_service.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Toteutetut ominaisuudet

### **1. Malli (Model)**  
`Tuote`-malli kuvaa yksittäistä tuotetta:

- id  
- nimi  
- kuvaus  
- hinta  

Malli perustuu Pydantic BaseModel -luokkaan.

---

### **2. Repository-kerros**
`ProductsRepository` toimii kovakoodattuna tietolähteenä ja tarjoaa metodit:

- `get_all()` – palauttaa kaikki tuotteet  
- `get_by_id(id)` – palauttaa yhden tuotteen ID:n perusteella  

---

### **3. Service-kerros**
`ProductsService` sisältää sovelluslogiikan ja välittää pyynnöt repositorylle.

- `get_all_products()`  
- `get_product_by_id(id)`  

---

### **4. Controller**
`products_controller` tarjoaa REST-endpointit:

- **GET /products** – kaikki tuotteet  
- **GET /products/{id}** – yksittäinen tuote  

Controller hyödyntää Service-kerrosta.

---

## ▶ API:n käynnistäminen

### 1. Asenna riippuvuudet
```
pip install -r requirements.txt
```

### 2. Käynnistä sovellus
```
uvicorn main:app --reload
```

Sovellus käynnistyy osoitteeseen:

http://localhost:8000

---

## API-endpointit

### Hae kaikki tuotteet  
**GET**  
`http://localhost:8000/products`

### Hae tuote ID:n perusteella  
**GET**  
`http://localhost:8000/products/{id}`
- esim. `http://localhost:8000/products/1`

---

## Dokumentaatio

FastAPI tuottaa dokumentaation automaattisesti:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc` 

---

## Käytetyt teknologiat

- Python 3  
- FastAPI  
- Uvicorn  
- Pydantic  
- Repository Pattern  
- Service Layer Pattern  
- Swagger / OpenAPI  

---

## Tavoite

Harjoituksen tavoitteena on ymmärtää ja toteuttaa:

- FastAPI-sovellus kerrosarkkitehtuurilla  
- erilliset Models-, Repositories-, Services- ja Controllers-kansiot  
- REST-rajapinta  
- automaattinen Swagger- ja ReDoc-dokumentaatio


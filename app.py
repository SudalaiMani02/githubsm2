from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import status
from fastapi import HTTPException
app = FastAPI(title="welcome da")

@app.get("/")
def root():
    return{"messege":"Hello FastAPI"}

@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id, "type":str(type(user_id))}

@app.get("/search")
def search(q:str, page:int=1, limit: int=10):
    return{"q":q, "page":page, "limit":limit}

class UserCreate(BaseModel):
    name:str
    email:str
    age:int | None = None

@app.post("/users")
def create_user(payload:UserCreate):
    return{"created": True, "user":payload.model_dump()}

class ProductCreate(BaseModel):
    name:str = Field(min_length=2, max_length=50)
    price:float = Field(gt=0)
    stock: int = Field(gt=0)

@app.post("/products")
def create_products(p:ProductCreate):
    return p.model_dump()

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return{"created": True}

FAKE_DB ={1:"mani", 2:"venki"}

@app.get("/users/db/{user_id}")
def user_from_db(user_id:int):
    if user_id not in FAKE_DB:
        raise HTTPException(status_code=404, detail="user not found")
    return{"id": user_id, "name": FAKE_DB[user_id]}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    id: int
    name: str
    email: str

db = []

@app.get("/customers")
def get_customers():
    return db

@app.post("/customers")
def add_customer(customer: Customer):
    db.append(customer.dict())
    return {"message": "Customer added"}

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    for c in db:
        if c["id"] == customer_id:
            c.update(customer.dict())
            return {"message": "Customer updated"}
    return {"error": "Customer not found"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    global db
    db = [c for c in db if c["id"] != customer_id]
    return {"message": "Customer deleted"}

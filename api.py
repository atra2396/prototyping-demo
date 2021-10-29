from os import environ

from faker import Faker
from fastapi import FastAPI
from pony.orm import db_session

from db import db, Contact

db_path = environ.get("DB_PATH", "database.sqlite")

app = FastAPI()
db.bind(provider='sqlite', filename=db_path, create_db=True)
db.generate_mapping(create_tables=True)

fake = Faker()

@app.get("/contact/{contact_id}")
def get_contact(contact_id: int):
    with db_session:
        contact = Contact[contact_id]
    return {
        "name": contact.name,
        "address": contact.address
    }

@app.post("/contacts")
def create_contact():
    with db_session:
        contact = Contact(name=fake.name(), address=fake.address())
    return contact.id
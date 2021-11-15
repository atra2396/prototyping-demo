from os import environ

from faker import Faker
from fastapi import FastAPI
from pony.orm import db_session, select

from db import db, Contact

db_path = environ.get("DB_PATH", "database.sqlite")

app = FastAPI()
db.bind(provider='sqlite', filename=db_path, create_db=True)
db.generate_mapping(create_tables=True)

fake = Faker()

@app.get("/contacts")
def get_contacts():
    with db_session:
        contacts = [
            {
                "name": contact.name,
                "phone": contact.phone
            }
            for contact in select(c for c in Contact)
        ]
    return contacts

@app.post("/contacts")
def create_contact():
    with db_session:
        contact = Contact(name=fake.name(), phone=fake.phone_number())
    return {
        "name": contact.name,
        "phone": contact.phone
    }

import random
from os import environ

from faker import Faker
from fastapi import FastAPI
from fastapi.responses import Response
from pony.orm import db_session, select

from db import Contact, db

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
                "phone_number": contact.phone
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

@app.get("/liveness")
def liveness(response: Response):
    health_percent = int(environ.get("HEALTH_PERCENT", 100))
    random_value = random.randrange(1, 101)
    if health_percent >= random_value:
        response.status_code = 200
    else:
        response.status_code = 500


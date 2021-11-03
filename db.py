from pony.orm import Database, Required

db = Database()

class Contact(db.Entity):
    name = Required(str)
    phone = Required(str)
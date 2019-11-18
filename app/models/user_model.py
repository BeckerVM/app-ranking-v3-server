from app import db

class Users(db.Document):
  email = db.StringField(required=True)
  names = db.StringField(required=True)
  surnames = db.StringField(required=True)
  password = db.StringField(required=True)
  rol = db.StringField(required=True)
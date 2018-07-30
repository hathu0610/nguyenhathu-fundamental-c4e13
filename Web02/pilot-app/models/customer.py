from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
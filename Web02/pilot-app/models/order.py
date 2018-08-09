from mongoengine import *

class Order(Document):
    serviceid = StringField()
    userid = StringField()
    currentime = DateTimeField()
    is_accepted= BooleanField()

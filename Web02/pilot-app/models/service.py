from mongoengine import *
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = StringField()
    image = StringField()


# new_service = Service(
#     name = "thu",
#     yob = 1999,
#     gender = 0,
#     height = 162,
#     phone = "000999338",
#     address = "ha noi",
#     status = True
# )


# new_service.save()
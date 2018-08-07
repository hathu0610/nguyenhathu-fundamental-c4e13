from models.service import Service
import mlab
from faker import Faker
from random import *
mlab.connect()

fake = Faker()

# print(fake.address())

    
image_link =["https://bit.ly/2OLDjhE", "https://bit.ly/2AMXvwR", "https://bit.ly/2nhxQ5L", "https://bit.ly/2KziXVz"]
for image in image_link:
    ran_description = sample(["ngoan hiền", "dễ thương", "lễ phép với gia đình", "cute", "thích uống trà sữa", "thích đi chơi", "ngủ nhiều"], 3)
    ran_mea = [randint(80,100), randint(50,70), randint(80,100)]
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True,False]),
        description = "{0}, {1}, {2}".format(*ran_description),
        measurements = "{0} - {1} - {2}".format(*ran_mea),
        image = image
    )
    new_service.save()


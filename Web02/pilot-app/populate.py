from models.service import Service
import mlab
from faker import Faker
from random import *
mlab.connect()

fake = Faker()

# print(fake.address())

    
image_link =["http://bit.ly/2nHXuAP","https://scontent.fhan5-7.fna.fbcdn.net/v/t1.0-9/38492579_1786246014804552_3611468412422717440_n.jpg?_nc_cat=0&oh=d035f8848b1ca0d70a21c575b3714c27&oe=5C060DE2"]
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


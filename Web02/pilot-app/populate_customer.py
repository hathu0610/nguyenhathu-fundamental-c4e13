from models.customer import Customer
import mlab
from faker import Faker
from random import randint,choice

mlab.connect()


fake = Faker()

for i in range(10):
    print("is saving..")
    fake_name = fake.name()
    new_customer = Customer(
        name = fake_name,
        gender = randint(0,1),
        email =  "{}@email.com".format(fake_name.lower().replace(" ", "")),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True,False])
    )
    new_customer.save()
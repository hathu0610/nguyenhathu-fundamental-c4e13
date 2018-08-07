from models.service import Service
import mlab
mlab.connect()

id_to_find = "5b5caab11ab9434396b3bf61"

# service = Service.objects.get(id = id_to_find) 

# service = Service.objects(id = id_to_find) #=>[]]

service = Service.objects.with_id(id_to_find)
# delete

if service is not None:
    # service.delete()
    # print("Deleted")
    # update
    print("Before",service.to_mongo())
    service.update(set__name = "thu", set__yob = 2000)
    service.reload()
    print("after",service.to_mongo())
else:
    print("not found")


# print(service.to_mongo())
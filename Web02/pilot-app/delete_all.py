from models.service import Service
import mlab
mlab.connect()

Service.objects.delete()
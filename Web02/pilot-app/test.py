from models.order import Order
import mlab
from datetime import *

mlab.connect()

currentime = datetime.now()
 

service_req = Order (
    serviceid = "hi",
    userid = "hi",
    currentime = currentime,
    is_accepted= False
)

service_req.save()
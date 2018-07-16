from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database() 

customers = db['customers']



count_events = customers.find({"ref": "events"}).count()
count_wom = customers.find({"ref": "wom"}).count()
count_ads = customers.find({"ref": "ads"}).count()





print("Events: {}".format(count_events))
print("Wom: {}".format(count_wom))
print("Ads: {}".format(count_ads))

labels = ["Events", "Wom", "Ads"]
values = [count_events,count_wom,count_ads]
colors = ["xkcd:lavender","red","blue"]
explode = [0, 0, 0]

pyplot.pie(values,
            labels = labels, 
            colors = colors,
            explode= explode)
pyplot.axis('equal')

pyplot.show()
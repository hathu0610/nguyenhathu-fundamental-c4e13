from pymongo import MongoClient

uri = "mongodb://admin:Thu,1999@ds235411.mlab.com:35411/c4e19"

#1. connect to database
client = MongoClient(uri)
#2. get database
db = client.get_default_database() 
#3. create collection
games= db['games']
# 4. create document
# new_color = {
#     "name": "blue",
#     "description": "mau xanh"
# }
#5. insert doc into collection
# color.insert_one(new_color)

# get all documents
all_games = games.find()

print(all_games[0]['name'])
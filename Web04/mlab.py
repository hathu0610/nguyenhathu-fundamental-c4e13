import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds215172.mlab.com:15172/youtube

host = "ds215172.mlab.com"
port = 15172
db_name = "youtube"
user_name = "hathu0610"
password = "hathu0610"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
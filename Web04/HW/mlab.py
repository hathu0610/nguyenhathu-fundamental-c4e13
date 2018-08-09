import mongoengine

# mongodb://hathu0610:Thu,1999@ds259001.mlab.com:59001/muadongkhonglanhc4e19

host = "ds259001.mlab.com"
port = 59001
db_name = "muadongkhonglanhc4e19"
user_name = "hathu0610"
password = "Thu,1999"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
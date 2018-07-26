from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database() 

posts = db['posts']
new_post = {
    "title": "Chạy ngay đi",
    "author": "Hà Thu",
    "content": """
    Chạy ngay đi trước khi
    Mọi điều dần tồi tệ hơn
    Chạy ngay đi trước khi
    Lòng hận thù cuộn từng cơn
    Tựa giông tố đến bên ghé thăm
    Từ nơi hố sâu tối tăm
    Chạy đi trước khi
    Mọi điều dần tồi tệ hơn
    """
}

posts.insert_one(new_post)
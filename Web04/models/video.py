from mongoengine import *

class Video(Document):
    linkyoutube = StringField()
    title = StringField()
    views = IntField()
    thumbnail = StringField()
    youtubeid = StringField()
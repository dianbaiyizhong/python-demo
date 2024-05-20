from peewee import *

db = Proxy()


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        global db
        database = db


class Book(BaseModel):
    author = CharField(null=True)
    edition = IntegerField(null=True)
    price = FloatField(null=True)
    title = CharField(null=True)

    class Meta:
        table_name = 'book'


def init_db(my_db):
    db.initialize(my_db)
    db.connect()

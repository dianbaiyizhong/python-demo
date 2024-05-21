from peewee import *

database = MySQLDatabase('testdb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Book(BaseModel):
    author = CharField(unique=True)
    edition = IntegerField(null=True)
    my_id = AutoField()
    price = FloatField(null=True)
    title = CharField(null=True)

    class Meta:
        table_name = 'book'


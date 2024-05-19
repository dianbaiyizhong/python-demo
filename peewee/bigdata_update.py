from peewee import *
from shortcuts import dict_to_model, model_to_dict

database = MySQLDatabase('testdb',
                         **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost',
                            'port': 3306, 'user': 'root', 'password': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Book(BaseModel):
    author = CharField(null=True)
    edition = IntegerField(null=True)
    price = FloatField(null=True)
    title = CharField(null=True)

    class Meta:
        table_name = 'book'


database.connect()

data_list = list()
for index in range(10):
    data_list.append(model_to_dict(Book(id=index, title="三体一---", author="<NAME>")))

# Book.insert_many(data_list).execute()
Book.bulk_update(data_list, [Book.title])


# database.execute_sql()
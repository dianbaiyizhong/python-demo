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


database.connect()

data_list = list()
for index in range(100):
    # data_list.append(Book.create(title="三体222" + str(index)))
    data_list.append(model_to_dict(Book(title="三体" + str(index), edition=2, author="key" + str(index))))

# author字段一定要设置为unique索引才生效
Book.insert_many(data_list).on_conflict(
    conflict_where=[Book.author],
    preserve=[Book.title, Book.edition],
).execute()

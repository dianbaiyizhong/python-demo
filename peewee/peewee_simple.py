from peewee import *

# 创建MySQL数据库连接
db = MySQLDatabase('testdb', user='root', password='root',host='localhost', port=3306)


class Book(Model):
    id = AutoField(primary_key=True)
    title = CharField()
    author = CharField()
    price = FloatField()
    edition = IntegerField()

    class Meta:
        database = db


db.connect()


book = Book(title="三体一", author="刘慈欣", price=59.5, edition=6)
book.save()


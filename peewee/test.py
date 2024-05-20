from db_model import *


def test_query():
    res = list(Book.select().dicts())
    print(res)
    pass


if __name__ == '__main__':
    database = MySQLDatabase('testdb',
                             **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                                'host': 'localhost',
                                'port': 3306, 'user': 'root', 'password': 'root'})

    init_db(database)
    test_query()


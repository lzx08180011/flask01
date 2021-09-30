import pymysql
from pymysql.cursors import DictCursor
import hashlib
CONFIG = {
    'host':'192.168.30.128',
    'port':3306,
    'user':'root',
    'db':'bank_server',
    'password':'0011',
    'charset':'utf8',
    'cursorclass': DictCursor
}

class DB():
    def __init__(self):
        self.conn = pymysql.Connect(**CONFIG)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:#有异常
            self.conn.rollback()
        else:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

class BaseDao():
    def __init__(self):
        self.db = DB()

    def find_all(self, table, where=None, *whereArgs):
        sql= "select * from %s" %table
        if where:
            sql += where
        with self.db as c:
            c.execute(sql, whereArgs)
            # 将可列对象转换为列表
            result = list(c.fetchall())
        return result

if __name__ == '__main__':
    pwd = hashlib.md5('888888'.encode('utf-8')).hexdigest()
    print(pwd)
    dao = BaseDao()
    pes = dao.find_all('bank',' where name=%s and password=%s','辣子',pwd)
    print(pes)
        

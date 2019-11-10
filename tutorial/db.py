import pymysql
import time,hashlib
from twisted.enterprise import adbapi
from pymysql import cursors

class NoveltySpiderPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '139.219.8.80',
            'port': 4321,
            'user': 'test',
            'password': 'test',
            'database': 'novelty',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    @property
    def insert(self):
        if not self._sql:
            self._sql = """
                insert into T_article_list(F_cat,F_detail,F_title,F_time,F_pc,F_note,F_post_like,F_thumb) values(%s,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql

    @property
    def exist(self, res):    
        sql = """
                select F_detail from T_article_list where F_detail = %s
                """
        cursor.execute(sql, (res))
        result = cursor.fetchone()
        # 不在数据库中, 则插入
        if result != None: 
            return True;
        return False;  
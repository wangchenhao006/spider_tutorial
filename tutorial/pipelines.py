# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time,hashlib
from twisted.enterprise import adbapi
from pymysql import cursors

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()

class NoveltySpiderPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '139.219.8.80',
            'port': 4321,
            'user': 'root',
            'password': 'root',
            'database': 'novelty',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (create_id(),item['cat'], item['detail'], item['title'], item['time'], item['pc'], item['note'],item['post_like'],item['thumb']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into T_article_list(F_id,F_cat,F_detail,F_title,F_time,F_pc,F_note,F_post_like,F_thumb) values(null,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            return self._sql
        return self._sql
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time,hashlib
from twisted.enterprise import adbapi
from pymysql import cursors
from . import db

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()

class NoveltySpiderPipeline(object):
    def process_item(self, item, spider):
        print(int(create_id(),16))
        db_manager = db.DatabaseManager()
        return db_manager.insert(item)


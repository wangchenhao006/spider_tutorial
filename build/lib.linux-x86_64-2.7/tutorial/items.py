# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NoveltyItem(scrapy.Item):
    # 标签
    cat = scrapy.Field()
    # 正文链接
    detail = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 评论
    pc = scrapy.Field()
    # 简介
    note = scrapy.Field()
    # 点赞
    post_like = scrapy.Field()
    # 封面
    thumb = scrapy.Field()
    pass

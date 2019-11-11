# -*- coding: utf-8 -*-
import scrapy


class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['jingjibao789.com']
    start_urls = ['https://www.jingjibao789.com']

    def parse(self, response):
        pass

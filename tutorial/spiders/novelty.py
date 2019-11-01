# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import NoveltyItem

class NoveltySpider(scrapy.Spider):
    name = 'novelty'
    allowed_domains = ['fulibus.net']
    start_urls = ['https://fulibus.net/']

    def parse(self, response):
        src = response.xpath("//div[@class='content-wrap']/div[@class='content'][1]/article")

        for article in src:
            item = NoveltyItem()
            item['cat'] = article.xpath('header/a/text()').extract_first()
            item['title'] = article.xpath('a/img/@alt').extract_first()
            item['detail'] = article.xpath('a/@href').extract_first()
            item['time'] = article.xpath('p[@class="meta"]/time/text()').extract_first()
            item['pc'] = article.xpath('p[@class="meta"]/a[@class="pc"]/text()').extract_first()
            item['post_like'] = article.xpath('p[@class="meta"]/a[@class="post-like"]/span/text()').extract_first()
            item['thumb'] = article.xpath('a/img/@src').extract_first()
            yield(item)
            print(item)
            print("--------\n")

        next_page = response.xpath("//div[@class='content-wrap']/div[@class='content'][1]/div[@class='pagination']/ul/li[@class='next-page']/a/@href").extract_first()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True )
        pass

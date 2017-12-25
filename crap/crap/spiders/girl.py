# -*- coding: utf-8 -*-
import scrapy


class GirlSpider(scrapy.Spider):
    name = "girl"
    allowed_domains = ["www.xiaohuar.com"]
    start_urls = ['http://www.xiaohuar.com/']

    def parse(self, response):
        pass

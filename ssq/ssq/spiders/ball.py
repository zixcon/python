# -*- coding: utf-8 -*-
import scrapy
from lxml import etree


class BallSpider(scrapy.Spider):
    name = "ball"
    allowed_domains = ["kaijiang.zhcw.com"]
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']

    def parse(self, response):
        print(response.body)

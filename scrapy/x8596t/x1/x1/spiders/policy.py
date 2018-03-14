# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class PolicySpider(scrapy.Spider):
    name = "policy"
    allowed_domains = ["bbs.tianya.cn"]
    start_urls = ['http://bbs.tianya.cn/post-develop-2212810-1.shtml']
    domain = "http://bbs.tianya.cn/post-develop-2212810-"

    # 页面编号组装url
    def parse_url(self, pagenum):
        url = self.domain + str(pagenum) + '.shtml'
        return url

    def parse(self, response):
        sel = Selector(response=response)
        elements = sel.css(".atl-item").extract()
        for element in elements:
            elem = Selector(text=element)
            elem.css(".atl-content > .bbs-content").extract()


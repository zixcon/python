# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import Request
from x1.items import X1Item


class PolicySpider(scrapy.Spider):
    name = "policy"
    allowed_domains = ["bbs.tianya.cn"]
    start_urls = ['http://bbs.tianya.cn/post-develop-2212810-1.shtml']
    domain = "http://bbs.tianya.cn"

    def parse_url(self, pagenum):
        url = self.domain + str(pagenum) + '.shtml'
        return url

    def parse_next_page(self, response):
        sel = Selector(response=response)
        elements = sel.css("form > a").extract()
        for element in elements:
            elem = Selector(text=element)
            next = elem.css("a::text").extract()[0]
            print(next)
            if (next == '下页'):
                page_href = elem.css("a::attr(href)").extract()
                href = self.domain + page_href[0]
                return href
        return None

    def parse(self, response):
        sel = Selector(response=response)
        elements = sel.css(".atl-item").extract()
        for element in elements:
            elem = Selector(text=element)
            host = elem.css(".atl-item::attr(_host)").extract()[0]
            if (host == 'x8596t'):
                item = X1Item()
                item['time'] = elem.css(".atl-item::attr(js_restime)").extract()
                content = elem.css(".bbs-content").extract()
                item['content'] = content[0]
                yield item

        page_href = self.parse_next_page(response)
        if page_href is not None:
            yield Request(page_href, callback=self.parse)

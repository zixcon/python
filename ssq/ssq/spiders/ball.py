# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from lxml import etree


class BallSpider(scrapy.Spider):
    name = "ball"
    allowed_domains = ["kaijiang.zhcw.com"]
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']

    def parse(self, response):
        # print(response.body)
        sel = Selector(response=response)
        # tbody 取不到，可能因为是自定义标签缘故
        # elements = sel.css("tbody > tr").extract()
        elements = sel.css("table > tr").extract()
        for element in elements:
            # print(element)
            elem = Selector(text=element)
            # arr = elem.css("td::text")
            # if arr:
            #     date = arr.pop(1).extract()
            #     print(date)
            arr = elem.css("td::text").extract()
            if len(arr) > 2:
                print(arr[1])
            em_arr = elem.css('em::text').extract()
            if em_arr:
                index = 0
                for em in em_arr:
                    print(em)
                    index = index + 1

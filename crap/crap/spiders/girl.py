# -*- coding: utf-8 -*-
# https://docs.scrapy.org/en/latest/
import scrapy


class GirlSpider(scrapy.Spider):
    name = "girl"
    allowed_domains = ["www.xiaohuar.com"]
    start_urls = ['http://www.xiaohuar.com/mm/']

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码

        for item in response.css('div.items'):
            yield {
            'src':item.css('img::attr(src)').extract_first(),
            'name':item.css('p > a::text').extract_first(),
            }



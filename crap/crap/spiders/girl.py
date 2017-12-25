# -*- coding: utf-8 -*-
# https://docs.scrapy.org/en/latest/
import scrapy
import wget

class GirlSpider(scrapy.Spider):
    name = "girl"
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/p/suyan/']
    split_str = '.'

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码

        # for item in response.css('div.items'):
        #     yield {
        #     'src':item.css('img::attr(src)').extract_first(),
        #     'name':item.css('p > a::text').extract_first(),
        #     }

        for item in response.css('div.item'):
            href = 'http://www.xiaohuar.com' + item.css('div.img a > img::attr(src)').extract_first()
            name = item.css('div.img a > img::attr(alt)').extract_first()
            wget.download(href, name + self.split_str + href.split(self.split_str)[-1])

            yield {
            'href':href,
            'name':name,
            }



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
            href = 'http://www.xiaohuar.com/p/suyan' + item.css('div.img a > img::attr(src)').extract_first()
            name = item.css('div.img a > img::attr(alt)').extract_first()
            wget.download(href, name + self.split_str + href.split(self.split_str)[-1])

            yield {
                'href': href,
                'name': name,
            }
        #
        # for page in [2,3,4,5,6,7]:
        #     next_page = self.start_urls[0] + 'index_' + page + '.html'
        #     if next_page is not None:
        #         yield response.follow(next_page, callback=self.parse)

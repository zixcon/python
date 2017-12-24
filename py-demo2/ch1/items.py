# 设置数据存储模板，用于结构化数据

import scrapy


class GirlItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()
    qq = scrapy.Field()
    info = scrapy.Field()
    more = scrapy.Field()

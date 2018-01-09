# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SsqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    period = scrapy.Field()
    red_ball_1 = scrapy.Field()
    red_ball_2 = scrapy.Field()
    red_ball_3 = scrapy.Field()
    red_ball_4 = scrapy.Field()
    red_ball_5 = scrapy.Field()
    red_ball_6 = scrapy.Field()
    blue_ball = scrapy.Field()
    pass

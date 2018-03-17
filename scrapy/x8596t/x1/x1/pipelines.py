# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs


class X1Pipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        # self.file = open('items.jl', 'w')
        self.file = codecs.open('2017年到底是通货膨胀还是通货紧缩，理财的网民们可要看准罗.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        self.file.write(str(item['time']))
        self.file.write("\n")
        self.file.write(str(item['content']))
        self.file.write("\n")
        return item

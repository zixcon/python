# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import Request
from ssq.items import SsqItem


class BallSpider(scrapy.Spider):
    name = "ball"
    allowed_domains = ["kaijiang.zhcw.com"]
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']
    domain = "http://kaijiang.zhcw.com"

    # 页面编号组装url
    def parse_url(self, pagenum):
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(pagenum) + '.html'
        return url

    # 匹配下一页链接地址，并组装真实页面编号地址
    def parse_next_pagenum(self, response):
        sel = Selector(response=response)
        next_pagenum = sel.re('<a href="/zhcw/inc/ssq/ssq_wqhg.jsp\\?pageNum=\d+">下一页</a>')
        print(next_pagenum[0])
        next_page = Selector(text=next_pagenum[0])
        page_href = next_page.css('a::attr(href)').extract()[0]
        pagenum = page_href.split('=')[1]
        return pagenum

    # 匹配下一页链接地址返回
    def parse_next_page(self, response):
        sel = Selector(response=response)
        next_pagenum = sel.re('<a href="/zhcw/inc/ssq/ssq_wqhg.jsp\\?pageNum=\d+">下一页</a>')
        print(next_pagenum[0])
        next_page = Selector(text=next_pagenum[0])
        page_href = next_page.css('a::attr(href)').extract()[0]
        return self.domain + page_href

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

            item = SsqItem()
            arr = elem.css("td::text").extract()
            if len(arr) > 2:
                item['date'] = arr[0]
                item['period'] = arr[1]
            em_arr = elem.css('em::text').extract()
            if len(em_arr) == 7:
                item['red_ball_1'] = em_arr[0]
                item['red_ball_2'] = em_arr[1]
                item['red_ball_3'] = em_arr[2]
                item['red_ball_4'] = em_arr[3]
                item['red_ball_5'] = em_arr[4]
                item['red_ball_6'] = em_arr[5]
                item['blue_ball'] = em_arr[6]
                # index = 0
                # for em in em_arr:
                #     print(em)
                #     if index == 6:
                #         item['blue_ball'] = em
                #     else:
                #         item_name = 'red_ball_' + str(index)
                #         item[item_name] = em
                #     index = index + 1
                yield item

        # 方法1：通过组装后的真实地址请求
        # pagenum = self.parse_next_pagenum(response)
        # yield Request(self.parse_url(pagenum), callback=self.parse)

        # 方法2：通过下一页链接地址进行跳转
        yield Request(self.parse_next_page(response), callback=self.parse)

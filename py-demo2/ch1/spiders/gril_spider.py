import scrapy


class GrilSpider(scrapy.Spider):
    name = "beautifulGirl"
    allowed_domains = ["xiaohuar.com"]
    start_urls = ["http://www.xiaohuar.com/mm/"]

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码

    def __init__(self, name=None, **Kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)
        self.__dict__.update(Kwargs)
        if not hasattr(self, 'start_urls'):
            self.start_urls = []



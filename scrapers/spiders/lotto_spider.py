from datetime import datetime

import scrapy


class LottoSpider(scrapy.Spider):
    from_ = datetime.now()
    to_ = datetime.now()

    def parse(self, response):
        pass

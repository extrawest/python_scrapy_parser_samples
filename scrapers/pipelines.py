# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

import requests

from scrapers.items import ScrapersItem
from scrapers.spiders.lotto_spider import LottoSpider


class ScrapersPipeline(object):
    result = {}

    def open_spider(self, spider: LottoSpider):
        self.result['from'] = datetime.now()
        self.result['to'] = datetime.now()
        self.result['draws'] = []
        self.result['name'] = spider.name

    def df_format(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return str(obj)

    def close_spider(self, spider: LottoSpider):
        self.file = open(spider.name + '.json', 'w')

        line = json.dumps(self.result, default=ScrapersPipeline.df_format) + "\n"
        self.file.write(line)

        self.file.close()

        print(type(spider.settings['UPLOAD']))
        if spider.settings['UPLOAD'] == 'True' or spider.settings['UPLOAD'] is True:
            r = requests.put("http://localhost:8080/api/draw", data=line, headers={'Content-type': 'application/json'})
            print(r.text)
        else:
            print("Not uploaded")

    def process_item(self, item: ScrapersItem, spider: LottoSpider):
        self.result["draws"].append(item)

        from_date = self.result['from']
        to_date = self.result['to']

        if to_date < item['draw_date']:
            self.result['to'] = item['draw_date']
        elif from_date > item['draw_date']:
            self.result['from'] = item['draw_date']

        return item

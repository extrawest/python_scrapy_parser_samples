# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsFlLottoSpider(LottonumbersSpider):
    name = 'us_fl_lotto'
    start_urls = ['http://www.lottonumbers.com/florida-lotto']
    ball_types = ['ball', 'lotto-xtra']

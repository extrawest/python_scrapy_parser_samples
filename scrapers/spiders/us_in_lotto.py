# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsInLottoSpider(LottonumbersSpider):
    name = 'us_in_lotto'
    start_urls = ['http://www.lottonumbers.com/indiana-hoosier-lotto']
    ball_types = ['ball']

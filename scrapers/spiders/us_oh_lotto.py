# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsOhClassicLottoSpider(LottonumbersSpider):
    name = 'us_oh_lotto'
    start_urls = ['http://www.lottonumbers.com/ohio-classic-lotto']
    ball_types = ['ball']

# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsFlLottoSpider(LottonumbersSpider):
    name = 'us_tx_lotto'
    start_urls = ['http://www.lottonumbers.com/lotto-texas']
    ball_types = ['ball']

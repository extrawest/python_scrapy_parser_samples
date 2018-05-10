# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsGaFantasySpider(LottonumbersSpider):
    name = 'us_ga_fantasy'
    start_urls = ['http://www.lottonumbers.com/georgia-fantasy-5']
    ball_types = ['ball']

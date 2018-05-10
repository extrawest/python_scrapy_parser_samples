# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsLottoAmericaSpider(LottonumbersSpider):
    name = 'us_lotto_america'
    start_urls = ['http://www.lottonumbers.com/lotto-america']
    ball_types = ['ball', 'starball', 'allstarbonus']

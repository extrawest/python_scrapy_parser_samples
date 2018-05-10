# -*- coding: utf-8 -*-
import dateparser as dateparser
import scrapy

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider
from scrapers.spiders.lotto_spider import LottoSpider


class UsNjPick6Spider(LottonumbersSpider):
    name = 'us_nj_pick'
    start_urls = ['http://www.lottonumbers.com/new-jersey-pick-six-lotto']
    ball_types = ['ball', 'extra-shot']

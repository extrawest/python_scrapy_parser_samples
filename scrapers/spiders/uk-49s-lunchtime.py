# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class Uk49sLunchtime(LottonumbersSpider):
    name = 'uk-49s-lunchtime'
    start_urls = ['http://www.lottonumbers.com/uk-49s-lunchtime']
    ball_types = ['ball', 'bonus-ball']

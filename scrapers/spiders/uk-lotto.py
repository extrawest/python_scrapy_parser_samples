# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class UkLotto(LottonumbersSpider):
    name = 'uk-lotto'
    start_urls = ['http://www.lottonumbers.com/uk-lotto']
    ball_types = ['ball', 'bonus-ball']

# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class DeuGermanLotto(LottonumbersSpider):
    name = 'deu_german-lotto'
    start_urls = ['http://www.lottonumbers.com/german-lotto']
    ball_types = ['ball', 'super-ball']

# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class UkThunderball(LottonumbersSpider):
    name = 'uk-thunderball'
    start_urls = ['http://www.lottonumbers.com/thunderball']
    ball_types = ['ball', 'thunderball']

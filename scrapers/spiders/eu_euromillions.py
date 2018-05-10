# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class EuEuromillions(LottonumbersSpider):
    name = 'eu_euromillions'
    start_urls = ['http://www.lottonumbers.com/euromillions']
    ball_types = ['ball', 'lucky-star']

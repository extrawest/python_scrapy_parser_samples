# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class EuEurojackpot(LottonumbersSpider):
    name = 'eu_eurojackpot'
    start_urls = ['http://www.lottonumbers.com/eurojackpot']
    ball_types = ['ball', 'euro']

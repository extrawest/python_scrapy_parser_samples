# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class Uk49sTeatime(LottonumbersSpider):
    name = 'uk-49s-teatime'
    start_urls = ['http://www.lottonumbers.com/uk-49s-teatime']
    ball_types = ['ball', 'bonus-ball']

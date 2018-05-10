# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class SpaElGordo(LottonumbersSpider):
    name = 'spa_el-gordo'
    start_urls = ['http://www.lottonumbers.com/el-gordo']
    ball_types = ['ball', 'bonus-ball']

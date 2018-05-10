# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class UkHealthLottery(LottonumbersSpider):
    name = 'uk-health-lottery'
    start_urls = ['http://www.lottonumbers.com/health-lottery']
    ball_types = ['ball', 'bonus-ball']

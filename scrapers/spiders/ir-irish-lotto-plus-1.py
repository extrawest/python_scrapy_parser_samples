# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class IrIrishLottoPlus1(LottonumbersSpider):
    name = 'ir_irish-lotto-plus-1'
    start_urls = ['http://www.lottonumbers.com/irish-lotto-plus-1']
    ball_types = ['ball', 'bonus-ball']

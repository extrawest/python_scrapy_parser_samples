# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class IrIrishLottoPlus2(LottonumbersSpider):
    name = 'ir_irish-lotto-plus-2'
    start_urls = ['http://www.lottonumbers.com/irish-lotto-plus-2']
    ball_types = ['ball', 'bonus-ball']

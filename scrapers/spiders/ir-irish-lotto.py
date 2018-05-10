# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class IrIrishLotto(LottonumbersSpider):
    name = 'ir_irish-lotto'
    start_urls = ['http://www.lottonumbers.com/irish-lotto']
    ball_types = ['ball', 'bonus-ball']

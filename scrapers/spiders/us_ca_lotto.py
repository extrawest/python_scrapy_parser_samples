# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class UsCaSuperLottoPlusSpider(LottonumbersSpider):
    name = 'us_ca_lotto'
    start_urls = ['http://www.lottonumbers.com/california-superlotto']
    ball_types = ['ball', 'mega-ball']

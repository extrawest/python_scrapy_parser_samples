# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class UsMegamillionsSpider(LottonumbersSpider):
    name = 'us_mega_millions'
    start_urls = ['http://www.lottonumbers.com/mega-millions']
    ball_types = ['ball', 'megaplier', 'megaball']

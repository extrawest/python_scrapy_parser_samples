# -*- coding: utf-8 -*-

from scrapers.spiders.LottonumbersSpider import LottonumbersSpider


class EspSuperenalotto(LottonumbersSpider):
    name = 'esp_superenalotto'
    start_urls = ['http://www.lottonumbers.com/superenalotto']
    ball_types = ['ball', 'jolly','superstar']

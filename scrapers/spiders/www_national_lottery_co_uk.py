# -*- coding: utf-8 -*-

from scrapy.spiders import CSVFeedSpider

from scrapers.items import ScrapersItem


class WwwNationalLotteryCoUkSpider(CSVFeedSpider):
    name = 'www.national-lottery.co.uk'
    allowed_domains = ['www.national-lottery.co.uk']
    start_urls = ['https://www.national-lottery.co.uk/results/lotto/draw-history/csv',
                  '']
    delimiter = ','
    quotechar = "'"
    headers = ['DrawDate', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'Ball 6', 'Bonus Ball', 'Ball Set',
               'Machine', 'Raffles', 'DrawNumber']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = ScrapersItem()
        item['draw_date'] = row['DrawDate']
        item['balls'] = {row['Ball 1'], row['Ball 2'], row['Ball 3'], row['Ball 4'], row['Ball 5'], row['Ball 6']}
        item['bonus_ball'] = row['Bonus Ball']
        item['draw_number'] = row['DrawNumber']

        return item

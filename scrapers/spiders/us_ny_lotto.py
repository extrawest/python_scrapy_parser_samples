import datetime

import dateparser

from scrapers.spiders.lotto_spider import LottoSpider


class UsNyLotto(LottoSpider):
    name = 'us_ny_lotto'
    allowed_domains = ['https://nylottery.ny.gov/']
    start_urls = ['https://nylottery.ny.gov/lotto/past-winning-numbers']

    def parse(self, response):
        for i in response.css('div.views-row'):
            balls = []
            for ball in i.css('p.winning-numbers span.numbers::text').extract_first().split('-'):
                balls.append({"ball_type": 'ball', "ball_value": ball})
            balls.append({"ball_type": 'bonus_ball', "ball_value": i.css('p.bonus-number::text').extract_first()})

            draw_date = dateparser.parse(i.css('p.result-date::text').extract_first(), date_formats=['%m/%d/%Y'])

            yield {
                "balls": balls,
                "draw_date": draw_date
            }

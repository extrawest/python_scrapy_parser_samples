# -*- coding: utf-8 -*-
import dateparser
import scrapy
from scrapy.http import TextResponse

from scrapers.spiders.lotto_spider import LottoSpider


class UsPowerballSpider(LottoSpider):
    name = 'us_powerball'
    allowed_domains = ['http://www.powerball.com/powerball/']
    start_urls = ['http://www.powerball.com/powerball/winnums-text.txt']
    delimiter = ' '

    def parse(self, response: TextResponse):
        for l in response.text.split("\r\n")[1:-1]:
            str_elements = l.split("  ")

            draw_date = dateparser.parse(str_elements[0])

            balls = []

            for ball in str_elements[1:6]:
                balls.append({
                    "ball_type": "ordinal",
                    "ball_value": ball
                })

            balls.append({
                "ball_type": "powerball",
                "ball_value": str_elements[6]
            })

            if str_elements[7] is not "":
                balls.append({
                    "ball_type": "powerplay",
                    "ball_value": str_elements[7]
                })

            yield {
                "draw_date": draw_date,
                "balls": balls
            }

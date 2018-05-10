# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    draw_date = scrapy.Field()
    balls = scrapy.Field()
    bonus_ball = scrapy.Field()
    draw_number = scrapy.Field()

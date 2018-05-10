import dateparser
import scrapy

from scrapers.spiders.lotto_spider import LottoSpider


class LottonumbersSpider(LottoSpider):
    allowed_domains = ['lottonumbers.com']
    ball_types = None

    def parse(self, response):
        for year_results_url in response.css('div.sidebar-container:last-child li a::attr(href)').extract()[1:]:
            yield scrapy.Request(url='http://www.lottonumbers.com/' + year_results_url,
                                 callback=self.parse_year_results)

    def parse_year_results(self, response):

        for i in response.css('table.lotteryTable tr'):
            balls = []

            td_list = i.css('td')
            if len(td_list) == 3:

                for ball_type in self.ball_types:
                    for b in td_list[1].css('li.' + ball_type + '::text').extract():
                        balls.append({"ball_type": ball_type, "ball_value": b})

                yield {
                    "balls": balls,
                    "draw_date": dateparser.parse(td_list[0].css('a::attr(href)').extract_first()[-10:])
                }

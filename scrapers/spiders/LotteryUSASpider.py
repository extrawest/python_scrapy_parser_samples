import dateparser
import datetime

from scrapers.spiders.lotto_spider import LottoSpider


class LotteryUSASpider(LottoSpider):
    allowed_domains = ['lotteryusa.com']
    ball_types = None
    from_ = datetime.datetime.now()
    to_ = datetime.datetime.now()

    def parse(self, response):

        for i in response.css('table.game-results tbody tr'):
            balls = []

            datetime_str = i.css('time::attr(datetime)').extract_first()

            if datetime_str:
                datetime = dateparser.parse(datetime_str, date_formats=['%Y-%m-%d'])

                print(datetime)
                print(self.to_)
                print(self.from_)
                if datetime > self.to_:
                    self.to_ = datetime

                if datetime < self.from_:
                    self.from_ = datetime

                for b in i.css('span.string-results::text').extract_first().split(','):
                    balls.append({"ball_type": "ball", "ball_value": b})

                yield {
                    "balls": balls,
                    "draw_date": datetime
                }


class UsAr5CardCash(LotteryUSASpider):
    name = 'us_ar_5-card-cash'
    start_urls = ['http://www.lotteryusa.com/arizona/' + name[6:] + '/year']

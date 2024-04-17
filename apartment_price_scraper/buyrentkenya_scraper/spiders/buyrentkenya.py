import scrapy


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com/flats-apartments-for-rent"]

    def parse(self, response):
        pass

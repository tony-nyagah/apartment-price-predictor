import scrapy


class Property24Spider(scrapy.Spider):
    name = "property24"
    allowed_domains = ["www.property24.co.ke"]
    start_urls = ["https://www.property24.co.ke"]

    def parse(self, response):
        pass

import scrapy


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com/flats-apartments-for-sale"]

    def parse(self, response):
        for selector in response.css("div.listing-card"):
            yield {
                "location": selector.css("p.ml-1.truncate.text-grey-650::text").get(),
                "bedrooms": selector.css("span[data-cy='card-beds']::text").get(),
                "bathrooms": selector.css("span[data-cy='card-bathrooms']::text").get(),
                "price": selector.css("span[data-cy='card-price']::text").get(),
            }

        next_page_link = response.css("")

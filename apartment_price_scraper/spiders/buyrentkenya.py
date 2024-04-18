import scrapy
from apartment_price_scraper.items import ApartmentPriceScraperItem


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com/flats-apartments-for-rent"]

    def parse(self, response):
        try:
            listings = response.css("div.listing-card")

            for _ in listings:
                relative_url = response.css("h5.text-md a.block").attrib["href"]
                listing_url = "https://www.buyrentkenya.com" + relative_url
                yield response.follow(listing_url, callback=self.parse_listing_page)

            next_page_url = response.xpath(
                '//*[@id="mainContent"]/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div/a/@href'
            ).get()

            if next_page_url is not None:
                yield response.follow(next_page_url, callback=self.parse)

        except Exception as e:
            self.logger.error(f"Error occurred in parse method: {e}")

    def parse_listing_page(self, response):
        item = ApartmentPriceScraperItem()

        item["title"] = response.xpath(
            '//*[@id="mainContent"]/div[2]/div[2]/div[2]/div[1]/h1/text()'
        ).extract()
        item["description"] = response.css("div.my-3 div.text-grey-550 ::text").get()
        item["price"] = response.xpath(
            '//*[@id="mainContent"]/divres[2]/div[3]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/span/span/text()'
        ).get()
        item["frequency"] = response.xpath(
            '//*[@id="mainContent"]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/span/span/span/text()'
        ).get()
        item["location"] = response.xpath(
            '//*[@id="mainContent"]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div[1]/div/p/text()'
        ).get()
        item["bedrooms"] = response.xpath(
            '//*[@id="mainContent"]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div[2]/div/div/span[1]/text()'
        )[1].get()
        item["bathrooms"] = response.xpath(
            '//*[@id="mainContent"]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div[2]/div/div/span[2]/text()'
        )[1].get()
        item["features"] = response.css(
            "ul.flex li.flex div.overflow-hidden ::text"
        ).getall()

        yield item

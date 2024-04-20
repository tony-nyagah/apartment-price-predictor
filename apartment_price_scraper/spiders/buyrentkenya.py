import scrapy

from apartment_price_scraper.items import ApartmentPriceScraperItem


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com/flats-apartments-for-rent"]

    def parse(self, response):
        try:
            listings = response.css("div.listing-card")

            for listing in listings:
                listing_link = listing.css("a::attr(href)").get()
                listing_url = f"https://buyrentkenya.com{listing_link}"
                yield response.follow(listing_url, callback=self.parse_listing_page)

        except Exception as e:
            self.logger.error(f"Error occurred in parse method: {e}")

    def parse_listing_page(self, response):
        listing_details = ApartmentPriceScraperItem(
            title=response.css("h1::text").get().strip(),
            description=response.css("div.my-3 div.text-grey-550::text").get().strip(),
            price=response.css("span[aria-label='price']::text")
            .get()
            .strip()
            .replace("KSh ", ""),
            location=response.css("p.items-center.text-sm.text-gray-500::text")
            .get()
            .strip(),
            bedrooms=response.css('span[aria-label="bedrooms"]::text')
            .getall()[-1]
            .strip(),
            bathrooms=response.css('span[aria-label="bathrooms"]::text')
            .getall()[-1]
            .strip(),
            # internal_features =
            # external_features =
            # nearby =
        )
        print(listing_details)
        yield listing_details

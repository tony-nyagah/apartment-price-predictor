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
        price = (
            response.css("span[aria-label='price']::text")
            .get()
            .strip()
            .replace("KSh ", "")
            .replace(",", "")
        )
        bedrooms = (
            response.css('span[aria-label="bedrooms"]::text').getall()[-1].strip()
        )
        bathrooms = (
            response.css('span[aria-label="bathrooms"]::text').getall()[-1].strip()
        )
        internal_features = response.css(
            "div.flex.flex-col:contains('Internal features') li div::text"
        ).getall()
        external_features = response.css(
            "div.flex.flex-col:contains('External features') li div::text"
        ).getall()
        nearby = response.css(
            "div.flex.flex-col:contains('Nearby') li div::text"
        ).getall()

        listing_details = ApartmentPriceScraperItem(
            title=response.css("h1::text").get().strip(),
            price=int(price),
            location=response.css("p.items-center.text-sm.text-gray-500::text")
            .get()
            .strip(),
            bedrooms=int(bedrooms),
            bathrooms=int(bathrooms),
            internal_features=[
                feature.strip() for feature in internal_features if feature.strip()
            ],
            external_features=[
                feature.strip() for feature in external_features if feature.strip()
            ],
            nearby=[feature.strip() for feature in nearby if feature.strip()],
        )
        print(listing_details)
        yield listing_details

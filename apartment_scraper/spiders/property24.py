import scrapy


class Property24Spider(scrapy.Spider):
    name = "property24"
    allowed_domains = ["www.property24.co.ke"]
    start_urls = [
        "https://www.property24.co.ke/apartments-flats-to-rent?cityids=1890,1846&suburbids=14611,14520,14595,14580"
    ]

    def parse(self, response):
        for selector in response.css("div.sc_searchResultsP24Style"):
            yield {
                "location": str(selector.css("span.p24_location::text").get()),
                "bedrooms": int(
                    selector.css("span[title='Bedrooms'] > span::text").get()
                ),
                "bathrooms": int(
                    selector.css("span[title='Bathrooms'] > span::text").get()
                ),
                "price": int(
                    "".join(
                        char
                        for char in selector.css("span.p24_price::text").get().strip()
                        if char.isdigit()
                    )
                ),
                "site": "Property24",
            }

        next_page_links = response.css(
            "div.sc_searchResultsPagerBottom a::attr(href)"
        ).getall()
        for link in next_page_links:
            yield response.follow(link, callback=self.parse)

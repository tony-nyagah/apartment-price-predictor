import scrapy


class BuyrentkenyaSpider(scrapy.Spider):
    name = "buyrentkenya"
    allowed_domains = ["buyrentkenya.com"]
    start_urls = ["https://www.buyrentkenya.com/flats-apartments-for-rent"]

    def parse(self, response):
        for selector in response.css("div.listing-card"):
            yield {
                "location": selector.css("p.ml-1.truncate.text-grey-650::text").get(),
                "bedrooms": selector.css("span[data-cy='card-beds']::text").get(),
                "bathrooms": selector.css("span[data-cy='card-bathrooms']::text").get(),
                "price": selector.css(
                    "div.relative.w-full.overflow-hidden.rounded-2xl.bg-white::attr("
                    "data-bi-listing-price)"
                ).get(),
                "site": "BuyRentKenya",
            }

        next_page_links = response.css(
            "ul.pagination-page-nav li.page-item a::attr(href)"
        ).getall()
        for link in next_page_links:
            yield response.follow(link, callback=self.parse)

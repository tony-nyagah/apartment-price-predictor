# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApartmentPriceScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    frequency = scrapy.Field()
    location = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    features = scrapy.Field()
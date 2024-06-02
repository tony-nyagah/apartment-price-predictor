import csv

from apartment_scraper.spiders.buyrentkenya import BuyrentkenyaSpider
from apartment_scraper.spiders.property24 import Property24Spider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher


def apartment_spider_results():
    apartment_results = []

    def crawler_results(item):
        apartment_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess()
    # process.crawl(BuyrentkenyaSpider, Property24Spider)
    process.crawl(Property24Spider)
    process.start()

    return apartment_results


if __name__ == "__main__":
    apartment_data = apartment_spider_results()

    keys = apartment_data[0].keys()
    with open("apartment_data.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(apartment_data)

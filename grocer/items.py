# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WooliesItems(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    dislplayname = scrapy.Field()
    stockcode = scrapy.Field()
    price = scrapy.Field()
    cup_price = scrapy.Field()
    cupmeasure = scrapy.Field()
    unitweight = scrapy.Field()
    wasprice = scrapy.Field()
    instorewasprice = scrapy.Field()
    savings_message = scrapy.Field()
    store_DOM = scrapy.Field()
    scrape_time = scrapy.Field()

    pass

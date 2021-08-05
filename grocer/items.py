# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WooliesItems(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(serializer=str)
    displayname = scrapy.Field(serializer=str)
    stockcode = scrapy.Field(serializer=str)
    price = scrapy.Field(serializer=str)
    cup_price = scrapy.Field(serializer=str)
    cupmeasure = scrapy.Field(serializer=str)
    unitweight = scrapy.Field(serializer=str)
    wasprice = scrapy.Field(serializer=str)
    instorewasprice = scrapy.Field(serializer=str)
    savings_message = scrapy.Field(serializer=str)
    store_DOM = scrapy.Field(serializer=str)
    scrape_time = scrapy.Field(serializer=str)

    pass

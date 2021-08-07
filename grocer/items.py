# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def serialise_stockcode(value):
    return str(value)


class WooliesItems(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    displayName = scrapy.Field()
    stockcode = scrapy.Field(serializer=serialise_stockcode)
    price = scrapy.Field()
    cupprice = scrapy.Field()
    cupmeasure = scrapy.Field()
    unitweightingrams = scrapy.Field()
    wasprice = scrapy.Field()
    instorewasprice = scrapy.Field()
    savingsamount = scrapy.Field()
    url = scrapy.Field()
    scrapetime = scrapy.Field()

    pass
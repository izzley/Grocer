import datetime
import logging
from typing import Dict, Generator, Set

import scrapy
# from grocer.pipelines import StoreToWooliesDatabase

logger = logging.getLogger('harrisfarm')


class HarrisfarmSpider(scrapy.Spider):
    name = 'harrisfarm'
    allowed_domains = ['harrisfarm.com']
    ui = 'https://www.harrisfarm.com.au/products/'
    now = datetime.datetime.now()  # timestamp
    data = {'excludeUnavailable': 'false'}
    # pipelines = set([StoreToWooliesDatabase])

    product_params = {
        'Almond_butter': 'noya-nut-butter-almond',
        }

    # useful scrapy shell interactive object for dev
    # https://docs.scrapy.org/en/latest/topics/shell.html#invoking-the-shell-from-spiders-to-inspect-responses
    shell_interact = False
    shell_grocery = 'Almond_butter'  # To interact with everything set as 'ALL'

    def start_requests(self) -> Generator[scrapy.Request, None, None]:
        prod_params = self.product_params
        ui = self.ui
        for product in prod_params:
            url = f'{ui}{prod_params[product]}'
            # @TODO 
            yield scrapy.Request(url=url, meta=self.data)
    
    def parse(self, response) -> Generator[Dict, None, None]:
        logger.info("Running harrisfarm spider")
        item = {}
        item['name'] = response.xpath('//h1[@itemprop="name"]/text()').extract()[0]
        item['displayName'] = item['name']
        item['price'] = response.xpath('//span[@class="from_price"]/text()').extract()[0]
        # @TODO can't get small attribute eg ['$3.80 per 100g']
        item['cupprice'] = response.xpath('//span[@class="unit_price"]').extract()
        pass
        

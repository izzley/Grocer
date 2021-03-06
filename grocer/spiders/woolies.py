import datetime
import logging
from typing import Dict, Generator, Set

import scrapy
from grocer.pipelines import StoreToWooliesDatabase

# https://github.com/stav/wgrep
# https://stackoverflow.com/questions/63058957/how-to-extract-hidden-html-content-with-scrapy
logger = logging.getLogger('woolies')


class WooliesSpider(scrapy.Spider):
    name = 'woolies'
    allowed_domains = ['woolworths.com']
    ui = 'https://www.woolworths.com.au/apis/ui/products/'
    now = datetime.datetime.now()  # timestamp
    data = {'excludeUnavailable': 'false'}
    pipelines = set([StoreToWooliesDatabase])

    product_params = {
        'Merediths_big': '663973',  # big jar
        'Merediths_small': '135884',  # small jar
        'Kehoes_beet': '876670',  # beetroot
        'Kehoes_kim': '876671',  # kimchi
        'Mary_cracks': '325292',  # Marys gone crackers
        'Minor_oat': '155063',  # full (dark grey)
        'Mntn_bread': '16436',  # rye
        'Cider_vngr': '476910',  # braggs
        'Tuna_chilli': '257374',  # sirena fillets 125g
        'Frz_blueberry': '931859',  # oob organic 450g
        'Frz_Rasp': '792993',  # oob organic 450g
        'Frz_Strawb': '780094',  # oob organic 450g
        'Frz_mixed': '815129',  # Macro mixed 450g
        'Coyo_nat': '896940',  # Natural 500g coyoghurt
        'Nakula_nat': '872611',  # Nakula 1kg coyoghurt
        'Peanut_b': '127012',  # Mayvers 750g
        'Almond_meal': '120690',  # Woolies brand 665g
        'Pasta_gfree': '795044',  # Olive green tri grain 300g
        'Pasta_gfree_spiral': '378934',  # Buenotempo rice 500g
        'Choc_grnblk': '2514',  # Green & black 70% Cocoa 90g
    }

    # useful scrapy shell interactive object for dev
    # https://docs.scrapy.org/en/latest/topics/shell.html#invoking-the-shell-from-spiders-to-inspect-responses
    shell_interact = False
    shell_grocery = '663973'  # To interact with everything set as 'ALL'

    def start_requests(self) -> Generator[scrapy.Request, None, None]:
        prod_params = self.product_params
        endpoint_l = [prod_params[key] for key in prod_params]
        ui = self.ui

        # Interactive option to only get item response
        if self.shell_interact:
            for end_p in prod_params:
                    url = f'{ui}{prod_params[end_p]}'
                    yield scrapy.Request(url=url, meta=self.data)
        else:
            endpoints = ','.join(endpoint_l)
            url = f'{ui}{endpoints}'
            # @TODO Create url params iterable fo output each keyword as endpoint
            yield scrapy.Request(url=url, meta=self.data)

    def parse(self, response) -> Generator[Dict, None, None]:
        logger.info("Running woolies spider")
        data = response.json()
        stockcode = str(data[0]["Stockcode"])  # ['Stockcode'] == int -> str
        # json.dumps(parsed, indent=4, sort_keys=True)
        if self.shell_interact and stockcode in self.shell_grocery:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        for a in data:
            yield {
                # @TODO Stockcode str of numbers is coerced into int
                'stockcode': a['Stockcode'], # int
                'name': a['Name'], # str
                'displayName': a['DisplayName'], # str
                'price': a['Price'], # int
                'cupprice': a['CupPrice'], # float
                'cupmeasure': a['CupMeasure'], # str
                'unitweightingrams': a['UnitWeightInGrams'], # int
                'wasprice': a['WasPrice'], # int
                'instorewasprice': a['InstoreWasPrice'], # int
                'savingsamount': a['SavingsAmount'], # int
                'url': self.allowed_domains[0], # str
                'scrapetime': self.now # str
            }

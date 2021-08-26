# Scrapy settings for grocer project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import configparser
import pathlib

BOT_NAME = 'grocer'

SPIDER_MODULES = ['grocer.spiders']
NEWSPIDER_MODULE = 'grocer.spiders'

# pull database credentials from local file
# https://docs.python.org/3/library/configparser.html#module-configparser
# @TODO PurePath walk upwards from pathlib.Path()
# https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents
p = pathlib.Path('.') / 'settings/grocer.ini'
config = configparser.ConfigParser()
config.read(p)

EMAIL = {
    'portnumber': config['EMAIL']['portnumber'],
    'mailserver': config['EMAIL']['mailserver'],
    'password': config['EMAIL']['password'],
    'fromaddress': config['EMAIL']['fromaddress'],
    'toaddress': config['EMAIL']['toaddress'],
}

DATABASE = {
    'drivername': config['DATABASE']['drivername'],
    'host': config['DATABASE']['host'],
    'port': config['DATABASE']['port'],
    'username': config['DATABASE']['username'],
    'password': config['DATABASE']['password'],
    'database': config['DATABASE']['database'],
}

db_url = f"{DATABASE['drivername']}://{DATABASE['host']}/{DATABASE['database']}?{DATABASE['username']}=other&password=secret"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'grocer (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'grocer.middlewares.GrocerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'grocer.middlewares.GrocerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'grocer.pipelines.StoreToWooliesDatabase': 300,
}

LOG_LEVEL = "INFO"
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

if __name__ == '__main__':
  print(EMAIL['mailserver'])
# Scrapy settings for myfitnesspal project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myfitnesspal'

SPIDER_MODULES = ['myfitnesspal.spiders']
NEWSPIDER_MODULE = 'myfitnesspal.spiders'

SPIDER_MIDDLEWARES = { 'myfitnesspal.ignore.IgnoreVisitedItems': 560, }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myfitnesspal (+http://www.yourdomain.com)'

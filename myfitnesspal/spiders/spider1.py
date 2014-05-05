import urlparse

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from myfitnesspal.items import MyfitnesspalItem

import BeautifulSoup
import HTMLParser

INDEX = [
        'Name', 
        'Servings', 
        'Calories', 
        'Sodium', 
        'Total Fat', 
        'Potassium', 
        'Saturated', 
        'Total Carbs', 
        'Polyunsaturated', 
        'Dietary Fiber', 
        'Monounsaturated', 
        'Sugars', 
        'Trans', 
        'Protein', 
        'Cholesterol', 
        'Vitamin A', 
        'Calcium', 
        'Vitamin C', 
        'Iron'
    ]

csvWriter = open('nutrition_chart.csv','wb')
csvWriter.write(('|'.join(INDEX) + '\n'))

def getNutrtionValuesCSV(nutritionHTML):

    sample = nutritionHTML
    soup = BeautifulSoup.BeautifulSoup(sample)
    
    details = []

    # Food Name
    details.append(soup.find("h2", {"class" : "food-description"}).text)

    # Servings
    # details.append(soup.find("input", {"id" : "food_entry_quantity"})['value'])
    servings = ''
    for serving in soup.find("select", {"id" : "food_entry_weight_id"}).findAll('option'):
        servings += serving.text + ';;'
    details.append(servings)

    # Nutrition Table
    for row in soup.find("table", {"id": "nutrition-facts"}).findAll('tr'):
        nutrition = row.findAll('td')
        nutritionLen = len(nutrition)
        for i in xrange(0,nutritionLen,2):
            nutVal = nutrition[i+1].text.replace('&nbsp;', '')
            if nutVal != '':
                details.append(nutVal)

    return HTMLParser.HTMLParser().unescape(('|'.join(details) + '\n').encode('utf-8'))


class MyfitnesspalSpider(CrawlSpider):
    """ General configuration of the Crawl Spider """

    name = 'Myfitnesspal'

    # urls from which the spider will start crawling
    allowed_domains = ['myfitnesspal.com']
    start_urls = ['http://www.myfitnesspal.com']

    rules = [
        Rule(SgmlLinkExtractor(allow=[r'/tag/show/.*']), follow=True),
        Rule(SgmlLinkExtractor(allow=[r'/nutrition-facts-calories/.*']), follow=True),
        Rule(SgmlLinkExtractor(allow=[r'/food/calories/.*']), callback='parse_item', follow=True),
        ]

    def parse_item(self, response):
        # print getNutrtionValuesCSV(response.body)
        csvWriter.write(getNutrtionValuesCSV(response.body))

    def print_url(self, response):
        print response.url
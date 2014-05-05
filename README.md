## MyFitnessPal.com Scraper and Parser
======================================

* Scraps the site (myfitnesspal.com)
* Gets the pages according to regex /food/calories/.*
* Parses the page to get info on a food item about calories, iron, vitamins etc
* Stores them in a csv file (delimiter='|').

#### Dependencies
-----------------

* scrapy
* BeautifulSoup
* HTMLParser

#### Run
-----------------
`$ scrapy crawl Myfitnesspal`
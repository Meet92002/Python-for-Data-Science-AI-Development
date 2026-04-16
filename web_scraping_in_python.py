# Web Scraping - A Key Tool in Data Science

# Introduction

# Web scraping, also known as web harvesting or web data extraction, 
# is a technique used to extract large amounts of data from websites. 
# The data on websites is unstructured, and web scraping enables us to convert it into a structured form.

# BeautifulSoup :-
# BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files.
# It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Scrapy:-
# Scrapy is an open-source and collaborative web crawling framework for Python. 
# It is used to extract the data from the website

import scrapy # type: ignore
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

# Selenium:- 
# Selenium is a tool used for controlling web browsers through programs and automating browser tasks.

from selenium import webdriver # type: ignore
driver = webdriver.Firefox()
driver.get("http://www.example.com")

# Web Scraping Tables using Pandas

# The Pandas library in Python contains a function read_html() 
# that can be used to extract tabular information from any web page.

import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)   


URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(URL)
df = tables[2] # the required table will have index 2
print(df)